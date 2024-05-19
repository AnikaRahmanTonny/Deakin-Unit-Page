pipeline {
    agent any

    environment {
        DIRECTORY_PATH = '/path/to/code/directory'
        TESTING_ENVIRONMENT = 'Staging'
        PRODUCTION_ENVIRONMENT = 'Production' 
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building the code...'
                //sh 'mvn clean install' // Placeholder for Maven build command test
            }
        }

        stage('Unit and Integration Tests') {
            steps {
                echo 'Running unit tests...'
                //sh 'mvn test' // Placeholder for running unit tests with Maven
                echo 'Running integration tests...'
                //sh 'mvn integration-test' // Placeholder for running integration tests
            }

            post {
                success {
                    // Send email notification on test success
                    emailext body: "Test Stage: Success\n\nPlease find attached test logs.",
                             subject: "Pipeline Test Status: Success",
                             to: 'tonnyanikarahman10@gmail.com',
                             attachmentsPattern: "sample.log"
                }
                failure {
                    // Send email notification on test failure
                    emailext body: "Test Stage: Failure\n\nPlease find attached test logs.",
                             subject: "Pipeline Test Status: Failure",
                             to: ''tonnyanikarahman10@gmail.com ',
                             attachmentsPattern: "sample.log"
                }
            }
        }

        stage('Code Analysis') {
            steps {
                echo 'Analyzing code...'
                //sh 'sonar-scanner' // Placeholder for SonarQube code analysis
            }
        }

        stage('Security Scan') {
            steps {
                echo 'Performing security scan...'
                //sh 'owasp-zap -scan' // Placeholder for OWASP ZAP security scan
            }

            post {
                success {
                    // Send email notification on security scan success
                    emailext body: "Security Scan Stage: Success\n\nPlease find attached security scan logs.",
                             subject: "Pipeline Security Scan Status: Success",
                             to: ''tonnyanikarahman10@gmail.com ',
                             attachmentsPattern: "*.log"
                }
                failure {
                    // Send email notification on security scan failure
                    emailext body: "Security Scan Stage: Failure\n\nPlease find attached security scan logs.",
                             subject: "Pipeline Security Scan Status: Failure",
                             to: ''tonnyanikarahman10@gmail.com’,
                             attachmentsPattern: "*.log"
                }
            }
        }

        stage('Deploy to Staging') {
            steps {
                echo 'Deploying to staging environment...'
                //sh 'ssh user@staging-server "deploy-script.sh"' // Placeholder for deployment to staging server
            }
        }

        stage('Integration Tests on Staging') {
            steps {
                echo 'Running integration tests on staging...'
                //sh 'mvn verify' // Placeholder for running tests on staging environment
            }
        }

        stage('Deploy to Production') {
            steps {
                echo 'Deploying to production environment...'
                //sh 'ssh user@production-server "deploy-script.sh"' // Placeholder for deployment to production server
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
        success {
            emailext body: 'Pipeline succeeded. All stages completed successfully.',
                     subject: 'Pipeline Status: Success',
                     to: 'tonnyanikarahman10@gmail.com',
                     attachmentsPattern: '**/*.log'
        }
        failure {
            emailext body: 'Pipeline failed. Check logs for details.',
                     subject: 'Pipeline Status: Failure',
                     to: 'tonnyanikarahman10@gmail.com',
                     attachmentsPattern: '**/*.log'
        }
    }
}


