pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
            
           
                
             withCredentials([azureServicePrincipal(credentialsId: '4651382e-5cd7-4503-875a-595730238b31',
                                    subscriptionIdVariable: 'SUBS_ID',
                                    clientIdVariable: 'CLIENT_ID',
                                    clientSecretVariable: 'CLIENT_SECRET',
                                    tenantIdVariable: 'TENANT_ID')]) {
    powershell """
  
    az login --service-principal -u $CLIENT_ID -p $CLIENT_SECRET -t $TENANT_ID
    az account set --name $SUBS_ID
    dotnet publish -o PublishFolder
    Compress-Archive -DestinationPath ./PublishFolder.zip -Path ./PublishFolder
    Compress-Archive -DestinationPath ./PublishFolder.zip -Path ./PublishFolder -Force
    az webapp deployment source config-zip \
    -g "MyFirst_Jenkins_API" -n "myfirstwebAzure" \
    --src "./PublishFolder.zip"
                
   """
}
                
            }
        }
        stage('Test') {
            steps {
               
             echo 'Testing....'
            }
        }
        stage('Deploy') {
            steps {
                
                echo 'Deploying....'
            }
        }
    }
