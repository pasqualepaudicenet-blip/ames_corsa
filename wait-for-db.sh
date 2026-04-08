#!/bin/bash
# Attende che la porta 1433 del database sia aperta
until timeout 1 bash -c "echo > /dev/tcp/db/1433" 2>/dev/null; do
  echo "SQL Server non è ancora pronto... attendo 1 secondo"
  sleep 1
done

echo "SQL Server è pronto! Eseguo le migrazioni..."
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000