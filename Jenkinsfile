pipeline {
    agent any
    environment 
    {
        id= "${params.id}"
    }
    stages {
        stage('Build') {
            steps {
               
                
            
             script{
                               $VERSION =powershell(
returnStdout:true,
script: '''
$Url="https://api.instantwebtools.net/v1/airlines/"
$data=Invoke-RestMethod -Method 'Get' -Uri $Url -Body $Body
$data | Where-Object {
    $_.id -eq $env:id
} | Select-Object name, country,logo,slogan

'''

)
echo $VERSION
          mongo --help
                
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
