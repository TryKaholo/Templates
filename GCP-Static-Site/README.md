# GCP Static Site

To use this, you will need to edit the code layer variables. 

Note that the GCP bucket (BUCKET_NAME), needs to be a unique name. It is suggested to use random characters at the end of the variable name.

Additionally, you will need to update the SECRET_KEY variable name to match the key name in the vault. To GCP Credentials is a service account created within the project ID.

Lastly, if the git repo needs authentication to reach, then the Clone Repo action needs to be modify to include proper credentials.
