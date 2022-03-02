# HTTPS Load Balancing on GCP

To understand how this pipeline is created on GCP,  see this [page](https://cloud.google.com/iap/docs/load-balancer-howto)

## Requirements:  
- Existing static site on GCP bucket. You can use this template here to create on: 
  - Note the bucket name needs to be the same on this code layer
- *Clear all resources with the same name that you are going to be using* (There's a pipeline for that!)
  - If you have a resource with the same name, it will fail the pipeline
- Once the DNS zones are created, you will need to update the domains nameservers on the registrar. Go to the Cloud DNS to find the nameserver GCP has created 

## Code Layer
The code layer has variables that need to be filled in for this pipeline to work. Please view the code layer and read the comments to execute this pipeline properly
