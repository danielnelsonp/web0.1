pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // Add build commands here
                sh 'npm install' // Example: Installing dependencies
            }
        }
        stage('Test') {
            steps {
                echo 'Running Tests...'
                // Add test scripts here
                sh 'npm test' // Example: Running tests
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // Add deployment steps here
                sh 'docker build -t myapp .' // Example: Docker build
                sh 'docker run -d -p 8080:80 myapp' // Example: Running container
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
            echo 'Monitoring job history for stability...'
            sh 'jenkins-cli list-jobs' // Example: Monitoring Jenkins jobs
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

