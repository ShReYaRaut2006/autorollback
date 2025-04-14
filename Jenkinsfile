pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Deploy App') {
            steps {
                sh 'python3 main.py &'
                sleep time: 5, unit: 'SECONDS'
            }
        }

        stage('Test App') {
            steps {
                sh 'bash test.sh'
            }
        }
    }

    post {
        always {
            mail to: 'shreyaraut002@gmail.com',
                 subject: "🔔 Build ${currentBuild.currentResult}: Job ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: """Hello Shreya 👩‍💻,

Your Jenkins pipeline for project *SafeDeploy* has completed.

📋 Job: ${env.JOB_NAME}
🔢 Build No: ${env.BUILD_NUMBER}
📊 Status: ${currentBuild.currentResult}

🌐 URL: ${env.BUILD_URL}

Cheers,
SafeDeploy Jenkins 🚀
"""
            }
        }
    }
}
