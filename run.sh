#!/bin/bash
ECSImageId=ami-09a41e26df464c548
SecurityGroup=sg-0b90b622bf5484b42

# if [ "$SecurityGroup" == "" ]; then
#     OldGroups=$(aws ec2 describe-security-groups --query "SecurityGroups[].GroupId" --output text)
#     for group in $OldGroups
#     do
#         if [ "$group" != "$DefaultSecurityGroup" ]; then
#             aws ec2 delete-security-group --group-id $group
#         fi
#         sleep 10
#     done
#     SecurityGroup=$(aws ec2 create-security-group --description "tp2-group" --group-name tp2-group --output text)
#     # enable inbound ssh to debug and http for us to view the webapp
#     aws ec2 authorize-security-group-ingress --group-id $SecurityGroup --protocol tcp --port 22   --cidr 0.0.0.0/0
#     aws ec2 authorize-security-group-ingress --group-id $SecurityGroup --protocol tcp --port 80   --cidr 0.0.0.0/0
#     aws ec2 authorize-security-group-ingress --group-id $SecurityGroup --protocol tcp --port 443  --cidr 0.0.0.0/0
#     # for downloads, enable http/https outbound
#     aws ec2 authorize-security-group-egress  --group-id $SecurityGroup --protocol tcp --port 80   --cidr 0.0.0.0/0
#     aws ec2 authorize-security-group-egress  --group-id $SecurityGroup --protocol tcp --port 443  --cidr 0.0.0.0/0
# fi
curl https://raw.githubusercontent.com/aicha04/inf8102-tps/main/setupInstance.sh > setupInstance.sh
subnetId=subnet-01cd3fe0dc6eba810
M4Large="$(aws ec2 run-instances --image-id $ECSImageId --count 1 --instance-type m4.large --security-group-ids $SecurityGroup --key-name vockey --user-data file://setupInstance.sh --subnet-id $subnetId --query "Instances[].[InstanceId]" --output text)"
echo $M4Large