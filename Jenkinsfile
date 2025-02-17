pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:$PATH" // Ensure npm is in the PATH
    }

    tools {
        nodejs 'NodeJS' // Ensure Node.js is available in Jenkins
    }

    stages {
        stage('Setup') {
            steps {
                echo 'Checking Node.js and npm installation...'
                sh '''
                if ! command -v node >/dev/null 2>&1; then
                    echo "Node.js not found. Installing..."
                    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
                    sudo apt-get install -y nodejs
                fi
                node -v
                npm -v
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'Building...'
                sh 'npm install' // Installing dependencies
            }
        }

        stage('Test') {
            steps {
                echo 'Running Tests...'
                sh 'npm test' // Running tests
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh 'docker build -t myapp .' // Docker build

                // Check for port conflicts and find an available port
                script {
                    def port = 8081
                    def availablePort = port
                    def maxTries = 10
                    def tries = 0

                    while (tries < maxTries) {
                        def result = sh(script: "lsof -i :${availablePort}", returnStatus: true, script: true)
                        if (result != 0) {
                            echo "Port ${availablePort} is available."
                            break
                        } else {
                            tries++
                            availablePort++
                            echo "Port ${availablePort - 1} is occupied. Trying port ${availablePort}."
                        }
                    }

                    if (tries == maxTries) {
                        error "Unable to find an available port after ${maxTries} tries."
                    }

                    // Run the Docker container on the available port
                    sh "docker run -d -p ${availablePort}:80 myapp"
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
        always {
            script {
                if (currentBuild.result == null || currentBuild.result != 'FAILURE') {
                    echo "This runs only if the build is NOT failed."
                }
            }
        }
    }
}

