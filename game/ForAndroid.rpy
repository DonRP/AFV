#init python:
#    if renpy.android or renpy.ios:
#        config.overlay_screens.append("androidButton")
        
init:
    
    image settingsIdle = im.Scale("images/interface_images/for_android/settingIcon.png", 52, 52)
    image settingsHover = Transform(
        im.MatrixColor("images/interface_images/for_android/settingIcon.png", im.matrix.invert()),
        size=(52, 52))  #Enter specific numbers <--

    image backIdle = im.Scale("images/interface_images/for_android/BackIcon.png", 52, 52)
    image backHover = Transform(
        im.MatrixColor("images/interface_images/for_android/BackIcon.png", im.matrix.invert()),
        size=(52, 52))  #Enter specific numbers <--

#screen androidButton():
#    variant "touch"

#    zorder 150
    
#    imagebutton:
#        pos (0.017, 0.03)
#        idle "settingsIdle"
#        hover "settingsHover"
#        action ToggleScreen("androidMenu", transition=Dissolve(1.0))

screen androidMenu():
    
    zorder 100
    
    frame at truecenter:
#        xalign 0.2 ypos 0.2
        vbox:
            
            text _("Quick Menu") at center
            text "---------------------------------------------------" at center
            
            if persistent.patch_on:
                hbox at center:
                    textbutton _(If( persistent.patreonsafe,
                        "iPatch: {color=#E60000}OFF{/color}",
                        "iPatch: {color=#1DDB16}ON{/color}")) text_size 20 action If(persistent.patreonsafe,
                        [ SetField(persistent, "patreonsafe", False),
                            SetVariable("Mom", "Mom"),
                            SetVariable("mom", "mom"),
                            SetVariable("Dad", "Dad"),
                            SetVariable("dad", "dad"),
                            SetVariable("uncle", "uncle " + uncle_name),
                            SetVariable("Uncle", "Uncle " + uncle_name),
                            SetVariable("Auntie", "Aunt " + auntie_name_short),
                            SetVariable("auntie", "aunt " + auntie_name_short),
                            SetVariable("Auntie_2", "Aunt "),
                            SetVariable("auntie_2", "aunt ") ],
                        [ SetField(persistent, "patreonsafe", True),
                            SetVariable("Mom", mom_name),
                            SetVariable("mom", mom_name),
                            SetVariable("Dad", dad_name),
                            SetVariable("dad", dad_name),
                            SetVariable("uncle", uncle_name),
                            SetVariable("Uncle", uncle_name),
                            SetVariable("Auntie", auntie_name),
                            SetVariable("auntie", auntie_name),
                            SetVariable("Auntie_2", ""),
                            SetVariable("auntie_2", "") ])
                    
            text "---------------------------------------------------" at center
            
            hbox at center:
                textbutton _("Menu") text_size 20 action [ ShowMenu(), Hide("androidMenu", transition=Dissolve(1.0)) ]
            
            hbox:
                text "        " size 20
                
                textbutton _("History") text_size 20 action [ ShowMenu('history'), Hide("androidMenu", transition=Dissolve(1.0)) ]
                
                text "     " size 20
                
                textbutton _("Prefs") text_size 20 action [ ShowMenu('preferences'), Hide("androidMenu", transition=Dissolve(1.0)) ]
                
                text "     " size 20
                
                textbutton _("Skip") text_size 20 action Skip() alternate Skip(fast=True, confirm=True)
            
                text "        " size 20
                
                textbutton _("Auto") text_size 20 action Preference("auto-forward", "toggle")
            
                text "        " size 20                
                
            hbox:
                
                text "        " size 20
                
                textbutton _("Save") text_size 20 action [ ShowMenu('save'), Hide("androidMenu", transition=Dissolve(1.0)) ]
                
                text "        " size 20
                
                textbutton _("Load") text_size 20 action [ ShowMenu('load'), Hide("androidMenu", transition=Dissolve(1.0)) ]
                
                text "     " size 20
            
                textbutton _("Q.Save") text_size 20 action QuickSave()
                
                text "     " size 20
            
                textbutton _("Q.Load") text_size 20 action QuickLoad()
                
                text "        " size 20
            
            hbox at center:
                textbutton _("Console") text_size 20 action [ Function(_console.enter) ]
            
            textbutton _("Close quick menu!") text_size 20 action Hide("androidMenu", transition=Dissolve(1.0)) at center
            