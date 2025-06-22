# 🐳 Proyecto Flask + MySQL con Docker

## 🔹 Autores:
- **Juan David Ramírez Calderón**
- **Fredy Rodríguez**
- **Brayan Salguero**


## 🔹 Descripción general

Este proyecto implementa una aplicación web desarrollada con **Flask** (Python) que interactúa con una base de datos **MySQL**. Todo el entorno se ejecuta en contenedores Docker, orquestados mediante **Docker Compose**, lo que facilita el desarrollo, pruebas, despliegue y la integración continua.

---

## 🔹 Objetivo

- Demostrar cómo construir y conectar una aplicación Flask y una base de datos MySQL usando Docker.
- Implementar prácticas de **Integración Continua/Entrega Continua (CI/CD)** con Jenkins y GitHub Actions.

---

## 🔹 Tecnologías utilizadas

| Herramienta/Tecnología | Versión/Descripción                  |
|------------------------|--------------------------------------|
| Python                 | 3.10                                 |
| Flask                  | Microframework para aplicaciones web |
| MySQL                  | 8.0                                  |
| Docker                 | Contenedores                         |
| Docker Compose         | Orquestación de contenedores         |
| Jenkins                | Automatización CI/CD                 |
| GitHub Actions         | Automatización CI/CD                 |
| pytest/pytest-cov      | Pruebas y cobertura                  |

---

## 🔹 Estructura del proyecto

```
proyecto-docker/
├── app/
│   ├── main.py
│   ├── requirements.txt
│   ├── ... (otros módulos, rutas, modelos)
├── tests/
│   ├── test_main.py
│   └── test_example.py
├── Dockerfile
├── docker-compose.yml
├── wait-for-db.sh
├── Jenkinsfile
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```

---

## 🔹 Contenedores definidos

1. **web** – Contenedor para la aplicación Flask.
   - Construido con el `Dockerfile` del proyecto.
   - Expone el puerto `5000` (mapeado a `8000` en el host).
   - Espera a que la base de datos esté lista antes de iniciar.
   - Usa variables de entorno para conectarse a MySQL.

2. **db** – Contenedor con imagen oficial de MySQL.
   - Configurado con usuario, contraseña y base de datos inicial.
   - Expone el puerto `3306` (mapeado a `3311` en el host).
   - Incluye healthcheck para asegurar que el servicio esté listo antes de que la app intente conectarse.

3. **jenkins** – Contenedor para Jenkins (CI/CD).
   - Imagen personalizada.
   - Expone el puerto `8080` (mapeado a `8081` en el host).
   - Monta volúmenes para persistencia y acceso al socket Docker.

---

## 🔹 Comunicación entre contenedores

- Los servicios se comunican a través de una red interna creada por Docker Compose.
- La aplicación Flask usa el nombre del servicio `db` como host para conectarse a MySQL (`DB_HOST=db`).

---

## 🔹 Comando para levantar el entorno

```bash
docker-compose up --build
```

- Accede a la aplicación en: [http://localhost:8000](http://localhost:8000)
- Jenkins disponible en: [http://localhost:8081](http://localhost:8081)

---

## 🔹 Integración Continua/Entrega Continua (CI/CD)

### Jenkins

- El pipeline definido en `Jenkinsfile` automatiza:
  - Descarga del código (`Checkout`)
  - Construcción de imágenes Docker (`Build`)
  - Ejecución de pruebas unitarias y de integración con cobertura (`Run Tests with Coverage`)
  - Archivado de reportes de cobertura (`Archive Coverage Report`)
  - Simulación de despliegue en rama `main` (`Deploy`)
  - Verificación post-despliegue (`Verificación`)
- Usa Docker Compose para levantar los servicios y ejecutar pruebas en un entorno idéntico al de producción.

### GitHub Actions

- Workflow definido en `.github/workflows/ci.yml`:
  - Se ejecuta en cada push a la rama `main`.
  - Levanta un servicio MySQL y ejecuta pruebas en el contenedor Flask usando Docker Compose.
  - Genera reportes de cobertura.

---

## 🔹 Pruebas

- Las pruebas están en la carpeta `tests/`.
- Se ejecutan automáticamente en los pipelines de CI/CD.
- Ejemplo de ejecución manual:
  ```bash
  docker compose run web pytest --cov=main --cov-report=term-missing tests
  ```

---

## 🔹 Scripts y utilidades

- **wait-for-db.sh:**  
  Script que espera a que MySQL esté listo antes de iniciar la aplicación Flask y crear las tablas necesarias.

---

## 🔹 Buenas prácticas y recomendaciones

- Usa variables de entorno para credenciales y configuración sensible.
- Agrega un volumen para persistencia de datos de MySQL si se requiere mantener la información tras reinicios.
- Amplía la cobertura de pruebas y el manejo de errores en la aplicación.
- No expongas contraseñas en archivos de configuración en producción.

---

## 🔹 Enlaces útiles

- [Repositorio en GitHub](https://github.com/Juanda099/proyecto-docker)

---

## 🔹 Ejemplo de uso

```bash
# Levantar el entorno completo
docker-compose up --build

# Acceder a la app
http://localhost:8000

# Acceder a Jenkins
http://localhost:8081
```

---
