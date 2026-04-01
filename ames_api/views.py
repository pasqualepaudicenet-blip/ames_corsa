import csv
import io, os
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from .models import Sample
from django.conf import settings

#def upload_csv(request):
#    if request.method == "POST":
#        csv_file = request.FILES.get('file')
#        
#        # Controllo se il file è presente e se è un CSV
#        if not csv_file or not csv_file.name.endswith('.csv'):
#            messages.error(request, 'Per favore carica un file CSV valido.')
#            return render(request, 'upload.html')
#
#        # Leggiamo il file
#        data_set = csv_file.read().decode('UTF-8')
#        io_string = io.StringIO(data_set)
#        
#        # Saltiamo l'intestazione (header)
#        next(io_string)
#
#        for row in csv.reader(io_string, delimiter=',', quotechar='"'):
#            # row[1] è SAMPLEID, row[2] è SAMPLENAME basandosi sul file creato prima
#            _, created = Sample.objects.update_or_create(
#                sample_id=row[1],
#                defaults={'sample_name': row[2]}
#            )
#
#        messages.success(request, 'Dati importati con successo!')
#    
#    return render(request, 'upload.html')


def import_local_csv(request):
    # Costruisce il percorso assoluto: /percorso/progetto/data/dati_campioni.csv
    file_path = os.path.join(settings.BASE_DIR, '', 'example.csv')

    # Verifica se il file esiste davvero
    if not os.path.exists(file_path):
        return HttpResponse("Errore: Il file CSV non è stato trovato nella cartella 'dawta'.")

    try:
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            # Usiamo DictReader per accedere alle colonne tramite il loro nome (ID, SAMPLEID, ecc.)
            reader = csv.DictReader(csv_file)
            
            count = 0
            for row in reader:
                # Accediamo direttamente ai nomi delle colonne definiti nel CSV
                Sample.objects.update_or_create(
                    sample_id=row['SAMPLEID'],
                    defaults={'sample_name': row['SAMPLENAME']}
                )
                count += 1

        return HttpResponse(f"Importazione completata! Processate {count} righe.")
    
    except Exception as e:
        return HttpResponse(f"Si è verificato un errore durante la lettura: {e}")