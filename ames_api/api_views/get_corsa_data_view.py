import os
import re
import csv
import xml.etree.ElementTree as ET
from django.http import JsonResponse, HttpResponse
from django.views import View


class CorsaSampleCreateView(View):
    path = "/mnt/nas/NovaSeq"
    pattern = re.compile(
        r'^(?P<date>\d{6})_A(?P<description>\d+)_(?P<run>\d{4})_(?P<code>[A-Z0-9]+)$'
    )
    def get(self, request, *args, **kwargs):
        try:
            results = self.get_folders()
            for folder in results:
                folder['samples'] = self.read_samplesheet(folder['original'],)
            return JsonResponse({"results": results})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def get_folders(self):
        results = []
        for name in os.listdir(self.path):
            match = self.pattern.match(name)
            if match:
                data = match.groupdict()

                yy = int(data["date"][:2])
                mm = data["date"][2:4]
                dd = data["date"][4:6]
                year = 2000 + yy
                formatted_date = f"{year}-{mm}-{dd}"

                exp_type = self.read_run_parameters(name)

                results.append({
                    "original": name,
                    "date": formatted_date,
                    "description": f"A{data['description']}",
                    "type":exp_type,
                    "run": data["run"],
                    "code": data["code"],
                    "derivation_path": f"192.168.0.232/NovaSeq/NovaSeq/{name}"
                })
        return results
    
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
       