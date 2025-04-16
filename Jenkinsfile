pipeline {
    agent any

    environment {
        IMAGE_NAME = '123shreya/autorollback'  
        VERSION_FILE = '/var/lib/jenkins/version_data/version.txt'
        RECIPIENT = 'shreyaraut002@gmail.com'  
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/ShReYaRaut2006/autorollback.git'
            }
        }

        stage('Read Version') {
            steps {
                script {
                    def PREV_VERSION = readFile(env.VERSION_FILE).trim()
                    def VERSION = (PREV_VERSION.toInteger() + 1).toString()
                    env.IMAGE_TAG = "${IMAGE_NAME}:${VERSION}"
                    env.PREV_IMAGE_TAG = "${IMAGE_NAME}:${PREV_VERSION}"
                    env.VERSION = VERSION
                    env.PREV_VERSION = PREV_VERSION
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${env.IMAGE_TAG} ."
                }
            }
        }

        stage('Deploy & Test') {
            steps {
                script {
                    env.DEPLOYMENT_SUCCESS = "false"
                    try {
                        sh "chmod +x deploy.sh test.sh"
                        sh "./deploy.sh ${env.IMAGE_TAG}"
                        sh "./test.sh"
                        env.DEPLOYMENT_SUCCESS = "true"
                    } catch (err) {
                        echo "App failed to deploy or respond after multiple attempts"
                        env.DEPLOYMENT_SUCCESS = "false"
                    }
                }
            }
        }

        stage('Push or Rollback') {
            steps {
                script {
                    if (env.DEPLOYMENT_SUCCESS == "true") {
                        echo "Deployment succeeded. Pushing image to Docker Hub..."

                        withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                            sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                            sh "docker push ${env.IMAGE_TAG}"
                        }

                        writeFile file: env.VERSION_FILE, text: env.VERSION

                    } else {
                        echo "Rolling back to previous stable image: ${env.PREV_IMAGE_TAG}"
                        sh "docker pull ${env.PREV_IMAGE_TAG}"
                        sh "./deploy.sh ${env.PREV_IMAGE_TAG}"
                    }
                }
            }
        }

        stage('Send Email Notification') {
            steps {
                script {
                    def subject = ''
                    def body = ''
                    def recipient = "${env.RECIPIENT}"
                    def appIp = "http://100.26.61.200:8000"
                    def buildUrl = "${env.BUILD_URL}"

                    if (env.DEPLOYMENT_SUCCESS == "true") {
                        subject = "✅ Deployment Successful"
                        body = """
                        <html>
                        <body>
                            <p>Hello,</p>

                            <p>✅ Your app has been successfully deployed.</p>

                            <p>🌐 Access it at: <a href="${appIp}">${appIp}</a></p>

                            <p>🔍 <a href="${buildUrl}">View Jenkins Console Output</a></p>

                            <br>
                            <p>Regards,<br>
                            Jenkins Deployment Pipeline</p>
                        </body>
                        </html>
                        """
                    } else {
                        subject = "❌ Deployment Failed - Auto Rollback Triggered"
                        body = """
                        <html>
                        <body>
                            <p>Hello,</p>

                            <p>❌ Deployment failed. Auto rollback has been triggered.</p>
                            <p>✅ Your app is running with the previous stable version.</p>

                            <p>🌐 Access it at: <a href="${appIp}">${appIp}</a></p>

                            <p>📄 <a href="${buildUrl}">Check Jenkins Console Output</a> for more details.</p>

                            <br>
                            <p>Regards,<br>
                            Jenkins Deployment Pipeline</p>
                        </body>
                        </html>
                        """
                    }

                    emailext(
                        subject: subject,
                        body: body,
                        to: recipient,
                        mimeType: 'text/html'
                    )
                }
            }
        }
    }
}
