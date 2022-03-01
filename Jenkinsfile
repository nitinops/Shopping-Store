pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
               
                script{
                    
                $VERSION =powershell(
returnStdout:true,
script: '''(Invoke-RestMethod -Method 'Post' -Uri https://api.instantwebtools.net/v1/airlines -Credential $Cred -{
    "name": "John Doe",
    "trips": 250,
    "airline": 5
} $body -OutFile output.csv

)'''
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
