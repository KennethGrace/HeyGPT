# HeyGPT: A Simple Task-Oriented Conversational AI

## Introduction

HeyGPT is a simple API and command-line interface for task-oriented conversational AI. It is built on top of the [Transformers](https://pypi.org/project/transformers/) and [FastAPI](https://fastapi.tiangolo.com/) libraries. HeyGPT is designed to be simple to use and easy to extend. The API is made available as a Docker container for easy deployment. Once the container is up and running, you can interact with the API using the command-line interface or by sending HTTP requests to the API.

_Here is an example using the command-line interface:_

```bash
hey "Hello, HeyGPT."
```

The command-line interface will automatically pull the your name from the environment variable `USER` and send it along with the message to the API, unless you set the `HEY_USER` environment variable. The `HEY_API` environment variable must be set to the URL of the API. The default value is `http://localhost:23450`.

## Installation

### API Server

To get started with the HeyGPT API server, you will need to have Docker installed on your system. You can download Docker from [here](https://www.docker.com/products/docker-desktop). Once installed, you can pull the HeyGPT API server image from Docker Hub.

```bash
docker pull kennethgrace/heygpt
```

HeyGPT requires two volume mounts for persistent storage of user conversation history and model checkpoints, `/app/models` and `/app/cache`. You can also optionally set two environment variables to control what model and what persona the AI will use. The default model is `PygmalionAI/pygmalion-2-7b` which requires ~13GB of memory. The default persona is named `Jai`, a friendly robot.

_Here is an example of running the HeyGPT API server:_

```bash
docker run -d --name heygpt -p 23450:23450 -v heygpt_models:/app/models -v heygpt_cache:/app/cache -e HEY_MODEL=PygmalionAI/pygmalion-2-13b -e HEY_PERSONA=Other kennethgrace/heygpt
```

### Command-Line Interface

To get started with the HeyGPT command-line interface, you will need to have Python 3 installed on your system. You can download Python 3 from [here](https://www.python.org/downloads/). It is required that you use Python version 3.10 or higher. Once installed, you'll need the [Requests](https://requests.readthedocs.io/en/latest/) library. You can install it using the following command:

```bash
pip install requests
```

Next, you'll need to download the HeyGPT command-line interface. You can do this by cloning the HeyGPT repository.

```bash
git clone https://github.com/kennethgrace/heygpt.git
```

You may need to set two environment variables, `HEY_API` and `HEY_USER`. And it is recommended that you symlink the `hey` script to a directory in your `PATH`. For example:

```bash
export HEY_API=http://server.domain:23450
export HEY_USER=John
ln -s /path/to/heygpt/hey /usr/local/bin/hey
```

## Developing

The HeyGPT API is simple and easy to use. It is composed of a payload consisting of only two values, a `sender_name` and a `message`.

_Here is an example using CURL to send a request to the API:_

```bash
curl -X POST "http://localhost:23450/chat/message" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"message\":\"Hello, HeyGPT.\",\"sender_name\":\"Bob\"}"
```