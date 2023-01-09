#!/usr/bin/env bash

# script to return the nodePort of the ingress-nginx-controller service 
# and worker node hostname, IP to generate haproxy config blocks

# cleanup
if [[ -f wrkfile.dat ]]; then 
    rm -v wrkfile.dat
fi

if [[ -f wrkfile.out ]]; then
    rm -v wrkfile.out
fi

NodePort="$(kubectl get svc -n ingress-nginx ingress-nginx-controller -o json | jq -c '.spec.ports[] | select( .appProtocol == "https" )' | jq -r '.nodePort')"

#kubectl get nodes -o='custom-columns=NodeName:.metadata.name,IP:.status.addresses[?(@.type=="InternalIP")].address'

# filter control-plane out
kubectl get nodes --selector='!node-role.kubernetes.io/control-plane' -o='custom-columns=NodeName:.metadata.name,IP:.status.addresses[?(@.type=="InternalIP")].address' |grep -v NodeName > wrkfile.dat

python3 haproxy_cfg.py wrkfile.dat $NodePort

echo
echo "Generated config block: "
echo 
cat wrkfile.out
