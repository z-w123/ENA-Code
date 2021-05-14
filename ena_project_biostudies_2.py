## retrieving project xml data (for single project only)
import requests, xmltodict
url_start = "https://www.ebi.ac.uk/ena/browser/api/xml"
project_acc = "PRJEB38723"
url = "{0}/{1}".format(url_start, project_acc)
response = requests.get(url) #get requests retrieve the webpage for display
data = xmltodict.parse(response.content) #this function converts the xml content into a dictionary
#print(data)

##project xml attributes:
project_name = (data['PROJECT_SET']['PROJECT']['NAME'])
####TODO: need to convert release date to YYYY-MM-DD format for Biostudies
release_date = (data['PROJECT_SET']['PROJECT']['PROJECT_ATTRIBUTES']['PROJECT_ATTRIBUTE'][0]['VALUE']) #is first public date always at this 0 index location of project_attribute??? NOPE you needt obtain first public tag
project_title = (data['PROJECT_SET']['PROJECT']['TITLE'])
project_description = (data['PROJECT_SET']['PROJECT']['DESCRIPTION'])
center_name = (data['PROJECT_SET']['PROJECT']['@center_name'])
project_accession = (data['PROJECT_SET']['PROJECT']['@accession'])


## creating two 'key:value' style lists
# projects = ["PRJEB38723"]
#keys = ["Submission", "Title", "ReleaseDate", "", "Study", "Title", "Description", "Center Name", "", "Link", "Description", "Type", "", "Link", "Type", "", "Author", "Name", "Email", "<affiliation>", "", "Organization", "Name"]
keys = ["Submission", "Title", "ReleaseDate", "", "Study", "Title", "Description", "Center Name", "", "Link", "Description", "Type", "", "Link", "Type", ""]

###### TODO:I don't think the keys [] above accounts for multiple authors :/
###### TODO: have the script allow multiple projects to be specified#############
values = []
values.extend((None, project_name, release_date, ""))
values.extend((None, project_title, project_description, center_name, ""))
values.extend((project_accession, "Raw Data", "ENA", ""))
values.extend(("<insert DOI here>", "DOI", "")) #will need manual adding


##take in author details
# e.g bob, dylan, jameela
# bob@ebi.ac.uk, o2, EBI
# dylan@ebi.ac.uk, o2, EBI
# jameela@uit.ac.uk , o3, uit

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-a', '--author', help='full name of each author enclosed in quotes', type=str, nargs='*',
                    required=True)  # takes in multiple authors
parser.add_argument('-e', '--email', help='email addresses separated by a space', type=str, nargs='*',
                    required=True)  # takes in multiple email addresses
parser.add_argument('-i', '--institution', help='each institution name to be enclosed in quotes', type=str, nargs='*',
                    required=True)  # takes in multiple institutes
args = parser.parse_args()

# print(args.author[1]) # how to specify which specific author or email address

authors = len(args.author)
unique_institutions = len(set(args.institution)) #number of unique institutions
#institutions = args.institution
#print(type(unique_institutions)) - institution arguments are lists

# print(vars(args)) #gets dictionary attribute form of the args?
#def create_author_entries(args):
    #["Author", "Name", "Email", "<affiliation>", "", [
    # # Organization", "Name"] could be the same for multiple authors - include in another for loop
    ###

def create_author_entries(args):
    print()
    print("adding author details below:")
    for i in range(authors):
        keys.extend(("Author", "Name", "Email", "<affiliation>", ""))
        values.extend(("", args.author[i], args.email[i]))
        if authors == unique_institutions:
            values.extend(("o" + str(i + 1), "")) #value for author 'affiliation' key
        else:
            ???
    ###TODO: add <affiliation> cell to each author block
    ##check if args.institution contains duplicate values
    ##if yes, use the length of unique_institutions (e.g, 3) and do str(u+1) for each institution and attribute it to the corresponding author
    #organisation block#
#    for u in range(unique_institutions):
#        keys.extend(("Organization", "Name", ""))
#        values.extend(("o" + str(u + 1), args.institution[u], "")) # this is breaking the script and giving a TypeError: list indices must be integers or slices, not str
create_author_entries(args)


###affiliation block:
        #if authors == unique_institutions:
        # values.extend(("o" + str(i + 1))) #value for author 'affiliation' key
        #    else:
        #for unique_institute in range(unique_institutions):

####see below code for 14th May_2 spreadsheet:
#def create_author_entries(args):
#    print()
#    print("adding author details below:")
#    for i in range(authors):
#        keys.extend(("Author", "Name", "Email", ""))
#        values.extend(("", args.author[i], args.email[i], ""))
    ###TODO: add <affiliation> cell to each author block
    ##check if args.institution contains duplicate values
    ##if yes, use the length of unique_institutions (e.g, 3) and do str(u+1) for each institution and attribute it to the corresponding author
    #organisation block#
#    for u in range(unique_institutions):
#        keys.extend(("Organization", "Name", ""))
#        values.extend(("o" + str(u + 1), args.institution[u], "")) # this is breaking the script and giving a TypeError: list indices must be integers or slices, not str
#create_author_entries(args)





####see below code for 14th May spreadsheet:
#def create_author_entries(args):
#    print()
#    print("adding author details below:")
#    for i in range(authors):
#        keys.extend(("Author", "Name", "Email"))
#        values.extend(("None", args.author[i], args.email[i]))
#    for u in range(unique_institutions):
#        keys.extend(("<affiliation>", "", "Organization", "Name"))
#        values.extend(("o" + str(u + 1), "", "o" + str(u + 1), args.institution[u])) # this is breaking the script and giving a TypeError: list indices must be integers or slices, not str
#create_author_entries(args)

# if args.author: #performs a function for a specific parameter
#    print("correct!")
# else:
#    print("no authors provided")

# values.extend((None, "Zahra", "zahra@ebi.ac.uk", "o1", ""))
#values.extend(("o1", "EBI"))
# print(values)
# need to keep this order below

# values.append(None) #can we append '' instead of none for consistency?
# values.append(data['PROJECT_SET']['PROJECT']['NAME'])
# values.append(data['PROJECT_SET']['PROJECT']['PROJECT_ATTRIBUTES']['PROJECT_ATTRIBUTE'][0]['VALUE'])
# values.append("")
# values.append(None) #have to get rid of None's from excel sheet later
# values.append(data['PROJECT_SET']['PROJECT']['TITLE'])
# values.append(data['PROJECT_SET']['PROJECT']['DESCRIPTION'])
# values.append(data['PROJECT_SET']['PROJECT']['@center_name'])
# values.append("")
# values.append(data['PROJECT_SET']['PROJECT']['@accession'])
# values.append("Raw Data")
# values.append("ENA")
# values.append("")
# values.append("<insert DOI here>")
# values.append("DOI")
# values.append("")
# values.append(None)
# values.append("Zahra")
# values.append("zahra@ebi.ac.uk")
# values.append("o1")
# values.append("")
# values.append("o1")
# values.append("EBI")

print(keys)
print(values)
#keys_values = list(zip(keys,values))
#print("Keys and values are:", keys_values)

## creates a dataframe from zipping tuples together
#import pandas as pd
#df = pd.DataFrame(data=keys_values)
#pd.set_option("display.max_rows", None, "display.max_columns", None)
#print()
#print(df)
## create the pagetab file - note csv format NOT accepted!
#df.to_excel('test14May_2.xlsx', header=None, index=False)


# TODO2) enable multiple projects being linked to a single pagetab
