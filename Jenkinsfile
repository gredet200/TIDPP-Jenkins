#!groovy

pipeline {


    agent any

     options {
          buildDiscarder(logRotator(numToKeepStr: '10'))
          timestamps()
     }

     parameters {
         string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Helpful description for Person param')

         text(name: 'BIOGRAPHY', defaultValue: '', description: 'Enter some important info about the person biography')

         booleanParam(name: 'CHECKBOX', defaultValue: true, description: 'Check me if you can')

         choice(name: 'CHOICE', choices: ['First', 'Second', 'Third'], description: 'Pick something')

         password(name: 'PASSWORD', defaultValue: 'VERYSECRET', description: 'Enter a password you already know')
     }

     environment {
         DELETE_FOLDER_AFTER_STAGES = 'false'
         DB_ENGINE    = 'sqlite3'
     }

    stages() {


        stage("Procesul de Build") {
        
            steps {
                echo "Build number ${BUILD_NUMBER} and ${BUILD_TAG}"

                bat 'py mvn compile'
            }


        }


        stage("Procesul de Testing") {
        
            steps {
                sh '. ${BUILD_TAG}/bin/activate && python manage.py test && deactivate'
            }

        }

        stage("Delivery/Deployment") {
        
            steps {
                echo "Deployment stage"
            }

        }

    }

      post {
          always {

               echo "${BUILD_TAG}"
               echo "${params.PERSON}"
               echo "${params.BIOGRAPHY}"
               echo "${params.CHECKBOX}"
               echo "${params.CHOICE}"
               echo "${params.PASSWORD}"


               script {
                   if (DELETE_FOLDER_AFTER_STAGES == 'true') {
                       echo 'Deleting BUILD_TAG folder'
                       sh 'rm -rf ${BUILD_TAG}'
                   } else {
                       echo 'BUILD_TAG not folder deleted'
                   }
               }

               junit '**/test-reports/unittest/*.xml'

          }


         success {
              echo "I am running because the job ran successfully"

              script {

                   def existsDB = fileExists 'db.sqlite3'

                   if (existsDB) {

                       echo "Database exists"

                   } else {

                       echo "No database exists"

                   }
              }
         }

         unstable {
              echo "The build is unstable. Try fix it"
         }

          failure {
             echo "Something happened"
          }

      }


}
