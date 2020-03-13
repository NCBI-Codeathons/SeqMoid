#!/usr/bin/env python

import os
import glob
# import sys
def download_ftp_data(ftps):
    for ftp in ftps:
        accession = ftp.split('/')[-1]
        os.system('curl -o ./protein_data_ncbi/{} {}'.format(accession, ftp))



def get_protein_data(proteins):
    for protein in proteins:
        os.system('bash ./src/filter_proteins.sh {}'.format(protein))

def get_filtered_data(data, proteins):
    if data[0] == 'downloaded':
        get_protein_data(proteins)
    elif data[0] == 'ftp':
        download_ftp_data(data[1])
        get_protein_data(proteins)
    else:
        print("Data not in the correct folder")

def get_idxs(data, protein):
    return [idx for idx, j in enumerate(data.get_headers()) if protein.lower() in j.lower()]

def get_faa_data(idxs, data):
    gseqs = [data.get_seqs()[idx] for idx in idxs]
    gheaders = [data.get_headers()[idx] for idx in idxs]
    return gseqs, gheaders
