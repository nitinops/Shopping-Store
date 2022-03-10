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
    
    az login --service-principal -u $CLIENT_ID -p $CLIENT_SECRET -t $TENANT_ID || az account set --name $SUBS_ID
                
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
}
