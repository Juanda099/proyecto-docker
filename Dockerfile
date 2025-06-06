# Usa la imagen base de Python
FROM python:3.10

# Instala el cliente MySQL
RUN apt-get update && \
    apt-get install -y default-mysql-client && \
    apt-get clean

# Crea el directorio de trabajo
WORKDIR /app

# Copia los archivos
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

COPY wait-for-db.sh .

# Da permisos de ejecución al script de espera
RUN chmod +x wait-for-db.sh

# Comando por defecto se define en docker-compose.yml (con el script)
