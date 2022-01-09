# How to create/destroy ELK stack
#### Install Ansible
```
python -m pip install --user ansible==2.11.4
```
###### In `inventory/all.yml` update
`service_account_file: <path-to-the-file>/on-demand-elk-5cf1db7974ac.json`

#### Run below given command to provision the instance/vm
```
ansible-playbook -i inventory/all.yml -e "instance_name=elk-stack" playbook/provision.yaml
```
#### Run below given command to setup the ELK
```
ansible-playbook -e "ansible_python_interpreter=/usr/bin/python" -e "instance_name=elk-stack" -i 34.122.169.136, playbook/elk-stack.yaml
```
##### Note: `34.122.169.136` is the IP address on newly created instance/vm, so update it accordingly.


#### Run below given command to destroy the ELK stack
```
ansible-playbook -i inventory/all.yml -e "instance_name=elk-stack" playbook/destroy.yaml
```
