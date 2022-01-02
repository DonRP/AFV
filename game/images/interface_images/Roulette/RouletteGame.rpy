
####################################################################################################################################################
### Powerd by D.S.-sama ############################################################################################################################
####################################################################################################################################################
####################################################################################################################################################

init python:

    # you don't need this but let it here
    def atl_complete(*args):
        renpy.hide_screen("betRoulette")
        renpy.transition(Dissolve(1.5))
        renpy.jump("lblCheckRoll")

    def exitRoulette():
        store.betPickVar.clear()
        store.select100 = False
        store.select500 = False
        store.select1000 = False
        store.betAmmount = 0
        renpy.hide_screen("startRoulette")
        renpy.transition(Dissolve(1.5))
        renpy.call("gamble_end")  #<== change with wath label you want to jump to

    def rouletteBetPick( var ):
        # The bet code
        if var == "100":
            store.betAmmount = 100
            store.select100 = True
            store.select500 = False
            store.select1000 = False
        elif var == "500":
            store.betAmmount = 500
            store.select100 = False
            store.select500 = True
            store.select1000 = False
        elif var == "1000":
            store.betAmmount = 1000
            store.select100 = False
            store.select500 = False
            store.select1000 = True

    def checkRoll():
        if store.theRoll in store.rouletteRed:
            store.theRollColor = "Red"
            store.theRollColor_text = "{outlinecolor=#ffffff}{color=#FF0000}{b}Red{/b}{/color}{/outlinecolor}"
        elif store.theRoll in store.rouletteBlack:
            store.theRollColor = "Black"
            store.theRollColor_text = "{outlinecolor=#ffffff}{color=#000000}{b}Black{/b}{/color}{/outlinecolor}"
        else:
            store.theRollColor = "Green"
            store.theRollColor_text = "{outlinecolor=#ffffff}{color=#008000}{b}Green{/b}{/color}{/outlinecolor}"

        if store.theRoll in store.rouletteOdd:
            store.theRollOddOrEven = "Odd"
            store.theRollOddOrEven_text = "{outlinecolor=#ffffff}{color=#00008B}{b}Odd{/b}{/color}{/outlinecolor}"
        elif store.theRoll in store.rouletteEven:
            store.theRollOddOrEven = "Even"
            store.theRollOddOrEven_text = "{outlinecolor=#ffffff}{color=#00008B}{b}Even{/b}{/color}{/outlinecolor}"


    def playRoll():
        store.theRoll = renpy.random.randint(0,36)

        if theRoll == 0:
            store.degreesForNumbers = 0

        elif theRoll == 26: #32
            store.degreesForNumbers = 9.72972972972973
        elif theRoll == 3: #15
            store.degreesForNumbers = 19.45945945945946
        elif theRoll == 35: #19
            store.degreesForNumbers = 29.18918918918919
        elif theRoll == 12: #4
            store.degreesForNumbers = 38.91891891891892
        elif theRoll == 28: #21
            store.degreesForNumbers = 48.64864864864865
        elif theRoll == 7: #2
            store.degreesForNumbers = 58.37837837837838
        elif theRoll == 29: #25
            store.degreesForNumbers = 68.10810810810811
        elif theRoll == 18: #17
            store.degreesForNumbers = 77.83783783783784
        elif theRoll == 22: #34
            store.degreesForNumbers = 87.56756756756757

        elif theRoll == 9: #6
            store.degreesForNumbers = 97.2972972972973
        elif theRoll == 31: #27
            store.degreesForNumbers = 107.027027027027
        elif theRoll == 14: #13
            store.degreesForNumbers = 116.7567567567568
        elif theRoll == 20: #36
            store.degreesForNumbers = 126.4864864864865
        elif theRoll == 1: #11
            store.degreesForNumbers = 136.2162162162162
        elif theRoll == 33: #30
            store.degreesForNumbers = 145.9459459459459
        elif theRoll == 16: #8
            store.degreesForNumbers = 155.6756756756757
        elif theRoll == 24: #23
            store.degreesForNumbers = 165.4054054054054
        elif theRoll == 5: #10
            store.degreesForNumbers = 175.1351351351351

        elif theRoll == 10: #5
            store.degreesForNumbers = -175.1351351351351
        elif theRoll == 23: #24
            store.degreesForNumbers = -165.4054054054054
        elif theRoll == 8: #16
            store.degreesForNumbers = -155.6756756756757
        elif theRoll == 30: #33
            store.degreesForNumbers = -145.9459459459459
        elif theRoll == 11: #1
            store.degreesForNumbers = -136.2162162162162
        elif theRoll == 36: #20
            store.degreesForNumbers = -126.4864864864865
        elif theRoll == 13: #14
            store.degreesForNumbers = -116.7567567567568
        elif theRoll == 27: #31
            store.degreesForNumbers = -107.027027027027
        elif theRoll == 6: #9
            store.degreesForNumbers = -97.2972972972973

        elif theRoll == 34: #22
            store.degreesForNumbers = -87.56756756756757
        elif theRoll == 17: #18
            store.degreesForNumbers = -77.83783783783784
        elif theRoll == 25: #29
            store.degreesForNumbers = -68.10810810810811
        elif theRoll == 2: #7
            store.degreesForNumbers = -58.37837837837838
        elif theRoll == 21: #28
            store.degreesForNumbers = -48.64864864864865
        elif theRoll == 4: #12
            store.degreesForNumbers = -38.91891891891892
        elif theRoll == 19: #35
            store.degreesForNumbers = -29.18918918918919
        elif theRoll == 15: #3
            store.degreesForNumbers = -19.45945945945946
        elif theRoll == 32: #26
            store.degreesForNumbers = -9.72972972972973

        renpy.transition(Dissolve(1.5))
        renpy.show_screen("betRoulette")

    def handleBetPickVar( var ):
        if var in store.betPickVar:
            store.betPickVar.remove(var)
        else:
            store.betPickVar.append(var)

    def handleBetPickVarDozen( var ):
        store.betPickVar.clear()
        if int(var) == 1:
            store.betPickVar.append("1")
            store.betPickVar.append("2")
            store.betPickVar.append("3")
            store.betPickVar.append("4")
            store.betPickVar.append("5")
            store.betPickVar.append("6")
            store.betPickVar.append("7")
            store.betPickVar.append("8")
            store.betPickVar.append("9")
            store.betPickVar.append("10")
            store.betPickVar.append("11")
            store.betPickVar.append("12")
        elif int(var) == 2:
            store.betPickVar.append("13")
            store.betPickVar.append("14")
            store.betPickVar.append("15")
            store.betPickVar.append("16")
            store.betPickVar.append("17")
            store.betPickVar.append("18")
            store.betPickVar.append("19")
            store.betPickVar.append("20")
            store.betPickVar.append("21")
            store.betPickVar.append("22")
            store.betPickVar.append("23")
            store.betPickVar.append("24")
        elif int(var) == 3:
            store.betPickVar.append("25")
            store.betPickVar.append("26")
            store.betPickVar.append("27")
            store.betPickVar.append("28")
            store.betPickVar.append("29")
            store.betPickVar.append("30")
            store.betPickVar.append("31")
            store.betPickVar.append("32")
            store.betPickVar.append("33")
            store.betPickVar.append("34")
            store.betPickVar.append("35")
            store.betPickVar.append("36")

    def removeBetPickVar( var ):
        if var in store.betPickVar:
            store.betPickVar.remove(var)

    def clearBetPickVar():
        store.betPickVar.clear()

    def handleBetType( var ):
        store.betType = var
        store.betAmmount = 0
        store.select100 = False
        store.select500 = False
        store.select1000 = False
        renpy.hide_screen("betPickScreen")
        renpy.show_screen("betRoulette")
        renpy.transition(Dissolve(1.5))

