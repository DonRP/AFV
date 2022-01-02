
####################################################################################################################################################
### Powerd by D.S.-sama ############################################################################################################################
####################################################################################################################################################
####################################################################################################################################################

### The spacing between file slots.
define gui.slot_spacing_Shopping = 15

### File button layout.
define gui.file_slot_cols_Shopping = 4
define gui.file_slot_rows_Shopping = 2

define buy_var = ""

define spycam_locations = [ "spycaminlaurenroom", "spycaminbath", "spycaminlaurenroom" ]
define video_accessories = [ "6", "7", "8" ]
define video_start = False

define adv_org_time = 11
define adv_time = adv_org_time
define adv_choice = 1

####################################################################################################################################################
### Shopping screen

screen Shopping_gallery():#
    add "bg OnlineShopping"
    fixed:
        ### The grid of file slots.
        vpgrid cols gui.file_slot_cols_Shopping:
            mousewheel True
            arrowkeys True
            draggable True
            scrollbars "vertical"
            side_xalign 0.0
            ypos 450
            ymaximum 500
            style_prefix "slot"
            xalign 0.08
            yalign 0.48
            spacing gui.slot_spacing_Shopping
            for i in range(1 * 1):
                $ slot = i + 1
                imagebutton:
                        idle "images/interface_images/shopping_gallery_images/S_gal_Chocolate_idle.png"
                        hover_foreground "images/interface_images/shopping_gallery_images/S_gal_hover.png"
                        focus_mask True
                        action [ SetVariable("buy_var", "chocolate"), ui.callsinnewcontext("buying_label") ]
                imagebutton:
                        idle "images/interface_images/shopping_gallery_images/S_gal_Card_idle.png"
                        hover_foreground "images/interface_images/shopping_gallery_images/S_gal_hover.png"
                        focus_mask True
                        action [ SetVariable("buy_var", "giftcard"), ui.callsinnewcontext("buying_label") ]
                imagebutton:
                        idle "images/interface_images/shopping_gallery_images/S_gal_Flowers_idle.png"
                        hover_foreground "images/interface_images/shopping_gallery_images/S_gal_hover.png"
                        focus_mask True
                        action [ SetVariable("buy_var", "flowers"), ui.callsinnewcontext("buying_label") ]
                if failedsneakattempt == True:
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_Melatonin_idle.png"
                            hover_foreground "images/interface_images/shopping_gallery_images/S_gal_hover.png"
                            focus_mask True
                            action [ SetVariable("buy_var", "melatonin"), ui.callsinnewcontext("buying_label") ]
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_Spy_camera_idle.png"
                            hover_foreground "images/interface_images/shopping_gallery_images/S_gal_hover.png"
                            focus_mask True
                            action [ SetVariable("buy_var", "spycam"), ui.callsinnewcontext("buying_label") ]
                if loyaltycounter >= 2:
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_Jacky_bikini_01_idle.png"
                            hover_foreground "images/interface_images/shopping_gallery_images/S_gal_hover.png"
                            focus_mask True
                            action [ SetVariable("buy_var", "jacky_bikini_1"), ui.callsinnewcontext("buying_label") ]
                if gal_cosplay_items_01:
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_Green_screen_idle.png"
                            hover_foreground "images/interface_images/shopping_gallery_images/S_gal_hover.png"
                            focus_mask True
                            action [ SetVariable("buy_var", "green_screen"), ui.callsinnewcontext("buying_label") ]
                if gal_cosplay_items_01:
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_Pro_lights_idle.png"
                            hover_foreground "images/interface_images/shopping_gallery_images/S_gal_hover.png"
                            focus_mask True
                            action [ SetVariable("buy_var", "pro_lights"), ui.callsinnewcontext("buying_label") ]
                if gal_cosplay_items_01:
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_Camera_idle.png"
                            hover_foreground "images/interface_images/shopping_gallery_images/S_gal_hover.png"
                            focus_mask True
                            action [ SetVariable("buy_var", "camera"), ui.callsinnewcontext("buying_label") ]
                if inventory.has_item(camera):
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_Camera_accessories_1.png"
                            hover_foreground "images/interface_images/shopping_gallery_images/S_gal_hover.png"
                            focus_mask True
                            action [ SetVariable("buy_var", "accessories_1"), ui.callsinnewcontext("buying_label") ]
                if inventory.has_item(camera):
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_Camera_accessories_2.png"
                            hover_foreground "images/interface_images/shopping_gallery_images/S_gal_hover.png"
                            focus_mask True
                            action [ SetVariable("buy_var", "accessories_2"), ui.callsinnewcontext("buying_label") ]
                if inventory.has_item(camera):
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_Camera_accessories_3.png"
                            hover_foreground "images/interface_images/shopping_gallery_images/S_gal_hover.png"
                            focus_mask True
                            action [ SetVariable("buy_var", "accessories_3"), ui.callsinnewcontext("buying_label") ]
                if inventory.has_item(camera):
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_Camera_accessories_4.png"
                            hover_foreground "images/interface_images/shopping_gallery_images/S_gal_hover.png"
                            focus_mask True
                            action [ SetVariable("buy_var", "accessories_4"), ui.callsinnewcontext("buying_label") ]
                if inventory.has_item(camera):
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_Camera_accessories_5.png"
                            hover_foreground "images/interface_images/shopping_gallery_images/S_gal_hover.png"
                            focus_mask True
                            action [ SetVariable("buy_var", "accessories_5"), ui.callsinnewcontext("buying_label") ]
                if inventory.has_item(camera) and video_start:
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_Camera_accessories_6.png"
                            hover_foreground "images/interface_images/shopping_gallery_images/S_gal_hover.png"
                            focus_mask True
                            action [ SetVariable("buy_var", "accessories_6"), ui.callsinnewcontext("buying_label") ]
                if inventory.has_item(camera) and video_start:
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_Camera_accessories_7.png"
                            hover_foreground "images/interface_images/shopping_gallery_images/S_gal_hover.png"
                            focus_mask True
                            action [ SetVariable("buy_var", "accessories_7"), ui.callsinnewcontext("buying_label") ]
                if inventory.has_item(camera) and video_start:
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_Camera_accessories_8.png"
                            hover_foreground "images/interface_images/shopping_gallery_images/S_gal_hover.png"
                            focus_mask True
                            action [ SetVariable("buy_var", "accessories_8"), ui.callsinnewcontext("buying_label") ]
                if blackmailed_mom_matt or blackmailed_mom_megan:
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_Ballgag_idle.png"
                            hover_foreground "images/interface_images/shopping_gallery_images/S_gal_hover.png"
                            focus_mask True
                            action [ SetVariable("buy_var", "ball_gag"), ui.callsinnewcontext("buying_label") ]
                if ready_for_hp:
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_Book01_idle.png"
                            hover_foreground "images/interface_images/shopping_gallery_images/S_gal_hover.png"
                            focus_mask True
                            action [ SetVariable("buy_var", "ph_book1"), ui.callsinnewcontext("buying_label") ]
                if read_book1:
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_Book02_idle.png"
                            hover_foreground "images/interface_images/shopping_gallery_images/S_gal_hover.png"
                            focus_mask True
                            action [ SetVariable("buy_var", "ph_book2"), ui.callsinnewcontext("buying_label") ]
                if read_book2:
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_Book03_idle.png"
                            hover_foreground "images/interface_images/shopping_gallery_images/S_gal_hover.png"
                            focus_mask True
                            action [ SetVariable("buy_var", "ph_book3"), ui.callsinnewcontext("buying_label") ]
                imagebutton:
                        idle "images/interface_images/shopping_gallery_images/S_gal_no_bg.png"
                        focus_mask True
                        action NullAction()
                if failedsneakattempt and progress < 7:
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_no_bg.png"
                            focus_mask True
                            action NullAction()
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_no_bg.png"
                            focus_mask True
                            action NullAction()
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_no_bg.png"
                            focus_mask True
                            action NullAction()
                if not failedsneakattempt:
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_no_bg.png"
                            focus_mask True
                            action NullAction()
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_no_bg.png"
                            focus_mask True
                            action NullAction()
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_no_bg.png"
                            focus_mask True
                            action NullAction()
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_no_bg.png"
                            focus_mask True
                            action NullAction()
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_no_bg.png"
                            focus_mask True
                            action NullAction()
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_no_bg.png"
                            focus_mask True
                            action NullAction()
                    imagebutton:
                            idle "images/interface_images/shopping_gallery_images/S_gal_no_bg.png"
                            focus_mask True
                            action NullAction()
    imagebutton auto "images/interface_images/close_button_%s.png" xpos 1230 ypos 36 focus_mask True action [ Hide("Shopping_gallery"), Show("booble_screen") ]
    timer 1 repeat True:
        action If(adv_time > 0,
            [SetVariable('adv_time', adv_time - 1)],
            [If(adv_choice > 1,
                SetVariable('adv_choice', 1),
                SetVariable('adv_choice', 2)),
            SetVariable('adv_time', adv_org_time)]
            )
    if persistent.patreonsafe:
        if adv_choice > 1:
            imagebutton xalign 0.98 yalign 0.92:
                idle "advertising_banner_patreonsafe"
                focus_mask True
                action OpenURL("https://www.patreon.com/user?u=865554")
        else:
            imagebutton xalign 0.98 yalign 0.92:
                idle "advertising_banner_SubStar_patreonsafe"
                focus_mask True
                action OpenURL("https://subscribestar.adult/willtylor")
    else:
        if adv_choice > 1:
            imagebutton xalign 0.98 yalign 0.92:
                idle "advertising_banner"
                focus_mask True
                action OpenURL("https://www.patreon.com/user?u=865554")
        else:
            imagebutton xalign 0.98 yalign 0.92:
                idle "advertising_banner_SubStar"
                focus_mask True
                action OpenURL("https://subscribestar.adult/willtylor")
    text "{color=#000000}{size=+5}{b}My wallet: $[money]{/b}{/size}{/color}" xpos 0.75 ypos 0.075

