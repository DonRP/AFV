from fileinput import FileInput
from glob import glob
import os

# ATTENTION: there must not be 2 equal key or value
dict = {
    # search_text : replace_text
    """
translate crowdin""": """ ## translate crowdin""",
    """    # game""": """##@## game""",
    """:

    # """: """
msgid \"""",
    """    old \"""": """msgid  \"""",
    """    new \"""": """msgstr  \"""",
    """\" nointeract""": """ [nointeract]\"""",
    """\" with Dissolve(2.0)""": """ [withDissolve(2.0)]\"""",
    """    """: """msgstr \"""",
    # ch
    """ \"RT \"""": """ \"[RT] """,
    """ \"MT \"""": """ \"[MT] """,
    """ \"R \"""": """ \"[R] """,
    """ \"M \"""": """ \"[M] """,
    """ \"KT \"""": """ \"[KT] """,
    """ \"L \"""": """ \"[L] """,
    """ \"ST \"""": """ \"[ST] """,
    """ \"X \"""": """ \"[X] """,
    """ \"A \"""": """ \"[A] """,
    """ \"S \"""": """ \"[S] """,
    """ \"CT \"""": """ \"[CT] """,
    """ \"C \"""": """ \"[C] """,
    """ \"AD \"""": """ \"[AD] """,
    """ \"MG \"""": """ \"[MG] """,
    """ \"MBT \"""": """ \"[MBT] """,
    """ \"ADT \"""": """ \"[ADT] """,
    """ \"MPT \"""": """ \"[MPT] """,
    """ \"SRT \"""": """ \"[SRT] """,
    """ \"MDT \"""": """ \"[MDT] """,
    """ \"VOM \"""": """ \"[VOM] """,
    """ \"MD \"""": """ \"[MD] """,
    """ \"G \"""": """ \"[G] """,
    """ \"HGT \"""": """ \"[HGT] """,
    """ \"LT \"""": """ \"[LT] """,
    """ \"EV \"""": """ \"[EV] """,
    """ \"MB \"""": """ \"[MB] """,
    """ \"MGT \"""": """ \"[MGT] """,
    """ \"WTT \"""": """ \"[WTT] """,
    """ \"MST \"""": """ \"[MST] """,
    """ \"CMT \"""": """ \"[CMT] """,
    """ \"MS \"""": """ \"[MS] """,
    """ \"DS \"""": """ \"[DS] """,
    """ \"RLT_dealer \"""": """ \"[RLT_dealer] """,
    """ \"WT \"""": """ \"[WT] """,
    """ \"GF \"""": """ \"[GF] """,
    """ \"GP \"""": """ \"[GP] """,
    """ \"CM \"""": """ \"[CM] """,
    """ \"GCP \"""": """ \"[GCP] """,
    """ \"D \"""": """ \"[D] """,
    """ \"B \"""": """ \"[B] """,
    """ \"J \"""": """ \"[J] """,
    """ \"P \"""": """ \"[P] """,
    """ \"BJ_dealer \"""": """ \"[BJ_dealer] """,

    # Fix
    """msgstr \"\"[""": """msgstr \"[@""",
    """msgid \"\"[""": """msgid \"[@""",




    """
 ## translate crowdin strings:

""": """

#@@translate crowdin strings:@@
""",
    """:@@
##@## game""": """:@@##@## game""",


    # date
    """12:36

# game""": """HH:HH# game""",
}


# Creating a function to replace the text
def replacetext(search_text, replace_text, pathFile):

    # Read in the file
    with open(pathFile, "r+", encoding="utf8") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(search_text, replace_text)

    # Write the file out again
    with open(pathFile, 'w', encoding="utf8") as file:
        file.write(filedata)
    return True


def replaceDictionary(pathFile, dict={}, reverse=False):
    print(pathFile)
    if(reverse):
        for item in reversed(list(dict.items())):
            replacetext(pathFile=pathFile,
                        search_text=item[1], replace_text=item[0])
    else:
        for search_text in dict.keys():
            replacetext(pathFile=pathFile, search_text=search_text,
                        replace_text=dict[search_text])


def getListFiles():
    # Get the list of all files and directories
    path = "tl/"
    dir_list = glob(path + "/**/*.po", recursive=True)
    return dir_list


def rpytopo():
    for path in getListFiles():
        replaceDictionary(path, dict=dict)


def potorpy():
    for path in getListFiles():
        replaceDictionary(path, dict=dict, reverse=True)


rpytopo()
