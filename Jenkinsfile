pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                ~/.cargo/bin/cargo build 
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                ~/.cargo/bin/cargo run
                python script.py


            }
        }
       
    }
}