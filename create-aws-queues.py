import os
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import urllib2


response = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
content = response.read();
content = content.split (':');
response.close();

# Get the keys from a specific url and then use them to connect to AWS Service 
access_key_id = str(content[0])
secret_access_key = str(content[1])

# Set up a connection to the AWS service. 
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

# Create
queue = conn.create_queue(sys.argv[1])
