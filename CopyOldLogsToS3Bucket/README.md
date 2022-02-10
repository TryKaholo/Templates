Copy Old Logs to S3 Bucket

The pipeline allows you to move all your old logs to s3 Bucket.

In this pipeline is divided into 6 phases:

    1.- A working directory is created.
    2.- The pem key is entered (private key).
    3.- The correct permissions are given to the key.
    4.- The script is created and saved in the working directory.
    5.- We send the script to the server where the logs will be moved.
    6.- The server connection is made and the script is executed.

Variables that are added to the configuration:
    workDir
    pathLog
    bucket
    user
    host

Variables that are added in the interface:
    key.pem

Requirements:
    AWS CLI (The AWS CLI should already be configured).
