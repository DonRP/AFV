
####################################################################################################################################################
### Variables

init:

    default reverse_cuz = False

    default points_var_girls = "mom"
    default points_girls_name = "Mom"

    python:
        #to show points ------------------------------------------
        config.underlay.append(
            renpy.Keymap(
                p = lambda: renpy.run(
                    ToggleScreen("Points_screen_Sidney")
                            )
                        )
                    )

#        config.underlay.append(
#            renpy.Keymap(
#                P = lambda: renpy.run(
#                    ToggleVariable("reverse_cuz")
#                            )
#                        )
#                    )

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

image null_img = im.Scale("images/interface_images/points_images/Null.webp", 410, 176) #Enter specific numbers <--

###

image girls_points_img = ConditionSwitch(
    "points_var == 1", "Mom_points_img",
    "points_var == 2", "Lauren_points_img",
    "points_var == 3", "Sidney_points_img",
    "points_var == 4", "Aunt_points_img",
    "points_var == 5", "Cuz_points_img"
    )

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

image Cuz_points_img_2 = im.Scale("images/interface_images/points_images/Mandy_Points_button_2.webp", 410, 176) #Enter specific numbers <--
image Cuz_points_img_2_reverse = im.Scale("images/interface_images/points_images/Reverse_Mandy_Points_button_2.webp", 410, 176) #Enter specific numbers <--


image Aunt_points_img_2 = im.Scale("images/interface_images/points_images/Camille_Points_button_2.webp", 410, 176) #Enter specific numbers <--

image Mom_points_img_2 = im.Scale("images/interface_images/points_images/Jacky_Points_button_2.webp", 410, 176) #Enter specific numbers <--

####################################################################################################################################################
### Style

style sts_style:
    size 20
#    bold True
    color "#5c2967"
    hover_color "#b758cd"
    outlines [(3, "#25003a", 0,0)]
#    font "images/interface_images/nav_buttons/Apple Casual Regular.ttf"

style sts_name_style:
    color "#5c2967"
    size 30
#    bold True
    outlines [(3, "#25003a", 0,0)]
    font "images/interface_images/nav_buttons/Apple Casual Regular.ttf"
#    font "images/interface_images/points_images/times.ttf"

####################################################################################################################################################
### Points screen

screen Points_screen_Sidney():
    default points_var = 1

    if points_var == 1:
        $ points_var_girls = "mom"
        $ points_girls_name = "Mom"
    elif points_var == 2:
        $ points_var_girls = "lauren"
        $ points_girls_name = "Lauren"
    elif points_var == 3:
        $ points_var_girls = "sidney"
        $ points_girls_name = "Sidney"
    elif points_var == 4:
        $ points_var_girls = "aunt"
        if persistent.patreonsafe:
            $ points_girls_name = "Aunt Camille"
        else:
            $ points_girls_name = "Auntie"
    elif points_var == 5:
        $ points_var_girls = "cousin"
        $ points_girls_name = "Mandy"

    imagebutton xalign 0.025 yalign 0.2:
            idle ("points_screen_img")
            action NullAction()

    imagebutton xalign 0.025 yalign 0.2:
        if points_var == 1:
            idle ("Mom_points_img")
        elif points_var == 2:
            idle ("Lauren_points_img")
        elif points_var == 3:
            idle ("Sidney_points_img")
        elif points_var == 4:
            idle ("Aunt_points_img")
        elif points_var == 5:
            idle ("Cuz_points_img")
        action NullAction()

    text _("{}'s stats:".format(points_girls_name)):
        xalign 0.17
        yalign 0.2
        style "sts_name_style"

    text _("[{}affection]".format(points_var_girls)) xalign 0.17 yalign 0.25 style "nav_style"
    text _("[{}respect]".format(points_var_girls)) xalign 0.25 yalign 0.25 style "nav_style"
    text _("[{}libido]".format(points_var_girls)) xalign 0.25 yalign 0.32 style "nav_style"
    text _("[{}submission]".format(points_var_girls)) xalign 0.17 yalign 0.32 style "nav_style"
    text _("[{}anger]".format(points_var_girls)) xalign 0.315 yalign 0.28 style "nav_style"

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

    if reverse_cuz:
        imagebutton xalign 0.925 yalign 0.02:
            idle ("Cuz_points_img_2_reverse")
            action NullAction()

        text _("[cousinlibido]") xalign 0.77 yalign 0.17 style "nav_style"
        text _("[cousinsubmission]") xalign 0.84 yalign 0.17 style "nav_style"
    else:
        imagebutton xalign 0.025 yalign 0.02:
            idle ("Cuz_points_img_2")
            action NullAction()

        text _("[cousinlibido]") xalign 0.24 yalign 0.17 style "nav_style"
        text _("[cousinsubmission]") xalign 0.165 yalign 0.17 style "nav_style"

screen Points_screen_Mom_cosplay():

    imagebutton xalign 0.025 yalign 0.02:
        idle ("Mom_points_img_2")
        action NullAction()

    text _("[momlibido]") xalign 0.24 yalign 0.17 style "nav_style"
    text _("[momsubmission]") xalign 0.165 yalign 0.17 style "nav_style"
