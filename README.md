# SeqMo-ID: A pipeline for conserved protein sequence motif identification

## About SeqMo_ID

### What is a conserved protein sequence motif?

Consensus sequence motifs are short sequences of amino acids shared by proteins across multiple organisms that are associated with a specific biological function such as phosphorylation sites and metal binding sites. [Currated databases](http://elm.eu.org/elms) of sequence motifs are publically available. 

### What tools are currently available for sequence motif identification? 

There are currently web applications available that indentify sequence motifs from a database of motifs ([ELM](http://elm.eu.org/index.html)) or from either a database or a user specified sequence ([ScanProsite](https://prosite.expasy.org/scanprosite/)). Both of these resources include statistical tools to quantify the probability of a given motif occuring. However, the rate of false positives is still high as concensus motifs are short and can be found by chance.  

### How is SeqMo_ID unique?

SeqMo_ID works on the hypothesis that a high degree of conservation of consensus sites can be used to identify sequence motifs that are functional *in vivo*. It takes multiple protein sequences from different individuals or species and determines how conserved a given motif is across the sample. More highly conserved motifs are more likely candidates to be biologically functional. 

## Workflow

![alt text](https://github.com/NCBI-Codeathons/protein-motif-identification/blob/master/workflow.png "Workflow Schematic")

## Future directions

TBD

## Dependencies

TBD

## Contributors

Listed alphabetically by last name

* Miranda Lynch, PhD, Hauptman-Woodward Medical Research Institute 
* Kevin McPherson, Bellwethr 
* Amy Pomeroy, UNC Chapel Hill Medical School
* Kimiko Suzuki, UNC Chapel Hill Medical School 
