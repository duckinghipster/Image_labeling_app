# Image_labeling_app

Python Flask Application: 
1) To upload images in S3.
2) Then a SNS topic to enable additional services to subscribe to new image upload events.
3) Includes an asynchronous image labeling task executed by AWS Lambda.
4) Lambda function generates image labels with the help of AWS Rekognition.
5) And uses RDS to store the descriptions and tags of the user images. 
6) Integrated with Cognito User Pools to create a user directory and use it for authentication and authorization into the application.
7) Traces the performance of the application with AWS X-Ray.
8) Added a SQS to the application to allow for a new service to poll for incoming images.
9) Includes a load balancer in order to improve the availability and scalability of the application
