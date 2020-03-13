#!/usr/bin/env python

import os
import sys



def get_idxs(data, protein):
    return [idx for idx, j in enumerate(data.get_headers()) if protein.lower() in j.lower()]

def get_faa_data(idxs, data):
    gseqs = [data.get_seqs()[idx] for idx in idxs]
    gheaders = [data.get_headers()[idx] for idx in idxs]
    return gseqs, gheaders
