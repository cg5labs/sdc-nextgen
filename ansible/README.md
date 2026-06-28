
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

Playbook for xsrv011 invokes the Ansible Roles 'xoa' and 'nginx' to setup a Xen Orchestra appliance with Nginx as reverse proxy. 
The playbook also expects a TLS key and certificate to be present in the 'files' directory. The TLS key and certificate are used by Nginx to serve the Xen Orchestra web interface over HTTPS.

To create a self-signed TLS key and certificate, you can use the following command:

```
openssl genrsa -out ansible/roles/nginx/files/nginx.key 2048
openssl req -new -key ansible/roles/nginx/files/nginx.key -out ansible/roles/nginx/files/nginx.csr
openssl x509 -req -days 3650 -in ansible/roles/nginx/files/nginx.csr -signkey ansible/roles/nginx/files/nginx.key -out ansible/roles/nginx/files/nginx.crt
```
The XOA credentials (admin e-mail and password) are injected into the playbook via extra-vars. The playbook can now be run with the generated TLS key and cert and runtime XOA credentials:
```
(ansible) $ ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i inventory --private-key $HOME/.ssh/id_rsa -e @vars/<xsrv-varfile>.yaml -e "xo-cli_email=abc@def.com" -e "xo-cli_password=secret" playbooks/xen-vm-create.yaml
```

Playbooks are WIP. 

The inventory contains DNS names that are statically assigned with DHCP to the host VMs with the matching MAC addresses.
