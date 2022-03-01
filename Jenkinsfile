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
$Body= @{
$Response.InputFields | Where-Object {
    $_.name -like "* Value*"
} | Select-Object Name, Value
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
