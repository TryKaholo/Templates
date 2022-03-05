# Copy Logs from physical machine to GCS bucket

The pipeline allows you to move all your logs from your machine to a GCS bucket.
The machine can either be on an EC2 instance (hosted on AWS) or a compute engine (hosted on GCP).   

## The pipeline is divided into 5 phases:

* **Conf gsutil**: Configure gcloud and gsutil, the tools we will use for scp and upload the logs to the GCS bucket.
* **Conf project**: Setup the project id we will work on for gcloud cli.
* **Scp**: Scp copy from remote instance (EC2/Compute engine) and put the logs to a temporary directory.
* **Create bucket**: Create the bucket where we will upload the logs if it does not already exists.
* **Upload logs**: Upload the logs from the temporary path to the gcs bucket.

![image](https://github.com/Vgrob/Templates/blob/main/images/copy-logs-to-gcs-bucket-pipeline.png?raw=true)

### Configuration variables

* **projectId**: Your GCP project id (required).
* **bucket.name**: The bucket name you want to create and where you want to store your logs (required).
* **bucket.storageClass**: Storage class of the bucket you want to create (required).
* **bucket.location**: Location of the bucket you want to create (required).
* **gcpKey**: Name of the gcp service account key that you had previously stored on your kaholo vault (required).
* **localLogsPath**: Log paths where the logs will be temporary stored on kaholo machine, and finally on GCS.
* **instance.type**: Type of instance, can be either ce or ec2.
* **instance.remoteLogsPath**: Path where your logs are currently stored on your instance.
* **instance.user**: User which you are usually connecting to the instance and who have access to the logs folder.
* **instance.host**: Host of the instance.
* **instance.zone**: Zone of the instance.
* **instance.secretKey**: Name of the pem ec2 key that you had previously stored on your kaholo vault.
    
Example configuration for ec2 -> gcs setup:
```javascript
{
        "projectId" : "vincent-sandbox-275412",
        "bucket" : {
            "name" : "vincent-sandbox-project-logs",
            "storageClass" : "NEARLINE",
            "location" : "us-central1"
        },
        "gcpKey" : "credentials gcp",
        "localLogsPath" : "logs/",
        "instance" : {
            "type" : "ec2",
            "remoteLogsPath" : "/home/ec2-user/logs",
            "user" : "ec2-user",
            "host" : "ec2-44-203-116-3.compute-1.amazonaws.com",
            "secretKey" : "ec2-pem"
    }
}
```

Example configuration for compute-engine -> gcs setup:
```javascript
{
    "projectId" : "vincent-sandbox-275412",
    "bucket" : {
        "name" : "vincent-sandbox-project-logs2",
        "storageClass" : "NEARLINE",
        "location" : "us-central1"
    },
    "gcpKey" : "credentials gcp",
    "localLogsPath" : "logs/",
    "instance" : {
        "type" : "ce",
        "remoteLogsPath" : "/home/vincent_grob33/logs",
        "user" : "vincent_grob33",
        "host" : "instance-1",
        "zone" : "us-central1-a"
    }
}
```

### Requirements:

As mentionned above, you will need to create at least one key/value pair in your vault, and 2 if you are using ec2 -> gcs sync.
The name of the pair has to be in the conf as described above. In last example, the name of the pair is "credentials gcp", and on the first example, you will have to set two pairs "ec2-pem" and "credentials gcp".