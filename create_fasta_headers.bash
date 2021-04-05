#!/usr/bin/bash
#script to extract all fasta headers and append to text file

printf "all fasta files in this directory are:"
echo 
ls *fasta.gz 

FASTAS_GZ=`ls *fasta.gz`

for fasta in $FASTAS_GZ; do
	gunzip $fasta 
done

UNZ_FASTA=`ls *.fasta`

for unzfasta in $UNZ_FASTA; do
	head -1 $unzfasta | tr -d '>' >> fasta_headers.txt 
done

gzip *.fasta

echo `cat fasta_headers.txt | wc -l` "fasta headers"

if [[ $(sort fasta_headers.txt | uniq -c -d) ]]; then #if uniq produces some output then:
	echo "ERROR: Some fastas have duplicate headings. Submitter should ensure headings for each fasta are unique"
	echo
	echo "duplicate headers below"	
	sort fasta_headers.txt | uniq -c -d
else
	: #do nothing
fi



