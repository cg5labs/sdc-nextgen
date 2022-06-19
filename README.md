# sdc-nextgen
Next version of my homelab. New stack with xcp-ng as Hypervisor, packer for VM images. K8s cluster for apps.

## Workflows

### VM Image Building

The VM Images are built with Packer using templates from the Bento project.

The Packer templates are for the Xenserver-ISO provider and run Ubuntu 22.04 server as OS.

Packer builds are run remotely on the Xenserver host:

![VM-Image-Build Workflow](img/vm-image-build.drawio.png)


### VM Image Deployment

The VM images are installed using Ansible playbooks and roles. Currently there are two Ansible roles: Kubernetes Master and Worker:

![VM-Image-Deploy Workflow](img/vm-image-deploy.drawio)


The Ansible roles are nothing special, just very basic automation to bootstrap K8s with 'kubeadm' and Flannel as K8s Pod network. This is sufficient for a small vanilla K8s cluster with one master and some workers.

