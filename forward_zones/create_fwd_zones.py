#!/usr/local/bin/python3
'''
 Description:
    Create Forward zones from a CSV file with these headers zone, dns_view, dns_host, ext_fwd, nsgs

 Requirements:
   - pip3 install bloxone

 Author: Sif Baksh
 Date Last Updated: 20210530
 Todo:
  - Check if more than one External Forward exist
 Copyright (c) 2021 Sif Baksh
'''
__version__ = '0.1.0'
__author__ = 'Sif Baksh'
__author_email__ = 'sifbaksh@gmail.com'

import bloxone
import json
import csv

csp_token = 'csp.ini'
b1ddi = bloxone.b1ddi(csp_token)

def create_paylod(zone,view,host,ext_fwd,nsgs):
  # Create Forward Zone with NSG
  if not ext_fwd:
    payload = json.dumps({
      "forward_only": True,
      "fqdn": zone,
      "nsgs": [
          nsgs
      ],
      "tags": {
          "Owner": "sbaksh"
      },
      "view": view
    })
  # Create Forward Zone with External Forwarders
  else:
    payload = json.dumps({
      "external_forwarders": [
          {
              "address": ext_fwd
          }
      ],
      "forward_only": True,
      "fqdn": zone,
      "hosts": [
          host
      ],
      "tags": {
          "Owner": "sbaksh"
      },
      "view": view
    })
  return payload
# read csv file into a dict
# zone, dns_view, dns_host, ext_fwd, nsgs
reader = csv.DictReader(open("zones.csv"))
(reader.fieldnames)
for row in reader:
    zone = row['zone']
    # This will error out if External Forwarder and Name Server Group
    if not row['ext_fwd'] and not row['nsgs']:
      print(f'[-]{zone} missing External Forwarder and Name Server Groups')
    # If External Forwarder does not have a value this will run
    elif not row['ext_fwd']:
      view = b1ddi.get_id('/dns/view', key="name", value=row['dns_view'], include_path=True)
      nsg = b1ddi.get_id('/dns/forward_nsg', key='name', value=row['nsgs'], include_path=True)
      ext_fwd = ''
      nsgs = nsg
      zone = row['zone']
      payload = create_paylod(zone,view,host,ext_fwd,nsgs)
      r = b1ddi.create('/dns/forward_zone', body=payload)
      print(f'[+]{zone} was created NSG - {row["nsgs"]}')
    # Will create an External Forwarder 
    else:
      print(f'[+]{zone} was created')
      view = b1ddi.get_id('/dns/view', key="name", value=row['dns_view'], include_path=True)
      host = b1ddi.get_id('/dns/host', key='name', value=row['dns_host'], include_path=True)
      ext_fwd = row['ext_fwd']
      nsgs = ''
      zone = row['zone']
      payload = create_paylod(zone,view,host,ext_fwd,nsgs)
      r = b1ddi.create('/dns/forward_zone', body=payload)