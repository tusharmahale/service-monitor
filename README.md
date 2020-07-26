# service-monitor
Monitor Service with Python flask

### Pre-requisites

Python3 with flask
```sh
pip install flask
```

### How to Run

Run the program (Make sure input.csv is in same directory from where you are running below command)
```sh
$ cd service-monitor
$ python src/app.py
```
Access Application
  - [Stats in table](http://localhost:8000/stats)
  - [Api](http://localhost:8000/api)

### Docker
Application is easy to install and deploy in a Docker container.

```sh
cd service-monitor
docker build -t service-monitor:1.0 .
```
This will create the Service Monitor application image and pull in the necessary dependencies. 
By default application runs on 8000 port inside container if you want to change please update src/app.py file. Application will be exposed on local 8000 port as well

```sh
docker run --name service-monitor-dev -d -p 8000:8000 --restart="always" service-monitor:1.0
```

### CI/CD

CI/CD is set up with Jenkins. You can refer to [Jenkinsfile](Jenkinsfile) inside repo.
Jenkins CI/CD consists of below stages automatically provided dependent stages are successful
  - Build code
  - Run Unit tests
  - Deploy Container
  - Run Smoke Tests
