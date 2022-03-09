pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
            
           bat """ az login --service-principal -u ff417966-c1d5-4058-92ae-e759de533da6 -p Eq-7Q~dkUr-MpF4mmvKA538ba9pt7mz3t6tf4 -t 95b3fd34-bb88-48e0-8e3a-33fa33a1c53a """
                

            }
        }
        stage('Test') {
            steps {
               
             echo 'Testing....'
            }
        }
        stage('Deploy') {
            steps {
                
                echo 'Deploying....'
            }
        }
    }
}
