pipeline {

    agent any

    stages {

        stage('Clonar Repositorio') {
            steps {
                git 'https://github.com/wgoyola/IntegracionContinua.git'
            }
        }

        stage('Construir Docker') {
            steps {
                bat 'docker build -t integracioncontinua .'
            }
        }

        stage('Iniciar Contenedores') {
            steps {
                bat 'docker compose up -d'
            }
        }

        stage('Verificar') {
            steps {
                bat 'docker ps'
            }
        }
    }
}