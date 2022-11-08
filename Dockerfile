FROM ubuntu:focal
RUN apt-get update -y
RUN apt-get install -y wget
RUN wget https://s3.amazonaws.com/amazoncloudwatch-agent/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm
RUN rpm -U ./amazon-cloudwatch-agent.rpm
CMD /bin/bash