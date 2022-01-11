#!groovy

pipeline {


    agent any

     options {
          buildDiscarder(logRotator(numToKeepStr: '10'))
          timestamps()
     }

     

     environment {
         DELETE_FOLDER_AFTER_STAGES = 'false'
         DB_ENGINE    = 'sqlite3'
     }

    stages() {


        stage("Procesul de Build") {
        
            steps {
                echo "Build number ${BUILD_NUMBER} and ${BUILD_TAG}"

                bat 'where py && \
                py -m --version'
            }


        }


        stage("Procesul de Testing") {
        
            steps {
                bat 'py manage.py test'
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
