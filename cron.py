import boto3
import paramiko

def lambda_handler(event, context):
    #Get IP addresses of EC2 instances
    client = boto3.client('ec2')
    instDict=client.describe_instances(
            Filters=[{'Name':'tag:Name','Values':[event['SERVERNAME']]}]
        )

    s3bucket='s3_bucket_name'   # S3 bucket name
    keypath='/keys/sshkey.pem'  # Path to SSH key in bucket

    instances = [i for r in instDict['Reservations'] for i in r['Instances']]
    host=instances[0]["PrivateIpAddress"]

    s3_client = boto3.client('s3')
    #Download private key file from secure S3 bucket
    s3_client.download_file('revmax-key-bucket','keys/sshkey.pem', '/tmp/sshkey.pem')

    k = paramiko.RSAKey.from_private_key_file("/tmp/sshkey.pem")
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print "Connecting to " + host
    c.connect( hostname = host, username = "root", pkey = k )
    print "Connected to " + host

    commands = [
        event['CMD']
        ]

    for command in commands:
        print "Executing {}".format(command)
        stdin , stdout, stderr = c.exec_command(command)
        print stdout.read()
        print stderr.read()

    return
    {
        'message' : "Script execution completed. See Cloudwatch logs for complete output"
    }
