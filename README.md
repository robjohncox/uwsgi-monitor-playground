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

To view the RabbitMQ management web UI (user: admin, password: password) go to

    http://localhost:15672
    
To call the __Hello World__ API:

    curl -H "Content-Type: application/json" -X POST -d '{"username":"xyz","password":"xyz"}' http://localhost:8001

To call the __Post RabbitMQ Message__ API:

    curl -X POST http://localhost:8002

To call the __General Process Metrics__ API:

    curl -X POST http://localhost:8003/metrics

To run UWSGI-top for viewing UWSGI statistics

    pip install uwsgitop
    # Hello world app
    uwsgitop http://localhost:3101
    # Post RabbitMQ message app
    uwsgitop http://localhost:3102
    
