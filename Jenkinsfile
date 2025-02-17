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
                
                // Build the Docker image
                sh 'docker build -t myapp .'
                
                // Check if the port is already in use
                script {
                    def portInUse = false
                    def port = 8081

                    // Check if the port is in use
                    def checkPortCmd = "lsof -i :${port}"
                    def result = sh(script: checkPortCmd, returnStatus: true)

                    if (result == 0) {
                        echo "Port ${port} is already in use."
                        portInUse = true
                    } else {
                        echo "Port ${port} is available."
                    }

                    // If the port is in use, try a different port
                    if (portInUse) {
                        def newPort = 8082
                        echo "Switching to port ${newPort}."
                        sh "docker run -d -p ${newPort}:80 myapp"
                    } else {
                        // Port is available, proceed with deployment
                        sh "docker run -d -p ${port}:80 myapp"
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
            echo 'Monitoring job history for stability...'
            // Removed jenkins-cli command
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

