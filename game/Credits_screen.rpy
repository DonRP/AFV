
####################################################################################################################################################
### Powerd by D.S.-sama ############################################################################################################################
####################################################################################################################################################
####################################################################################################################################################

####################################################################################################################################################
### Inventory variable
####################################################################################################################################################

init:

    transform scroll_trans:
        yoffset 500
        linear 100.0 yoffset -5865 #or whatever height you need to have them all scroll off fully
        repeat

    image icon_patreon = "images/interface_images/ico_patreon.png"

#    image creditscroll:
#        Text([
#    "{b}{i}Family with Benefits:{/i}{/b} \n"
#    "\nFrayed80 \n"
#    "{b}{i}My Family:{/i}{/b} \n"
#    "\nMoistness"
#    "\nMr.Grey"
#    "\nTheSearcher81 \n"
#    "\n{b}{i}My BFFS:{/i}{/b} \n"
#    "\nebaker456"
#    "\ngamersglory"
#    "\nJoFry"
#    "\nPolaxymer"
#    "\nroey2690"
#    "\nSheggy Sullivan"
#    "\nvrod302 \n"
#    "\n{b}{i}My Best Friends:{/i}{/b} \n"
#    "\nBrollo"
#    "\nDerek MacRae"
#    "\neddie baker"
#    "\nGrub"
#    "\nklaas444"
#    "\nklx"
#    "\nMark Schulz"
#    "\nNic Arcari"
#    "\nShaun Wilson \n"], outlines=[(1.1, "#4118fa", 0, 0)], text_align=0.5) #18b3fb
#        anchor (0.5, -0.6)
#        pos (0.25, 0.7)
#        linear 15.0 ypos 1.0 yanchor 1.0

####################################################################################################################################################
### Credits screen
####################################################################################################################################################

screen credits():
    tag menu

    use game_menu(_("                               Credits"), scroll=""):
        #add "#000000"
        style_prefix "credits"

        ##add "#000"
        text _(" We would like to thank all the game developers that have accepted to let us use some of their creations in our game, also we'd like to thank our subscribestar/patreon supporters that make this game posible.")

        frame xalign 1.0 yalign 1.5:
            background None

            has vbox # IMPORTANT TO ADD SO THAT IT UNITES ALL IN TO ONE

            text _("Game developers") outlines [(1.1, "#4118fa", 0, 0)] at center

            text _("") size 20

            side ("c r"):
                area (1,0,315,450)
                viewport id "credits_devs": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                    draggable True mousewheel True
                    vbox:
                        imagebutton xalign .5:
                            idle "images/interface_images/credits_images/Button_Akabur.png"
                            hover_foreground "images/interface_images/credits_images/Hover_dev_buttons.png"
                            action OpenURL("https://www.patreon.com/akabur")

