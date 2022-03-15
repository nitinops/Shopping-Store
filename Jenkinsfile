pipeline {
    agent any
    stages {
        stage('Build') {
            steps{
                script{
                    import requests
response = requests.get("http://api.open-notify.org/astros.json")
print(response)
         response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
print(response.json())



           
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
    }
    
