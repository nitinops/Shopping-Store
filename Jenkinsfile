pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat """
        dir
        xcopy
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
