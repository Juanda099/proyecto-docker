FROM python:3.10

RUN apt-get update && \
    apt-get install -y default-mysql-client && \
    apt-get clean

WORKDIR /app

# ✅ Establece PYTHONPATH para que Python pueda encontrar main.py
ENV PYTHONPATH=/app

# Copiar primero los requirements desde la carpeta app/
COPY app/requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Luego copiar SOLO el contenido de app/ (no toda la raíz)
COPY app/ .

# Copiar la carpeta de tests desde la raíz del proyecto
COPY tests/ ./tests

# Copiar el script de espera que sí está en la raíz del proyecto
COPY wait-for-db.sh .

# Dar permisos de ejecución
RUN chmod +x wait-for-db.sh
