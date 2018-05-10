pipeline {
    agent { docker { image 'python:3.6.5-alpine' } }
    stages {
        stage('pre-check') {
            steps {
                sh 'python --version'
            }
        }
        stage('build') {
            steps {
                sh 'docker-compose build'
            }
        }
        stage('test') {
            steps {
                sh 'docker-compose run test'
            }
        }
    }
}