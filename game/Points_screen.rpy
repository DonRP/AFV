
####################################################################################################################################################
### Variables

init:

    python:
        #to show points ------------------------------------------
        config.underlay.append(
            renpy.Keymap(
                p = lambda: renpy.run(
                    ToggleScreen("Points_screen_Sidney")
                            )
                        )
                    )

#        #to show points ------------------------------------------
#        config.underlay.append(
#            renpy.Keymap(
#                P = lambda: renpy.run(
#                    ToggleScreen("Points_screen_Lauren_cosplay")
#                            )
#                        )
#                    )

#define points_var = 1

####################################################################################################################################################
### Points screen buttons image definition

image anger = "images/interface_images/points_images/Anger.webp"

image libido = "images/interface_images/points_images/Libido.webp"

image submission = "images/interface_images/points_images/Submission.webp"

image affection = "images/interface_images/points_images/Affection.webp"

image respect = "images/interface_images/points_images/Respect.webp"

image election = "images/interface_images/points_images/Vot.webp"

image load_counter = "images/interface_images/points_images/Load_counter.webp"

###

image iconM = "images/interface_images/points_images/icon_M.webp"

image iconL = "images/interface_images/points_images/icon_L.webp"

image iconS = "images/interface_images/points_images/icon_S.webp"

image iconA = "images/interface_images/points_images/icon_A.webp"

image iconC = "images/interface_images/points_images/icon_C.webp"

image iconMG = "images/interface_images/points_images/icon_MG.webp"

image iconR = "images/interface_images/points_images/icon_R.webp"

image iconMT = "images/interface_images/points_images/icon_MT.webp"

###

image null_img = im.Scale("images/interface_images/points_images/Null.webp", 410, 176) #Enter specific numbers <--

###

image points_screen_img = im.Scale("images/interface_images/points_images/points_screen.webp", 410, 176) #Enter specific numbers <--

image Mom_points_img = im.Scale("images/interface_images/points_images/Mom_Points_button.webp", 410, 176) #Enter specific numbers <--

image Lauren_points_img = im.Scale("images/interface_images/points_images/Lauren_Points_button.webp", 410, 176) #Enter specific numbers <--

image Sidney_points_img = im.Scale("images/interface_images/points_images/Sidney_Points_button.webp", 410, 176) #Enter specific numbers <--

image Aunt_points_img = im.Scale("images/interface_images/points_images/Aunt_Points_button.webp", 410, 176) #Enter specific numbers <--

image Cuz_points_img = im.Scale("images/interface_images/points_images/Cuz_Points_button.webp", 410, 176) #Enter specific numbers <--

###

image Lauren_points_img_2 = im.Scale("images/interface_images/points_images/Lauren_Points_button_2.webp", 410, 176) #Enter specific numbers <--

image Sidney_points_img_2 = im.Scale("images/interface_images/points_images/Sidney_Points_button_2.webp", 410, 176) #Enter specific numbers <--

image Cuz_points_img_2 = im.Scale("images/interface_images/points_images/Cuz_Points_button_2.webp", 410, 176) #Enter specific numbers <--

####################################################################################################################################################
### Style

style sts_style:
    size 20
#    bold True
    color "#5c2967"
    hover_color "#b758cd"
    outlines [(3, "#25003a", 0,0)]
#    font "images/interface_images/nav_buttons/Apple Casual Regular.ttf"

####################################################################################################################################################
### Points screen

screen Points_screen_Sidney():
    default points_var = 1

    imagebutton xalign 0.025 yalign 0.2:
            idle ("points_screen_img")
            action NullAction()

    if points_var == 1:
        imagebutton xalign 0.025 yalign 0.2:
            idle ("Mom_points_img")
            action NullAction()

        text _("Mom's stats:"):
            xalign 0.17
            yalign 0.2
            color "#5c2967"
            size 30
#            bold True
            outlines [(3, "#25003a", 0,0)]
            font "images/interface_images/nav_buttons/Apple Casual Regular.ttf"
#            font "images/interface_images/points_images/times.ttf"

        text _("[momaffection]") xalign 0.17 yalign 0.25 style "nav_style"
        text _("[momrespect]") xalign 0.25 yalign 0.25 style "nav_style"
        text _("[momlibido]") xalign 0.25 yalign 0.32 style "nav_style"
        text _("[momsubmission]") xalign 0.17 yalign 0.32 style "nav_style"
        text _("[momanger]") xalign 0.315 yalign 0.28 style "nav_style"

    if points_var == 2:
        imagebutton xalign 0.025 yalign 0.2:
            idle ("Lauren_points_img")
            action NullAction()

        text _("Lauren's stats:"):
            xalign 0.17
            yalign 0.2
            color "#5c2967"
            size 30