####################################################################################################################################################
### Online Shopping label

label online_shopping:
    if firsttimeshopping == False:
        scene bg OnlineShopping_1
        with fade
        RT "{i}HardnLong.dong it's the best online shop that has the best prices, they deliver everywhere and they also accept online currency that'll help me be anonymous.{/i}"
        scene bg OnlineShopping
        $ hardnLong_search = False
#        $ hardnLong_searched = True
        $ firsttimeshopping = True
        if persistent.patreonsafe:
            RT "{i}Since I don't want the FBI to know I'm spending money, and I don't want my family to know what I'm buying, I'll have my purchases delivered to Dad's warehouse.{/i}"
        else:
            RT "{i}Since I don't want the FBI to know I'm spending money, and I don't want my family to know what I'm buying, I'll have my purchases delivered to Dad's warehouse.{/i}"
        RT "{i}Plus, since I'm going to become a HardnLong prime member, my items will already have been delivered before I can even drive over there.{/i}"
        call screen Shopping_gallery
    if failedsneakattempt == True:
        scene bg OnlineShopping_3
        with fade
        call screen Shopping_gallery
    else:
        scene bg OnlineShopping_2
        with fade
        RT "{i}HardnLong is taking over the world!{/i}"
        call screen Shopping_gallery
    return

