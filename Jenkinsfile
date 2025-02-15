pipeline {
    agent any

    environment {
        NODEJS_HOME = tool 'nodejs' 
        PATH = "${NODEJS_HOME}/bin:${env.PATH}"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/danielnelsonp/web0.1.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'npm install'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'npm test'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t node-jenkins-demo .'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker run -d -p 3000:3000 node-jenkins-demo'
            }
        }
    }
}
