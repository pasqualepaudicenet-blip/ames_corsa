import os
import re
import csv
import xml.etree.ElementTree as ET
from rest_framework import viewsets, filters
from ames_api.models import Corsa, Sample
from ames_api.serializers import CorsaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

class DieciProdottiPagination(PageNumberPagination):
    page_size = 10


class CorsaViewSet(viewsets.ModelViewSet):
    queryset = Corsa.objects.all()
    serializer_class = CorsaSerializer
    pagination_class = DieciProdottiPagination
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['description', 'type']

    def get_queryset(self):
        queryset = super().get_queryset()
        description = self.request.query_params.get('description', None)
        tipo = self.request.query_params.get('type', None)

        filters = Q()
        if description:
            filters &= Q(description__icontains=description)
        if tipo:
            filters &= Q(type__icontains=tipo)

        if filters:
            queryset = queryset.filter(filters)
        return queryset 

class CorsaSampleCreateView(View):
    #path = "/mnt/nas/NovaSeq"
    path = "/app/novaSeq"
    pattern = re.compile(
        r'^(?P<date>\d{6})_A(?P<description>\d+)_(?P<run>\d{4})_(?P<code>[A-Z0-9]+)$'
    )
    def get(self, request, *args, **kwargs):
        try:
            results = self.get_folders()
            return JsonResponse({"results": results})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def get_folders(self):
        saved_corse = []
        for name in os.listdir(self.path):
            match = self.pattern.match(name)
            if match:
                data = match.groupdict()

                yy = int(data["date"][:2])
                mm = data["date"][2:4]
                dd = data["date"][4:6]
                year = 2000 + yy
                formatted_date = f"{year}-{mm}-{dd}"

                exp_type = self.read_run_parameters(name) or ""
                samples_data = self.read_samplesheet(name)

                # verifica se la Corsa esiste già
                corsa, created = Corsa.objects.get_or_create(
                    derivation_path=os.path.join(self.path, name),
                    defaults={
                        "date": formatted_date,
                        "description": name,
                        "type": exp_type
                    }
                )
                
                    # aggiunge solo i sample mancanti
                existing_sample_ids = set(corsa.samples.values_list('sample_id', flat=True))
                print('existing_sample_ids: ', existing_sample_ids)
                try:    
                    for s in samples_data:
                        print('s: ', s)
                        if s['Sample_ID'] not in existing_sample_ids:
                            Sample.objects.create(
                                sample_id=s['Sample_ID'],
                                sample_name=s['Sample_Name'],
                                corsa=corsa
                            )
                            print('after creation',s)
                except Exception as e:
                    print("ASSA", e)
                
                saved_corse.append({
                    "id": corsa.pk,
                    "folder_name": name,
                    "date": formatted_date,
                    "type": exp_type,
                    "samples": samples_data
                })

                #results.append({
                #    "original": name,
                #    "date": formatted_date,
                #    "description": f"A{data['description']}",
                #    "type":exp_type,
                #    "run": data["run"],
                #    "code": data["code"],
                #    "derivation_path": f"192.168.0.232/NovaSeq/NovaSeq/{name}"
                #})
        return saved_corse
    
    def read_samplesheet(self, folder_path):
        csv_path = f'{self.path}/{os.path.join(folder_path, "SampleSheet.csv")}'
        samples = []

        if os.path.exists(csv_path):
            with open(csv_path, newline='', encoding='utf-8') as f:
                # salta le righe fino a [Data]
                for line in f:
                    if line.strip() == "[Data]":
                        break
                # ora il reader legge la riga successiva come header
                reader = csv.DictReader(f)
                for row in reader:
                    if 'Sample_ID' in row and 'Sample_Name' in row:
                        samples.append({
                            "Sample_ID": row['Sample_ID'],
                            "Sample_Name": row['Sample_Name']
                        })
        return samples
    
    def read_run_parameters(self, folder_name):
        """Legge RunParameters.xml e ritorna il valore di <ExperimentName>"""

        folder_path = os.path.join(self.path, folder_name)
        xml_path = os.path.join(folder_path, "RunParameters.xml")
        if os.path.exists(xml_path):
            try:
                tree = ET.parse(xml_path)
                root = tree.getroot()
                # trova il primo ExperimentName
                exp_name = root.findtext('ExperimentName')
                if exp_name:
                    return exp_name
            except ET.ParseError:
                pass
        return None
    
    def export_csv(self, request, *args, **kwargs):
        """Esporta i risultati in un CSV"""
        try:
            results = self.get_folders()
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="folders.csv"'

            writer = csv.DictWriter(response, fieldnames=["original", "date", "description", "run", "code"])
            writer.writeheader()
            for row in results:
                writer.writerow(row)

            return response
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
       