default degreesForNumbers = 0
default theRoll = 0
default theRollColor_text = ""
default theRollColor = ""
default theRollOddOrEven_text = ""
default theRollOddOrEven = ""
default rouletteRolled = False
default payout = 0
default betPickVar = []
default betType = ""
default betAmmount = 0
default select100 = False
default select500 = False
default select1000 = False

define rouletteRed = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
define rouletteBlack = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
define rouletteOdd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
define rouletteEven = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]

define listRedBlack = [ 'Red', 'Black' ]
define listOddEven = [ 'Odd', 'Even' ]

define RLT_dealer = Character(_("Croupier"), color="#4118fa", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])

init:
    # The image definitions for roulette
    image bg rouletteStart = "images/interface_images/Roulette/Roulette01.png"

    image bg rouletteBallRoll = "images/interface_images/Roulette/Roulette02.png"
    image bg rouletteTable = "images/interface_images/Roulette/Roulette03.png"

    image rouletteBet = "images/interface_images/Roulette/Roulette01.png"
    image rouletteTable = "images/interface_images/Roulette/Roulette03.png"
    image rouletteTableHover = "images/interface_images/Roulette/Roulette03_hover.png"
    image rouletteWheel = im.Scale("images/interface_images/Roulette/RouletteWheel.png", 350, 350)
    image rouletteBall = im.Scale("images/interface_images/Roulette/RouletteBall.png", 350, 350)

    image roulettePlay = im.MatrixColor("images/interface_images/Roulette/rlt_icon.png", im.matrix.invert())
    image rouletteIcon:
        "images/interface_images/Roulette/rlt_icon.png"
        rotate -30

    image rltBetChip100 = im.Scale("images/interface_images/Roulette/bet100_chip.png", 200, 200)
    image rltBetChip500 = im.Scale("images/interface_images/Roulette/bet500_chip.png", 200, 200)
    image rltBetChip1000 = im.Scale("images/interface_images/Roulette/bet1000_chip.png", 200, 200)


    image betTypeStraight = im.Scale("images/interface_images/Roulette/betType_Straight_chip.png", 412, 412)
    image betTypeSplit = im.Scale("images/interface_images/Roulette/betType_Split_chip.png", 412, 412)
    image betTypeStreet = im.Scale("images/interface_images/Roulette/betType_Street_chip.png", 412, 412)
    image betTypeCorner = im.Scale("images/interface_images/Roulette/betType_Corner_chip.png", 412, 412)
    image betTypePenta = im.Scale("images/interface_images/Roulette/betType_Penta_chip.png", 412, 412)
    image betTypeLine = im.Scale("images/interface_images/Roulette/betType_Line_chip.png", 412, 412)
    image betTypeDozen = im.Scale("images/interface_images/Roulette/betType_Dozen_chip.png", 412, 412)
    image betTypeColor = im.Scale("images/interface_images/Roulette/betType_Color_chip.png", 412, 412)
    image betTypeEvenOdd = im.Scale("images/interface_images/Roulette/betType_EvenOdd_chip.png", 412, 412)

    image yesChip = im.Scale("images/interface_images/Roulette/chip_yes.png", 412, 412)
    image noChip = im.Scale("images/interface_images/Roulette/chip_no.png", 412, 412)

    # The transform definitions for roulette
    transform wheel_rot:
