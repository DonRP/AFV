transform timer_animation:
    zoom 1.15
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.5
    zoom 1.0
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.5
    repeat

transform win_animation:
    zoom 1.5
    linear 0.25 alpha 1.0
    linear 0.25 alpha 0.5
    zoom 1.0
    linear 0.25 alpha 1.0
    linear 0.25 alpha 0.5
    repeat

transform cards_animation:
    xalign 5.0
    linear 0.4 xalign 0.0
    linear 0.2 xalign 0.5

default memory_game_bet10 = False
default memory_game_bet25 = False
default memory_game_bet50 = False
default memory_game_bet_money = 0
default memo_w = 0
default memo_l = 0

style text_frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame1.png", 25, 25)

style text_win_lose:
    xalign 0.5
    yalign 0.4
    size 60
    bold True
    outlines [(1.5, "#000000", 0,0)]

init:
    python:

        renpy.music.register_channel("memory_game_m", mixer="music", loop=False)

################################################################################################################################################################
        #import random

        class ParticleBurst(object):
            def __init__(self, theDisplayable, explodeTime=0, numParticles=100, particleTime = 0.500, particleXSpeed = 3, particleYSpeed = 3, centerZone = 200):
                self.sm = SpriteManager(update=self.update)
                # A list of (sprite, starting-x, speed).
                self.stars = [ ]
                self.displayable = theDisplayable
                self.centerZone = centerZone
                self.explodeTime = explodeTime
                self.particleMax = numParticles
                self.particleTime = particleTime
                self.particleXSpeed = particleXSpeed
                self.particleYSpeed = particleYSpeed
                self.timePassed = 0
                # Note: We store the displayable in a variable here.
                # That's important - it means that all of the stars at
                # a given speed have the same displayable. We render that
                # displayable once, and cache the result.

            def add(self, d, speed, st):
                s = self.sm.create(d)
                s.x = self.sm.width/2 - (renpy.random.random()*self.centerZone)
                s.y = self.sm.height/2 - (renpy.random.random()*self.centerZone)
                ySpeed = ((renpy.random.random() - 0.5) * self.particleYSpeed)
                xSpeed = ((renpy.random.random() - 0.5) * self.particleXSpeed)
                pTime = (renpy.random.random() * self.particleTime ) + st
                self.stars.append((s, ySpeed, xSpeed, pTime))

            def update(self, st):
                sindex=0
                for s, ySpeed, xSpeed, particleTime in self.stars:
                    if (st < particleTime):
                        s.x += xSpeed
                        s.y += ySpeed
                    else:
                        s.destroy()
                        self.stars.pop(sindex)
                    sindex += 1
                if len(self.stars) < self.particleMax:
                    if st < self.explodeTime or self.explodeTime == 0:
                        self.add(self.displayable, 2, st)
                return 0

################################################################################################################################################################
        class ExplodeFactory: # the factory that makes the particles

            def __init__(self, theDisplayable, explodeTime=0, numParticles=20):
                self.displayable = theDisplayable
                self.time = explodeTime
                self.particleMax = numParticles

            def create(self, partList, timePassed):
                newParticles = None
                if partList == None or len(partList) < self.particleMax:
                    if timePassed < self.time or self.time == 0:
                        newParticles = self.createParticles()
                return newParticles


            def createParticles(self):
                timeDelay = renpy.random.random() * 0.6
                return [ExplodeParticle(self.displayable, timeDelay)]

            def predict(self):
                return [self.displayable]

        class ExplodeParticle:

            def __init__(self, theDisplayable, timeDelay):
                self.displayable = theDisplayable
                self.delay = timeDelay
                self.xSpeed = (renpy.random.random() - 0.5) * 0.02
                self.ySpeed = (renpy.random.random() - 0.5) * 0.02
                self.xPos = 0.5
                self.yPos = 0.5


            def update(self, theTime):
                if (theTime > self.delay):
                    self.xPos += self.xSpeed
                    self.yPos += self.ySpeed

                    if self.xPos > 1.05 or self.xPos < -1.05 or self.yPos > 1.05 or self.yPos < -1.05:
                        return None

                return (self.xPos, self.yPos, theTime, self.displayable)