####################################################################################################################################################
### Buying label

label buying_label:
    $ randomnum = renpy.random.randint(1,2) # (randomize between 1 and 2)
    #$ renpy.retain_after_load()
    $ invchocolate = inventory.inv_amount(chocolate) + futchocolate
    $ invgiftcard = inventory.inv_amount(giftcard) + futgiftcard
    $ invflowers = inventory.inv_amount(flowers) + futflowers
    $ invmelatonin = inventory.inv_amount(melatonin) + futmelatonin
    if spycaminlaurenroom and spycaminbath and spycaminmomroom:
        $ invspycam = 3
    elif (spycaminlaurenroom and spycaminbath) or (spycaminmomroom and spycaminbath) or (spycaminmomroom and spycaminlaurenroom):
        $ invspycam = inventory.inv_amount(spycam) + futspycam + 2
    elif spycaminlaurenroom or spycaminbath or spycaminmomroom:
        $ invspycam = inventory.inv_amount(spycam) + futspycam + 1
    else:
        $ invspycam = inventory.inv_amount(spycam) + futspycam
    $ invgreen_screen = inventory.inv_amount(green_screen) + futgreen_screen
    $ invpro_lights = inventory.inv_amount(pro_lights) + futpro_lights
    $ invcamera = inventory.inv_amount(camera) + futcamera
    $ invj_bikini_1 = inventory.inv_amount(jacky_bikini_01) + futj_bikini_1
    $ invball_gag = inventory.inv_amount(ball_gag) + fut_ball_gag
    $ invph_book1 = inventory.inv_amount(ph_book1) + fut_ph_book1
    $ invph_book2 = inventory.inv_amount(ph_book2) + fut_ph_book2
    $ invph_book3 = inventory.inv_amount(ph_book3) + fut_ph_book3
    $ invaccessories_1 = inventory.inv_amount(camera_accessories_1) + futaccessories_1
    $ invaccessories_2 = inventory.inv_amount(camera_accessories_2) + futaccessories_2
    $ invaccessories_3 = inventory.inv_amount(camera_accessories_3) + futaccessories_3
    $ invaccessories_4 = inventory.inv_amount(camera_accessories_4) + futaccessories_4
    $ invaccessories_5 = inventory.inv_amount(camera_accessories_5) + futaccessories_5
    $ invaccessories_6 = inventory.inv_amount(camera_accessories_6) + futaccessories_6
    $ invaccessories_7 = inventory.inv_amount(camera_accessories_7) + futaccessories_7
    $ invaccessories_8 = inventory.inv_amount(camera_accessories_8) + futaccessories_8
    if failedsneakattempt == True:
        scene bg HardnlongVersion2
    else:
        scene bg Hardalong
    if buy_var == "chocolate":
        RT "{i}Is there a girl in the world who doesn't like chocolate? This gift would make anyone less angry.{/i}"
        if money <= 9:
            "You don't have enough money."
        elif invchocolate >= 3:
            if randomnum == 1:
                "You already have enough."
            elif randomnum == 2:
                "You have enough already."
        else:
            menu:
                "Buy chocolate":
                    $ futchocolate += 1
                    $ money -= 10
                    "You bought one chocolate bar."
                    RT "{i}I'll need to pick it up at Dad's warehouse.{/i}"
                "Don't buy":
                    RT "{i}Not right now.{/i}"
    elif buy_var == "giftcard":
        RT "{i}This seems like a good gift when the FBI is trying to track the money we spend.{/i}"
        if money <= 24:
            "You don't have enough money."
        elif invgiftcard >= 3:
            if randomnum == 1:
                "You already have enough."
            elif randomnum == 2:
                "You have enough already."
        else:
            menu:
                "Buy giftcard":
                    $ futgiftcard += 1
                    $ money -= 25
                    "You bought one gift card."
                    RT "{i}I'll need to pick it up at Dad's warehouse.{/i}"
                "Don't buy":
                    RT "{i}Not right now.{/i}"
    elif buy_var == "flowers":
        if money <= 49:
            "You don't have enough money."
        elif invflowers >= 3:
            if randomnum == 1:
                "You already have enough."
            elif randomnum == 2:
                "You have enough already."
        else:
            menu:
                "Buy Flowers":
                    $ futflowers += 1
                    $ money -= 50
                    "You bought one bouquet of flowers."
                    RT "{i}I'll need to pick it up at Dad's warehouse.{/i}"
                "Don't buy":
                    RT "{i}Not right now.{/i}"
    elif buy_var == "melatonin":
        RT "{i}Ok, this is the strongest over the counter sleep aid I can buy.{/i}"
        RT "{i}Oh look, it's all natural...non addictive...So it won't be bad for my family.{/i}"
        if money <= 99:
            "You don't have enough money."
        elif boughtmelatonin == True:
            "You don't need any more of this."
        else:
            menu:
                "Buy melatonin.":
                    $ futmelatonin += 1
                    $ money -= 100
                    $ boughtmelatonin = True
                    "You bought a bottle of Melatonin."
                    RT "{i}Awesome. Now I've just got to figure out how to get Mom and my sisters to take some each night.{/i}"
                    RT "{i}But first I need to go pick it up at the warehouse.{/i}"
                "Don't buy":
                    RT "{i}Not right now.{/i}"
    elif buy_var == "spycam":
        RT "{i}This could come in handy for a pervert like me.{/i}"
        if money <= 999:
                "You don't have enough money."
        elif invspycam >= 3:
            if any( [ getattr(store, "{}".format(k), False) for k in spycam_locations] ) and inventory.inv_amount(spycam) == 0 and futspycam == 0:
                $ invspycam -= 1
                $ futspycam += 1
                $ money -= 1000
                RT "{i}Good thing this is being delivered to Dad's warehouse. If anyone saw what I ordered, it could raise a few questions.{/i}"
            else:
                if randomnum == 1:
                    RT "{i}Let's not go overboard.{/i}"
                elif randomnum == 2:
                    RT "{i}I need to set up some of these before I buy anymore.{/i}"
        else:
            menu:
                "Buy spycam.":
                    $ futspycam += 1
                    $ money -= 1000
                    RT "{i}Good thing this is being delivered to Dad's warehouse. If anyone saw what I ordered, it could raise a few questions.{/i}"
                "Don't buy":
                    RT "{i}Not right now.{/i}"
    elif buy_var == "green_screen":
        RT "{i}I could make whatever background I want for my photo shoots!{/i}"
        if money <= 499:
            "You don't have enough money."
        elif invgreen_screen >= 1:
            if randomnum == 1:
                "You already have enough."
            elif randomnum == 2:
                "You have enough already."
        else:
            menu:
                "Buy green screen.":
                    $ futgreen_screen += 1
                    $ money -= 500
                    "You bought a green screen."
                    RT "{i}Great, now the pictures will be higher quality and will bring us more likes! I'll just need to pick it up at Dad's warehouse.{/i}"
                "Don't buy":
                    RT "{i}Not right now.{/i}"
    elif buy_var == "pro_lights":
        RT "{i}The flash on my camera just doesn't do enough.{/i}"
        if money <= 999:
            "You don't have enough money."
        elif invpro_lights >= 1:
            if randomnum == 1:
                "You already have enough."
            elif randomnum == 2:
                "You have enough already."
        else:
            menu:
                "Buy pro lights.":
                    $ futpro_lights += 1
                    $ money -= 1000
                    "You bought professional lights for your studio."
                    RT "{i}Great, now the pictures will be higher quality and will bring us more likes! I'll just need to pick it up at Dad's warehouse.{/i}"
                "Don't buy":
                    RT "{i}Not right now.{/i}"
    elif buy_var == "camera":
        RT "{i}This camera makes me drool!{/i}"
        if money <= 1499:
            "You don't have enough money."
        elif invcamera >= 1:
            if randomnum == 1:
                "You already have enough."
            elif randomnum == 2:
                "You have enough already."
        else:
            menu:
                "Buy DSLR camera.":
                    $ futcamera += 1
                    $ money -= 1500
                    "You bought a new DSLR camera."
                    RT "{i}Great, now the pictures will be higher quality and will bring us more likes! I'll just need to pick it up at Dad's warehouse.{/i}"
                "Don't buy":
                    RT "{i}Not right now.{/i}"
    elif buy_var == "accessories_1":
        if money <= 199:
            "You don't have enough money."
        elif invaccessories_1 >= 1:
            if randomnum == 1:
                "You already have enough."
            elif randomnum == 2:
                "You have enough already."
        else:
            menu:
                "Buy camera accessory.":
                    $ futaccessories_1 += 1
                    $ money -= 200
                    "You bought a new camera accessory."
                    RT "{i}Great, now the pictures will be higher quality and will bring us more likes! I'll just need to pick it up at Dad's warehouse.{/i}"
                "Don't buy":
                    RT "{i}Not right now.{/i}"
    elif buy_var == "accessories_2":
        if money <= 99:
            "You don't have enough money."
        elif invaccessories_2 >= 1:
            if randomnum == 1:
                "You already have enough."
            elif randomnum == 2:
                "You have enough already."
        else:
            menu:
                "Buy camera accessory.":
                    $ futaccessories_2 += 1
                    $ money -= 100
                    "You bought a new camera accessory."
                    RT "{i}Great, now the pictures will be higher quality and will bring us more likes! I'll just need to pick it up at Dad's warehouse.{/i}"
                "Don't buy":
                    RT "{i}Not right now.{/i}"
    elif buy_var == "accessories_3":
        if money <= 99:
            "You don't have enough money."
        elif invaccessories_3 >= 1:
            if randomnum == 1:
                "You already have enough."
            elif randomnum == 2:
                "You have enough already."
        else:
            menu:
                "Buy camera accessory.":
                    $ futaccessories_3 += 1
                    $ money -= 100
                    "You bought a new camera accessory."
                    RT "{i}Great, now the pictures will be higher quality and will bring us more likes! I'll just need to pick it up at Dad's warehouse.{/i}"
                "Don't buy":
                    RT "{i}Not right now.{/i}"
    elif buy_var == "accessories_4":
        if money <= 499:
            "You don't have enough money."
        elif invaccessories_4 >= 1:
            if randomnum == 1:
                "You already have enough."
            elif randomnum == 2:
                "You have enough already."
        else:
            menu:
                "Buy camera accessory.":
                    $ futaccessories_4 += 1
                    $ money -= 500
                    "You bought a new camera accessory."
                    RT "{i}Great, now the pictures will be higher quality and will bring us more likes! I'll just need to pick it up at Dad's warehouse.{/i}"
                "Don't buy":
                    RT "{i}Not right now.{/i}"
    elif buy_var == "accessories_5":
        if money <= 999:
            "You don't have enough money."
        elif invaccessories_5 >= 1:
            if randomnum == 1:
                "You already have enough."
            elif randomnum == 2:
                "You have enough already."
        else:
            menu:
                "Buy camera accessory.":
                    $ futaccessories_5 += 1
                    $ money -= 1000
                    "You bought a new camera accessory."
                    RT "{i}Great, now the pictures will be higher quality and will bring us more likes! I'll just need to pick it up at Dad's warehouse.{/i}"
                "Don't buy":
                    RT "{i}Not right now.{/i}"
    elif buy_var == "accessories_6":
        if money <= 499:
            "You don't have enough money."
        elif invaccessories_6 >= 1:
            if randomnum == 1:
                "You already have enough."
            elif randomnum == 2:
                "You have enough already."
        else:
            menu:
                "Buy camera accessory.":
                    $ futaccessories_6 += 1
                    $ money -= 500
                    "You bought a new camera accessory."
                    RT "{i}Great, now with this microphone we can make videos for more money. I'll just need to pick it up at Dad's warehouse.{/i}"
                "Don't buy":
                    RT "{i}Not right now.{/i}"
    elif buy_var == "accessories_7":
        if money <= 999:
            "You don't have enough money."
        elif invaccessories_7 >= 1:
            if randomnum == 1:
                "You already have enough."
            elif randomnum == 2:
                "You have enough already."
        else:
            menu:
                "Buy camera accessory.":
                    $ futaccessories_7 += 1
                    $ money -= 1000
                    "You bought a new camera accessory."
                    RT "{i}Great, now the video quality will be better and will bring us more likes. I'll just need to pick it up at Dad's warehouse.{/i}"
                "Don't buy":
                    RT "{i}Not right now.{/i}"
    elif buy_var == "accessories_8":
        if money <= 1499:
            "You don't have enough money."
        elif invaccessories_8 >= 1:
            if randomnum == 1:
                "You already have enough."
            elif randomnum == 2:
                "You have enough already."
        else:
            menu:
                "Buy camera accessory":
                    $ futaccessories_8 += 1
                    $ money -= 1500
                    "You bought a new camera accessory."
                    RT "{i}Great, now the video quality will be better and will bring us more likes. I'll just need to pick it up at Dad's warehouse.{/i}"
                "Don't buy":
                    RT "{i}Not right now.{/i}"
    elif buy_var == "jacky_bikini_1":
        RT "{i}Mmmmm... I can imagine all the girls in this... But I think it would look best on Mom.{/i}"
        if money <= 249:
            "You don't have enough money."
        elif invj_bikini_1 >= 1:
            if randomnum == 1:
                "You already have enough."
            elif randomnum == 2:
                "You have enough already."
        else:
            menu:
                "Buy bikini":
                    $ futj_bikini_1 += 1
                    $ money -= 250
                    "You bought a new swimsuit."
                    RT "{i}Wow! That's expensive, but Mom will only wear the most stylish swimsuits to the club pool. I'll just need to pick it up at Dad's warehouse.{/i}"
                "Don't buy":
                    RT "{i}Not right now.{/i}"
    elif buy_var == "ball_gag":
        if money <= 49:
            "You don't have enough money."
        elif invball_gag >= 1:
            if randomnum == 1:
                "You already have enough."
                $ ball_gag_owned = True
            elif randomnum == 2:
                "You have enough already."
                $ ball_gag_owned = True
            elif fut_ball_gag >= 1:
                RT "{i}I've already bought this... I still need to go pick it up at the warehouse.{/i}"
        else:
            menu:
                "Buy ball gag.":
                    $ fut_ball_gag += 1
                    $ money -= 50
                    "You bought a ball gag."
                    RT "{i}I don't know what I'm going to use this for, but it never hurts to have a ball gag on hand. I'd better go to Dad's warehouse to pick it up.{/i}"
                "Don't buy":
                    RT "{i}Not right now.{/i}"
    elif buy_var == "ph_book1":
        RT "{i}Here we go... Perry Hotter and the Sorceror's Bone.{/i}"
        RT "{i}One hundred and fifty dollars! Holy fuck! I should have just read them when everyone else was reading them. I guess my only option is this hardback collector's edition.{/i}"
        if money <= 149:
            "You don't have enough money."
        elif invph_book1 >= 1:
            if randomnum == 1:
                "You already have enough."
                $ first_book_owned = True
            elif randomnum == 2:
                "You have enough already."
                $ first_book_owned = True
            elif fut_ph_book1 >= 1:
                RT "{i}I've already bought this... I still need to go pick it up at the warehouse.{/i}"
        else:
            menu:
                "Buy Perry Hotter Book 1.":
                    $ fut_ph_book1 += 1
                    $ money -= 150
                    "You bought Perry Hotter Book 1."
                    RT "{i}This book had better live up to the hype!{/i}"
                "Don't buy":
                    RT "{i}Not right now.{/i}"
    elif buy_var == "ph_book2":
        RT "{i}Here we go... Perry Hotter and her chambers of Secrets. Am I the only one who think's these titles are questionably sexual?{/i}"
        RT "{i}Goddammit! Looks like my only option is the hardback collector's edition for this book too.{/i}"
        if money <= 149:
            "You don't have enough money."
        elif invph_book2 >= 1:
            if randomnum == 1:
                "You already have enough."
                $ second_book_owned = True
            elif randomnum == 2:
                "You have enough already."
                $ second_book_owned = True
            elif fut_ph_book2 >= 1:
                RT "{i}I've already bought this... I still need to go pick it up at the warehouse.{/i}"
        else:
            menu:
                "Buy Perry Hotter Book 2.":
                    $ fut_ph_book2 += 1
                    $ money -= 150
                    "You bought Perry Hotter Book 2."
                    RT "{i}At least the first book was slightly entertaining... Maybe this one won't be too bad either.{/i}"
                "Don't buy":
                    RT "{i}Not right now.{/i}"
    elif buy_var == "ph_book3":
        RT "{i}Alrigh... Perry Hotter and the prisoner of Moldevorts Dungeon. Oh come on... Even the cover is overtly sexual.{/i}"
        RT "{i}Of course! Another collector's edition. I guess third times the charm.{/i}"
        if money <= 149:
            "You don't have enough money."
        elif invph_book3 >= 1:
            if randomnum == 1:
                "You already have enough."
                $ third_book_owned = True
            elif randomnum == 2:
                "You have enough already."
                $ third_book_owned = True
            elif fut_ph_book3 >= 1:
                RT "{i}I've already bought this... I still need to go pick it up at the warehouse.{/i}"
        else:
            menu:
                "Buy Perry Hotter Book 3.":
                    $ fut_ph_book3 += 1
                    $ money -= 150
                    "You bought Perry Hotter Book 3."
                    RT "{i}I can't admit to anyone that I kind of like these stories.{/i}"
                "Don't buy":
                    RT "{i}Not right now.{/i}"
    return
