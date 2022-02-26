# On demand ELK stack

###### `Notes`:
* This pipeline is supposed to run on an Ubuntu based Kaholo agent node.
* This pipeline is designed to setup the ELK stack on Google cloud platform.

### Pre-requisites:
* A service account in GCP.
* Some dependencies/packages on the Kaholo agent node.
* Some other configation requirements are needed, as described below:

##### 1. Create an GCP service account:
You need to create a service account in GCP with edit role, which will be used by the Kaholo agent node to setup the resources on Google cloud. 

##### 2. Install some dependencies:
###### `Note`: These tasks are already incorporated in the pipeline so there is no need to install these dependencies manually.
* apt-transport-https
* ca-certificates
* gnupg
* google-cloud-sdk
* locales

##### 3. Some other configuration settings on the agent node:
###### `Note`: These tasks are already incorporated in the pipeline so there is no need to configure these manually.
###### Configure some locale settings:
```sh
locale-gen en_US en_US.UTF-8
echo 'LANG=en_US.UTF-8' >> /etc/environment
```
###### Make sure there are no old keys left:
```sh
rm -rf /root/.ssh/google_*
```
###### Setup GCP configuration on the Agent node:
```sh
vi /root/.config.json
# paste your service account json file content and save this file.
```

###### Activate-service account:
```sh
gcloud auth activate-service-account --key-file=/root/.config.json
```

###### Activate-service account:
```sh
echo 'y' | gcloud beta compute ssh --zone us-central1-a elkuser@elk-kaholo --project on-demand-elk
```

### Configurations:
This pipeline contains two configurations, `Create` and `Delete`. You can find below more details about these.
##### 1. Create
The `Create` configuration is used to create an ELK stack on Google cloud platform. It contains all required variables which are needed by the create pipeline.
###### action:
For `Create` pipeline its value will always be `create`. It tells the pipeline that we need to create an ELK stack. Please `avoid changing its value` as you will need to modify the pipeline accodingly.
###### name:
This is the name of the virtual machine which will be used to setup the ELK stack on GCP, further each relevant resources on the GCP like VPC, firewall, external IP etc will be prefixed with this name. You `can change its value` as needed.
###### project:
This is the name of the project on GCP under which the ELK stack will be setup. You `will have to change` its value as per your setup.
###### region:
This is the region name where ELK stack will be setup. You `will have to change` its value as per your setup.
###### zone:
The zone to use on the GCP. e.g `us-central1-a`. You `will have to change` its value as per your setup.
###### source_image: 
This is the URL of the image we will use to create the virtual machine. The preffered image is `projects/centos-cloud/global/images/centos-7-v20211105` 
Please `avoid changing its value` as it may break some pipeline steps.
###### machine_type:
This is the virtual machine type we will use to create the virtual machine. The preffered one is `n2-standard-4`. You `can change its value` as needed but make sure you are allocating enough resources to the stack.
###### disk_space:
This is the disk space we will allocate to the virtual machine, the default value is `50` (in GB) but you `can set it to any value` as per your need.
###### subnet:
The subnet group range, the default value is `10.` but you `can change it` as per your setup.
###### git_repo_url:
The Ansible playbooks and Kaholo template repository URL. The value must be `https://github.com/TryKaholo/Templates.git`
`Do not change` its value.
###### git_branch:
The branch to use from the repository, its value should be `main`. Please `avoid changing its value`, as `main` branch will always have latest stable code.
###### git_clone_path:
This is the local path on the Kaholo agent where git repository will be cloned. Its value must be `/root/elk`
Please `avoid changing its value` as you will need to modify the pipeline accodingly.
###### playbook_path:
This is the Ansible playbook path pipeline will run. Its value must be `playbook/elk-stack.yaml`
Please `avoid changing its value` as you will need to modify the pipeline accodingly, also note that its value depends upon the `git_clone_path` variable value because if you change the repository clone location then you might need to modify the playbook path accordingly.
###### gcp_config_file:
This is the Google cloud service account config file which is needed by the Kaholo agent to authenticate with GCP. The value must be `/root/.config.json`
Please `avoid changing its value` as you will need to modify the pipeline accodingly.
######  gcp_base64_config: 
This is the base64 encoded content of the service account json file. You can generate the same using below given command:
```sh
cat <your-service-account-json-file> | base64
```
or using some online platform like:
https://www.base64encode.org/
You `will have to set` its value as per your config.
######  elastic_password:
This is the password of the elastic search, the default value is `ybaPkSpTTGGTtt7mUqRB` but it is `highly recommended to change it`.
######  apm_password:
This is the apm password, the default value is `dasdadwdasda23TJ23FF` but it is `highly recommended to change it`.
######  kibana_password: 
This is the Kibana password, the default value is `dakjasdjdj2334snl` but it is `highly recommended to change it`.
######  logstash_passord:
This is the logstash password, the default value is `idfhoidsfldsnl22nc` but it is `highly recommended to change it`.
######  beats_password: 
This is the beats password, the default value is `ohha234dadasnxs` but it is `highly recommended to change it`.
######  remote_monitoring_password:
This is the remote monitoring password, the default value is `dfasfhdaslf123bksd` but it is `highly recommended to change it`.
######  logstash_dup_handler:
This is the value from the datafile which will be used as an ID within the elasticsearch index to avoid any duplication. The default value is `%{id}`. Its value must be something which is unique within the data file.
##### 2. Delete
The `Delete` configuration is used to delete the ELK stack. It contains all required variables which are needed by the delete pipeline.
###### action:
For `Delete` pipeline its value will always be `delete`. It tells the pipeline that we need to delete and ELK stack. Please `avoid changing its value` as you will need to modify the pipeline accodingly.
###### name:
This is the name of the virtual machine which is used by the ELK stack on GCP and same will be deleted. Further, each relevant resources on the GCP like VPC, firewall, external IP etc which are pre-fixed with this name and will be deleted too. Its `value must match` with the value you have in the `Create` configuration for this variable.
###### project:
This is the name of the project on GCP under which the ELK stack is running. Its `value must match` with the value you have in the `Create` configuration for this variable.
###### region:
This is the region name where ELK stack is running. Its `value must match` with the value you have in the `Create` configuration for this variable.
###### zone:
The zone under which ELK stack is running. Its `value must match` with the value you have in the `Create` configuration for this variable.
###### gcp_config_file:
This is the Google cloud service account config file which is needed by the Kaholo agent to authenticate with GCP. The value must be `/root/.config.json`
Its `value must match` with the value you have in the `Create` configuration for this variable.
######  gcp_base64_config: 
This is the base64 encoded content of the service account json file. You can generate the same using below given command:
```sh
cat <your-service-account-json-file> | base64
```
or using some online platform like:
https://www.base64encode.org/
Its `value must match` with the value you have in the `Create` configuration for this variable.
######  elastic_password:
This is the password of the elastic search, the default value is `ybaPkSpTTGGTtt7mUqRB`. It will be used in the delete pipeline to make sure we take a final snapshot of the stack before deleting it. Its `value must match` with the value you have in the `Create` configuration for this variable.

### How to run:
As explained above there are two configurations in this pipeline, `Create` and `Delete`. As the name indicates itself the `Create` pipeline is used to create the ELK stack and `Delete` pipeline deletes it.
* For creating an ELK stack, please select `Create` configuration from the drop down on the top right corner and click on `EXECUTE`.
* For deleting an ELK stack, please select `Delete` configuration from the drop down on the top right corner and click on `EXECUTE`.