################################################################################################################################################################

    image boom = Particles(ExplodeFactory("images/interface_images/Memory_game/star.png", numParticles=100, explodeTime = 1.0))

init:
    python:
        def cards_shuffle(x):
            renpy.random.shuffle(x)
            return x

    image C1 = im.Scale("images/interface_images/Memory_game/card_1.webp", 100, 152) #Enter specific numbers <--
    image C2 = im.Scale("images/interface_images/Memory_game/card_2.webp", 100, 152) #Enter specific numbers <--
    image C3 = im.Scale("images/interface_images/Memory_game/card_3.webp", 100, 152) #Enter specific numbers <--
    image C4 = im.Scale("images/interface_images/Memory_game/card_4.webp", 100, 152) #Enter specific numbers <--
    image C5 = im.Scale("images/interface_images/Memory_game/card_5.webp", 100, 152) #Enter specific numbers <--
    image C6 = im.Scale("images/interface_images/Memory_game/card_6.webp", 100, 152) #Enter specific numbers <--
    image C7 = im.Scale("images/interface_images/Memory_game/card_7.webp", 100, 152) #Enter specific numbers <--
    image C8 = im.Scale("images/interface_images/Memory_game/card_8.webp", 100, 152) #Enter specific numbers <--
    image C9 = im.Scale("images/interface_images/Memory_game/card_9.webp", 100, 152) #Enter specific numbers <--
    image C10 = im.Scale("images/interface_images/Memory_game/card_10.webp", 100, 152) #Enter specific numbers <--
    image C11 = im.Scale("images/interface_images/Memory_game/card_11.webp", 100, 152) #Enter specific numbers <--
    image C12 = im.Scale("images/interface_images/Memory_game/card_12.webp", 100, 152) #Enter specific numbers <--
    image C13 = im.Scale("images/interface_images/Memory_game/card_13.webp", 100, 152) #Enter specific numbers <--
    image C14 = im.Scale("images/interface_images/Memory_game/card_14.webp", 100, 152) #Enter specific numbers <--
    image C15 = im.Scale("images/interface_images/Memory_game/card_15.webp", 100, 152) #Enter specific numbers <--
    image C16 = im.Scale("images/interface_images/Memory_game/card_16.webp", 100, 152) #Enter specific numbers <--
    image C17 = im.Scale("images/interface_images/Memory_game/card_17.webp", 100, 152) #Enter specific numbers <--
    image C18 = im.Scale("images/interface_images/Memory_game/card_18.webp", 100, 152) #Enter specific numbers <--
    image C19 = im.Scale("images/interface_images/Memory_game/card_19.webp", 100, 152) #Enter specific numbers <--
    image C20 = im.Scale("images/interface_images/Memory_game/card_20.webp", 100, 152) #Enter specific numbers <--
    image C_Idle = im.Scale("images/interface_images/Memory_game/card_idle.webp", 100, 152) #Enter specific numbers <--
    image C_Hover = im.Scale("images/interface_images/Memory_game/card_hover.webp", 100, 152) #Enter specific numbers <--

    image GameIco = "images/interface_images/Memory_game/Brain_games.webp"

    image Bet10 = im.Scale("images/interface_images/Memory_game/Bet10.webp", 200, 200) #Enter specific numbers <--
    image Bet25 = im.Scale("images/interface_images/Memory_game/Bet25.webp", 200, 200) #Enter specific numbers <--
    image Bet50 = im.Scale("images/interface_images/Memory_game/Bet50.webp", 200, 200) #Enter specific numbers <--
    image BetHover = im.Scale("images/interface_images/Memory_game/BetHover.webp", 200, 200) #Enter specific numbers <--

    image Game_exit = im.Scale("images/interface_images/Memory_game/Game_exit.webp", 100, 100) #Enter specific numbers <--
    image Game_exit_hover = im.Scale("images/interface_images/Memory_game/Game_exit_h.webp", 100, 100) #Enter specific numbers <--

    image PlayAgain = "images/interface_images/Memory_game/Play again!.webp"
    image PlayAgainHover = "images/interface_images/Memory_game/BetHover.webp"

    image HelpNormal = im.Scale("images/interface_images/Memory_game/HelpNormal.png", 302, 109) #Enter specific numbers <--
    image HelpHover = im.Scale("images/interface_images/Memory_game/HelpHover.png", 302, 109) #Enter specific numbers <--

    image memory_game_bg1 = im.Scale("images/interface_images/Memory_game/Brain_games_1280x720.webp", 1280, 720) #Enter specific numbers <--

