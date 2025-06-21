pipeline {
    agent any

    environment {
        COVERAGE_DIR = 'htmlcov'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo "Simulación del proceso de construcción"
            }
        }
    stage('Run Tests with Coverage') {
        steps {
            script {
                // Limpiar y construir
                sh 'docker compose down --remove-orphans || true'
                sh 'docker compose build --no-cache web'
                sh 'docker compose up -d db'
                
                // Crear directorio para cobertura
                sh "mkdir -p ${WORKSPACE}/${COVERAGE_DIR}"
                
                // Ejecutar pruebas en contenedor temporal
                def containerId = sh(script: 'docker compose run -d --rm web sleep infinity', returnStdout: true).trim()
                
                // Ejecutar pytest dentro del contenedor
                sh """
                    docker exec ${containerId} sh -c '
                        pytest --cov=main --cov-report=html:/tmp/htmlcov tests
                    '
                """
                
                // Copiar reportes desde contenedor a host
                sh """
                    docker cp ${containerId}:/tmp/htmlcov ${WORKSPACE}/${COVERAGE_DIR}
                    docker stop ${containerId}
                """
                
                // Verificar contenido copiado
                echo "=== Verificación de archivos en ${WORKSPACE}/${COVERAGE_DIR} ==="
                sh "ls -la ${WORKSPACE}/${COVERAGE_DIR} || true"
                sh "ls -R ${WORKSPACE}/${COVERAGE_DIR} || true"
                
                // Ajustar permisos
                sh "chmod -R a+rX ${WORKSPACE}/${COVERAGE_DIR}"
            }
        }
    }
        stage('Archive Coverage Report') {
            steps {
                sh """
                    echo "=== Verificando htmlcov justo antes de archiveArtifacts ==="
                    ls -la "${WORKSPACE}/${COVERAGE_DIR}" || true
                    ls -R "${WORKSPACE}/${COVERAGE_DIR}" || true
                """
                archiveArtifacts artifacts: "${COVERAGE_DIR}/**", allowEmptyArchive: false
                echo "Reporte de cobertura archivado en ${WORKSPACE}/${COVERAGE_DIR}/"
            }
        }
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo "Simulación del despliegue (solo en rama main)"
            }
        }
        stage('Verificación') {
            steps {
                echo "Simulación de verificación del entorno"
            }
        }
    }

    post {
        always {
            sh 'docker compose down --remove-orphans || true'
            echo '✅ Pipeline completado'
        }
        failure {
            echo '❌ Pipeline falló'
        }
    }
}
