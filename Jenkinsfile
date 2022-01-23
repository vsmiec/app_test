pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                cargo build 
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                cargo run
                

            }
        }
       
    }
}