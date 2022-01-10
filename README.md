# Pyramid-DualRobot-Monitoring

## Introduction

Much like my previous two projects, this is also based on what I learned from the Cloud Native Application Architecture Nanodegree Program but this time using Pyramid and the module `gandi pyramid prometheus` which is forked from the `pyramid prometheus` module but unlike `gandi pyramid prometheus`, `pyramid prometheus` has not been updated since 2016. As before here is another breakdown of the layers of the project. 


## Breakdown Of Project

### Code
Unlike the previous frameworks these are the main files to be concerned with:

* `setup.py`: This sets up the required libraries for the application to work. To install the libraries run both `pip install -e .` and `pip install -e  "[.dev]"` to install the dev libraries. 
* `tests.py`: This tests the application routes to make sure they respond. This is optional but to make sure your routes work run `pytest dual/tests.py` and all the routes should pass.
* `views.py`: This sets up the views based on the routes. 
* `__init__.py`: This initializes the application by including the needed modules such as `gandi_pyramid_prometheus` and adds the routes.
* `development.ini`: This is required for the application to run.

To run the application run `pserve development.ini --reload`. Go to your browser and type `0.0.0.0:6543`. The application UI should appear. If you see on the right there is an icon to access the debug toolbar which you can use to test the routes. The app design is linked below. 

