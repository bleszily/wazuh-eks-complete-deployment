# initialize terraform configuration
terraform init

# validate terraform configuration
terraform validate

# create terraform plan
terraform plan -out state.tfplan

# apply terraform plan
terraform apply state.tfplan

# cleanup
terraform destroy -auto-approve

#Configure Kubectl
#Step1: Retrieve access credentials for the cluster and configure kubectl
aws eks --region $(terraform output -raw region) update-kubeconfig \
    --name $(terraform output -raw cluster_name)

#Step2: Verify the cluster is ready
kubectl cluster-info
kubectl get nodes


#Set default editor
export KUBE_EDITOR=nano

kubectl edit configmap -n kube-system aws-auth

kubectl get pod
kubectl describe pod <pod name>
kubectl exec -it wazuh-manager-master-0 -- /bin/bash