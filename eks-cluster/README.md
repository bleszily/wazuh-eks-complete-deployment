# Learn Terraform - Provision an EKS Cluster

Terraform configuration files to provision an EKS cluster on AWS.

The configuration defines a new VPC in which to provision the cluster, and uses the public EKS module to create the required resources, including Auto Scaling Groups, security groups, and IAM Roles and Policies.

Open the main.tf file to review the module configuration. The eks_managed_node_groups parameter configures the cluster with three nodes across two node groups.