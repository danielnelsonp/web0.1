
peline {
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
                sh 'docker run -d -p 8081:80 myapp' // Running container
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
lHost *:80>
    ServerAdmin admin@localhost
    DocumentRoot /var/www/html/drupal
    ServerName drupal.local

    <Directory /var/www/html/drupal>
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

