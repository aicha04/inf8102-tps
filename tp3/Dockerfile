FROM ubuntu:focal
RUN apt-get update -y
RUN apt-get install -y wget
RUN wget https://s3.amazonaws.com/amazoncloudwatch-agent/debian/amd64/latest/amazon-cloudwatch-agent.deb
RUN dpkg -i -E ./amazon-cloudwatch-agent.deb
CMD /bin/bash