screen displayTextScreen():
    key "hide_windows" action NullAction()
    zorder 100
    default displayText = ("")

    vbox:
        xalign 0.5
        yalign 0.01
        frame:
            style "text_frame"
            text "{size=+6}[displayText]{/size}"

screen memory_game_bet():
    key "hide_windows" action NullAction()
    add "memory_game_bg1"

    modal True
    vbox xalign 0.01 yalign 0.99:
        frame:
            xmaximum 200
            style "text_frame"
            text "W:{color=#00ff00}[memo_w]{/color} L:{color=#f00}[memo_l]{/color}"
    vbox xalign 0.95 yalign 0.01 spacing 20:
        frame:
            style "text_frame"
            text "$"+str(money) size 50

    imagebutton:
        xpos 274
        ypos 232
        focus_mask True
        idle Transform("Bet10")
        idle_foreground Transform("BetHover")
        clicked [ Play ("sound", "music/mouse_click.mp3"),
            If( money >= 10,
                [ SetVariable("money", money-10),
                    SetVariable("memory_game_bet10", True),
                    Jump("memory_game_roll") ],
                Jump("memory_game_label") ),
            Hide("displayTextScreen"),
            Hide("memory_game_bet") ]
#        hovered Show("displayTextScreen", displayText = "Bet $10!")
#        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 506
        ypos 232
        focus_mask True
        idle Transform("Bet25")
        idle_foreground Transform("BetHover")
        clicked [ Play ("sound", "music/mouse_click.mp3"),
            If( money >= 25,
                [ SetVariable("money", money-25),
                    SetVariable("memory_game_bet25", True),
                    Jump("memory_game_roll") ],
                Jump("memory_game_label") ),
            Hide("displayTextScreen"),
            Hide("memory_game_bet") ]
#        hovered Show("displayTextScreen", displayText = "Bet $25!")
#        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 737
        ypos 232
        focus_mask True
        idle Transform("Bet50")
        idle_foreground Transform("BetHover")
        clicked [ Play ("sound", "music/mouse_click.mp3"),
            If( money >= 50,
                [ SetVariable("money", money-50),
                    SetVariable("memory_game_bet50", True),
                    Jump("memory_game_roll") ],
                Jump("memory_game_label") ),
            Hide("displayTextScreen"),
            Hide("memory_game_bet") ]
#        hovered Show("displayTextScreen", displayText = "Bet $50!")
#        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1150
        ypos 600
        focus_mask True
        idle Transform("Game_exit")
        idle_foreground Transform("Game_exit_hover")
        action [ Play ("sound", "music/mouse_click.mp3"),
            Hide("displayTextScreen"),
            Hide("memory_game_again_screen"),
            Hide("memory_game_bet"),
            Jump("map_location") ]
#        hovered Show("displayTextScreen", displayText = "Exit game!")
#        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 955
        ypos 65
        focus_mask True
        idle Transform("HelpNormal")
        hover Transform("HelpHover")
        action NullAction()
#        hovered Show("displayTextScreen", displayText = "Help!")
#        unhovered Hide("displayTextScreen")

