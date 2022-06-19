
## Implementation

### Ansible 

#### Instantiate a Xenserver VM from template

Mainly adapted from [https://jrisch.medium.com/using-ansible-to-automate-vm-creation-on-xenserver-d092aa484a06](https://jrisch.medium.com/using-ansible-to-automate-vm-creation-on-xenserver-d092aa484a06)

Usage:

```
(ansible) $ ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i inventory --private-key $HOME/.ssh/id_rsa -e @vars/<xsrv-varfile>.yaml playbooks/xen-vm-create.yaml
```

Playbook for xsrv005 invokes the Ansible Roles 'k8s-common', 'k8s-master'  at the end to setup a Kubernetes master with 'kubeadm init'.

Playbook for xsrv006 invokes the Ansible Role 'k8s-common' and a few host-specific tasks at the end to setup a Kubernetes worker with 'kubeadm join'.

Playbooks are WIP. 

The inventory contains DNS names that are statically assigned with DHCP to the host VMs with the matching MAC addresses.
