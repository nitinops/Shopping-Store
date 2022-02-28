pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script{
                    $url='http://dummy.restapiexample.com/api/v1/employees'
                VERSION =powershell(
returnStdout:true,
script: '''(Invoke-RestMethod -Method 'Get' -Uri $url)'''
)
                
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
