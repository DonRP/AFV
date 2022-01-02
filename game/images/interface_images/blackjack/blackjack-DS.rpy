
####################################################################################################################################################
### Powerd by D.S.-sama ############################################################################################################################
####################################################################################################################################################
####################################################################################################################################################

init python:
    def backChange(): #<== it works but crashez the game
#        # this changes the variable for the back of the cards
        if store.cards_back <= 5:
            store.cards_back += 1
        elif store.cards_back == 6:
            store.cards_back = 1

    def betPickBlackJack( target ):
        store.betSum = int(target)
        store.betWin = (store.betSum/2) + store.betSum
        store.money -= store.betSum
        renpy.hide_screen('betBlackJack')
        renpy.transition(Dissolve(1.5))
        renpy.call('startGameBJ')

    def exitBlackJack():
        # Resets the values and jumps to the wanted label
        store.betSum = 0
        store.betWin = 0
        store.computerPick = False
        store.playerEndPick = False
        store.new_game_bj = True
        store.computerScore = 0
        store.playerScore = 0
        renpy.hide_screen("confirm")
        renpy.hide_screen("betBlackJack")
        renpy.hide_screen("cards")
        renpy.transition(Dissolve(1.5))
        renpy.call("gamble_end")  #<== change with wath label you want to jump to

    def restartBlackJack():
        store.computerPick = False
        store.playerEndPick = False
        store.new_game_bj = True
        store.computerScore = 0
        store.playerScore = 0
        renpy.hide_screen("cards")
        renpy.hide_screen("confirm")
        renpy.show_screen("betBlackJack")
        renpy.transition(Dissolve(1.5))

    def shuffleCards():
        # Reset the value
        store.cards = []
        store.computerCards = []
        store.playerCards = []
        store.computerScore = 0
        store.playerScore = 0
        store.handCheck = ""

        # generate a full 52 cards packet.
        # Each value must be one letter, so "T" is for "10".
        for i in [ "A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2" ]:
            # _x represent the color, choose which one will be what color.
            store.cards.append( i + "_diamonds" )
            store.cards.append( i + "_clubs" )
            store.cards.append( i + "_hearts" )
            store.cards.append( i + "_spades" )
       # Shuffle the packet.
        renpy.random.shuffle( store.cards )

    # Pick the next card
    def pick( target ):
        if target == "player":
            # Pick the first available card
            playerCards.append( cards.pop( 0 ) )

            # Get its value
            value = playerCards[-1][0]

            # If it's a figure, the value is 10.
            # Technically "T" isn't a figure, but it have the same value.
            if value in [ "K", "Q", "J", "T" ]:
                store.playerScore += 10
            # If it's an as, the value is either 1
            elif value == "A" and playerScore >= 11:
                store.playerScore += 1
            # or 10
            elif value == "A" and playerScore < 11:
                store.playerScore += 11
            # Else just get the value from the /name/ of the card
            else:
                store.playerScore += int( value )
        elif target == "computer":
            computerCards.append( cards.pop( 0 ) )
            value = computerCards[-1][0]
            if value in [ "K", "Q", "J", "T" ]:
                store.computerScore += 10
            elif value == "A" and computerScore >= 11:
                store.computerScore += 1
            elif value == "A" and computerScore < 11:
                store.computerScore += 11
            else:
                store.computerScore += int( value )

#    def burst_check():
#        if computerScore > 21:
#            renpy.say("Dealer", "Dealer Bust!")
#            persistent.playerWin += 1
#            renpy.call("end_bj")
#        elif playerScore > 21:
#            renpy.say("Dealer", "You bust! You lost .")
#            persistent.computerWin += 1
#            renpy.call("end_bj")
#        else:
#            return None

#    def bj_check():
#        if computerScore == 21 and playerScore == 21:
#            renpy.say("Dealer", "Blackjack! The dealer also has blackjack, so it's a push!")
#            persistent.computerWin += 1
#            renpy.call("end_bj")
#        elif playerScore == 21 and computerScore != 21:
#            renpy.say("Dealer", "Blackjack! You won .")
#            persistent.playerWin += 1
#            renpy.call("end_bj")
#        elif computerScore == 21 and playerScore != 21:
#            renpy.say("Dealer", "Dealer has blackjack! You lose .")
#            persistent.computerWin += 1
#            renpy.call("end_bj")
#        else:
#            return None

