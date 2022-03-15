pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
            def get = new URL("https://httpbin.org/get").openConnection();
def getRC = get.getResponseCode();
println(getRC);
if(getRC.equals(200)) {
    println(get.getInputStream().getText());
}

           
                
             
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
