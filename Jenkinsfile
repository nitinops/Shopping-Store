pipeline {
    agent any
    stages {
        stage('Build') {
            steps{
                script
                {
 
 powershell """ 
 python pyscripting.py
 
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