#        on show:
        rotate +3000
        easeout 6 rotate degreesForNumbers
    #        function atl_complete

    transform ball_rot:
#        on show:
        rotate -3000
        easeout 6 rotate 0

    transform rotation_Left2Right:
        zoom .5 #around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
        on idle:
            xzoom 1.0
        on hover:
            linear 0.008 xzoom -1.0
            linear 0.008 xzoom 1.0
            linear 0.008 xzoom -1.0
            linear 0.008 xzoom 1.0
            linear 0.008 xzoom -1.0
            linear 0.008 xzoom 1.0
            linear 0.008 xzoom -1.0
            linear 0.008 xzoom 1.0
            linear 0.008 xzoom -1.0
            linear 0.008 xzoom 1.0
            linear 0.008 xzoom -1.0
            linear 0.008 xzoom 1.0
            linear 0.008 xzoom -1.0
            linear 0.008 xzoom 1.0
            linear 0.008 xzoom -1.0
            linear 0.008 xzoom 1.0
            linear 0.008 xzoom -1.0
            linear 0.008 xzoom 1.0
            linear 0.008 xzoom -1.0
            linear 0.008 xzoom 1.0
            linear 0.008 xzoom -1.0
            linear 0.008 xzoom 1.0
            linear 0.008 xzoom -1.0
            linear 0.008 xzoom 1.0
            repeat

### Screens

screen startRoulette():

    add "rouletteBet"

    text _("Do you want to play the Roulette?") xpos 0.23 size 40 color "#E60000" outlines [(3, "#000", 0,0)]  #000056

    vbox xpos 0.555 ypos 0.62:
        hbox:
            imagebutton at inv_eff:
                idle "yesChip"
                action [ Hide("startRoulette", transition=Dissolve(1.0)), Show("betPickScreen", transition=Dissolve(1.0)) ]

            imagebutton at inv_eff:
                idle "noChip"
                action Function(exitRoulette)

screen betPickScreen():

    $ clearBetPickVar()

    add "rouletteBet"

    text _("What type of game do you want to play?") xpos 0.23 size 40 color "#E60000" outlines [(3, "#000", 0,0)]  #000056

    hbox:
        xalign 0.85
        yalign 0.8
        imagebutton at inv_eff:        # 1 muber
            idle "betTypeStraight"
            action Function(handleBetType, "Straight")
        imagebutton at inv_eff:        # 2 numbers
            idle "betTypeSplit"
            action Function(handleBetType, "Split")
        imagebutton at inv_eff:        # 3 numbers
            idle "betTypeStreet"
            action Function(handleBetType, "Street")
        imagebutton at inv_eff:        # 4 numbers
            idle "betTypeCorner"
            action Function(handleBetType, "Corner")
        imagebutton at inv_eff:        # 5 numbers
            idle "betTypePenta"
            action Function(handleBetType, "Penta")
    hbox:
        xalign 0.7
        yalign 1.15
        imagebutton at inv_eff:        # 6 numbers
            idle "betTypeLine"
            action Function(handleBetType, "Line")
        imagebutton at inv_eff:        # 12 numbers
            idle "betTypeDozen"
            action Function(handleBetType, "Dozen")
        imagebutton at inv_eff:        # 1 color
            idle "betTypeColor"
            action Function(handleBetType, "Color")
        imagebutton at inv_eff:        # even or odd
            idle "betTypeEvenOdd"
            action Function(handleBetType, "EvenOdd")

