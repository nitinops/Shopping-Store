pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
               
                script{
                               $VERSION =powershell(
returnStdout:true,


def Url = "https://api.instantwebtools.net/v1/airlines"
 def Body = @{
    
    "name": "John Doe",
    "trips": 250,
    "airline": 5

}
                                   script: '''(Invoke-RestMethod -Method 'Post' -Uri "${Url}" -Credential $Cred -Body "${Body}" -OutFile output.csv

)'''



                echo $Cred
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