#            bold True
            outlines [(3, "#25003a", 0,0)]
            font "images/interface_images/nav_buttons/Apple Casual Regular.ttf"

        text _("[laurenaffection]") xalign 0.17 yalign 0.25 style "nav_style"
        text _("[laurenrespect]") xalign 0.25 yalign 0.25 style "nav_style"
        text _("[laurenlibido]") xalign 0.25 yalign 0.32 style "nav_style"
        text _("[laurensubmission]") xalign 0.17 yalign 0.32 style "nav_style"
        text _("[laurenanger]") xalign 0.315 yalign 0.28 style "nav_style"

    if points_var == 3:
        imagebutton xalign 0.025 yalign 0.2:
            idle ("Sidney_points_img")
            action NullAction()

        text _("Sidney's stats:"):
            xalign 0.17
            yalign 0.2
            color "#5c2967"
            size 30
#            bold True
            outlines [(3, "#25003a", 0,0)]
            font "images/interface_images/nav_buttons/Apple Casual Regular.ttf"

        text _("[sidneyaffection]") xalign 0.17 yalign 0.25 style "nav_style"
        text _("[sidneyrespect]") xalign 0.25 yalign 0.25 style "nav_style"
        text _("[sidneylibido]") xalign 0.25 yalign 0.32 style "nav_style"
        text _("[sidneysubmission]") xalign 0.17 yalign 0.32 style "nav_style"
        text _("[sidneyanger]") xalign 0.315 yalign 0.28 style "nav_style"

    if points_var == 4:
        imagebutton xalign 0.025 yalign 0.2:
            idle ("Aunt_points_img")
            action NullAction()

#        text _("[Auntie]'s stats:"):
        text _(If( persistent.patreonsafe,
            "Auntie's stats:",
            "Auntie's stats:")):
            xalign 0.17
            yalign 0.2
            color "#5c2967"
            size 30
#            bold True
            outlines [(3, "#25003a", 0,0)]
            font "images/interface_images/nav_buttons/Apple Casual Regular.ttf"

        text _("[auntaffection]") xalign 0.17 yalign 0.25 style "nav_style"
        text _("[auntrespect]") xalign 0.25 yalign 0.25 style "nav_style"
        text _("[auntlibido]") xalign 0.25 yalign 0.32 style "nav_style"
        text _("[auntsubmission]") xalign 0.17 yalign 0.32 style "nav_style"
        text _("[auntanger]") xalign 0.315 yalign 0.28 style "nav_style"

    if points_var == 5:
        imagebutton xalign 0.025 yalign 0.2:
            idle ("Cuz_points_img")
            action NullAction()

#        text _(If( persistent.patreonsafe,
#            "Mandy's stats:",
#            "Cousin Mandy's stats:")):
        text _("Mandy's stats:"):
            xalign 0.17
            yalign 0.2
            color "#5c2967"
            size 30
#            bold True
            outlines [(3, "#25003a", 0,0)]
            font "images/interface_images/nav_buttons/Apple Casual Regular.ttf"

        text _("[cousinaffection]") xalign 0.17 yalign 0.25 style "nav_style"
        text _("[cousinrespect]") xalign 0.25 yalign 0.25 style "nav_style"
        text _("[cousinlibido]") xalign 0.25 yalign 0.32 style "nav_style"
        text _("[cousinsubmission]") xalign 0.17 yalign 0.32 style "nav_style"
        text _("[cousinanger]") xalign 0.315 yalign 0.28 style "nav_style"

    textbutton _("<<"):
        xalign 0.11
        yalign 0.2
        text_style "sts_style"
        if points_var > 1:
            action SetScreenVariable("points_var", points_var-1)
        elif points_var == 1:
            action SetScreenVariable("points_var", 5)
#        elif points_var == 1:
#            action NullAction()

    textbutton _(">>"):
        xalign 0.31
        yalign 0.2
        text_style "sts_style"
        if points_var >= 1 and points_var < 5:
            action SetScreenVariable("points_var", points_var+1)
        elif points_var == 5:
            action SetScreenVariable("points_var", 1)
#        elif points_var == 5:
#            action NullAction()

screen Points_screen_Lauren_cosplay():

    imagebutton xalign 0.025 yalign 0.02:
        idle ("Lauren_points_img_2")
        action NullAction()

    text _("[laurenlibido]") xalign 0.24 yalign 0.17 style "nav_style"
    text _("[laurensubmission]") xalign 0.165 yalign 0.17 style "nav_style"

screen Points_screen_Sidney_cosplay():

    imagebutton xalign 0.025 yalign 0.02:
        idle ("Sidney_points_img_2")
        action NullAction()

    text _("[sidneylibido]") xalign 0.24 yalign 0.17 style "nav_style"
    text _("[sidneysubmission]") xalign 0.165 yalign 0.17 style "nav_style"

screen Points_screen_Cuz_dare():

    imagebutton xalign 0.025 yalign 0.02:
        idle ("Cuz_points_img_2")
        action NullAction()

    text _("[cousinlibido]") xalign 0.24 yalign 0.17 style "nav_style"
    text _("[cousinsubmission]") xalign 0.165 yalign 0.17 style "nav_style"
