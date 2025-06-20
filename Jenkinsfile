pipeline {
    agent any
    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials')
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Juanda099/proyecto-docker.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker compose build'
            }
        }
        stage('Test') {
            steps {
                // Aquí inclimos los tests unitarios
                echo "Ejecutando pruebas..."
          
                // 🔍 Análisis SonarCloud
                  {
                    sh """
                         sonar-scanner \
                        -Dsonar.organization=FredyRod \
                        -Dsonar.projectKey=fredyrod_sonar-fredyrod \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=https://sonarcloud.io \
                        -Dsonar.login=1e4fc733fc38d86178d729f0ba08088039b13727
                    """
            }
        }
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh 'docker compose down --remove-orphans' // 🔥 Detiene y elimina contenedores viejos
                sh 'docker compose build --no-cache'      // 🔁 Fuerza rebuild de las imágenes
                sh 'docker compose up -d'                 // 🚀 Vuelve a levantar los servicios
            }
        }
        stage('Verificación') {
            steps {
                sh 'which docker'
                sh 'docker --version'
                sh 'docker compose version || docker-compose --version'
            }
        }

    }
    post {
        always {
            echo 'Pipeline completado'
        }
        failure {
            echo 'Pipeline falló'
        }
    }
}
