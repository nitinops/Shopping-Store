pipeline {
    agent any
    environment 
    {
    id= params.id
    }
    stages {
        stage('Build') {
            steps {
               
                
            
             script{
                               $VERSION =powershell(
returnStdout:true,
script: '''
$Url="https://api.instantwebtools.net/v1/airlines/$env:id"
Invoke-RestMethod -Method 'Get' -Uri $Url -Body $Body

'''

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
