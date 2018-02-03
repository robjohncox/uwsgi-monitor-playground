Add the following to `/etc/ansible/hosts` to enable local deployment

    [all]
    localhost ansible_connection=local

To install the software on localhost

    ./deploy.sh

To call the __Hello World__ API (simple python script hooked into UWSGI):

    curl -H "Content-Type: application/json" -X POST -d '{"username":"xyz","password":"xyz"}' http://localhost:8001

To view the raw Prometheus interface go to

    http://localhost:9090

To view the Grafana dashboard

    http://localhost:3000

The credentials are

    username: admin
    password: password
    
The API endpoint for gathering Prometheus metrics for Prometheus:

    http://localhost:9090/metrics
    
The API endpoint for gathering Grafana metrics for Prometheus:

    http://localhost:3000/metrics

The API endpoint for gathering NGINX metrics for Prometheus:

    http://localhost:9145/metrics
