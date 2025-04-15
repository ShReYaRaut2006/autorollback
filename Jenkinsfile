pipeline {
    agent any

    environment {
        IMAGE_NAME = '123shreya/autorollback'  // Updated image name for Shreya
        VERSION_FILE = '/var/lib/jenkins/version_data/version.txt'
        RECIPIENT = 'shreyaraut002@gmail.com'  // Replace with actual recipient email
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
                    // Dynamically fetch public IP using AWS CLI (based on instance name tag, update if needed)
                    def PUBLIC_IP = sh(script: "aws ec2 describe-instances --filters \"Name=tag:Name,Values=AppServer\" \"Name=instance-state-name,Values=running\" --query 'Reservations[*].Instances[*].PublicIpAddress' --output text", returnStdout: true).trim()

                    def subject = env.DEPLOYMENT_SUCCESS == "true" ? "✅ Deployment Successful" : "⚠️ Deployment Failed - Rollback Triggered"
                    def body = env.DEPLOYMENT_SUCCESS == "true" ?
                        "Your app was successfully deployed.\n\nAccess it at: http://${PUBLIC_IP}" :
                        "Deployment failed. Auto rollback has been triggered.\n\nApp is available at: http://${PUBLIC_IP}"

                    emailext (
                        subject: subject,
                        body: body,
                        to: "${env.RECIPIENT}"
                    )
                }
            }
        }
    }
}