screen memory_game_scr():
    key "game_menu" action NullAction()
    key "hide_windows" action NullAction()
    add "memory_game_bg1"


    if memo_timer >0.1:
        timer 0.1 action [ If( memo_timer > 0.1,
            SetVariable("memo_timer", memo_timer - 0.1),
            [ Function(renpy.block_rollback),
                SetVariable("memo_l", memo_l + 1),
                Hide("memory_game_scr"),
                Show("screen_memory_game_losemoney") ] ) ] repeat True

    if memo_timer >10:
        vbox  xalign 0.54 yalign 0.014 spacing 20:
            frame:
                style "text_frame"
                text str("{size=+20}Time:{color=#00ff00} [memo_timer]{/color}{/size}")

    if memo_timer <10 and memo_timer > 0.1:
        timer 1.9 action [Play ("memory_game_m", "music/card_lose.wav")]
        vbox  xalign 0.54 yalign 0.014 spacing 20:
            frame:
                style "text_frame"
                text str("{size=+20}Time:{color=#00ff00} [memo_timer]{/color}{/size}") at timer_animation

    elif memo_timer <0.1:
        timer 0.1 action [ Function(renpy.block_rollback),
            SetVariable("memo_l", memo_l + 1),
            Hide("memory_game_scr"),
            Show("screen_memory_game_losemoney") ]
        text str("{size=+20}{color=#f00}0{/color}{/size}") xalign 0.54 yalign 0.014

    vbox xalign 0.95 yalign 0.01 spacing 20:
        frame:
            style "text_frame"
            text str("{size=+18} Turns Left:{color=#00ff00}[turns_left] {/color}{/size}")

    $ a = cards_gird
    $ b = cards_gird2
    grid a b:

        xalign 0.5
        yalign 0.5
        spacing 50
        at cards_animation
        for card in cards_list:
            imagebutton:


                if card["c_chosen"]:

                    idle (card["c_value"])
                    hover (card["c_value"])
                else:
                    idle ("C_Idle")
                    idle_foreground Transform("C_Hover",zoom=0.98)

                if memo_timer >0.1:
                    action [ If( (card["c_chosen"] or not can_click),
                        None,
                        [Play ("sound", "music/card_flip.wav"),
                            SetDict(cards_list[card["c_number"]], "c_chosen", True),
                            Return(card["c_number"]) ] ) ]

label memory_game_label:
    $ can_hide_windows = False
    $ renpy.block_rollback()
    scene memory_game_bg1
    call screen memory_game_bet

label memory_game_roll:
    $ values_list_roll = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "C16", "C17", "C18", "C19", "C20"]
    $ values_list_rolled = []

    if memory_game_bet10 == True:
        $ memory_game_bet_money = 10
        $ turns_left_roll = 2
        $ memo_timer = 38
        $ cards_number = 6
        $ cards_gird = 4
        $ cards_gird2 = 3
        $ memory_game_bet_money = 10
        jump memory_game_cards_roll

    if memory_game_bet25 == True:
        $ memory_game_bet_money = 25
        $ turns_left_roll = renpy.random.choice([2,3,])
        if turns_left_roll == 2:
            $ cards_number = 8
            $ memo_timer = 75
            $ cards_gird = 8
            $ cards_gird2 = 2
        if turns_left_roll == 3:
            $ memo_timer = 66
            $ cards_gird = 6
            $ cards_gird2 = 3
            $ cards_number = 6
        jump memory_game_cards_roll

    if memory_game_bet50 == True:
        $ memory_game_bet_money = 50
        $ turns_left_roll = renpy.random.choice([3,4])
        $ cards_gird = 8
        $ cards_gird2 = 3

        if turns_left_roll == 4:
            $ memo_timer = 80
            $ cards_number = 6
        if turns_left_roll == 3:
            $ memo_timer = 88
            $ cards_number = 8
        jump memory_game_cards_roll
###
        label memory_game_cards_roll:
            if cards_number > 0:
                $ card_roll = renpy.random.choice(values_list_roll)
                if turns_left_roll == 4:
                    $ values_list_rolled.append(card_roll)
                    $ values_list_rolled.append(card_roll)
                    $ values_list_rolled.append(card_roll)
                    $ values_list_rolled.append(card_roll)

                if turns_left_roll == 3:
                    $ values_list_rolled.append(card_roll)
                    $ values_list_rolled.append(card_roll)
                    $ values_list_rolled.append(card_roll)

                if turns_left_roll == 2:
                    $ values_list_rolled.append(card_roll)
                    $ values_list_rolled.append(card_roll)
                $ values_list_roll.remove(card_roll)
                $ cards_number -= 1
                jump memory_game_cards_roll
            else:
                jump memory_game

