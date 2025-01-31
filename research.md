# UWSGI, Prometheus, Grafana and Alertmanager

This document summarises a research project to evaluate four technologies

* __UWSGI__: a web server, specifically the ease of hosting multiple lightweight applications that
  use the HTTP protocol.
* __Prometheus__: a system for collecting, storing and exposing time series metrics, along with a
  custom query language.
* __Grafana__: a web based dashboard interface that integrates closely with Prometheus and enables
  creation of dashboards & re-use of ones already created and available online.
* __Alertmanager__: a general alerts handling system that integrates closely with Prometheus and
  provides a rule based system and web UI for managing alerts.

## Running the example code

To really get a feel for these systems, you should fire up the example code that was built as
part of this research and have a play around:

* Fire up an Ubuntu box (ideally a one-off VM, as this will install a lot of software)
* Clone https://github.com/robjohncox/metrics-experiment
* Run `./deploy.sh`
* Go to `README.md` for instructions on how to use and test the various applications

Please note that this example is running old versions of the software, this was what was installed
by the playbooks sourced from Ansible Galaxy. These proved perfectly good for the purpose of this
evaluation.

## Appraisal of individual technologies

### UWSGI

https://uwsgi-docs.readthedocs.io/en/latest/

UWSGI is an application server that can host web applications written in a number of languages,
including Python. We wanted to see how easy it is to write small applications in pure Python,
without using a web framework, that respond to HTTP requests, and host these on a server.

It turns out to be trivial:

* You write a function that takes in a dictionary of HTTP metadata and a function used to push
  back a response. You can get the request URI, headers and any other request data easily, do
  your thing, and then use the response function to provide a response status code and response
  headers (including content type). Finally, you return the response content, HTML, JSON, whatever.
* A small UWSGI configuration file wires this function to the UWSGI app server
* A small NGINX configuration file wires the application to an external HTTP server and port.

It was quick to write applications that

* Take a JSON request and post it to a RabbitMQ message queue
* Calculate server process metrics and expose them at a given URL

These are indicative of the sort of simple apps this approach looks suited to. From examining the
Django WSGI integration code, it is not difficult to support more advanced cases such as streaming
large data responses.

This approach could prove valuable as we trend towards having larger numbers of smaller
applications hosted on servers, as a simple way of building small HTTP based applications
quickly and cleanly. For these reasons, it lends itself nicely to prototype and experimental
applications, and applications with limited lifespans. It is also a useful technique to support
integration with off-the-shelf software, given that current trends are towards web based software
that uses HTTP calls and APIs to handle custom integrations.

### Prometheus

https://prometheus.io/docs/introduction/overview/

Prometheus is a metrics server which

* Stores time series data for a number of different types of metric
* Handles metrics collection primarily by pulling them from URLs which expose those metrics
* Provides a rich query language for analysing the metrics
* Integrates a rules engine for firing alerts to Alertmanager based on those metrics

This is a very well built piece of software, focused and excellent at the task at hand, clearly
very capable in its field. The way that metrics are stored is logical, and the query language on
top of it is very powerful. It is designed to be installed on each __node__ (i.e. server) that you
have, and handle gathering and storing metrics for that single node. You can also use Prometheus
for gathering metrics across a number of nodes, however the recommendation is that this only used
for collecting a small number of metrics that want to be compared across nodes, and not as a way
of centralizing metrics storage. Having played around with it, this makes sense, it feels more
logical to treat each node as a single entity, with its own metrics dashboard.

#### Gathering metrics

There are all sorts of metrics that you can gather, here are just a few examples:

* CPU, memory, hard disk, network etc. statistics for the server
* NGINX request times, latencies, response codes
* UWSGI requests (more detailed than NGINX)
* RabbitMQ, Memcached, Postgresql etc etc
* Application specific metrics using hand rolled metrics exporters.

Each set of metrics is added to Prometheus by configuring a metrics exporter. These are ready
made and available for a lot of popular software packages, and it is also quite simple to write
your own, which is important given that Google advises you need a combination of black-box and
white-box metrics for your applications to be able to effectively monitor them.

There is one caveat on the exporters that are already available for things like UWSGI, RabbitMQ and
Memcached. These turned out to be quite hard to install (and in the scope of this experiment, I gave
up). To use these you would need to either put a lot of effort into getting these working, write
your own, or use Docker (which seemed to be the __easy__ way to use them). As a side note, this is
something to keep an eye on, we may be moving towards a time where even if our own applications are
not utilising containers, we may need to start using container technologies for the installation of
other software packages, as this becomes the standard approach to packaging and distributing
software. This does not seem like a bad thing.

#### Viewing metrics

The best way to get a feel for the power of the metrics is to plot them. The Prometheus UI is
handy for basic exploring, plotting and debugging (as well as getting a general feel for what
Prometheus is doing), however you should fire up Grafana to really get a feel for their power.
It looks straightforward to hook into these metrics from other systems too using the Prometheus
API, however I did not try this out.

#### Raising alerts

Prometheus has a sophisticated system for raising alerts. We need to draw a clear distinction
here between Prometheus and Alertmanager. Prometheus simply handles the __firing__ of alerts, and
Alertmanager decides what to do with them. Alerts are configured individually in Prometheus, where
you provide for each one:

* A name for the alert
* An expression using the Prometheus query language to indicate when to fire the alert
* How long the alert needs to be active for before we fire it
* A dictionary of labels which are used to categorize alerts
* A dictionary of annotations which provide additional information

CONTINUE HERE talking about how alert firing works, be detailed this is important.

#### Summary

To summarise, Prometheus looks to be a tremendously powerful system for automating the storage
and use of metrics. It is very flexible, can cope with both general black-box and application
specific white-box metrics easily, supports both sophisticated alerting for automated
monitoring and notifying people of problems, and powerful dashboards for viewing and exploring
detailed system behaviour.

### Grafana

TODO

### Alertmanager

TODO

## General TODO

* Summarise everything from site.yml
* Talk about architecture for Prometheus, Grafana and Alertnanager (what is local, central etc)
* Suitability of Prometheus & Grafana for business focused metrics
* How Grafana and the off-the-shelf dashboards makes ramp-up fast and helps teach Prometheus
  query language
