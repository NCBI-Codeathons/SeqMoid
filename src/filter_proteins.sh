#!/usr/bin/env

FILES=../protein_data_ncbi/*.faa.gz
for f in $FILES;
do
        zcat $f | seqkit grep -i -r -n -p $1[p]*;
done > $1_out.faa
