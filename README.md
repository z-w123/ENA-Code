# ENA-Code contents:
1. **checksum_md5_script_v6.sh**: File integrity code written for the covid-utils drag and drop tool
2. **covid_file_transfer_full.bash**: Script to automate transfer of files between covid-utils upload area and the covid dir on ebi-cli (and then back to bioinformatician's local machine)

## checksum_md5_script_v6.sh
Script to compare md5 values for the read files submitted using the covid-utils tool.
Things to note:
- input read files must have some kind of hash at the end of the filename (examples provided in script comments) 
- change the 'submitted_read_files' variable to point to the location where your test files are located
- this script works successfully on the ebi-cli cluster; but **does not currently work on a Mac or PyCharm terminal** due to discrepancies between Linux (GNU) and Mac (BSD) outputs of the 'md5sum' command

## covid_file_transfer_full.bash
Run script as follows: sh covid_file_transfer_full.bash <UUID> <username>
eg: sh covid_file_transfer_full.bash 58b02410-887c-4294-b3b9-58253c907193 zahra
