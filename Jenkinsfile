pipeline {
    agent any
  
    stages {
        stage('Build') {
            steps {
               
 
                script{
                               $VERSION =powershell(
returnStdout:true,
script: '''
$Response = Invoke-WebRequest -URI https://www.bing.com/search?q=how+many+feet+in+a+mile
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