screen betRoulette():

    default tt = Tooltip("")

    $ playerPiked = ', '.join(betPickVar)

    add "rouletteTable"

    ### Bet imagebuttons
    imagemap:
        ground "rouletteTable"
        hover "rouletteTableHover"

        if not rouletteRolled:
            if betType == "Color":
                # Black
                hotspot (770,551,94,53) action [ Function(removeBetPickVar, "Red"), Function(handleBetPickVar, "Black") ]
                # Red
                hotspot (676,551,94,53) action [ Function(removeBetPickVar, "Black"), Function(handleBetPickVar, "Red") ]

            if betType == "EvenOdd":
                # ODD
                hotspot (872,551,94,53) action [ Function(removeBetPickVar, "Even"), Function(handleBetPickVar, "Odd") ]
                # EVEN
                hotspot (578,551,94,53) action [ Function(removeBetPickVar, "Odd"), Function(handleBetPickVar, "Even") ]

            if betType in [ "Straight", "Split", "Street", "Corner", "Penta", "Line", "Dozen" ]:
                # 0
                hotspot (385,251,93,239) action Function(handleBetPickVar, "0") #SetVariable("betPickVar", 0)
                # 1
                hotspot (479,417,44,74) action Function(handleBetPickVar, "1") #SetVariable("betPickVar", 1)
                #2
                hotspot (479,339,44,74) action Function(handleBetPickVar, "2") #SetVariable("betPickVar", 2)
                #3
                hotspot (479,260,44,74) action Function(handleBetPickVar, "3") #SetVariable("betPickVar", 3)
                #4
                hotspot (530,417,44,74) action Function(handleBetPickVar, "4") #SetVariable("betPickVar", 4)
                #5
                hotspot (530,339,44,74) action Function(handleBetPickVar, "5") #SetVariable("betPickVar", 5)
                #6
                hotspot (530,260,44,74) action Function(handleBetPickVar, "6") #SetVariable("betPickVar", 6)
                #7
                hotspot (578,417,44,73) action Function(handleBetPickVar, "7") #SetVariable("betPickVar", 7)
                #8
                hotspot (578,339,44,74) action Function(handleBetPickVar, "8") #SetVariable("betPickVar", 8)
                #9
                hotspot (578,260,44,74) action Function(handleBetPickVar, "9") #SetVariable("betPickVar", 9)
                #10
                hotspot (629,417,44,74) action Function(handleBetPickVar, "10") #SetVariable("betPickVar", 10)
                #11
                hotspot (629,339,44,74) action Function(handleBetPickVar, "11") #SetVariable("betPickVar", 11)
                #12
                hotspot (629,260,44,74) action Function(handleBetPickVar, "12") #SetVariable("betPickVar", 12)
                #13
                hotspot (676,417,44,74) action Function(handleBetPickVar, "13") #SetVariable("betPickVar", 13)
                #14
                hotspot (676,339,44,74) action Function(handleBetPickVar, "14") #SetVariable("betPickVar", 14)
                #15
                hotspot (676,260,44,74) action Function(handleBetPickVar, "15") #SetVariable("betPickVar", 15)
                #16
                hotspot (726,417,44,74) action Function(handleBetPickVar, "16") #SetVariable("betPickVar", 16)
                #17
                hotspot (726,339,44,74) action Function(handleBetPickVar, "17") #SetVariable("betPickVar", 17)
                #18
                hotspot (726,260,44,74) action Function(handleBetPickVar, "18") #SetVariable("betPickVar", 18)
                #19
                hotspot (773,417,44,74) action Function(handleBetPickVar, "19") #SetVariable("betPickVar", 19)
                #20
                hotspot (773,339,44,74) action Function(handleBetPickVar, "20") #SetVariable("betPickVar", 20)
                #21
                hotspot (773,260,44,74) action Function(handleBetPickVar, "21") #SetVariable("betPickVar", 21)
                #22
                hotspot (822,417,44,74) action Function(handleBetPickVar, "22") #SetVariable("betPickVar", 22)
                #23
                hotspot (822,339,44,74) action Function(handleBetPickVar, "23") #SetVariable("betPickVar", 23)
                #24
                hotspot (822,260,44,74) action Function(handleBetPickVar, "24") #SetVariable("betPickVar", 24)
                #25
                hotspot (872,417,44,74) action Function(handleBetPickVar, "25") #SetVariable("betPickVar", 25)
                #26
                hotspot (872,339,44,74) action Function(handleBetPickVar, "26") #SetVariable("betPickVar", 26)
                #27
                hotspot (872,260,44,74) action Function(handleBetPickVar, "27") #SetVariable("betPickVar", 27)
                #28
                hotspot (920,417,44,74) action Function(handleBetPickVar, "28") #SetVariable("betPickVar", 28)
                #29
                hotspot (920,339,44,74) action Function(handleBetPickVar, "29") #SetVariable("betPickVar", 29)
                #30
                hotspot (920,260,44,74) action Function(handleBetPickVar, "30") #SetVariable("betPickVar", 30)
                #31
                hotspot (969,417,44,74) action Function(handleBetPickVar, "31") #SetVariable("betPickVar", 31)
                #32
                hotspot (969,339,44,74) action Function(handleBetPickVar, "32") #SetVariable("betPickVar", 32)
                #33
                hotspot (969,260,44,74) action Function(handleBetPickVar, "33") #SetVariable("betPickVar", 33)
                #34
                hotspot (1019,417,44,74) action Function(handleBetPickVar, "34") #SetVariable("betPickVar", 34)
                #35
                hotspot (1019,339,44,74) action Function(handleBetPickVar, "35") #SetVariable("betPickVar", 35)
                #36
                hotspot (1019,260,44,74) action Function(handleBetPickVar, "36") #SetVariable("betPickVar", 36)
            if betType == "Dozen":
                # 1-12
                hotspot (479,495,193,54) action Function(handleBetPickVarDozen, "1")
                # 13-24
                hotspot (675,495,193,54) action Function(handleBetPickVarDozen, "2")
                # 25-36S
                hotspot (870,495,193,54) action Function(handleBetPickVarDozen, "3")

    vbox xpos 0.75 ypos 0.08:
        hbox:

            imagebutton at inv_eff:
                idle "rltBetChip100"
                selected select100
                if not rouletteRolled:
                    action Function(rouletteBetPick, "100")
                else:
                    action NullAction()

            imagebutton at inv_eff:
                idle "rltBetChip500"
                selected select500
                if not rouletteRolled:
                    action Function(rouletteBetPick, "500")
                else:
                    action NullAction()

            imagebutton at inv_eff:
                idle "rltBetChip1000"
                selected select1000
                if not rouletteRolled:
                    action Function(rouletteBetPick, "1000")
                else:
                    action NullAction()

    hbox:
        xalign 0.68
        yalign 0.045
        imagebutton at rotation_Left2Right:
            idle "roulettePlay"
            action [ Hide("betRoulette", transition=Dissolve(1.0)), Jump("gameTypeErrorCheck") ]
            hovered tt.Action("Roll ball!")
            alt "Roll ball!"
    fixed fit_first True pos (0.28,0.13):
        text _("Game type: [betType]\nYou bet on: [playerPiked]") color "#E60000" outlines [(1.1, "#000000", 0, 0)]
