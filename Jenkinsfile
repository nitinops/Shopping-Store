pipeline {
    agent any
    stages {
        stage('Build') {
            steps{
                script{
>>> import requests
>>> api_url = "https://jsonplaceholder.typicode.com/todos/1"
>>> response = requests.get(api_url)
>>> response.json()
{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
                    >>> response.status_code
200

>>> response.headers["Content-Type"]
'application/json; charset=utf-8'

            }   
                
             
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
    
    
