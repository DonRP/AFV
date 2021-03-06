from fileinput import FileInput
from glob import glob
import os

# ATTENTION: there must not be 2 equal key or value
dict = {
    # potorpy only#--- "Ignore this. translate only: One"
    """\n  """: """#--- \"Ignore this. translate only: One\"\n\n  """,
    """ """: """#p--- \"Ignore this. translate only: One\"\n """,
    """:\n\n    # """: """:\n    # """,
    # not traslate
    """\n# game""": """    new \"\"\n\n# game""",
    # accapo
    """    new \"[""": """    [""",
    """""": """\"
\"""",
    """""": """\"\n\"""",
    """""": """\"\n\"""",
    """    old \"""": """msgid \"""",
    """    new \"""": """msgstr[0] \"""",

    # search_text : replace_text
    """
translate crowdin""": """ ## translate crowdin""",
    """    # game""": """# XX## game""",
    """:
    # """: """:
msgid \"""",
    """\" nointeract""": """ [nointeract]\"""",
    """\" with Dissolve(2.0)""": """ [withDissolve(2.0)]\"""",
    """\n    """: """\nmsgstr \"""",
    # ch
    """ \"D \"""": """ \"[D] """,
    """ \"B \"""": """ \"[B] """,
    """ \"J \"""": """ \"[J] """,
    """ \"P \"""": """ \"[P] """,
    """ \"Z \"""": """ \"[Z] """,
    """ \"H \"""": """ \"[H] """,
    """ \"K \"""": """ \"[K] """,
    """ \"W \"""": """ \"[W] """,
    """ \"R \"""": """ \"[R] """,
    """ \"M \"""": """ \"[M] """,
    """ \"L \"""": """ \"[L] """,
    """ \"X \"""": """ \"[X] """,
    """ \"A \"""": """ \"[A] """,
    """ \"S \"""": """ \"[S] """,
    """ \"C \"""": """ \"[C] """,
    """ \"G \"""": """ \"[G] """,
    """ \"RT \"""": """ \"[RT] """,
    """ \"MT \"""": """ \"[MT] """,
    """ \"KT \"""": """ \"[KT] """,
    """ \"ST \"""": """ \"[ST] """,
    """ \"CT \"""": """ \"[CT] """,
    """ \"AD \"""": """ \"[AD] """,
    """ \"MG \"""": """ \"[MG] """,
    """ \"MD \"""": """ \"[MD] """,
    """ \"LT \"""": """ \"[LT] """,
    """ \"EV \"""": """ \"[EV] """,
    """ \"MB \"""": """ \"[MB] """,
    """ \"MS \"""": """ \"[MS] """,
    """ \"DS \"""": """ \"[DS] """,
    """ \"WT \"""": """ \"[WT] """,
    """ \"GF \"""": """ \"[GF] """,
    """ \"GP \"""": """ \"[GP] """,
    """ \"CM \"""": """ \"[CM] """,
    """ \"PH \"""": """ \"[PH] """,
    """ \"CD \"""": """ \"[CD] """,
    """ \"MP \"""": """ \"[MP] """,
    """ \"SG \"""": """ \"[SG] """,
    """ \"MJ \"""": """ \"[MJ] """,
    """ \"CC \"""": """ \"[CC] """,
    """ \"VP \"""": """ \"[VP] """,
    """ \"IV \"""": """ \"[IV] """,
    """ \"SR \"""": """ \"[SR] """,
    """ \"PM \"""": """ \"[PM] """,
    """ \"HG \"""": """ \"[HG] """,
    """ \"UB \"""": """ \"[UB] """,
    """ \"SY \"""": """ \"[SY] """,
    """ \"RG \"""": """ \"[RG] """,
    """ \"P1 \"""": """ \"[P1] """,
    """ \"BR \"""": """ \"[BR] """,
    """ \"LRG \"""": """ \"[LRG] """,
    """ \"PMT \"""": """ \"[PMT] """,
    """ \"CDT \"""": """ \"[CDT] """,
    """ \"MBT \"""": """ \"[MBT] """,
    """ \"ADT \"""": """ \"[ADT] """,
    """ \"MPT \"""": """ \"[MPT] """,
    """ \"SRT \"""": """ \"[SRT] """,
    """ \"MDT \"""": """ \"[MDT] """,
    """ \"VOM \"""": """ \"[VOM] """,
    """ \"HGT \"""": """ \"[HGT] """,
    """ \"MGT \"""": """ \"[MGT] """,
    """ \"WTT \"""": """ \"[WTT] """,
    """ \"MST \"""": """ \"[MST] """,
    """ \"CMT \"""": """ \"[CMT] """,
    """ \"GCP \"""": """ \"[GCP] """,
    """ \"EBE \"""": """ \"[EBE] """,
    """ \"AUB \"""": """ \"[AUB] """,
    """ \"RLT_dealer \"""": """ \"[RLT_dealer] """,
    """ \"BJ_dealer \"""": """ \"[BJ_dealer] """,
    # Fix
    """msgstr \"\"[""": """msgstr \"[@""",
    """msgid \"\"[""": """msgid \"[@""",
    #Final
    """\n ## translate crowdin strings:\n\n""": """\n\n# XXtranslate crowdin strings:XX\n""",
    """:XX\n# XX## game""": """:XX# XX## game""",
    # date
    """HH:HH\n\n# game""": """HH:HH# game""",
    """HH:HH\n\n# XXtranslate""": """HH:HH# XXtranslate""",
    # potorpy only
    """msgstr \"[""": """msgstr \"\"[""",
    """msgstr \"\"""": """msgstr \"""",
    """""": """msgstr \"\"""",
    """#p---""": """msgid_plural""",
    """#---""": """msgstr[1]""",
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
    path = "game/tl/"
    dir_list = glob(path + "/**/*.rpy", recursive=True)
    return dir_list


def rpytopo():
    for path in getListFiles():
        replaceDictionary(path, dict=dict)


def potorpy():
    for path in getListFiles():
        replaceDictionary(path, dict=dict, reverse=True)


potorpy()
