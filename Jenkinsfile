pipeline {
    agent any

    environment {
        BIG_SECRET = credentials('secret_1')
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                echo pwd
                sh 'ls'
                echo $BIG_SECRET
                // ~/.cargo/bin/cargo build 
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                // ~/.cargo/bin/cargo run
                sh 'python script.py --secrets $BIG_SECRET'


            }
        }
       
    }
}