# RabbitMQ listeners

## Description

The program starts to listen specified queues
and outputs messages to stdout or file.

Each queue listener starts in a different process.

All configuration is in *config.yaml*.

## Usage

1. Add your configuration to *config.yaml*.
2. Run

    ``$ python listener.py``

## Additional: parser

To parse collected data and retrieve only needed part use *parse_output.py*.

``$ python parse_output.py``
