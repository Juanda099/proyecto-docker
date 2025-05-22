#!/bin/bash
echo "Esperando a que MySQL esté lista..."

until mysql -h db -u root -ppassword -e "SHOW DATABASES;" > /dev/null 2>&1; do
  echo "⏳ Esperando conexión a MySQL en db:3306..."
  sleep 2
done

echo "✅ Conexión exitosa con MySQL. Iniciando aplicación Flask..."
exec "$@"
