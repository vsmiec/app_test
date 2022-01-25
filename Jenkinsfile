pipeline {
    agent any

    environment {
        BIG_SECRET = credentials('secret_1')
    }

    stages {
        when {
             branch 'master'
        }
        stage('Build') {
            steps {
                echo 'Building..'
                sh('/var/jenkins_home/.cargo/bin/cargo build') 
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh('/var/jenkins_home/.cargo/bin/cargo run')
                sh('python script.py --secrets $BIG_SECRET')

            }
        }
       
    }
}