#    def win_check():
#        if computerScore < playerScore:
#            renpy.say("Dealer", "You win")
#            persistent.playerWin += 1
#            renpy.call("end_bj")
#        elif playerScore < computerScore:
#            renpy.say("Dealer", "You loose")
#            persistent.computerWin += 1
#            renpy.call("end_bj")
#        elif playerScore == computerScore and playerScore != 21:
#            renpy.say("Dealer", "The dealer also has [computerScore], so it's a push")
#            persistent.computerWin += 1
#            renpy.call("end_bj")
#        else:
#            return None

    def handCheckFunction():
        # Checks the cards in your or computers hands
        if computerScore > 21 and computerPick:
            store.handCheck = "computer_bust"
            renpy.call("handCheckLabel")
        elif playerScore > 21:
            store.playerEndPick = True
            store.handCheck = "player_bust"
            renpy.call("handCheckLabel")
        elif computerScore == 21 and playerScore == 21:# and computerPick:
            store.computerPick = True
            store.handCheck = "player_BJ_push"
            renpy.call("handCheckLabel")
        elif playerScore == 21 and computerScore != 21:
            store.computerPick = True
            store.handCheck = "player_BJ"
            renpy.call("handCheckLabel")
        elif computerScore == 21 and playerScore != 21:
            store.handCheck = "computer_BJ"
            renpy.call("handCheckLabel")
        elif computerScore < playerScore and computerPick:
            store.handCheck = "player_win"
            renpy.call("handCheckLabel")
        elif playerScore < computerScore and computerPick:
            store.handCheck = "computer_win"
            renpy.call("handCheckLabel")
        elif playerScore == computerScore and playerScore != 21 and computerPick:
            store.handCheck = "computer_push"
            renpy.call("handCheckLabel")
        else:
            return None

# The variables
default cards = []
default computerCards = []
default playerCards = []
default computerScore = 0
default playerScore = 0
default persistent.computerWin = 0
default persistent.playerWin = 0
default new_game_bj = True
default computerPick = False
default playerEndPick = False
default second_card_value = 0
default handCheck = ""

default cards_back = 1

default betSum = 0
default betWin = 0

define BJ_dealer = Character(_("Dealer"), color="#000056", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])

init:
    # The image definitions for bg
    image bg blackjackBet = "images/interface_images/blackjack/BlackJack01.png"
    image bg blackjackDeal = "images/interface_images/blackjack/BlackJack02.png"
    image bg blackjackTable = "images/interface_images/blackjack/BlackJack03.png"

    image blackjackBet = "images/interface_images/blackjack/BlackJack01.png"
    image blackjackTable = "images/interface_images/blackjack/BlackJack03.png"

    image betChip100 = im.Scale("images/interface_images/blackjack/bet100_chip.png", 412, 412)
    image betChip500 = im.Scale("images/interface_images/blackjack/bet500_chip.png", 412, 412)
    image betChip1000 = im.Scale("images/interface_images/blackjack/bet1000_chip.png", 412, 412)

    # The images for the back of the cards
    image cardsBack = ConditionSwitch(
        "cards_back == 1", "images/interface_images/blackjack/cards/back_blue.png",
        "cards_back == 2", "images/interface_images/blackjack/cards/back_gray.png",
        "cards_back == 3", "images/interface_images/blackjack/cards/back_green.png",
        "cards_back == 4", "images/interface_images/blackjack/cards/back_purple.png",
        "cards_back == 5", "images/interface_images/blackjack/cards/back_red.png",
        "cards_back == 6", "images/interface_images/blackjack/cards/back_yellow.png"
        )

    image cardsBack_small = ConditionSwitch(
        "cards_back == 1", im.Scale("images/interface_images/blackjack/cards/back_blue.png", 33, 50),
        "cards_back == 2", im.Scale("images/interface_images/blackjack/cards/back_gray.png", 33, 50),
        "cards_back == 3", im.Scale("images/interface_images/blackjack/cards/back_green.png", 33, 50),
        "cards_back == 4", im.Scale("images/interface_images/blackjack/cards/back_purple.png", 33, 50),
        "cards_back == 5", im.Scale("images/interface_images/blackjack/cards/back_red.png", 33, 50),
        "cards_back == 6", im.Scale("images/interface_images/blackjack/cards/back_yellow.png", 33, 50)
        )

screen betBlackJack():

    add "blackjackBet"

    text _("Place your bets!") xpos 0.358 size 40 color "#E60000" outlines [(3, "#000", 0,0)]  #000056

    vbox xpos 0.35 ypos 0.62:
        hbox:
            imagebutton at inv_eff:
