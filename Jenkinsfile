pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
               
                script{
                    
 $VERSION =powershell(
returnStdout:true,
                   
$Body = @{
    search = "search index=_internal | reverse | table index,host,source,sourcetype,_raw"
    output_mode = "csv"
    earliest_time = "-2d@d"
    latest_time = "-1d@d"
}
script: '''(Invoke-RestMethod -Method 'Post' -Uri https://api.instantwebtools.net/v1/airlines -Credential $Cred -
    $body -OutFile output.csv

)'''


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
