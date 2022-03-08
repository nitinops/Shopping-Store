pipeline {
   agent { label 'master' }
   parameters {
      choice(choices: ['Success', 'Failure'], description:  'Expected status', name: 'expected')
   }
   stages {
       stage('build') {
           steps {
               echo "Hello World!"
               sh "pwd"
               sh "printenv | sort"
               println("Number: ${currentBuild.number}")
               println("Result: ${currentBuild.result}")
               println("Display name: ${currentBuild.displayName}")
               println("Expected: ${params.expected}")
               script {
                   //manager.addShortText("Foo Bar ${params.expected}")
                   //manager.addShortText("\nSome text", "black", "yellow", "0px", "white")
                   //currentBuild.displayName = "hello"
                   //currentBuild.description = "hello this is going to be a long line and I don't know what will happen now\nworld\nhow\nare\nyou"
                   def description = ""
                   description = "First\n"
                   description += "Second\n"
                   description += "Third\n"
                   description += "Fourth\n"
                   description += "Fifth\n"
                   description += "Sixth\n"
                   currentBuild.description = "${description}"
                                  //manager.addBadge("star-gold.gif", "Successful build")
                   def commands = ["xyz", "abc", "pwd"]
                   def errors = ''
                   commands.each {
                       def res = sh(script: it, returnStatus: true)
                       println("cmd: $it res $res")
                       if (res !=0 ) {
                           errors += " $it"
                       }
                   }
 
                   //if (params.expected == 'Success') {
                   //    sh "pwd"
                   //} else {
                   //    sh "xyz"
                   //}
                   if (errors) {
                       error(errors)
                   }
                                  }
           }
       }
   }
   post {
       always {
           echo "post always"
           println("Number: ${currentBuild.number}")
           println("Result: ${currentBuild.result}")
           println("Display name: ${currentBuild.displayName}")
           script {
               text = "Result: ${currentBuild.result}"
           }
           println('----------')
           println(currentBuild.getPreviousBuild())
           println(currentBuild.getPreviousBuild().result)
           println('----------')
       }
       success {
           echo "post success"
           echo text
       }
       failure {
           echo "post failure"
       }
   }
}
