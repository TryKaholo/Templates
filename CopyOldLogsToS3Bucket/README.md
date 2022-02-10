# Copy Old Logs to S3 Bucket

The pipeline allows you to move all your old logs to s3 Bucket.

## In this pipeline is divided into 6 phases:

    1.- A working directory is created.
    2.- The pem key is entered (private key).
    3.- The correct permissions are given to the key.
    4.- The script is created and saved in the working directory.
    5.- We send the script to the server where the logs will be moved.
    6.- The server connection is made and the script is executed.

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


The private key is entered in the file content.
![image](https://user-images.githubusercontent.com/6090240/153495855-53c9f18c-8202-4825-a1f4-f95da4c35d2b.png)
![image](https://user-images.githubusercontent.com/6090240/153495574-cf8211a6-df1b-40a9-99ad-e86f924a4401.png)
![image](https://user-images.githubusercontent.com/6090240/153493809-c970a751-faff-4495-984e-a9f52727f03f.png)

### Requirements:
AWS CLI (The AWS CLI should already be configured).