#                idle im.Scale("images/interface_images/blackjack/bet100.png", 512, 200) #<== It allows to use an image at a certain size
                idle "betChip100"
                if money >= 100:
                    action [ Confirm(_("Do you want to bet $100 and start the game?"), Function(betPickBlackJack, "100"), None) ]#, Hide("blackjackBet", transition=Dissolve(1.0)) ]
                else:
                    action [ ui.callsinnewcontext("noMoney") ]

            imagebutton at inv_eff:
#                idle im.Scale("images/interface_images/blackjack/bet500.png", 512, 200)
                idle "betChip500"
                if money >= 500:
                    action [ Confirm(_("Do you want to bet $500 and start the game?"), Function(betPickBlackJack, "500"), None) ]#, Hide("blackjackBet", transition=Dissolve(1.0)) ]
                else:
                    action [ ui.callsinnewcontext("noMoney") ]

            imagebutton at inv_eff:
#                idle im.Scale("images/interface_images/blackjack/bet1000.png", 512, 200)
                idle "betChip1000"
                if money >= 1000:
                    action [ Confirm(_("Do you want to bet $1000 and start the game?"), Function(betPickBlackJack, "1000"), None) ]#, Hide("blackjackBet", transition=Dissolve(1.0)) ]
                else:
                    action [ ui.callsinnewcontext("noMoney") ]

    vbox xpos 0.85 ypos 0.9:
        hbox:
            imagebutton at inv_eff:
                idle im.Scale("images/interface_images/blackjack/exit_bj.png", 512, 200)
                action Confirm(_("Do you want to leave the BlackJack game?"), Function(exitBlackJack), None)

screen cards():

    default tt = Tooltip("")

    add "blackjackTable"

    text _("Games won: [persistent.playerWin] / lost: [persistent.computerWin]") outlines [(3, "#000", 0,0)]

    imagebutton:
        xpos 0.96
        idle "cardsBack_small"
        action Function(backChange)

    vbox xpos 0.8 ypos 0.6:
        hbox:
            imagebutton:
                idle "images/interface_images/blackjack/hit.png"
                hover "images/interface_images/blackjack/hit_hover.png"
                if not playerEndPick:
                    action [ Function(pick, "player"), Function(handCheckFunction) ]
                hovered tt.Action("Hit")
                alt "Hit"

            imagebutton:
                idle "images/interface_images/blackjack/stand.png"
                hover "images/interface_images/blackjack/stand_hover.png"
                if not playerEndPick:
                    action [ SetVariable("computerPick", True), SetVariable("playerEndPick", True), Jump("dealerRound") ]
                hovered tt.Action("Stand")
                alt "Stand"
                at standHands

    text tt.value xpos 0.85 ypos 0.55

    vbox xpos 0.25 ypos 0.2:
        text _(If(not computerPick,
            "Dealers cards: [second_card_value]",
            "Dealers cards: [computerScore]")) outlines [(3, "#000", 0,0)]
        hbox at center:
            if not computerPick:
                # Displays the back image of the first card
                add "cardsBack" size (131, 200)
                # Displays the image of the second card
                add "images/interface_images/blackjack/cards/{}.png".format( computerCards[1] ) size (131, 200)
            else:
                # For all the cards picked by dealer
                for c in computerCards:
                    # Display the image of the card
                    add "images/interface_images/blackjack/cards/[c].png" size (131, 200)

    vbox xpos 0.01 ypos 0.6:
        text _("Player cards: [playerScore]") outlines [(3, "#000", 0,0)]
        hbox:
            # For all the cards picked by player
            for c in playerCards:
#                add im.Scale("images/interface_images/blackjack/cards/{}.png".format( c ), 163, 250)
                add "images/interface_images/blackjack/cards/[c].png" size (163, 250)

transform standHands:  # This deals with the transform for the 'Stand' image
    on hover:
        linear 0.2 rotate 10
        linear 0.1 rotate -10
        linear 0.2 rotate 10
        linear 0.1 rotate 0.0
    on idle:
        rotate 0.0

label startGameBJ:

    scene bg blackjackDeal
    with Dissolve(1.5)
    BJ_dealer "I'll start dealing the cards!{w=2.0}{nw}"
    $ shuffleCards()
    jump startFirstRound

