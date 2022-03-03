## Provision and Setup k8s on EKS with Monitoring

This pipeline template makes use of the [Command Line](https://github.com/Kaholo/kaholo-plugin-cmd) plugin. It can be used to create an EKS cluster, with Prometheus and Grafana deployed for monitoring.

### Pipeline Template

![Pipeline Template](/images/create-eks-cluster-with-monitoring.png "Pipeline Template")

### Configuration Variables

- **region**: The region where the cluster is to be deployed.
- **aws_access_key_id_vault_name**: The name of the Vault variable that stores the AWS Access Key Id. Can leave it to default `aws_access_key_id` if it has been uploaded to vault under the same name.
- **aws_secret_access_key_vault_name**: The name of the Vault variable that stores the AWS Access Key Id. Can leave it to default `aws_secret_access_key` if it has been uploaded to vault under the same name.
- **cluster_name**: The name of the EKS cluster.
- **k8s_version**: The version of Kubernetes. Leave it to default if unsure.
- **node_type**: The type of VM to use for cluster nodes. A list of all possible node types can be found [here](https://aws.amazon.com/ec2/instance-types/).
- **num_nodes**: The number of nodes to create in the default nodegroup.
- **node_volume_size_gb**: The size of the node disk in GB.
- **node_image_family**: The image family to use as the host OS.

##### Example

```
{
    "aws_access_key_id_vault_name": "aws_access_key_id",
    "aws_secret_access_key_vault_name": "aws_secret_access_key",
    "cluster_name": "mycluster",
    "region": "us-east-1",
    "k8s_version": "1.21",
    "node_type": "t2.medium",
    "num_nodes": "3",
    "node_volume_size_gb": "50",
    "node_image_family": "Ubuntu2004"
}
```

### Vault Secrets

- **aws_access_key_id**: The Access Key Id of the AWS user.
- **aws_secret_access_key**: The Secret Access Key of the AWS user.

### Setting up Grafana with Prometheus

The [Prometheus and Grafana stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) has already been deployed to the cluster. Prometheus is already collecting the default cluster metrics.

To configure Grafana to connect to Prometheus, do the following -
1. Login using the default credentials - `admin/[password](https://github.com/prometheus-community/helm-charts/blob/main/charts/kube-prometheus-stack/values.yaml#L661)`
2. Add a data source and select prometheus.
3. Run `kubectl get svc -n default` to get a list of services. By default the Prometheus service will be named `prometheus-stack-kube-prom-prometheus`.
4. Add the prometheus address as `http://prometheus-stack-kube-prom-prometheus:9090/....`. Now grafana should be able to connect to Prometheus and show all the metrics being collected.
