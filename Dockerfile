FROM ubuntu:focal
RUN sudo apt update -y
RUN sudo apt install -y yum-utils
RUN sudo apt update -y
RUN sudo yum install -y amazon-cloudwatch-agent
CMD /bin/bash