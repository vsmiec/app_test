pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                echo pwd
                ls
                // ~/.cargo/bin/cargo build 
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                // ~/.cargo/bin/cargo run
                sh 'python script.py --secrets "dupa"'


            }
        }
       
    }
}