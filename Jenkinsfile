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
                sh 'docker run -d -p 8080:80 myapp' // Running container
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
            echo 'Monitoring job history for stability...'
            sh 'jenkins-cli list-jobs' // Monitoring Jenkins jobs
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

