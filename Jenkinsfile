// Jenkinsfile
pipeline {
    agent {
        node {
            label 'oracle1'
        }
        node {
            label 'oracle3'
        }
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
