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

    "_id": "5ef4a412aab3841847750ce8",
    "name": "John Doe",
    "trips": 250,
    "airline": [
        {
            "id": 5,
            "name": "Eva Air",
            "country": "Taiwan",
            "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/e/ed/EVA_Air_logo.svg/250px-EVA_Air_logo.svg.png",
            "slogan": "Sharing the World, Flying Together",
            "head_quaters": "376, Hsin-Nan Rd., Sec. 1, Luzhu, Taoyuan City, Taiwan",
            "website": "www.evaair.com",
            "established": "1989"
        }
    ],
    "__v": 0


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
