pipeline {
    agent any
  
    stages {
        stage('Build') {
            steps {
               
 
                script{
                               $VERSION =powershell(
returnStdout:true,
script: '''
$Url="https://api.instantwebtools.net/v1/airlines"
$Body= @{"name": "John Doe","trips": 250,"airline": 5}
$data=Invoke-RestMethod -Method 'Post' -Uri $Url -Body $Body
Write-Host $data
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