label memory_game:

    $ renpy.block_rollback()
    window hide

    $ values_list = values_list_rolled

    $ values_list = cards_shuffle(values_list)
    $ cards_list = []

    python:
        for i in range (0, len(values_list) ):
            cards_list.append ( {"c_number":i, "c_value": values_list[i], "c_chosen":False} )

    $ renpy.sound.play("music/card_slide.wav")
    show screen memory_game_scr

    label memory_game_loop:
        $ can_click = True
        $ turned_cards_numbers = []
        $ turned_cards_values = []


        if turns_left_roll == 2:
            $ turns_left = 2
        if turns_left_roll == 3:
            $ turns_left = 3
        if turns_left_roll == 4:
            $ turns_left = 4

        label turns_loop:
            if turns_left > 0:
                $ result = ui.interact()
                $ memo_timer = memo_timer
                $ turned_cards_numbers.append (cards_list[result]["c_number"])
                $ turned_cards_values.append (cards_list[result]["c_value"])
                $ turns_left -= 1
                jump turns_loop


        $ can_click = False

        if turned_cards_values.count(turned_cards_values[0]) != len(turned_cards_values):
            $ renpy.sound.play("music/card_failure.wav")
            $ renpy.pause (1.0, hard = True)
            $ renpy.sound.play("music/card_flip.wav")
            python:
                for i in range (0, len(turned_cards_numbers) ):
                    cards_list[turned_cards_numbers[i]]["c_chosen"] = False

        else:
            $ renpy.sound.play("music/card_correct.wav")
            $ renpy.pause (1.0, hard = True)
            $ renpy.sound.play("music/card_flip.wav")
            python:
                for i in range (0, len(turned_cards_numbers) ):
                    cards_list[turned_cards_numbers[i]]["c_value"] = Null()

                for j in cards_list:
                    if j["c_chosen"] == False:
                        renpy.jump ("memory_game_loop")
                renpy.jump ("memory_game_win")



        jump memory_game_loop


screen screen_memory_game_losemoney():
    modal True
    key "hide_windows" action NullAction()
    text _("You lose!") style "text_win_lose"
    $ renpy.block_rollback()
    if memory_game_bet10 == True:
        text "{size=+25}{color=#00ff00}-10{/color}{color=#00ff00}${/color}{/size}" xalign 0.502 yalign 0.53
    if memory_game_bet25 == True:
        text "{size=+25}{color=#00ff00}-25{/color}{color=#00ff00}${/color}{/size}" xalign 0.502 yalign 0.53
    if memory_game_bet50 == True:
        text "{size=+25}{color=#00ff00}-50{/color}{color=#00ff00}${/color}{/size}" xalign 0.502 yalign 0.53
    timer 3.0 action [ SetVariable("memory_game_bet10", False),
            SetVariable("memory_game_bet25", False),
            SetVariable("memory_game_bet50", False),
            Hide("screen_memory_game_losemoney"),
            Show("memory_game_again_screen") ]

screen screen_memory_game_wonmoney():
    default win_timer = ("#%06x" % renpy.random.randint(0, 0xFFFFFF)) #"#34f500"

    timer 0.5 repeat True:
        action [SetScreenVariable('win_timer', ("#%06x" % renpy.random.randint(0, 0xFFFFFF)))]

    modal True
    key "hide_windows" action NullAction()
    text _("YOU WON!!!") style "text_win_lose" color win_timer at win_animation
    #add "boom"
    add ParticleBurst("images/interface_images/Memory_game/star.png", explodeTime=0, numParticles=1000, particleTime=4.0, particleXSpeed = 3, particleYSpeed = 3).sm at truecenter
    if memory_game_bet10 == True:
        text "{size=+25}{color=#00ff00}+20{/color}{color=#00ff00}${/color}{/size}" xalign 0.502 yalign 0.53
    if memory_game_bet25 == True:
        text "{size=+25}{color=#00ff00}+50{/color}{color=#00ff00}${/color}{/size}" xalign 0.502 yalign 0.53
    if memory_game_bet50 == True:
        text "{size=+25}{color=#00ff00}+100{/color}{color=#00ff00}${/color}{/size}" xalign 0.502 yalign 0.53
    timer 3.0 action [ SetVariable("memory_game_bet10", False),
            SetVariable("memory_game_bet25", False),
            SetVariable("memory_game_bet50", False),
            Hide("screen_memory_game_wonmoney"),
            Show("memory_game_again_screen") ]