#        text "bet type: [betType], bet: [playerPiked] / roll: [theRoll], [theRollColor_text], [theRollOddOrEven_text]" outlines [(1.1, "#000000", 0, 0)]

    fixed fit_first True pos (0.16,0.65) anchor (0.5,0.5):
        showif rouletteRolled:
            add "rouletteWheel" at wheel_rot
    fixed fit_first True pos (0.16,0.65) anchor (0.5,0.5):
        showif rouletteRolled:
            add "rouletteBall" at ball_rot
    if rouletteRolled:
        timer 10 action [ Hide("betRoulette", transition=Dissolve(1.0)), Jump("lblCheckRoll") ]
    else:
        text tt.value xpos 0.628 ypos 0.085 color "#4118fa" outlines [(1.1, "#000000", 0, 0)] #4118fa

#### Labels
label test:
    "[betPickVar]"
    call screen betRoulette with Dissolve(2.0)

label gameTypeErrorCheck:

    $ betError = len(betPickVar)

    if betAmmount == 0:
        scene bg rouletteStart
        with Dissolve(1.5)
        RLT_dealer "Error: You haven't bet any amount of money.{w=3.0}{nw}" with Dissolve(2.0)
        call screen betRoulette with Dissolve(2.0)
    else:
        if betType == "Straight":
            if betError == 0 or betError > 1:
                scene bg rouletteStart
                with Dissolve(1.5)
                RLT_dealer "Error: With the Straight betting game you can pick any roulette number. Please supply a list of one number.{w=3.0}{nw}" with Dissolve(2.0)
                call screen betRoulette with Dissolve(2.0)
            else:
                $ rouletteRolled = True
                jump call_rotate
        elif betType == "Split":
            if betError == 1 or betError > 2:
                scene bg rouletteStart
                with Dissolve(1.5)
                RLT_dealer "Error: With the Split betting game you can pick any 2 (two) roulette numbers. Please supply a list of two different numbers.{w=3.0}{nw}" with Dissolve(2.0)
                call screen betRoulette with Dissolve(2.0)
            else:
                $ rouletteRolled = True
                jump call_rotate
        elif betType == "Street":
            if betError <= 2 or betError > 3:
                scene bg rouletteStart
                with Dissolve(1.5)
                RLT_dealer "Error: With the Street betting game you can pick any 3 (three) roulette numbers. Please supply a list of three different numbers.{w=3.0}{nw}" with Dissolve(2.0)
                call screen betRoulette with Dissolve(2.0)
            else:
                $ rouletteRolled = True
                jump call_rotate
        elif betType == "Corner":
            if betError <= 3 or betError > 4:
                scene bg rouletteStart
                with Dissolve(1.5)
                RLT_dealer "Error: With the Corner betting game you can pick any 4 (four) roulette numbers. Please supply a list of four different numbers.{w=3.0}{nw}" with Dissolve(2.0)
                call screen betRoulette with Dissolve(2.0)
            else:
                $ rouletteRolled = True
                jump call_rotate
        elif betType == "Penta":
            if betError <= 4 or betError > 5:
                scene bg rouletteStart
                with Dissolve(1.5)
                RLT_dealer "Error: With the Penta betting game you can pick any 5 (five) roulette numbers. Please supply a list of 5 different numbers.{w=3.0}{nw}" with Dissolve(2.0)
                call screen betRoulette with Dissolve(2.0)
            else:
                $ rouletteRolled = True
                jump call_rotate
        elif betType == "Line":
            if betError <= 5 or betError > 6:
                scene bg rouletteStart
                with Dissolve(1.5)
                RLT_dealer "Error: With the Line betting game you can pick any 6 (six) roulette numbers. Please supply a list of six different numbers.{w=3.0}{nw}" with Dissolve(2.0)
                call screen betRoulette with Dissolve(2.0)
            else:
                $ rouletteRolled = True
                jump call_rotate
        elif betType == "Dozen":
            if betError <= 11 or betError > 12:
                scene bg rouletteStart
                with Dissolve(1.5)
                RLT_dealer "Error: With the Dozen betting game you can pick any 12 (twelve) roulette numbers. Please supply a list of 12 different numbers.{w=3.0}{nw}" with Dissolve(2.0)
                call screen betRoulette with Dissolve(2.0)
            else:
                $ rouletteRolled = True
                jump call_rotate
        elif betType == "Color":
            if betPickVar:
                if str(betPickVar[0]) not in listRedBlack:
                    scene bg rouletteStart
                    with Dissolve(1.5)
                    RLT_dealer "Error: You have picked an incorrect color. Acceptable colors are {outlinecolor=#ffffff}{color=#FF0000}Red{/color}{/outlinecolor} and {outlinecolor=#ffffff}{color=#000000}Black{/color}{/outlinecolor}.{w=3.0}{nw}" with Dissolve(2.0)
                    call screen betRoulette with Dissolve(2.0)
                else:
                    $ rouletteRolled = True
                    jump call_rotate
            else:
                scene bg rouletteStart
                with Dissolve(1.5)
                RLT_dealer "Error: You have picked an incorrect color. Acceptable colors are {outlinecolor=#ffffff}{color=#FF0000}Red{/color}{/outlinecolor} and {outlinecolor=#ffffff}{color=#000000}Black{/color}{/outlinecolor}.{w=3.0}{nw}" with Dissolve(2.0)
                call screen betRoulette with Dissolve(2.0)

        elif betType == "EvenOdd":
            if betPickVar:
                if str(betPickVar[0]) not in listOddEven:
                    scene bg rouletteStart
                    with Dissolve(1.5)
                    RLT_dealer "Error: You have picked an incorrect bet. Acceptable bets are {outlinecolor=#ffffff}{color=#00008B}Odd{/color}{/outlinecolor} or {outlinecolor=#ffffff}{color=#00008B}Even{/color}{/outlinecolor}.{w=3.0}{nw}" with Dissolve(2.0)
                    call screen betRoulette with Dissolve(2.0)
                else:
                    $ rouletteRolled = True
                    jump call_rotate
            else:
                scene bg rouletteStart
                with Dissolve(1.5)
                RLT_dealer "Error: You have picked an incorrect bet. Acceptable bets are {outlinecolor=#ffffff}{color=#00008B}Odd{/color}{/outlinecolor} or {outlinecolor=#ffffff}{color=#00008B}Even{/color}{/outlinecolor}.{w=3.0}{nw}" with Dissolve(2.0)
                call screen betRoulette with Dissolve(2.0)


