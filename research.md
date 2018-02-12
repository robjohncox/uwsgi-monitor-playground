# UWSGI, Prometheus, Grafana and AlertManager

This document summarises a research project into four technologies

* __UWSGI__ - a web server, specifically the ease of hosting multiple lightweight applications that
  use the HTTP protocol.
* __Prometheus__ - a system for collecting, storing and exposing time series metrics, along with a
  custom query language.
* __Grafana__ - a web based dashboard interface that integrates closely with Prometheus and enables
  creation of dashboards & re-use of ones already created and available online.
* __AlertManager__ - a general alerts handling system that integrates closely with Prometheus and
  provides a rule based system & web UI for managing alerts.

The system that was built whilst doing this research can be found at

    http://github.com/robjohncox/uwsgi-monitor-playground

Clone this to an Ubuntu based system, and follow the instructions in `README.md`

## Appraisal of individual technologies

### UWSGI

UWSGI is an application server that can host web applications written in a number of languages,
including Python. We wanted to see how easy it is to write small applications in pure Python,
without using a web framework, that respond to HTTP requests, and host these on a server.

In summary, it is trivial:

* You write a function that takes in a dictionary of HTTP metadata and a function used to push
  back a response. You can get the request URI, headers and any other request data easily, do
  your thing, and then use the response function to provide a response status code and response
  headers (including content type). Finally, you return the response content, HTML, JSON or
  whatever.
* A small UWSGI configuration file wires this function to the app server
* A small NGINX configuration file wires the application to an external HTTP server and port.

It was quick to write an application to take a JSON request and post it to a RabbitMQ message
queue, and also an application that would calculate server process metrics & expose them at a
given URL, these are indicative of the sort of simple apps this approach looks suited to. From
examining the Django WSGI integration code, it is not difficult to support more advanced cases such
as streaming large data responses.

    https://uwsgi-docs.readthedocs.io/en/latest/

### Prometheus

TODO

### Grafana

TODO

### AlertManager

TODO

## General TODO

* Summarise everything from site.yml
* Talk about architecture for Prometheus, Grafana and AlertManager (what is local, central etc)
* Suitability of Prometheus & Grafana for business focused metrics
* How would we be able to replace our current alerts with alertmanager? Scope out the project
* Discuss how this can potentially be the 'support systems at scale' solution