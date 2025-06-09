# 🐳 Proyecto Flask + MySQL con Docker

## 🔹 Nombre del estudiante:
**Juan David**

## 🔹 Nombre del proyecto:
**Aplicación Flask con base de datos MySQL usando Docker**

## 🔹 Descripción general

Durante esta semana se implementó un proyecto web utilizando el microframework **Flask** junto con una base de datos **MySQL**. Todo el entorno fue montado y gestionado mediante **Docker**, permitiendo ejecutar los servicios en contenedores que se comunican entre sí a través de una red virtual definida por `docker-compose`.

## 🔹 Objetivo

Emplear Docker como herramienta de integración continua para construir dos contenedores:
- Uno que contenga la aplicación web desarrollada con Flask.
- Otro que contenga la base de datos MySQL.

## 🔹 Tecnologías utilizadas

| Herramienta/Tecnología | Versión/Descripción                  |
|------------------------|--------------------------------------|
| Python                 | 3.x                                  |
| Flask                  | Microframework para aplicaciones web |
| MySQL                  | Motor de base de datos relacional    |
| Docker                 | Contenedores                         |
| Docker Compose         | Orquestación de contenedores         |
| Git/GitHub             | Control de versiones                 |

## 🔹 Estructura del proyecto

proyecto-docker/
├── app/
│ ├── app.py
│ └── requirements.txt
├── docker-compose.yml
├── Dockerfile
└── README.md


## 🔹 Contenedores definidos

1. **web** – Contenedor para la aplicación Flask.
   - Construido con `Dockerfile`.
   - Expone el puerto `5000`.

2. **db** – Contenedor con imagen oficial de MySQL.
   - Usa volumen para persistencia de datos.
   - Expone el puerto `3306`.

Ambos contenedores se gestionan desde `docker-compose.yml` y están conectados a través de una red virtual interna de Docker.

## 🔹 Comunicación entre contenedores

- Se usó el nombre del servicio `db` como host en la conexión MySQL dentro de Flask (`host='db'`).
- Docker Compose se encarga de la red interna que permite esta comunicación sin necesidad de configurar IPs.

## 🔹 Comando para levantar el entorno

```bash
docker-compose up --build

✅ Conexión exitosa con MySQL. Iniciando aplicación Flask...
http://localhost:8000


📎 https://github.com/Juanda099/proyecto-docker

# Prueba de webhook con Jenkins y ngrok
# Prueba #2 credenciales. 
# Prueba de conexión, GitHub y Jenkins. 
# Prueba de conexión, GitHub, y Jenkins, Wedhooks
# Nueva Prueba. 
# Nuevo push, prueba en github, y jenkins
# Nuevo push, prueba en github, y jenkins, falla en el puerto, 8000, ahora en 8081
# Nueva prueba
# Nueva prueba 2
# Nueva prueba 3