#                        imagebutton:
#                            idle "images/interface_images/credits_images/game_Milfy_city.png"
#                            hover_foreground "images/interface_images/credits_images/game_img_hover.png"
#                            action OpenURL("https://f95zone.com/threads/milfy-city-v0-5c-icstor.8012/")

                        text _("") size 20

                        imagebutton xalign .5:
                            idle "images/interface_images/credits_images/Button_ICSTOR.png"
                            hover_foreground "images/interface_images/credits_images/Hover_dev_buttons.png"
                            action OpenURL("https://www.patreon.com/icstor")

                        imagebutton:
                            idle "images/interface_images/credits_images/game_Milfy_city.png"
                            hover_foreground "images/interface_images/credits_images/game_img_hover.png"
                            action OpenURL("https://f95zone.com/threads/milfy-city-v0-5c-icstor.8012/")

                        text _("") size 20

                        imagebutton xalign .5:
                            idle "images/interface_images/credits_images/Button_Dark_Silver.png"
                            hover_foreground "images/interface_images/credits_images/Hover_dev_buttons.png"
                            action OpenURL("https://www.patreon.com/sandlustgames")

                        imagebutton:
                            idle "images/interface_images/credits_images/game_Big_Brother.png"
                            hover_foreground "images/interface_images/credits_images/game_img_hover.png"
                            action OpenURL("https://f95zone.com/threads/big-brother-v0-13-0-007-dark-silver.1519/")

                        text _("") size 20

                        imagebutton xalign .5:
                            idle "images/interface_images/credits_images/Button_Faerin.png"
                            hover_foreground "images/interface_images/credits_images/Hover_dev_buttons.png"
                            action OpenURL("https://www.patreon.com/faerin")

                        imagebutton:
                            idle "images/interface_images/credits_images/game_Man_of_the_house.png"
                            hover_foreground "images/interface_images/credits_images/game_img_hover.png"
                            action OpenURL("https://f95zone.to/threads/man-of-the-house-v0-9-7-extra-faerin.3691/")

                        #text _("") size 20

                        #imagebutton xalign .5:
                        #    idle "images/interface_images/credits_images/Button_Mr.C.png"
                        #    hover_foreground "images/interface_images/credits_images/Hover_dev_buttons.png"
                        #    action OpenURL("https://www.patreon.com/mrc")

                        #imagebutton:
                        #    idle "images/interface_images/credits_images/game_corruption.png"
                        #    hover_foreground "images/interface_images/credits_images/game_img_hover.png"
                        #    action OpenURL("https://f95zone.to/threads/corruption-v1-45-mr-c.1878/")

                        text _("") size 20

                vbar value YScrollValue("credits_devs") #TAKES YOUR VIEWPORT ID AS THE ARG

        null height 20 #just a height set.

        frame xalign .2 yalign 1.5:
            background None

            has vbox # IMPORTANT TO ADD SO THAT IT UNITES ALL IN TO ONE

            text _("Subscribers/Patrons") outlines [(1.1, "#4118fa", 0, 0)]

            text _("") size 20

            side ("c"):
                area (1,0,315,450)
                viewport id "credits_patrons": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                    draggable True mousewheel True
                    vbox:

                        text _("\n{b}{i}Game Designer, Master Coder, Patch Creator, Gallery Guru:{/i}{/b} \n") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans

                        text _("{a=https://www.patreon.com/DS_sama}{image=icon_patreon} D.S.-Sama{/a}") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans

                        text _("\n{b}{i}Spelling and Grammar Editor:{/i}{/b} \n") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans

                        text _("lapdragon") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans

                        text _("\n{b}{i}Game Writer, Coder, Images, Animations:{/i}{/b} \n") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans

                        text _("Will Tylor") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans

                        text _("\n{b}{i}Ghost Writer:{/i}{/b} \n") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans

                        text _("Strenif") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans

                        text _("\n{b}{i}My Family with Benefits:{/i}{/b} \n") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans

                        text _("Frayed80") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Jtf1357") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Urqy") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans

                        text _("\n{b}{i}My Family:{/i}{/b} \n") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans

                        text _("Bremen") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("deadpool25") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("DerSucher81") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Drew G") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Elthaun") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Ghost101") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Grub") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Imyourbuddy") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("ironpic") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Nathan Allison") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Thomas Roe") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("TheSearcher81") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans

                        text _("\n{b}{i}My BFFS:{/i}{/b} \n") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans

                        text _("Adam") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("afburnham") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Alvise") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("ArcAngl") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Armesone23") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Benja Talos") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("BlackCastleStorm84") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("bob") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Brian Svensen") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("ch3") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Chadsgn") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Chenzillla") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("chimcham123") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Christian von Briel") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("claudio Rodriguez") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Colin") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Coscara88") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("crayon") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("cvxc sdf") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("DaemonSD") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Dartred") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Dustin Patterson") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Eden") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("EverynameDies") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Fen") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("gillin") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("GOkuma") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("griffor") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Hanshans1313") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("hdoggcool") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Hoboscotty") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("ItsMrGru") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Jack") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Javier Soto") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("jayjay") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("John Levell") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("John Smith") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("john tozer") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Joseph Matuzka") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Joshua Harris") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("K.S") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("kos2255") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("kp helman") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("kyle lambert") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Logiteach6757") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("M0rmegil") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Macrotrauma") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Marc") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Marco") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Martin") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Matt") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Matthew Pelc") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Michael Lillie") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Mitchell Sandlin") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Mr.Grey") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("nicoud gregory") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("nitro2889") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("NoPro") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Old Man") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Osamabeenfappin") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("patrick") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Perdurabo88") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Peren D'Wolff") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Pikiriti") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Polaxymer") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Prentis Talbot") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Qozz") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("RCF") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Ross Kirchner") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Saitama") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("SandPiper") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("shen") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Shivawn") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Silvio lori") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Simon Bissig") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Stephan") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Strenif") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Sunwind") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Takola") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("tccds") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Thaco4") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("TheHorror") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("thr33ve") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Tosàt stonfo") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("TRex") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Turbo") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Tyr13") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("TyRaNT-KiNG") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("randylj17") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("uncejay") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("William Ensley") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans
                        text _("Wotto") outlines [(1.1, "#4118fa", 0, 0)] text_align 0.5 at scroll_trans

                    #add "creditscroll"

        null height 20 #just a height set.

        #timer 20.0 action [ Hide("credits"), ShowMenu("credits") ]

####################################################################################################################################################
### Credits styles
####################################################################################################################################################

style credits_hbox:
    spacing 30
    ysize 25

style credits_label:
    xalign 0.5

style credits_text:
    xalign 0.5
