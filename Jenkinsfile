pipeline {
    agent any
    stages {
        stage('Build') {
            steps{
            script{
            import requests
response = requests.get("http://api.open-notify.org/astros.json")
print(response)
>>>> Response<200>


           
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
    }
