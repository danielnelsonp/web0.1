pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'master', credentialsId: '5b2c07d5-80dd-486a-8e83-76736e622d7e', url: 'git@github.com:danielnelsonp/web0.1.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'npm install'
                sh 'npm install --save-dev jest'  // Ensure Jest is installed
            }
        }

        stage('Run Tests') {
            steps {
                sh 'ls -la'                      // Debug workspace files
                sh 'cat package.json'            // Check JSON integrity
                sh 'ls -la node_modules/.bin/'   // Debug Jest installation
                sh 'npx jest --version'          // Verify Jest is available
                sh 'npx jest'                    // Run Jest tests
            }
        }

        stage('Build Docker Image') {
            when {
                not { failed() }
            }
            steps {
                sh 'test -f Dockerfile && docker build -t my-app:latest . || echo "Dockerfile not found!"'
            }
        }

        stage('Deploy') {
            when {
                not { failed() }
            }
            steps {
                sh 'chmod +x deploy.sh'
                sh './deploy.sh'
            }
        }
    }
}

