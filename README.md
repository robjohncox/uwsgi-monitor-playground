To install the software on localhost (arguments will be passed to `ansible-playbooks`)

    ./deploy.sh [args]

To view the Prometheus web UI go to

    http://localhost:9090

To see the Prometheus endpoints

    http://localhost:9090/targets

To see the Alertmanager web UI go to

    http://localhost:9093

To view the Grafana web UI (user: admin, password: password) go to

    http://localhost:3000
    
To call the __Hello World__ API (simple python script hooked into UWSGI):

    curl -H "Content-Type: application/json" -X POST -d '{"username":"xyz","password":"xyz"}' http://localhost:8001
