FROM ubuntu:focal
RUN apt-get update -y
RUN wget https://s3.amazonaws.com/amazoncloudwatch-agent/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm
RUN rpm -U ./amazon-cloudwatch-agent.rpm
RUN apt-get install -y amazon-cloudwatch-agent
CMD /bin/bash