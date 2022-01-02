style inventory_label:
    xalign .4

style slot:
    background Frame("square", 0,0)
    minimum(80,80)
    maximum(80,80)
    xalign 0.5

screen stats_screen():
    style_prefix "stats"

    add "MobileScreen.png"
    modal True

    frame xalign .495 yalign .297:# at truecenter:
        background  "Mobile_event_Screen.png"
        has vbox

        side ("c"):
            area (1,0,315,510)
            viewport id "stats_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                vbox:

                    text _("") size 10

                    text _("{color=#42f456}Mom's:{/color}") outlines [ (3,"#000000",0,0) ] xpos .1 ypos .08
                    text _("{color=#000000}Respect..............[momrespect]{/color}") xpos .4 ypos .11
                    text _("{color=#000000}Affection............[momaffection]{/color}") xpos .4 ypos .14
                    text _("{color=#000000}Libido................[momlibido]{/color}") xpos .4 ypos .17
                    text _("{color=#000000}Submission........[momsubmission]{/color}") xpos .4 ypos .40
                    text _("{color=#000000}Anger..................[momanger]{/color}") xpos .4 ypos .43

                    text _("{color=#f442d9}Lauren's:{/color}") outlines [ (3,"#000000",0,0) ] xpos .1 ypos .47
                    text _("{color=#000000}Respect............[laurenrespect]{/color}") xpos .4 ypos .30
                    text _("{color=#000000}Affection.........[laurenaffection]{/color}") xpos .4 ypos .33
                    text _("{color=#000000}Libido.............[laurenlibido]{/color}") xpos .4 ypos .37
                    text _("{color=#000000}Submission....[laurensubmission]{/color}") xpos .4 ypos .40
                    text _("{color=#000000}Anger..............[laurenanger]{/color}") xpos .4 ypos .43

                    text _("{color=#006600}Sidney's:{/color}") outlines [ (3,"#000000",0,0) ] xpos .1 ypos .47
                    text _("{color=#000000}Respect............[sidneyrespect]{/color}") xpos .4 ypos .50
                    text _("{color=#000000}Affection.........[sidneyaffection]{/color}") xpos .4 ypos .53
                    text _("{color=#000000}Libido.............[sidneylibido]{/color}") xpos .4 ypos .56
                    text _("{color=#000000}Submission.....[sidneysubmission]{/color}") xpos .4 ypos .59
                    text _("{color=#000000}Anger...............[sidneyanger]{/color}") xpos .4 ypos .62

                    text _("{color=#9966FF}Aunt Camille's:{/color}") outlines [ (3,"#000000",0,0) ] xpos .1 ypos .47
                    text _("{color=#000000}Respect............[auntrespect]{/color}") xpos .4 ypos .50
                    text _("{color=#000000}Affection.........[auntaffection]{/color}") xpos .4 ypos .53
                    text _("{color=#000000}Libido.............[auntlibido]{/color}") xpos .4 ypos .56
                    text _("{color=#000000}Submission.....[auntsubmission]{/color}") xpos .4 ypos .59
                    text _("{color=#000000}Anger...............[auntanger]{/color}") xpos .4 ypos .62

                    text _("{color=#85c1e9}Mandy's:{/color}") outlines [ (3,"#000000",0,0) ] xpos .1 ypos .47
                    text _("{color=#000000}Respect............[cousinrespect]{/color}") xpos .4 ypos .50
                    text _("{color=#000000}Affection.........[cousinaffection]{/color}") xpos .4 ypos .53
                    text _("{color=#000000}Libido.............[cousinlibido]{/color}") xpos .4 ypos .56
                    text _("{color=#000000}Submission.....[cousinsubmission]{/color}") xpos .4 ypos .59
                    text _("{color=#000000}Anger...............[cousinanger]{/color}") xpos .4 ypos .62

                    text _("") size 20

            #vbar value YScrollValue("stats_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG

    textbutton "{color=#ff0000}Return{/color}":
        action [ Hide("stats_screen"), Show("phone_interface") ]
        xalign 0.5
        yalign 0.85
        text_size 30
