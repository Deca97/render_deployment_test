# Base image
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Copia i file
COPY . .

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Comando di avvio dell'app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