![app](https://github.com/sentairanger/Pyramid-DualRobot-Monitoring/blob/main/images/app-design.png)

### Docker

Once the application runs correctly the next step is packaging the application using Docker. The `Dockerfile` provides explains each step to run the container. Here are the steps and what each means:

* FROM: This sets up what the image will be based on. In this case it's `python:3.8-slim`. I chose slim as I wanted to reduce image size and only use the required libraries. This is good practice and avoids security issues.
* LABEL: This is an optional step as it names the maintainer of the image.
* COPY: Here the files from the current directory are copied to a directory called `/app`.
* WORKDIR: Here, the working directory is set as `/app`.
* RUN: Here, a command can be run on the image. In this case we are installing the necessary libraries from `requirements.txt`. And after that we also need to install the files from the `setup.py` file.
* CMD: Here the code is run using the command listed. Remember to separate with commas and quotations.

To run the Docker image, first build the image with `docker build -t pyramid-dual .`. Then run with `docker run -d -p 6543:6543 pyramid-dual`. Like before, this runs the image detached in the background. Access the application the same way as before and it should work. Then tag the image with `docker tag pyramid-dual <your-dockerhub-username>/pyramid-dual:<tag>` and then push with `docker push <your-dockerhub-username>/pyramid-dual:<tag>`. Make sure you created an account in Dockerhub for this to work. And make sure you're logged in with `docker login`.


### Kubernetes

Just like before, after packaging with Docker, Kubernetes is used to deploy the application. And as before here is the breakdown of the `pyramid-dual.yaml` manifest file. Make sure you have installed Kubernetes on either your own machine or the Vagrantbox. Optionally you can use services like AWS, Google Kubernetes Engine, and other Kubernetes services to run this application if your hardware can't run a cluster. Like before, here is the breakdown of the manifest file:

* The deployment section: This holds the docker image and adds the annotations for Jaeger and Prometheus. In order for Prometheus to work the scrape option should be set to true, with the `/metrics` endpoint and port 8000. Also make sure to set sidecar injection to true for Jaeger to work.
* The service section: This sets the service port to 6543 and the type is set to LoadBalancer. This is needed to port-foward the application.
* The service monitor section: This is used to monitor the application using the `/metrics` endpoint and the interval set at 15ms.

The diagram of the project is posted below. To run the cluster, run the command `kubectl apply -f pyramid-dual`. The deploy, service and servicemonitor should appear. You can test the app with the command `kubectl port-forward svc/django-dual 6543`. Or use `6543:6543` if running inside a VagrantBox.

![kubernetes](https://github.com/sentairanger/Pyramid-DualRobot-Monitoring/blob/main/images/app-diagram.png)

### Github Actions

Continuous Integration is the action of merging code changes into a repository. And just like in my other projects I created two workflows that merge any changes to the Docker Repository. 

* `docker-build.yml` builds a new image any time there is a change in the repo.
* `docker-sha-tag.yml` creates new sha-tags for each build. This is good for security.

### ArgoCD

Aside from running the cluster directly on the machine or a VagrantBox, ArgoCD is another way to deploy it. I have provided a script to install ArgoCD either on the host or on the VagrantBox. To access the GUI, I have provided the `argocd-service-nodeport.yaml` file and the service should now be exposed. Run the application with the same command `kubectl apply -f pyramid-dual.yaml`. Then the application should appear in the GUI and then you can sync the application. An example of a successful deployment is posted below.

![ArgoCD](https://github.com/sentairanger/Pyramid-DualRobot-Monitoring/blob/main/images/argocd-deploy.png)

### Jaeger

Just like my previous projects, Jaeger is used to find the spans that are traced any time Linus or Torvald's eyes are blinked. In this case the Jaeger client is set up in the `views.py` file and references the `JAEGER_HOST` found in the `pyramid-dual.yaml` manifest.  In order to use Jaeger I have provided an `observability-jaeger.sh` script and `helm-install.sh` to get Jaeger installed. To view the spans in my case I would run `kubectl port-forward svc/my-jaeger-tracing-default-query 16686`. If using a different query make sure to reference that instead. Go to `localhost:16686` and the Jaeger UI should be posted. If using VagrantBox, make sure to change `localhost` to the IP address of the VM. Then select the service, and then click on Find traces. The spans should show up. A sample span is posted below. 

![Jaeger](https://github.com/sentairanger/Pyramid-DualRobot-Monitoring/blob/main/images/jaeger-span.png)

### Prometheus

Prometheus is used to scrape and collect data from the `/metrics` endpoint as done before with Flask and Django. I have provided a `monitoring-prometheus.sh` script to install both Prometheus and Grafana. Once installed then to make sure that Prometheus is monitoring the application run the command `kubectl port-forward -n monitoring svc/prometheus-kube-prometheus-prometheus 9090` and then go to `localhost:9090` or the IP address of your VM if using Vagrantbox. Then go under Status and then Targets. There you should see your application. A screenshot of what it would look like is shown below.

![Prometheus](https://github.com/sentairanger/Pyramid-DualRobot-Monitoring/blob/main/images/prometheus-target.png)

### Grafana

Once Prometheus collects the data, that is processed in Grafana. To go to Grafana make sure to run the command `kubectl port-forward -n monitoring svc/prometheus-grafana 3000` and then go to either `localhost:3000` or replace `localhost` with the IP of your VM if using VagrantBox. Then login with admin and then prom-operator as the password. Change that as that is not secure. To display Jaeger spans, you need to go to Data Sources and then add a data source. Prometheus is added by default so make sure to use the correct FQDN of your Jaeger host and then the port 16686. In my case that's `my-jaeger-tracing-default-query.default.svc.local:16686`. Once that's done you can go to the plus symbol and create your own dashboard. I have provided a json file so that you can use that and adjust as you wish. The Dashboard I created is posted below to get an idea of what it is. However, this time I need address a few changes. While the CPU, RAM usage, pod uptime and Jaeger Spans have not changed, there are several changes from prometheus flask and Django Prometheus. So here are the metrics I used that can help you:

* `pyramid_request_created`: This lists the HTTP requests created.
* `pyramid_request_sum`: This lists the HTTP requests made during a timespan.

![Grafana](https://github.com/sentairanger/Pyramid-DualRobot-Monitoring/blob/main/images/grafana-dashboard.png)

### Using Vagrant 

If using Mac or Windows I have provided a Vagrantfile that already has k3s and Docker ready to be installed. Make sure to install Vagrant first which the instructions can be found [here](https://www.vagrantup.com/downloads).
