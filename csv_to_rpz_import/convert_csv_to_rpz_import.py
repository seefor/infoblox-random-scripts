#!/usr/bin/env python3
#vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
'''

 Description:

    Import CSV File for Infoblox NIOS and perform appropriate action.
    Allows for the monitoring of the CSV job progress.

 Requirements:
   Python 3.6+

 Author: Sif Baksh

 Date Last Updated: 20210507

 Todo:

 Copyright (c) 2021 Sif Baksh

 Redistribution and use in source and binary forms,
 with or without modification, are permitted provided
 that the following conditions are met:

 1. Redistributions of source code must retain the above copyright
 notice, this list of conditions and the following disclaimer.

 2. Redistributions in binary form must reproduce the above copyright
 notice, this list of conditions and the following disclaimer in the
 documentation and/or other materials provided with the distribution.

 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 POSSIBILITY OF SUCH DAMAGE.

'''
__version__ = '0.1.1'
__author__ = 'Sif Baksh'
__author_email__ = 'sifbaksh@gmail.com'

# Import the required Python modules.
import os
import sys

#
# You can edit these as needed
#
input_csv = "bad_domains.txt"
rpz = "local.baksh.com"
output_csv = "import_file.csv"
view = "default"

# ** Misc Functions **
def reverse_labels(domain):
    '''
    Reserve order of domain labels (or any dot separated data, e.g. IP)
    Parameters:
        domain (str): domain.labels
    Returns:
        rdomain (str): labels.domain
    '''
    rdomain = ""
    labels = domain.split(".")
    for l in reversed(labels):
        if rdomain:
            rdomain = rdomain+"."+l
        else:
            rdomain = l
    return rdomain


def create_import_file(rpz, rev):
    wfile = open(output_csv, 'w')
    # These are the required fields for the HEADER of the CSV file
    wfile.write("header-responsepolicycnamerecord,fqdn*,canonical_name,parent_zone,view\n")
    file1 = open(input_csv, 'r')
    domains = file1.readlines()
    # Strips the newline character and appended rpz to it
    for domain in domains:
        name = domain.rstrip() + "." + rpz
        wfile.write("responsepolicycnamerecord," + name + ",*," + rev + "," + view + "\n")

#
# This will reverse the RPZ zone for
#
rev = reverse_labels(rpz)
#
# This will create the import csv file
#
create_import_file(rpz, rev)

