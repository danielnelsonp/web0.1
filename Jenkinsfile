pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install the latest npm version
                    sh(script: "npm install -g npm@latest")
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    // Run npm install to install dependencies
                    sh(script: "npm install")
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run tests
                    sh(script: "npm test")
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Build the Docker image
                    sh(script: "docker build -t myapp .")
                }

                script {
                    // Check if port 8081 is available
                    def result = sh(script: "lsof -i :8081", returnStdout: true).trim()
                    if (result) {
                        echo "Port 8081 is already in use, skipping deployment"
                    } else {
                        // Run the Docker container if port 8081 is available
                        sh(script: "docker run -d -p 8081:80 myapp")
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up after the pipeline run'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}

