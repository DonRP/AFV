style inventory_label:
    xalign 0.2

style slot:
    background Frame("square", 0,0)
    minimum (80,80)
    maximum (80,80)
    xalign 0.5
image back_01 = im.Scale("images/interface_images/Button_backgal_idle.png", 80, 40) #Enter specific numbers <--
image back_02 = im.Scale("images/interface_images/Button_backgal_hover.png", 80, 40) #Enter specific numbers <--
image next_01 = im.Scale("images/interface_images/Button_nextgal_idle.png", 80, 40) #Enter specific numbers <--
image next_02 = im.Scale("images/interface_images/Button_nextgal_hover.png", 80, 40) #Enter specific numbers <--

init 1 screen stats_screen():

#    if persistent.patreonsafe:
#        $ Mom = "Mom"
#        $ mom = "Mom"
#        $ Dad = "Dad"
#        $ dad = "Dad"
#        $ uncle = "Uncle Bobby"
#        $ Uncle = "Uncle Bobby"
#        $ Auntie = "Aunt Camille"
#        $ auntie = "Aunt Camille"
#        $ Auntie_2 = "Auntie"
#        $ auntie_2 = "Auntie"
#        $ cousin = "Cousin Mandy"
#        $ Cousin = "Cousin Mandy"
#    else:
#        $ Mom = "Mom"
#        $ mom = "mom"
#        $ Dad = "Dad"
#        $ dad = "dad"
#        $ uncle = "uncle Bobby"
#        $ Uncle = "Uncle Bobby"
#        $ Auntie = "Aunt Camille"
#        $ auntie = "aunt Camille"
#        $ Auntie_2 = "Aunt "
#        $ auntie_2 = "aunt "
#        $ cousin = "cousin Mandy"
#        $ Cousin = "Cousin Mandy"

    style_prefix "stats"

    add "MobileScreen.png"
    modal True
    
    imagebutton:
        xalign 0.38
        yalign 0.11
        idle "back_01"
        hover "back_02"
        action [ Hide("stats_screen"),
            Show("stats_screen_boys") ]

    imagebutton:
        xalign 0.604
        yalign 0.11
        idle "next_01"
        hover "next_02"
        action [ Hide("stats_screen"),
            Show("stats_screen_boys") ]
        
    frame xalign .495 yalign .300:# at truecenter:
        background None
        has vbox

        text _("") size 3
        
        text _("Girls stats") at center:
            outlines [(3, "#000", 0,0)]

        text _("{color=#E60000}---------------------------------------{/color}") #at center

        side ("c"):
            area (1,0,315,460)
            viewport id "stats_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                vbox:

                    text _("") size 10
                    ###
                    text _("{image=iconM} {color=#42f456}Mom's:{/color}") outlines [ (3,"#000000",0,0) ] xpos .1 ypos .08
#                    text "" size 0.5
                    text _("{image=respect}{color=#000000} Respect..............[momrespect]{/color}") xpos .25 ypos .11
                    text _("{image=affection}{color=#000000} Affection............[momaffection]{/color}") xpos .25 ypos .14
                    text _("{image=libido}{color=#000000} Libido..................[momlibido]{/color}") xpos .25 ypos .17
                    text _("{image=submission}{color=#000000} Submission........[momsubmission]{/color}") xpos .25 ypos .40
                    text _("{image=anger}{color=#000000} Anger...................[momanger]{/color}") xpos .25 ypos .43
                    ###
                    text _("{image=iconL} {color=#f442d9}Lauren's:{/color}") outlines [ (3,"#000000",0,0) ] xpos .1 ypos .28