label memory_game_win:
    $ renpy.music.stop(channel='memory_game_m', fadeout=None)
    $ renpy.sound.play("music/card_win.wav")
    $ renpy.block_rollback()
    $ memo_w += 1
    $ money += 2 * memory_game_bet_money
    call screen screen_memory_game_wonmoney

screen memory_game_again_screen():
    modal True
    key "hide_windows" action NullAction()
    $ renpy.block_rollback()

    imagebutton:
        xpos 500
        ypos 250
        focus_mask True
        idle Transform("PlayAgain")
        idle_foreground Transform("PlayAgainHover")
        action [ Play ("sound", "music/mouse_click.mp3"),
            Hide("displayTextScreen"),
            Hide("memory_game_again_screen"),
            Hide("memory_game_scr"),
            Hide("screen_memory_game_losemoney"),
            Hide("screen_memory_game_wonmoney"),
            Jump("memory_game_label") ]
#        hovered Show("displayTextScreen", displayText = "Play Again!")
#        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1150
        ypos 600
        focus_mask True
        idle Transform("Game_exit")
        idle_foreground Transform("Game_exit_hover")
        action [ Play ("sound", "music/mouse_click.mp3"),
            Hide("displayTextScreen"),
            Hide("memory_game_again_screen"),
            Hide("memory_game_scr"),
            Hide("screen_memory_game_losemoney"),
            Hide("screen_memory_game_wonmoney"),
            Jump("map_location") ]
#        hovered Show("displayTextScreen", displayText = "Exit game!")
#        unhovered Hide("displayTextScreen")

label map_location:

    hide screen Points_screen_Sidney

    if any([screen_on == "{}".format(k) for k in ryan_screens]): # ryan_screens
        jump myroom
    elif any([screen_on == "{}".format(k) for k in lounge_screens]): # lounge_screens
        jump lounge
    elif any([screen_on == "{}".format(k) for k in bath_screens]): # bath_screens
        jump bath
    elif any([screen_on == "{}".format(k) for k in kitchen_screens]): # kitchen_screens
        jump kitchen
    elif any([screen_on == "{}".format(k) for k in mom_screens]): # mom_screens
        jump momroom
    elif any([screen_on == "{}".format(k) for k in lauren_screens]): # lauren_screens
        jump laurenroom
    elif any([screen_on == "{}".format(k) for k in school_screens]): # school_screens
        if timeofdaycounter <= 3:
            jump school
        else:
            RT "{i}School has ended, I must return home.{/i}"
            jump myroom
    elif any([screen_on == "{}".format(k) for k in class_screens]): # class_screens
        if timeofdaycounter <= 3 and start_of_campaign:
            jump new_classroom
        elif timeofdaycounter <= 3:
            jump classroom
        else:
            RT "{i}School has ended, I must return home.{/i}"
            jump myroom
    elif any([screen_on == "{}".format(k) for k in schoolbath_screens]): # schoolbath_screens
        if timeofdaycounter <= 3:
            jump schoolbathroom
        else:
            RT "{i}School has ended, I must return home.{/i}"
            jump myroom
    elif any([screen_on == "{}".format(k) for k in girlslocker_screens]): # girlslocker_screens
        if timeofdaycounter <= 3:
            jump girlslockers
        else:
            RT "{i}School has ended, I must return home.{/i}"
            jump myroom
    elif any([screen_on == "{}".format(k) for k in city_screens]): # city_screens
        if timeofdaycounter <=4:
            $ screen_on = "citymapmap"
            call screen citymapmap
        else:
            $ screen_on = "citymapmapnight"
            call screen citymapmapnight
