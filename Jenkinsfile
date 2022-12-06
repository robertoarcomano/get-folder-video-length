// Jenkinsfile
pipeline {
    agent {
        label 'oracle1 && oracle3'
    }
    // Let's test
    stages {
        stage('show directory contents') {
            steps {
                script {
                    sh("./start.sh")
                }
            }
        }
    }
}
