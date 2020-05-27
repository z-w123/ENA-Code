#!/usr/bin/bash

#The following script is to check file integrity by comparing the md5 values for submitted files against those calculated, as part of the development of a new, covid data submissions tool on the covid-data portal
#currently, submitted read files have thier md5 sums in the file name itself, rather than a separate file. Eg: a fastq file looks like this: testread.fastq.gz.3396695902fd7ab76d5aaa2fe6297cdc

#testread.fastq.gz.3396695902fd7ab76d5aaa2fe6297cdc
submitted_read_files=$(basename -a `ls /c/Users/zahra/Documents/test/{*fastq*,*cram*,*bam*}`) #change dir according to where read files are #remember all submitted read files have to have hash at the end of filename e.g: testread.fastq.gz.3396695902fd7ab76d5aaa2fe6297cdc  

for file in $submitted_read_files; do
	md5sum $file > ${file}.md5     #testread.fastq.gz.3396695902fd7ab76d5aaa2fe6297cdc.md5 
	new_hash=`cut -d ' ' -f 1 ${file}.md5`  #isolates the hash that we just calculated, inside of the .md5 file we just generated: 3396695902fd7ab76d5aaa2fe6297cdc 
	original_hash=`echo ${file##*.}` #remove everything before the last full stop in filename- so we are left with the hash only
	echo original hash of submitted file $file is $original_hash
	echo newly generated hash for submitted file is $new_hash
	if [[ $new_hash == $original_hash ]];
	then
		echo
		echo submitted and calculated md5 values match - file $file PASSED verification
		echo
		mv $file ${file%.*}  #to rename the 'testread.fastq.gz.3396695902fd7ab76d5aaa2fe6297cdc' files to just 'testread.fastq.gz' so they can be used for downstream analysis
	else
		echo
		echo submitted and calculated md5 values DO NOT match - file $file FAILED verification
		echo
	fi
	
done

