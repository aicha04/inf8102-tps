ECSImageId=ami-09a41e26df464c548
SecurityGroup=$(aws ec2 describe-security-groups --query "SecurityGroups[].GroupId" --filter "Name=group-name,Values=tp2-group" --output text)

if [ "$SecurityGroup" == "" ]; then
    OldGroups=$(aws ec2 describe-security-groups --query "SecurityGroups[].GroupId" --output text)
    for group in $OldGroups
    do
        if [ "$group" != "$DefaultSecurityGroup" ]; then
            aws ec2 delete-security-group --group-id $group
        fi
        sleep 10
    done
    SecurityGroup=$(aws ec2 create-security-group --description "tp2-group" --group-name tp2-group --output text)
    # enable inbound ssh to debug and http for us to view the webapp
    aws ec2 authorize-security-group-ingress --group-id $SecurityGroup --protocol tcp --port 22   --cidr 0.0.0.0/0
    aws ec2 authorize-security-group-ingress --group-id $SecurityGroup --protocol tcp --port 80   --cidr 0.0.0.0/0
    aws ec2 authorize-security-group-ingress --group-id $SecurityGroup --protocol tcp --port 443  --cidr 0.0.0.0/0
    # for downloads, enable http/https outbound
    aws ec2 authorize-security-group-egress  --group-id $SecurityGroup --protocol tcp --port 80   --cidr 0.0.0.0/0
    aws ec2 authorize-security-group-egress  --group-id $SecurityGroup --protocol tcp --port 443  --cidr 0.0.0.0/0
fi
curl  > setupInstance.sh
subnetId=
M4Large="$(aws ec2 run-instances --image-id $ECSImageId --count 1 --instance-type m4.large --security-group-ids $SecurityGroup --key-name vockey --user-data file://setupInstance.sh --subnet-id $subnetId --query "Instances[].[InstanceId]" --output text)"
echo $M4Large