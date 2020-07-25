pipeline {
  options {
    disableConcurrentBuilds()
  }

  environment {
    PRODUCT = "service-monitor"
    VER = "1.0"
  }

  stages {
    
    stage('init') {
      when {
        branch 'develop'
      }
      steps {
        script {
          checkout scm
        }
      }
    }
 
    stage('generateTag') {
      when {
        branch 'develop'
      }
      steps {
        script {
          def BUILD = sh(returnStdout: true, script: 'git rev-parse --short HEAD').trim()
          env.VERSION = "${VER}-${BUILD}"
          env.TAG ="${PRODUCT}:$VERSION"
          currentBuild.displayName = "$VERSION"
        }
      }
    }

    stage('buildImage') {
      when {
        branch 'develop'
      }
      steps {
          sh 'docker build -t "$TAG" -f Dockerfile'
      }
    }

    stage('unitTest') {
      when {
        branch 'develop'
      }
      steps {
        script{
          appContainer = docker.image("$TAG")
          appContainer.pull()
          appContainer.inside(){
            sh 'python /app/tests/unitTest.py'
          }
        }
      }
    }
  }
}
