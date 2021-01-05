#!/usr/bin/bash

#part1: copies files from covid-upload area to ebi-cli dir
#should be run from the directory where you would like the UUID dir (+ files) to be created & kept

UUID=$1 #setting UUID as argument to pass
USERNAME=$2 #for ssh'ing into ebi-cli

covid-util select ${UUID} 
echo "Files in this upload area:" 
covid-util list

echo "transferring files to the following ebi-cli directory: /nfs/production/ena_utils/covid/${UUID}"

#logs in to correct dir on ebi-cli + activate aws + creates UUID dir on ebi-cli & then copy files from covid-utils upload area to ebi-cli location and closes login shell
ssh -t ${USERNAME}@ebi-cli "cd /nfs/production/ena_utils/covid; cd venv/; source bin/activate; aws configure; cd bin; echo && echo 'first creating directory /nfs/production/ena_utils/covid/${UUID} on ebi-cli' && echo; mkdir /nfs/production/ena_utils/covid/${UUID}; cd /nfs/production/ena_utils/covid/${UUID}; aws --endpoint-url https://s3.embassy.ebi.ac.uk s3 cp s3://covid-utils-ui-88560523/${UUID} . --recursive; echo && echo 'files transferred to ebi-cli:' && echo; ls -lthra; exit; bash -l"
#note: cannot add more commands to the line above and leave the ssh terminal open, as the login shell expects user typed input only

#part 2: copies files from ebi-cli dir back to local machine

mkdir submission_files_${UUID} #creates drag n drop submission directory on local machine (which files will be transferred to)
cd submission_files_${UUID}

{ echo "cd /nfs/production/ena_utils/covid/${UUID}" && echo "ls -lthra" && echo "lpwd" && echo "mget *" && echo "bye" ; } | sftp ${USERNAME}@ebi-cli  #copies all files from ebi-cli to local dir; run from local dir



#############
##improvements TODO:
#1) Add option to transfer specific files only to cluster rather than everything ? maybe by default copy over everything, but if you want to copy specific files, have a warning message and provide user option to type in?

#2) automate aws user input? 
#	option 1: pipe the contents of text file with credentials:  cat "aws_credentials.txt" | ./part_2_covid_file_transfer.bash, but gives error: Pseudo-terminal will not be allocated because stdin is not a terminal.
#	option 2 : write an expect script cont. credentials and then call that from this bash script (but this does not seem to work on git bash)
