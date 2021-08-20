#!/usr/local/bin/python3
__version__ = '0.1.0'
__author__ = 'Sif Baksh'
__author_email__ = 'sifbaksh@gmail.com'

import bloxone
import json
from itertools import islice

csp_token = 'csp.ini'

# Create a BloxOne DDI Object
tdc = bloxone.b1tdc(csp_token)

# 50,000 is the max a Custom list can hold
n = 50000
sum = 0
# Read the filename bad_domains.txt
with open('bad_domains.txt') as file:
    while True:
        next_n_lines = list(islice(file, n))
        if not next_n_lines:
            break
        sum = sum + 1
        if sum <= 10:
            bob = sum - 1
            payload_list = []
            # Strips the newline character
            for line in next_n_lines:
                payload_list.append(line.rstrip())
            sif = str(bob)
            name = "sbaksh-custom-list-" + sif
            payload = json.dumps({
            "items": payload_list,
            "name": name,
            "type": "custom_list"
            })
        else:
            # This will end either at 10 list created which is 500K
            break
        r1 = tdc.post('/named_lists', body=payload).json()
