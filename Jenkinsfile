pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                $url='http://dummy.restapiexample.com/api/v1/employees'
                script{
                    
                $VERSION =powershell(
returnStdout:true,
script: '''(Invoke-RestMethod -Method 'Get' -Uri $url)'''
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
