pipeline {
    agent any
    stages {
        stage('Build') {
            steps{
                script
                {
 
 bat """ python pyscripting.py
 
"""


            }   
                
             
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