#                    text "" size 0.5
                    text _("{image=respect}{color=#000000} Respect..............[laurenrespect]{/color}") xpos .25 ypos .31
                    text _("{image=affection}{color=#000000} Affection............[laurenaffection]{/color}") xpos .25 ypos .33
                    text _("{image=libido}{color=#000000} Libido..................[laurenlibido]{/color}") xpos .25 ypos .37
                    text _("{image=submission}{color=#000000} Submission........[laurensubmission]{/color}") xpos .25 ypos .40
                    text _("{image=anger}{color=#000000} Anger...................[laurenanger]{/color}") xpos .25 ypos .43
                    if start_of_campaign:
                        text _("{image=election}{color=#000000} School influence.[school_influence]{/color}") xpos .25 ypos .46
                    ###
                    text _("{image=iconS} {color=#006600}Sidney's:{/color}") outlines [ (3,"#000000",0,0) ] xpos .1 ypos .48
                    text "" size 4
                    text _("{image=respect}{color=#000000} Respect..............[sidneyrespect]{/color}") xpos .25 ypos .51
                    text _("{image=affection}{color=#000000} Affection............[sidneyaffection]{/color}") xpos .25 ypos .53
                    text _("{image=libido}{color=#000000} Libido..................[sidneylibido]{/color}") xpos .25 ypos .56
                    text _("{image=submission}{color=#000000} Submission........[sidneysubmission]{/color}") xpos .25 ypos .59
                    text _("{image=anger}{color=#000000} Anger...................[sidneyanger]{/color}") xpos .25 ypos .62
#                    text _("{image=load_counter}{color=#000000} Load counter.....[sidney_cum_loads_counter]{/color}") xpos .25 ypos .65
                    ###
                    text _("{image=iconC} {color=#85c1e9}Cousin Mandy's:{/color}") outlines [ (3,"#000000",0,0) ] xpos .1 ypos .68
                    text "" size 7
                    text _("{image=respect}{color=#000000} Respect..............[cousinrespect]{/color}") xpos .25 ypos .71
                    text _("{image=affection}{color=#000000} Affection............[cousinaffection]{/color}") xpos .25 ypos .73
                    text _("{image=libido}{color=#000000} Libido..................[cousinlibido]{/color}") xpos .25 ypos .76
                    text _("{image=submission}{color=#000000} Submission........[cousinsubmission]{/color}") xpos .25 ypos .79
                    text _("{image=anger}{color=#000000} Anger...................[cousinanger]{/color}") xpos .25 ypos .82
                    ###
                    text _("{image=iconA} {color=#9966FF}Aunt Camille's:{/color}") outlines [ (3,"#000000",0,0) ] xpos .1 ypos .85
                    text "" size 7
                    text _("{image=respect}{color=#000000} Respect..............[auntrespect]{/color}") xpos .25 ypos .88
                    text _("{image=affection}{color=#000000} Affection............[auntaffection]{/color}") xpos .25 ypos .91
                    text _("{image=libido}{color=#000000} Libido..................[auntlibido]{/color}") xpos .25 ypos .94
                    text _("{image=submission}{color=#000000} Submission........[auntsubmission]{/color}") xpos .25 ypos .97
                    text _("{image=anger}{color=#000000} Anger...................[auntanger]{/color}") xpos .25 ypos 1.00
                    ###
#                    text _("{image=iconMG} {color=#99FF99}Mandy's:{/color}") outlines [ (3,"#000000",0,0) ] xpos .1 ypos 1.03
#                    text "" size 7
#                    text _("{image=load_counter}{color=#000000} Load counter.....[megan_cum_loads_counter]{/color}") xpos .25 ypos 1.06
                    ###
                    text _("") size 40

            #vbar value YScrollValue("stats_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG


    imagebutton auto "images/interface_images/phone_screen_images/home_%s.png":
        action [ Hide("stats_screen"), Show("phone_interface") ]
        xalign 0.495
        yalign 0.91

    imagebutton:
        xalign 0.6345
        yalign 0.15
        idle "phoneExitIdle"
        hover "phoneExitHover"
        if persistent.mod_on:
            action [ [ Hide("{}".format(k)) for k in close_phone_screens ],
                [ SetVariable("stats_var{}".format(k), False) for k in list_girl_characters ],
                SetVariable("items_var", False),
                SetVariable("week_day_var", False) ]
        else:
            action [ Hide("{}".format(k)) for k in close_phone_screens ]

