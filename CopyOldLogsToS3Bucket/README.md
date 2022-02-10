# Copy Old Logs to S3 Bucket

The pipeline allows you to move all your old logs to S3 Bucket.

## The pipeline is divided into 6 phases:

* **workDir**: A working directory is created.
* **pemFile**: The pem key is entered (private key).
* **Permission**: The correct permissions are given to the key.
* **CopyOldLogsToS3Bcuket.sh**: The script is created and saved in the working directory.
* **Setup Script**: We send the script to the server where the logs will be moved.
* **Execution**: The server connection is made and the script is executed.

![image](https://user-images.githubusercontent.com/6090240/153493323-6cdfc2eb-de9b-459e-bea0-73bd1a987388.png)

### Configuration variables

* **workDir**: Directory where the private key and the script are saved.
* **pathLog**: Directory where the logs are located.
* **bucket**: Name of the S3 Bucket where the old logs will be uploaded.
* **user**: Server user.
* **host**: Server IP.
* **pem**: Private key.
    
Example configuration:
```javascript
    {
        "workDir":"/work",
        "pathLog": "/var/logs",
        "bucket": "kaholo-test",
        "user": "ubuntu",
        "host": "0.0.0.0"
    }
```

The private key is entered on the file content.

![image](https://user-images.githubusercontent.com/6090240/153496370-db140b72-3abe-435d-8c70-36119263370e.png)

### Requirements:
AWS CLI (The server should have it installed and configured).
