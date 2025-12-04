pipeline {
  agent any

  environment {
    API_DIR = "services/api"
    IMAGE  = "mojitech/yoruba-kids-api"
    TAG    = "build-${env.BUILD_NUMBER}"
    DOCKER = "/usr/local/bin/docker"
    PATH   = "/usr/local/bin:/usr/bin:/bin"
  }

  stages {
    stage('Checkout') {
      steps {
        // Pull the branch that triggered this build
        checkout scm
      }
    }

    stage('Unit tests (Python 3.12 container)') {
      steps {
        dir("${API_DIR}") {
          sh '''
            "$DOCKER" run --rm -v "$PWD":/src -w /src python:3.12-slim bash -lc "
              pip install -r requirements.txt && pytest -q
            "
          '''
        }
      }
    }

    stage('Build API Docker image') {
      steps {
        dir("${API_DIR}") {
          sh '"$DOCKER" build -t $IMAGE:$TAG -t $IMAGE:latest .'
        }
      }
    }

    // No deploy yet – we’ll add that later, and only from main
  }

  post {
    always {
      // Clean up any leftover test containers if we add them later
      sh '"$DOCKER" rm -f yoruba-kids-api-test 2>/dev/null || true || true'
    }
  }
}
