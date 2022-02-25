pipeline {
    agent any

    stages {
        stage('Build') {
            steps {

                echo 'Building..'
                             "C:\Program Files\dotnet\"dotnet msbuild "Shoping Store.csproj" /p:DeployOnBuild=true /p:PublishProfile="myDotnetApplication - Web Deploy.pubxml" /p:Password="2hXkavMLL6H0cryR6CAZo38sajsMqg6qtgJvPutudhu7D5vFgb6jPioZ2KdC"

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
