pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
            
    bat """
 
       query = {'id':''}
response = requests.get('http://fakestoreapi.com/products', params=query)
print(response())
    }
}
                
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
