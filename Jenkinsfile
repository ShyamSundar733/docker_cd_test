pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-app"
        IMAGE_TAG  = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                sh "docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest"
            }
        }

        stage('Test') {
            steps {
                sh """
                    docker run -d --name test-container -p 5001:5000 ${IMAGE_NAME}:${IMAGE_TAG}
                    
                    curl -f http://localhost:5001/health || exit 1
                    docker stop test-container
                    docker rm test-container
                """
            }
        }

        stage('Deploy') {
            steps {
                sh """
                    docker stop flask-app || exit 0
                    docker rm flask-app || exit 0
                    docker run -d --name flask-app -p 5000:5000 ${IMAGE_NAME}:latest
                """
            }
        }
    }

    post {
        always {
            sh "docker system prune -f || exit 0"
        }
        success {
            echo "Pipeline succeeded! App is running on http://localhost:5000"
        }
        failure {
            echo "Pipeline failed"
        }
    }
}