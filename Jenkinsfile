pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
            
                
           bat """
            cd freddie-app
            mvn clean package
        
       
      
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
