pipeline {

  agent none

  options {
    disableConcurrentBuilds()
    skipDefaultCheckout()
  }

  environment {
    PRODUCT = "service-monitor"
    VER = "1.0"
  }

  stages {
    
    stage('buildImage') {
      agent{
        label 'dev-server'
      }
      when {
        branch 'develop'
      }
      steps {
          checkout scm
          script{
            def BUILD_HASH = sh(returnStdout: true, script: 'git rev-parse --short HEAD').trim()
            env.VERSION = "${VER}-${BUILD_HASH}"
            env.TAG ="${PRODUCT}:$VERSION"
            currentBuild.displayName = "$VERSION"
          }
          sh 'docker build -t "$TAG" .'
      }
    }

    stage('unitTest') {
      agent{
        docker '$TAG'
      }
      when {
        branch 'develop'
      }
      steps {
          sh 'python /app/tests/unitTest.py'
      }
    }

    stage('Deploy-Dev') {
      agent{
        label 'dev-server'
      }
      when {
        branch 'develop'
      }
      steps {
          sh 'docker rm -f $(docker ps -f name=service-monitor-dev -q)'
          sh 'docker run --name service-monitor-dev -d -p 8000:8000 $TAG'
      }
    }
  }
}
