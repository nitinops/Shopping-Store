pipeline {
    agent any
    environment
    {
    Url="https://api.instantwebtools.net/v1/airlines"
    Body= '@{"name": "John Doe","trips": 250,"airline": 5}'
    }
    stages {
        stage('Build') {
            steps {
               
 
                script{
                               $VERSION =powershell(
returnStdout:true,
script: '''(Invoke-RestMethod -Method 'Post' -Uri ${env.Url} -Body "${env.Body}" -OutFile output.csv)'''

)
echo $VERSION
                
                }

                echo 'Building..'

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
