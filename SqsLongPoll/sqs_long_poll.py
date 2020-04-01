"Long polling the SQS queue for image uploads"
import sys
import json
import boto3

# Create SQS client
sqs = boto3.client('sqs')


if len(sys.argv) < 2:
    print("Usage: pass the SQS queue url as the first parameter")
    sys.exit(0)

queue_url = sys.argv[1]

print("Polling the photos queue.  Ctrl-C to exit.")

# Long poll for message on provided SQS queue
while True:
    response = sqs.receive_message(
        QueueUrl=queue_url,
        WaitTimeSeconds=20
    )
    if 'Messages' in response:
        receipt_handle = response['Messages'][0]["ReceiptHandle"]
        body = json.loads(response['Messages'][0]["Body"])
        message = json.loads(body["Message"])
        if "Records" in message:
            s3_bucket = message["Records"][0]["s3"]["bucket"]["name"]
            s3_object_key = message["Records"][0]["s3"]["object"]["key"]
            s3_object_size = message["Records"][0]["s3"]["object"]["size"]
            print("We have a new upload: bucket: %s key: %s, size: %s bytes" %
                  (s3_bucket, s3_object_key, s3_object_size))
        else:
            print("Not the message we were expecting")
            print(message)

        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )
