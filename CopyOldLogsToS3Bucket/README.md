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

* **workDir**: The environment where the app will be deployed.
* **pathLog**: The directory where the agent will work to deploy your app.
* **bucket**: The repository source.
* **user**: The branch where the code is located.
* **host**: The file path with extension of the k8s deployment yaml file.
* **pem**:
    
Example:
```javascript
    {
        "workDir":"/work",
        "pathLog": "/var/logs",
        "bucket": "kaholo-test",
        "user": "ubuntu",
        "host": "10.0.0.0"
    }
```

![image](https://user-images.githubusercontent.com/6090240/153493809-c970a751-faff-4495-984e-a9f52727f03f.png)

### Requirements:
    AWS CLI (The AWS CLI should already be configured).
