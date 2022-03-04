# Copy-Elastic-Results-to-S3


The pipeline allows you to execute Elastic Search using Query Strings and Copies your Search results into AWS S3 Bucket.

## The pipeline is divided into 6 phases:

* **doElasticSearch**: Searches by query.
* **cleanSearchDir**: Cleans the search directory to remove any previous result.
* **createSearchDir**: A search directory is created.
* **convertObj2File**: Converts the search  results from the previous step into string and stores into file.
* **listFile**: It gets the name of the latest file created.
* **copySearchResults2AWS**: It uploads the file in AWS S3 bucket.

![image](https://github.com/Sonalisikdar/Templates/blob/4795a8a7e8f114ad4d972bee211556b2991a5f67/Copy-Elastic-Results-to-S3/CopyElasticSearchResult2AWSS3.JPG)

### Configuration variables

* **Connection String**: The url and credentials to connect to Elasticsearch node. Must follow this format: https://[username]:[password]@[host]:[port]/ .
* **Path**: Directory where the ElasticSearch results will be stored.
* **Access Key ID**: This is a parameter taken from the vault to access AWS.
* **Access Key Secret**: This is a parameter taken from the vault to access AWS.
* **Dest Object Path**: Destination to upload the file in the S3 bucket..
* **File Path**: Local location of the file to upload.
    


### Requirements:
AWS CLI (The server should have it installed and configured).
