<img align="right" src="https://raw.githubusercontent.com/soxoj/maigret/main/static/maigret.png"/>

# Maigret API

[![Python Ver.](https://img.shields.io/badge/python-%3E=_3.6-green.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Api for maigret module.

Maigret is significantly better than Sherlock. Use and contribute to it instead.

## Prerequisites

This REST API is built on top of [Django REST Framework](https://www.django-rest-framework.org/)
(known as DRF). You would need at least the fundamental knowledge about DRF in
order to do development to this project.

### Installation

```sh
# clone the repo
$ git clone https://github.com/hhhtylerw/api.git

# change the working directory to api
$ cd api

# install the requirements
$ python3 -m pip install -r requirements.txt
```

*P.S. Please use `python` instead of `python3` if you are on Windows system*

### Run API Server

```sh
# propagate modules
$ python3 manage.py migrate

# in the root of project diretory..
$ python3 manage.py runserver 0.0.0.0:8000
```

Start you browser and type [127.0.0.1:8000](http://127.0.0.1:8000/) in as
your target URL and hit return.

Now you should able to test your Maigret API through DRF browser interface!

## License

MIT © Sherlock Project

Original Creator - [Shen, Jen-Chieh](https://github.com/jcs090218)
