pipeline {
    agent any
    stages {
        stage('Build') {
            steps{
                script
                {
 
 powershell """ import requests
 api_url = "https://jsonplaceholder.typicode.com/todos/1"
 response = requests.get(api_url)
 print(response.json)
print(response.status_code)
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
