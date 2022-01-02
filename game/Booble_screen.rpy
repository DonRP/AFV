
####################################################################################################################################################
### Powerd by D.S.-sama ############################################################################################################################
####################################################################################################################################################
####################################################################################################################################################

define hardnlong_first_time = False
define hardnlong_search = True
define cosplay_search = False
define hardnlong_searched = False
define cosplay_searched = False

####################################################################################################################################################
### Booble screen

screen booble_screen():

    add "images/interface_images/booble_images/Booble.png"

    imagebutton  xalign 0.779 yalign 0.4365 at inv_eff:
        idle "images/interface_images/booble_images/Search_button.png"
        if hardnlong_search:
            action [ SetVariable("hardnlong_searched", True), Jump("online_shopping")]
        #elif cosplay_search:
        #    action Jump("cosplay_call")
        else:
            action NullAction()

    if hardnlong_searched:
        imagebutton  xalign 0.2 yalign 0.7 at inv_eff:
            idle "images/interface_images/booble_images/int_hardnLong_button.png"
            action [ Hide("booble_screen"), Jump("online_shopping") ]
        text _("{color=#ffffff}{b}hardnLong.dong online shopping{/b}{/color}") outlines [(2.2, "#000000", 0, 0)] size 17 xalign 0.1 yalign 0.88

    if cosplay_searched:
        imagebutton  xalign 0.5 yalign 0.7 at inv_eff:
            idle "images/interface_images/booble_images/int_cosplay_button.png"
            action [ Hide("booble_screen"), Jump("cosplay_call") ]
        text _("{color=#ffffff}{b}cosplayheaven.cos cosplay site{/b}{/color}") outlines [(2.2, "#000000", 0, 0)] size 17 xalign 0.495 yalign 0.88

    imagebutton auto "images/interface_images/close_button_%s.png" xpos 1230 ypos 36 focus_mask True action [ Hide("booble_screen"), Show("desktopcompmap") ]

####################################################################################################################################################
### Booble labels

label booble_search:

    if not hardnlong_first_time:
        $ hardnlong_first_time = True
        show bg CosplayWarehouse19
        RT "{i}I should do a search on booble.com to find a way to buy the stuff I need so that the FBI won't ask me from where I got the money.{/i}"
        call screen  booble_screen

    #elif hardnlong_searched and not cosplay_searched and progress >=7:
    #    $ cosplay_search = True
    #    show bg CosplayWarehouse19
    #    RT "{i}The photoshoot with the girls gave me an idea, I should do a search on booble.com and see if I can make some money out of this.{/i}"
    #    call screen  booble_screen

    #elif hardnlong_searched and cosplay_searched:
    #    show bg CosplayWarehouse19
    #    RT "{i}What should I do today on the internet.{/i}"
    #    call screen  booble_screen

    else:
        show bg CosplayWarehouse19
        RT "{i}What should I do today on the internet?{/i}"
        call screen  booble_screen
