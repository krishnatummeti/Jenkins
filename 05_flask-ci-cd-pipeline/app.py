pipeline {
    agent { label 'AGENT-01' }

    environment {
        APP_SERVER = 'devuser@192.168.71.129'
        APP_DIR = '/home/devuser/flask-app'
        CODE_DIR = '05_flask-ci-cd-pipeline'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/krishnatummeti/Jenkins.git'
            }
        }

        stage('Install & Test') {
            steps {
                dir(CODE_DIR) {
                    sh '''
                    pip3 install -r requirements.txt --user
                    python3 test_app.py
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                dir(CODE_DIR) {
                    sh '''
                    ssh $APP_SERVER 'rm -rf $APP_DIR && mkdir -p $APP_DIR'
                    scp app.py requirements.txt $APP_SERVER:$APP_DIR
                    ssh $APP_SERVER 'cd $APP_DIR && pip3 install -r requirements.txt --user && nohup python3 app.py > app.log 2>&1 &'
                    '''
                }
            }
        }
    }

    post {
        success {
            echo '✅ Deployment Complete!'
        }
        failure {
            echo '❌ Something went wrong.'
        }
    }
}
