pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
            
                
           bat """
       
        cd c:\\Program Files\\Java\\jdk1.8.0_211\\bin
           
          echo 'Testing..'
          echo 'Testing..'
        """
                echo 'Testing....'
            }
        }
        stage('Test') {
            steps {
                bat """
       
        cd c:\\Program Files\\jdk-17_windows-x64_bin\\jdk-17.0.2\\bin
           
          echo 'Developing..'
          echo 'Developing..'
        """
                echo 'Developing....'
            }
        }
        stage('Deploy') {
            steps {
                bat """
       
        cd c:\\Program Files\\Robo 3T 1.4.4
           
          echo 'Developing..'
          echo 'Developing..'
        """
                echo 'Deploying....'
            }
        }
    }
}
