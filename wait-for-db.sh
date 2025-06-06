#!/bin/bash
echo "Esperando a MySQL..."

until mysql -h db -u root -ppassword -e "SHOW DATABASES;" > /dev/null 2>&1; do
  sleep 2
done

echo "✅ MySQL listo. Creando tablas..."
python -c "from models import create_tables; create_tables()"

echo "Iniciando aplicación Flask..."
exec "$@"
