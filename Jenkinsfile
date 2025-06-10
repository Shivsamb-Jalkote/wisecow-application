pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-1'
        ECR_REPO = 'wisecow'
        ECR_REGISTRY = "309272221057.dkr.ecr.us-east-1.amazonaws.com"
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Shivsamb-Jalkote/wisecow-application-.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $ECR_REGISTRY/$ECR_REPO:$IMAGE_TAG .'
            }
        }

        stage('Trivy Scan') {
            steps {
                sh 'trivy image $ECR_REGISTRY/$ECR_REPO:$IMAGE_TAG || true'
            }
        }

        stage('Login to ECR') {
            steps {
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'aws-creds'
                ]]) {
                    sh '''
                        aws ecr get-login-password --region $AWS_REGION | \
                        docker login --username AWS --password-stdin $ECR_REGISTRY
                    '''
                }
            }
        }

        stage('Push to ECR') {
            steps {
                sh 'docker push $ECR_REGISTRY/$ECR_REPO:$IMAGE_TAG'
            }
        }

        stage('Deploy to ECS') {
            steps {
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'aws-creds'
                ]]) {
                    sh '''
                        aws ecs update-service \
                          --cluster wisecow-cluster \
                          --service wisecow-task-def-service-ac16zcnm \
                          --force-new-deployment \
                          --region $AWS_REGION
                    '''
                }
            }
        }
    }
}
