
### Ansible 

#### Instantiate a Xenserver VM from template

Usage:

```
$ ansible-playbook -i inventory -e @vars/xsrv005.yaml playbooks/xen-vm-create.yaml
```

Output:
VM IP address detected by xe-guest-tools