label call_rotate:

    scene bg rouletteBallRoll
    with Dissolve(1.5)
    RLT_dealer "Let's roll the ball!{w=2.0}{nw}" with Dissolve(2.0)

    $ playRoll()

    $ checkRoll()

    call screen betRoulette with Dissolve(2.5)

label lblCheckRoll:

    $ playerPiked = ', '.join(betPickVar)

    $ money -= betAmmount

    $ select100 = False
    $ select500 = False
    $ select1000 = False

    scene bg rouletteStart
    with Dissolve(1.5)

    RLT_dealer "You bet the ball would land on [playerPiked]{w=3.0}{nw}" with Dissolve(2.0)
    if betType == "Straight":
        if theRoll == int(betPickVar[0]):
            $ rouletteRolled = False
            $ payout = 35 * betAmmount
            $ money += payout
            $ renpy.block_rollback ()
            RLT_dealer "You win! The number that rolled is [theRoll] and it's [theRollOddOrEven_text], the color is [theRollColor_text]!{w=3.0}{nw}" with Dissolve(2.0)
            RLT_dealer "The payout is 35 to 1, so you won $[payout]!{w=3.0}{nw}" with Dissolve(2.0)
            call screen startRoulette with Dissolve(2.0)
        else:
            $ renpy.block_rollback ()
            RLT_dealer "You lose! The number that rolled is [theRoll] and it's [theRollOddOrEven_text], the color is [theRollColor_text]!{w=3.0}{nw}" with Dissolve(2.0)
            $ rouletteRolled = False
            call screen startRoulette with Dissolve(2.0)
    elif betType == "Split":
        if theRoll == int(betPickVar[0]) or theRoll == int(betPickVar[1]):
            $ rouletteRolled = False
            $ payout = 17 * betAmmount
            $ money += payout
            $ renpy.block_rollback ()
            RLT_dealer "You win! The number that rolled is [theRoll] and it's [theRollOddOrEven_text], the color is [theRollColor_text]!{w=3.0}{nw}" with Dissolve(2.0)
            RLT_dealer "The payout is 17 to 1, so you won $[payout]!{w=3.0}{nw}" with Dissolve(2.0)
            call screen startRoulette with Dissolve(2.0)
        else:
            $ renpy.block_rollback ()
            RLT_dealer "You lose! The number that rolled is [theRoll] and it's [theRollOddOrEven_text], the color is [theRollColor_text]!{w=3.0}{nw}" with Dissolve(2.0)
            $ rouletteRolled = False
            call screen startRoulette with Dissolve(2.0)
    elif betType == "Street":
        if theRoll == int(betPickVar[0]) or theRoll == int(betPickVar[1]) or theRoll == int(betPickVar[2]):
            $ rouletteRolled = False
            $ payout = 11 * betAmmount
            $ money += payout
            $ renpy.block_rollback ()
            RLT_dealer "You win! The number that rolled is [theRoll] and it's [theRollOddOrEven_text], the color is [theRollColor_text]!{w=3.0}{nw}" with Dissolve(2.0)
            RLT_dealer "The payout is 11 to 1, so you won $[payout]!{w=3.0}{nw}" with Dissolve(2.0)
            call screen startRoulette with Dissolve(2.0)
        else:
            $ renpy.block_rollback ()
            RLT_dealer "You lose! The number that rolled is [theRoll] and it's [theRollOddOrEven_text], the color is [theRollColor_text]!{w=3.0}{nw}" with Dissolve(2.0)
            $ rouletteRolled = False
            call screen startRoulette with Dissolve(2.0)
    elif betType == "Corner":
        if theRoll == int(betPickVar[0]) or theRoll == int(betPickVar[1]) or theRoll == int(betPickVar[2]) or theRoll == int(betPickVar[3]):
            $ rouletteRolled = False
            $ payout = 8 * betAmmount
            $ money += payout
            $ renpy.block_rollback ()
            RLT_dealer "You win! The number that rolled is [theRoll] and it's [theRollOddOrEven_text], the color is [theRollColor_text]!{w=3.0}{nw}" with Dissolve(2.0)
            RLT_dealer "The payout is 8 to 1, so you won $[payout]!{w=3.0}{nw}" with Dissolve(2.0)
            call screen startRoulette with Dissolve(2.0)
        else:
            $ renpy.block_rollback ()
            RLT_dealer "You lose! The number that rolled is [theRoll] and it's [theRollOddOrEven_text], the color is [theRollColor_text]!{w=3.0}{nw}" with Dissolve(2.0)
            $ rouletteRolled = False
            call screen startRoulette with Dissolve(2.0)
    elif betType == "Penta":
        if theRoll == int(betPickVar[0]) or theRoll == int(betPickVar[1]) or theRoll == int(betPickVar[2]) or theRoll == int(betPickVar[3]) or theRoll == int(betPickVar[4]):
            $ rouletteRolled = False
            $ payout = 6 * betAmmount
            $ money += payout
            $ renpy.block_rollback ()
            RLT_dealer "You win! The number that rolled is [theRoll] and it's [theRollOddOrEven_text], the color is [theRollColor_text]!{w=3.0}{nw}" with Dissolve(2.0)
            RLT_dealer "The payout is 6 to 1, so you won $[payout]!{w=3.0}{nw}"
            call screen startRoulette with Dissolve(2.0)
        else:
            $ renpy.block_rollback ()
            RLT_dealer "You lose! The number that rolled is [theRoll] and it's [theRollOddOrEven_text], the color is [theRollColor_text]!{w=3.0}{nw}" with Dissolve(2.0)
            $ rouletteRolled = False
            call screen startRoulette with Dissolve(2.0)
    elif betType == "Line":
        if theRoll == int(betPickVar[0]) or theRoll == int(betPickVar[1]) or theRoll == int(betPickVar[2]) or theRoll == int(betPickVar[3]) or theRoll == int(betPickVar[4]) or theRoll == int(betPickVar[5]):
            $ rouletteRolled = False
            $ payout = 5 * betAmmount
            $ money += payout
            $ renpy.block_rollback ()
            RLT_dealer "You win! The number that rolled is [theRoll] and it's [theRollOddOrEven_text], the color is [theRollColor_text]!{w=3.0}{nw}" with Dissolve(2.0)
            RLT_dealer "The payout is 5 to 1, so you won $[payout]!{w=3.0}{nw}"
            call screen startRoulette with Dissolve(2.0)
        else:
            $ renpy.block_rollback ()
            RLT_dealer "You lose! The number that rolled is [theRoll] and it's [theRollOddOrEven_text], the color is [theRollColor_text]!{w=3.0}{nw}" with Dissolve(2.0)
            $ rouletteRolled = False
            call screen startRoulette with Dissolve(2.0)
    elif betType == "Dozen":
        if theRoll == int(betPickVar[0]) or theRoll == int(betPickVar[1]) or theRoll == int(betPickVar[2]) or theRoll == int(betPickVar[3]) or theRoll == int(betPickVar[4]) or theRoll == int(betPickVar[5]) or theRoll == int(betPickVar[6]) or theRoll == int(betPickVar[7]) or theRoll == int(betPickVar[8]) or theRoll == int(betPickVar[9]) or theRoll == int(betPickVar[10]) or theRoll == int(betPickVar[11]):
            $ rouletteRolled = False
            $ payout = 2 * betAmmount
            $ money += payout
            $ renpy.block_rollback ()
            RLT_dealer "You win! The number that rolled is [theRoll] and it's [theRollOddOrEven_text], the color is [theRollColor_text]!{w=3.0}{nw}" with Dissolve(2.0)
            RLT_dealer "The payout is 2 to 1, so you won $[payout]!{w=3.0}{nw}" with Dissolve(2.0)
            call screen startRoulette with Dissolve(2.0)
        else:
            $ renpy.block_rollback ()
            RLT_dealer "You lose! The number that rolled is [theRoll] and it's [theRollOddOrEven_text], the color is [theRollColor_text]!{w=3.0}{nw}" with Dissolve(2.0)
            $ rouletteRolled = False
            call screen startRoulette with Dissolve(2.0)
    elif betType == "Color":
        if theRollColor in betPickVar:
            $ rouletteRolled = False
            $ payout = 1 * betAmmount
            $ money += payout
            $ renpy.block_rollback ()
            RLT_dealer "You win! The number that rolled is [theRoll] and it's [theRollOddOrEven_text], the color is [theRollColor_text]!{w=3.0}{nw}" with Dissolve(2.0)
            RLT_dealer "The payout is 1 to 1, so you won $[payout]!{w=3.0}{nw}" with Dissolve(2.0)
            call screen startRoulette with Dissolve(2.0)
        else:
            $ renpy.block_rollback ()
            RLT_dealer "You lose! The number that rolled is [theRoll] and it's [theRollOddOrEven_text], the color is [theRollColor_text]!{w=3.0}{nw}" with Dissolve(2.0)
            $ rouletteRolled = False
            call screen startRoulette with Dissolve(2.0)
    elif betType == "EvenOdd":
        if theRollOddOrEven in betPickVar:
            $ rouletteRolled = False
            $ payout = 1 * betAmmount
            $ money += payout
            $ renpy.block_rollback ()
            RLT_dealer "You win! The number that rolled is [theRoll] and it's [theRollOddOrEven_text], the color is [theRollColor_text]!{w=3.0}{nw}" with Dissolve(2.0)
            RLT_dealer "The payout is 1 to 1, so you won $[payout]!{w=3.0}{nw}" with Dissolve(2.0)
            call screen startRoulette with Dissolve(2.0)
        else:
            $ renpy.block_rollback ()
            RLT_dealer "You lose! The number that rolled is [theRoll] and it's [theRollOddOrEven_text], the color is [theRollColor_text]!{w=3.0}{nw}" with Dissolve(2.0)
            $ rouletteRolled = False
            call screen startRoulette with Dissolve(2.0)