init 1 screen stats_screen_boys():


    style_prefix "stats"

    add "MobileScreen.png"
    modal True
    
    imagebutton:
        xalign 0.38
        yalign 0.11
        idle "back_01"
        hover "back_02"
        action [ Hide("stats_screen_boys"),
            Show("stats_screen") ]

    imagebutton:
        xalign 0.604
        yalign 0.11
        idle "next_01"
        hover "next_02"
        action [ Hide("stats_screen_boys"),
            Show("stats_screen") ]
        
    frame xalign .495 yalign .300:# at truecenter:
        background None
        has vbox

        text _("") size 3
        
        text _("  Loads counter {image=load_counter}") at center:
            outlines [(3, "#000", 0,0)]

        text _("{color=#E60000}---------------------------------------{/color}") #at center

        side ("c"):
            area (1,0,315,460)
            viewport id "stats_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                vbox:

                    text _("") size 10
                    ###
                    text _("{image=iconR} {color=#0000CC} By [ryan]:{/color}") outlines [ (3,"#000000",0,0) ] xpos .1 ypos .08
#                    text "" size 0.5
#                    text _("{image=iconM}{color=#42f456} in Mom..............[mom_cum_loads_counter]{/color}") outlines [ (3,"#000000",0,0) ] xpos .25 ypos .11
                    text _("{image=iconL}{color=#f442d9} in Lauren............[lauren_cum_loads_counter]{/color}") outlines [ (3,"#000000",0,0) ] xpos .25 ypos .14
                    text _("{image=iconS}{color=#006600} in Sidney.............[sidney_cum_loads_counter]{/color}") outlines [ (3,"#000000",0,0) ] xpos .25 ypos .17
#                    text _("{image=iconA}{color=#9966FF} in Aunt Camille........[aunt_cum_loads_counter]{/color}") outlines [ (3,"#000000",0,0) ] xpos .25 ypos .40
#                    text _("{image=iconC}{color=#85c1e9} in Cousin Mandy........[cousin_cum_loads_counter]{/color}") outlines [ (3,"#000000",0,0) ] xpos .25 ypos .43
                    text _("{image=iconMG}{color=#99FF99} in Megan.............[megan_cum_loads_counter]{/color}") outlines [ (3,"#000000",0,0) ] xpos .25 ypos .43
                    ###
                    text _("") size 20
                    ###
                    if lauren_matt_cum_loads_counter >= 1 :
                        text _("{image=iconMT} {color=#993300} By Matt:{/color}") outlines [ (3,"#000000",0,0) ] xpos .1 ypos .28
                        text "" size 0.5
#                        text _("{image=iconM}{color=#42f456} in Mom..............[mom_matt_cum_loads_counter]{/color}") outlines [ (3,"#000000",0,0) ] xpos .25 ypos .31
                        text _("{image=iconL}{color=#f442d9} in Lauren............[lauren_matt_cum_loads_counter]{/color}") outlines [ (3,"#000000",0,0) ] xpos .25 ypos .33
#                        text _("{image=iconS}{color=#006600} in Sidney..................[sidney_matt_cum_loads_counter]{/color}") outlines [ (3,"#000000",0,0) ] xpos .25 ypos .37
#                        text _("{image=iconA}{color=#9966FF} in Aunt Camille........[aunt_matt_cum_loads_counter]{/color}") outlines [ (3,"#000000",0,0) ] xpos .25 ypos .40
#                        text _("{image=iconC}{color=#85c1e9} in Cousin Mandy..................[cousin_matt_cum_loads_counter]{/color}") outlines [ (3,"#000000",0,0) ] xpos .25 ypos .43
#                        text _("{image=iconMG}{color=#99FF99} in Megan.....[megan_matt_cum_loads_counter]{/color}") outlines [ (3,"#000000",0,0) ] xpos .25 ypos .46
                        ###
                    text _("") size 40

            #vbar value YScrollValue("stats_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG


    imagebutton auto "images/interface_images/phone_screen_images/home_%s.png":
        action [ Hide("stats_screen_boys"), Show("phone_interface") ]
        xalign 0.495
        yalign 0.91

    imagebutton:
        xalign 0.6345
        yalign 0.15
        idle "phoneExitIdle"
        hover "phoneExitHover"
        action [ Hide("{}".format(k)) for k in close_phone_screens ]
