import boto3

client = boto3.client('ec2')

VPC = client.create_vpc(
    CidrBlock='10.0.0.0/16',
    AmazonProvidedIpv6CidrBlock=False,
    DryRun=True,
)
VpcId=VPC['Vpc']['VpcId']
publicSubnet1 = client.create_subnet(
    AvailabilityZone='us-east-1a',
    AvailabilityZoneId='use1-az6',
    CidrBlock='10.0.0.0/24',
    VpcId=VpcId,
    DryRun=True,
)
publicSubnet2 = client.create_subnet(
    AvailabilityZone='us-east-1b',
    AvailabilityZoneId='use1-az1',
    CidrBlock='10.0.16.0/24',
    VpcId=VpcId,
    DryRun=True,
)
privateSubnet1 = client.create_subnet(
    AvailabilityZone='us-east-1a',
    AvailabilityZoneId='use1-az6',
    CidrBlock='10.0.128.0/24',
    VpcId=VpcId,
    DryRun=True,
)
privateSubnet2 = client.create_subnet(
    AvailabilityZone='us-east-1b',
    AvailabilityZoneId='use1-az1',
    CidrBlock='10.0.144.0/24',
    VpcId=VpcId,
    DryRun=True,
)
internetGateway = client.create_internet_gateway()
inertnetGatewayAttachment = client.attach_internet_gateway(
    DryRun=True,
    InternetGatewayId=internetGateway['InternetGateway']['InternetGatewayId'],
    VpcId=VpcId
)
natGateway1 = client.create_nat_gateway(
    SubnetId=publicSubnet1['Subnet']['SubnetId'],
)
natGateway2 = client.create_nat_gateway(
    SubnetId=publicSubnet2['Subnet']['SubnetId'],
)

publicRouteTable = client.create_route_table(
    VpcId=VpcId,
)
defaultPublicRoute = client.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internetGateway['InternetGateway']['InternetGatewayId'],
    RouteTableId=publicRouteTable['RouteTable']['RouteTableId'],
)
publicRouteTableAssociation1 = client.associate_route_table(
    RouteTableId=publicRouteTable['RouteTable']['RouteTableId'],
    SubnetId=publicSubnet1['Subnet']['SubnetId'],
)
publicRouteTableAssociation2 = client.associate_route_table(
    RouteTableId=publicRouteTable['RouteTable']['RouteTableId'],
    SubnetId=publicSubnet2['Subnet']['SubnetId'],
)

privateRouteTable1 = client.create_route_table(
    VpcId=VpcId,
)
privateRouteTable2 = client.create_route_table(
    VpcId=VpcId,
)
defaultPrivateRoute1 = client.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    NatGatewayId=natGateway1['NatGateway']['NatGatewayId'],
    RouteTableId=privateRouteTable1['RouteTable']['RouteTableId'],
)
defaultPrivateRoute2 = client.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    NatGatewayId=natGateway2['NatGateway']['NatGatewayId'],
    RouteTableId=privateRouteTable2['RouteTable']['RouteTableId'],
)
privateRouteTableAssociation1 = client.associate_route_table(
    RouteTableId=privateRouteTable1['RouteTable']['RouteTableId'],
    SubnetId=privateSubnet1['Subnet']['SubnetId']
)
privateRouteTableAssociation2 = client.associate_route_table(
    RouteTableId=privateRouteTable2['RouteTable']['RouteTableId'],
    SubnetId=privateSubnet2['Subnet']['SubnetId']
)
securityGroup = client.create_security_group(
    Description='Security group allows SSH, HTTP, HTTPS, MSSQL, etc...',
    GroupName='polystudent-sg2',
    VpcId=VpcId
)

ingress1 = client.authorize_security_group_ingress(
    CidrIp='0.0.0.0/0',
    FromPort=22,
    ToPort=22,
    GroupId=securityGroup['GroupId'],
    GroupName='polystudent-sg2',
    IpProtocol='tcp',
)
ingress2 = client.authorize_security_group_ingress(
    CidrIp='0.0.0.0/0',
    FromPort=80,
    ToPort=80,
    GroupId=securityGroup['GroupId'],
    GroupName='polystudent-sg2',
    IpProtocol='tcp',
)
ingress3 = client.authorize_security_group_ingress(
    CidrIp='0.0.0.0/0',
    FromPort=443,
    ToPort=443,
    GroupId=securityGroup['GroupId'],
    GroupName='polystudent-sg2',
    IpProtocol='tcp',
)
ingress4 = client.authorize_security_group_ingress(
    CidrIp='0.0.0.0/0',
    FromPort=53,
    ToPort=53,
    GroupId=securityGroup['GroupId'],
    GroupName='polystudent-sg2',
    IpProtocol='tcp',
)
ingress5 = client.authorize_security_group_ingress(
    CidrIp='0.0.0.0/0',
    FromPort=53,
    ToPort=53,
    GroupId=securityGroup['GroupId'],
    GroupName='polystudent-sg2',
    IpProtocol='udp',
)
ingress6 = client.authorize_security_group_ingress(
    CidrIp='0.0.0.0/0',
    FromPort=1433,
    ToPort=1433,
    GroupId=securityGroup['GroupId'],
    GroupName='polystudent-sg2',
    IpProtocol='tcp',
)
ingress7 = client.authorize_security_group_ingress(
    CidrIp='0.0.0.0/0',
    FromPort=5432,
    ToPort=5432,
    GroupId=securityGroup['GroupId'],
    GroupName='polystudent-sg2',
    IpProtocol='tcp',
)
ingress8 = client.authorize_security_group_ingress(
    CidrIp='0.0.0.0/0',
    FromPort=3306,
    ToPort=3306,
    GroupId=securityGroup['GroupId'],
    GroupName='polystudent-sg2',
    IpProtocol='tcp',
)
ingress9 = client.authorize_security_group_ingress(
    CidrIp='0.0.0.0/0',
    FromPort=3389,
    ToPort=3389,
    GroupId=securityGroup['GroupId'],
    GroupName='polystudent-sg2',
    IpProtocol='tcp',
)
ingress10 = client.authorize_security_group_ingress(
    CidrIp='0.0.0.0/0',
    FromPort=1514,
    ToPort=1514,
    GroupId=securityGroup['GroupId'],
    GroupName='polystudent-sg2',
    IpProtocol='tcp',
)
ingress11 = client.authorize_security_group_ingress(
    CidrIp='0.0.0.0/0',
    FromPort=9200,
    ToPort=9300,
    GroupId=securityGroup['GroupId'],
    GroupName='polystudent-sg2',
    IpProtocol='tcp',
)