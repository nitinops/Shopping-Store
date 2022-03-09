pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
            
           bat """ az login """
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
