pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat """
        cmd_exec('echo "dir /a /b"')
        xcopy
        cmd_exec('echo "Buils starting..."')
      
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
