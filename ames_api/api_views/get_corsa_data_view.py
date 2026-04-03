import os
import re
from django.http import JsonResponse, HttpResponse
from django.views import View

class CorsaListView(View):
    path = "/mnt/nas/NovaSeq"
    pattern = re.compile(
        r'^(?P<date>\d{6})_A(?P<machine>\d+)_(?P<run>\d{4})_(?P<code>[A-Z0-9]+)$'
    )
    def get(self, request, *args, **kwargs):
        try:
            results = self.get_folders()
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

                results.append({
                    "original": name,
                    "date": formatted_date,
                    "machine": f"A{data['machine']}",
                    "run": data["run"],
                    "code": data["code"]
                })
        return results

    def export_csv(self, request, *args, **kwargs):
        """Esporta i risultati in un CSV"""
        try:
            results = self.get_folders()
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="folders.csv"'

            writer = csv.DictWriter(response, fieldnames=["original", "date", "machine", "run", "code"])
            writer.writeheader()
            for row in results:
                writer.writerow(row)

            return response
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        path = "/mnt/nas/NovaSeq"
        #pattern = re.compile(r'^\d{6}_A\d+_\d{4}_[A-Z0-9]+$')

        pattern = re.compile(
            r'^(?P<date>\d{6})_A(?P<machine>\d+)_(?P<run>\d{4})_(?P<code>[A-Z0-9]+)$'
        )

        results = []
        try:
            for name in os.listdir(path):
                match = pattern.match(name)
                if match:
                    data = match.groupdict()

                    yy = int(data["date"][:2])
                    mm = data["date"][2:4]
                    dd = data["date"][4:6]
                        
                    year = 2000 + yy  
                    formatted_date = f"{year}-{mm}-{dd}"

                    results.append({
                        "original": name,
                        "date": formatted_date,
                        "machine": f"A{data['machine']}",
                        "run": data["run"],
                        "code": data["code"]
                    })
            return JsonResponse({"results": results})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    #try:
    #    folders = [
    #        name for name in os.listdir(path)
    #        if os.path.isdir(os.path.join(path, name)) and pattern.match(name)
    #    ]
    #    return JsonResponse({"folders": folders})
    #except Exception as e:
    #    return JsonResponse({"error": str(e)}, status=500)