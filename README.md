# ENA-Code
Any bits of code written for ENA

## checksum_md5_script_v6.sh
Script to compare md5 values for the read files submitted using the covid-utils tool.
Things to note:
- input read files must have some kind of hash at the end of the filename (examples provided in script comments) 
- change the 'submitted_read_files' variable to point to the location where your test files are located
- this script works successfully on the ebi-cli cluster; but **does not work on a Mac or PyCharm terminal** due to discrepancies between Linux (GNU) and Mac (BSD) outputs of the 'md5sum' command
