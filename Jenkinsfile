pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat """
                cd C:\Windows\System32
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
