
### Ansible 

#### Instantiate a Xenserver VM from template

Mainly adapted from [!https://jrisch.medium.com/using-ansible-to-automate-vm-creation-on-xenserver-d092aa484a06](https://jrisch.medium.com/using-ansible-to-automate-vm-creation-on-xenserver-d092aa484a06)

Usage:

```
$ ansible-playbook -i inventory -e @vars/xsrv005.yaml playbooks/xen-vm-create.yaml
```

Output:
VM IP address detected by xe-guest-tools

