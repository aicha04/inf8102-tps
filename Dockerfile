FROM ubuntu:focal
RUN apt-get update -y
RUN apt-get install -y yum-utils
RUN apt-get update -y
RUN yum install -y amazon-cloudwatch-agent
CMD /bin/bash