#!/usr/bin/env python3

# generates config block for haproxy configuration
#
# usage: $0 input-file nodePort
#
# where nodePort is the K8s worker node port exposed by the Ingress-Nginx controller daemonset 

import sys

path = sys.argv[1]
node_port = sys.argv[2]

output_basename = path.split('.')[0]
output_filename = output_basename + ".out"

data_file = open(path, 'r')
output_file = open(output_filename, 'w')

# haproxy backends data structure

# hap_be[hostname] = { serverName: hostname,
#            serverIP: internal-IP,
#            nodePort: nodePort }

# read input file line, split into array elements
# store array elements in hap_be dict structure

hap_be = {}

for config_line in data_file:

    # split line into array elements [0,1]
    items = config_line.split()

    key = items[0]   # server hostname
    value = items[1] # internal-IP

    hap_be[key] = { 'serverName': key, 'serverIP': value, 'nodePort': node_port }

    
#print(hap_be)

for key in hap_be:

    cfg_line = "server %s %s:%s check port %s ssl verify none\n" % (hap_be[key]['serverName'], hap_be[key]['serverIP'], hap_be[key]['nodePort'], hap_be[key]['nodePort'])

    output_file.write(cfg_line)

