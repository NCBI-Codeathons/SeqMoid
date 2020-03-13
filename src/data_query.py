#!/usr/bin/env python

import os
import sys

def download_data(accession_num):
    os.system('curl -o ../protein_data_ncbi/{}.faa.gz https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/146/045/GCA_000146045.2_R64/GCA_000146045.2_R64_protein.faa.gz'.format(accession_num))

def unzip_data(accesssion_num, protein):
    os.system('!zcat ../protein_ncbi_data/GCA_000146045.2_R64_protein.faa.gz | seqkit grep -i -r -n -p {}[p]*'.format{protein})

def get_idxs(data, protein):
    return [idx for idx, j in enumerate(data.get_headers()) if protein.lower() in j.lower()]

def get_faa_data(idxs, data):
    gseqs = [data.get_seqs()[idx] for idx in idxs]
    gheaders = [data.get_headers()[idx] for idx in idxs]
    return gseqs, gheaders


# !zcat ../protein_ncbi_data/GCA_000146045.2_R64_protein.faa.gz | seqkit grep -i -r -n -p Ste50[p]*
