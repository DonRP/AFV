default ryan = "Ryan"
default mom_name = "Jacky"
default dad_name = "Tony"
default uncle_name = "Bobby"
default auntie_name = "Camille"
default cousin_name = "Mandy"

default Mom = mom_name
default mom = mom_name

default Dad = dad_name
default dad = dad_name

default uncle = uncle_name
default Uncle = uncle_name

default Auntie = auntie_name
default auntie = auntie_name
default Auntie_2 = ""
default auntie_2 = ""
default auntie_name_short = auntie_name[:4]
default auntie_name_short_2 = auntie_name[:3] + auntie_name[2:4]
default auntie_name_short_3 = auntie_name[:5]

default cousin = cousin_name
default Cousin = cousin_name

default upper_ryan = ryan.upper()

default upper_mom = mom.upper()
default upper_mom_name = mom_name.upper()

default upper_dad = dad.upper()
default upper_dad_name = dad_name.upper()

default upper_uncle = uncle.upper()
default upper_uncle_name = uncle_name.upper()

default upper_auntie = auntie.upper()
default upper_auntie_name = auntie_name.upper()

define R = Character(_("[ryan]"), color="0000CC", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define RT = Character(_("[ryan]'s Thoughts"), color="0000CC", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define M = Character(_("Mom"), color="42f456", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define MT = Character(_("Mom's Thoughts"), color="42f456", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define D = Character(_("Dad"), color="CCFF00", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define B = Character(_("Uncle Bobby"), color="7F86A0", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define L = Character(_("Lauren"), color="f442d9", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define LT = Character(_("Lauren's Thoughts"), color="f442d9", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define J = Character(_("Joey"), color="663300", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define G = Character(_("Mafia Goon"), color="330000", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define VOM = Character(_("Voice over Microphone"), color="66FFFF", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define X = Character(_("?????"), color="006666", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define MB = Character(_("Matt"), color="993300", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define S = Character(_("Sidney"), color="006600", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define ST = Character(_("Sidney's Thoughts"), color="006600", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define MG = Character(_("Megan"), color="99FF99", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define MD = Character(_("Mandy"), color="85c1e9", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define MDT = Character(_("Mandy's Thoughts"), color="85c1e9", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define C = Character(_("Aunt Camille"), color="9966FF", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define CT = Character(_("Aunt Camille's Thoughts"), color="9966FF", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])

init python:

    class Player:
        def __init__(self, drunk, drugged):
            self.drunk = drunk
            self.drugged = drugged

#init:

#    default mom = mom_name
#    default Mom = mom_name
#    default mom_name = "Jacky"

#    default dad = dad_name
#    default Dad = dad_name
#    default dad_name = "Tony"

#    default uncle = uncle_name
#    default Uncle = uncle_name
#    default uncle_name = "Bobby"

#    default auntie = auntie_name
#    default Auntie = auntie_name
#    default auntie_name = "Camille"
#    default auntie_name_short = auntie_name[:4]
