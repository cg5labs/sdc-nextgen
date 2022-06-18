
### Ansible 

#### Instantiate a Xenserver VM from template

Mainly adapted from [https://jrisch.medium.com/using-ansible-to-automate-vm-creation-on-xenserver-d092aa484a06](https://jrisch.medium.com/using-ansible-to-automate-vm-creation-on-xenserver-d092aa484a06)

Usage:

```
$ ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i inventory -e @vars/xsrv005.yaml playbooks/xen-vm-create.yaml
```

Playbook for xsrv005 invokes the Ansible Role 'k8s-master' at the end to setup a Kubernetes master with 'kubeadm init'.

