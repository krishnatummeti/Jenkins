# To create an Hybrid Pipeline both ( Scripted Pipeline & Declarative Pipeline )
                script {
                  sh """
                    echo 'This is Running Test.'
                    echo 'Project: $client'
                    sleep 15
                """

# set the post like success or failre status of pipline 
    post {
        always {
            echo 'I will always say Hello again!'
        }
        success {
            echo 'I will run when pipeline success!'
        }
        failure {
            echo 'I will run when pipeline failure!'
        }

# Set the agent lable 
agent { label 'AGENT-01' }


# Set in the environment variabuils 
    environment {
        client = 'TECH Base Hub'
        project = 'Health checks for DB and Apps'
        server    = 'Test'
    }

# excute or build it one by one
disableConcurrentBuilds() 

# time limit to abourt
timeout(time: 5, unit: 'SECONDS')


