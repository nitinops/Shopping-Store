pipeline {
    agent any
    stages {
        stage('Build') {
            steps{
            script{
            def get = new URL("http://fakestoreapi.com/products").openConnection();
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
    }
