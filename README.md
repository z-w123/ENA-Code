### Chromosome list file generation ###
Two scripts from this repository can be used to quickly create chromosome list files, for viral assembly submission to the ENA. This has been used for, e.g. SARS-CoV-2 assembly submission.
<br>
#### 1. create_fasta_headers.bash ####
First run this script to generate **a text file listing all fasta headers** from all fasta.gz files in a specific directory:
<br>
```sh create_fasta_headers.bash```
<br>
<br>
*Note: please be aware that leading whitespaces in fasta headers may cause slight indentations in the output file (i.e ```fasta_headers.txt```) produced by the script. Please check this file for any formatting issues before proceeding to Step 2 below.*
<br>

#### 2. generate_chromlistfile.sh ####
Then run this script to create **gzipped chromosome list files** from the list of fasta headers (i.e ```fasta_headers.txt```) produced in Step 1. 
<br>
You must specify the input file at the command line:
<br>
```sh generate_chromlistfile.sh fasta_headers.txt```


