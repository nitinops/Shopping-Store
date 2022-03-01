pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
               
                script{
                    

$Cred = Get-Credential
$Url = "https://api.instantwebtools.net/v1/airlines"
$Body = @{
    
    "name": "John Doe",
    "trips": 250,
    "airline": 5

}
Invoke-RestMethod -Method 'Post' -Uri $https://api.instantwebtools.net/v1/airlines -Credential $Cred -Body $body -OutFile output.csv



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
