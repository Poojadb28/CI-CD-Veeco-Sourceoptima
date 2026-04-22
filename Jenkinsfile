// pipeline {
//     agent any

//     environment {
//         PYTHON = "C:\\Users\\pooja.db\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
//     }

//     stages {

//         stage('Checkout Code') {
//             steps {
//                 checkout scm
//             }
//         }

//         stage('Install Dependencies') {
//             steps {
//                 bat "%PYTHON% -m pip install --upgrade pip"
//                 bat "%PYTHON% -m pip install -r requirements.txt"
//                 bat "%PYTHON% -m pip install pytest-html pytest-xdist pytest-rerunfailures"
//             }
//         }

//         stage('Prepare Folders') {
//             steps {
//                 bat "if not exist reports mkdir reports"
//                 bat "if not exist screenshots mkdir screenshots"
//                 bat "if not exist downloads mkdir downloads"
//             }
//         }

//         stage('Run Tests') {
//             steps {
//                 bat """
//                 %PYTHON% -m pytest tests/ ^
//                 -v ^
//                 --html=reports/report.html ^
//                 --self-contained-html ^
//                 --capture=tee-sys ^
//                 --reruns 1 ^
//                 """
//             }
//         }
//     }

//     post {
//         always {
//             publishHTML(target: [
//                 reportDir: 'reports',
//                 reportFiles: 'report.html',
//                 reportName: 'Automation Test Report',
//                 keepAll: true,
//                 alwaysLinkToLastBuild: true,
//                 allowMissing: true
//             ])
//         }
//     }
// }

pipeline {
    agent any

    environment {
        PYTHON = "C:\\Users\\pooja.db\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
    }

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat "%PYTHON% -m pip install --upgrade pip"
                bat "%PYTHON% -m pip install -r requirements.txt"
                bat "%PYTHON% -m pip install pytest-html pytest-xdist pytest-rerunfailures"
            }
        }

        stage('Prepare Folders') {
            steps {
                bat "if not exist reports mkdir reports"
                bat "if not exist screenshots mkdir screenshots"
                bat "if not exist downloads mkdir downloads"
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                %PYTHON% -m pytest tests/ ^
                -v ^
                --headless ^
                --html=reports/report.html ^
                --self-contained-html ^
                --capture=sys^
                --reruns 1
                """
            }
        }
    }

    post {

        always {
            publishHTML(target: [
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Automation Test Report',
                keepAll: true,
                alwaysLinkToLastBuild: true,
                allowMissing: true
            ])
        }

        success {
            echo "Build SUCCESS "
        }

        failure {
            echo "Build FAILED  - Check HTML Report"
        }
    }
}

