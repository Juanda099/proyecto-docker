FROM python:3.10

RUN apt-get update && \
    apt-get install -y default-mysql-client && \
    apt-get clean

WORKDIR /app

# Primero copiamos requirements e instalamos
COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Después copiamos toda la aplicación
COPY . .

# Damos permisos de ejecución al script de espera
RUN chmod +x wait-for-db.sh
