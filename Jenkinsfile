pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
               
                script{
                    
                $VERSION =powershell(
returnStdout:true,
script: '''(Invoke-RestMethod -Method 'Get' -Uri 'http://dummy.restapiexample.com/api/v1/employees')'''
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
