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
      agent any
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
      agent any
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
      agent any
      when {
        branch 'develop'
      }
      steps {
          sh 'docker build -t "$TAG" -f Dockerfile'
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
  }
}