label startFirstRound:

    scene bg blackjackTable
    with Dissolve(1.5)

    # Pick the first two cards
    if new_game_bj:
        $ new_game_bj = False
        $ pick( "player" )
        $ pick( "computer" )
        $ pick( "player" )
        $ pick( "computer" )
        if playerScore == 21:
            $ handCheck = "player_BJ"
            jump handCheckLabel

    # Finds the value of the second card in the computers hand
    python:
        store.second_card = computerCards[1]
        if second_card[0] in [ "K", "Q", "J", "T" ]:
            store.second_card_value = 10
        elif second_card[0] == "A":
            store.second_card_value = 11
        else:
            store.second_card_value = int( second_card[0] )

    call screen cards
    with Dissolve(1.5)
#    $renpy.pause()

label dealerRound:

    show screen cards #<== So that the screen doesn't disappear

    # It's a repeatable  action that adds new cards in the computers hands
    while computerScore <= 17 and computerPick:
        $ renpy.pause(1.5)
        $ pick( "computer" )

    $ renpy.pause(0.5)
    $ handCheckFunction()

label handCheckLabel:
    show screen cards
    $ renpy.pause(1.0)
    # It uses the 'handCheck' function to chose the necessary action
    if handCheck == "computer_bust": #_return
        hide screen cards
        with Dissolve(1.5)
        scene bg blackjackBet
        with Dissolve(1.5)
        $ renpy.block_rollback ()
        BJ_dealer "Dealer Bust, you won $[betWin]!{w=2.0}{nw}"
        $ handCheck = ""
        $ money += betWin
        $ persistent.playerWin += 1
        jump end_bj
    elif handCheck == "player_bust":
        hide screen cards
        with Dissolve(1.5)
        scene bg blackjackBet
        with Dissolve(1.5)
        $ renpy.block_rollback ()
        BJ_dealer "You bust! You lost $[betSum]!{w=2.0}{nw}"
        $ handCheck = ""
        $ persistent.computerWin += 1
        jump end_bj
    elif handCheck == "player_BJ_push":
        hide screen cards
        with Dissolve(1.5)
        scene bg blackjackBet
        with Dissolve(1.5)
        $ renpy.block_rollback ()
        BJ_dealer "Blackjack! The dealer also has blackjack, so it's a push! You get your $[betSum] back!{w=2.0}{nw}"
        $ handCheck = ""
        $ money += betSum
        jump end_bj
    elif handCheck == "player_BJ":
        hide screen cards
        with Dissolve(1.5)
        scene bg blackjackBet
        with Dissolve(1.5)
        $ renpy.block_rollback ()
        BJ_dealer "Blackjack! You won the game and $[betWin]!{w=2.0}{nw}"
        $ handCheck = ""
        $ money += betWin
        $ persistent.playerWin += 1
        jump end_bj
    elif handCheck == "computer_BJ":
        hide screen cards
        with Dissolve(1.5)
        scene bg blackjackBet
        with Dissolve(1.5)
        $ renpy.block_rollback ()
        BJ_dealer "Dealer has blackjack! You lose the game and $[betSum]!{w=2.0}{nw}"
        $ handCheck = ""
        $ persistent.computerWin += 1
        jump end_bj
    elif handCheck == "player_win":
        hide screen cards
        with Dissolve(1.5)
        scene bg blackjackBet
        with Dissolve(1.5)
        $ renpy.block_rollback ()
        BJ_dealer "You won the game and $[betWin]!{w=2.0}{nw}"
        $ handCheck = ""
        $ money += betWin
        $ persistent.playerWin += 1
        jump end_bj
    elif handCheck == "computer_win":
        hide screen cards
        with Dissolve(1.5)
        scene bg blackjackBet
        with Dissolve(1.5)
        $ renpy.block_rollback ()
        BJ_dealer "You lost the game and $[betSum]!{w=2.0}{nw}"
        $ handCheck = ""
        $ persistent.computerWin += 1
        jump end_bj
    elif handCheck == "computer_push":
        hide screen cards
        with Dissolve(1.5)
        scene bg blackjackBet
        with Dissolve(1.5)
        $ renpy.block_rollback ()
        BJ_dealer "The dealer also has [computerScore], so it's a push! You get your $[betSum] back!{w=2.0}{nw}"
        $ handCheck = ""
        $ money += betSum
        jump end_bj

label end_bj:

    scene bg blackjackBet
    with Dissolve(1.5)

    call screen confirm(message=_("Do you want to play again?"),
        yes_action=Function(restartBlackJack),
        no_action=Function(exitBlackJack))

label noMoney:

    scene bg blackjackBet
    with Dissolve(1.5)
    BJ_dealer "Sorry! You don't have enough money!{w=2.0}{nw}"

    return
