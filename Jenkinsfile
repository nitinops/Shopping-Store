pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
            
                
           bat """
        cd C:"\Program Files\Java\jdk1.8.0_211\bin"
           
          echo 'Testing..'
          echo 'Testing..'
        """
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
