FROM python:3.12-slim

# Installazione dipendenze di sistema e Driver Microsoft
RUN apt-get update && apt-get install -y \
    gnupg2 \
    curl \
    ca-certificates \
    g++ \
    build-essential \
    unixodbc-dev \
    && curl -sSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /usr/share/keyrings/microsoft.gpg \
    && echo "deb [signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    g++ \
    build-essential \
    unixodbc-dev \
    && apt-get clean

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Rende lo script eseguibile e lo imposta come comando di avvio
RUN chmod +x wait-for-db.sh
CMD ["./wait-for-db.sh"]