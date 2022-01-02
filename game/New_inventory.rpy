
####################################################################################################################################################
### Powerd by D.S.-sama ############################################################################################################################
####################################################################################################################################################
####################################################################################################################################################

define Gversions_allowed_patreon = [ "", "_patreon" ]

####################################################################################################################################################
### Inventory variable
####################################################################################################################################################

####################################################################################################################################################
### Inventory pythons

init -1 python:

    inv_show = False

    config.underlay.append(
        renpy.Keymap(
            i = lambda: renpy.run(
                Show("inventory_screen")
            ) ) )

init python:

    import renpy.store as store
    import renpy.exports as renpy # we need this so Ren'Py properly handles rollback with classes
    from operator import attrgetter # we need this for sorting items

    inv_page = 0 # initial page of the inventory screen
    item = None
    class NewPlayer(renpy.store.object):
        def __init__(self, name, consumable=None, permanent=None, accessories=None, book=None, outfit=None, out_select=None):
            self.name=name
            self.consumable=consumable
            self.permanent=permanent
            self.accessories=accessories
            self.book=book
            self.outfit=outfit
            self.out_select=out_select
    player = NewPlayer("Ryan")

    class NewItem(store.object):
        def __init__(self, name, consumable=False, permanent=False, accessories=False, book=False, outfit=False, image="", out_select=False, amount=0, cost=0):
            self.selected=False
            self.name = name
            self.image=image # image file to use for this item
            self.cost=cost # how much does it cost in shops?
            self.consumable=consumable # is this item consumable?
            self.permanent=permanent # is this item permanent?
            self.accessories=accessories # is this item accessories?
            self.book=book # is this item a book?
            self.outfit=outfit # is this item an outfit?
            self.out_select=out_select
            self.amount=amount

        @property
        def sorted_string(self):
            return "{}_{}".format(
                3 if self.permanent else 2 if self.consumable else 1,
                self.name )

        def use(self):
            if player.outfit == item.outfit:
                if self.out_select:
                    player.outfit=self.outfit
                    if self.outfit:
                        self.selected=not self.selected
                        if item.selected:
                            inventory.drop(item)

    class NewInventory(store.object):
        def __init__(self, money=0):
            self.money = money
            self.items = []
            self.items_amount = {}

        def add(self, item, amount=1):
            amount = amount if item.consumable else 1
            if item not in self.items:
                self.items.append(item)
                self.items_amount[item.name] = 0
            self.items_amount[item.name] += amount

#        def add(self, item):
#            if item.consumable:
#                if item not in self.items:
#                    self.items.append(item)
#                    self.items_amount[item.name] = 1
#                else:
#                    self.items_amount[item.name] += 1
#            else:
#                if item not in self.items:
#                    self.items.append(item)
#                    self.items_amount[item.name] = 1

        def add_outf_amount(self, item):
            if item.outfit:
                self.items_amount[item.name] += 1

        def test_add(self, item):
            self.items.append(item)

        def test_drop(self, item):
            self.items.remove(item)

        def drop(self, item):
            if item.name in self.items_amount:
                self.items_amount[item.name] -= 1
                if self.items_amount[item.name] <= 0:
                    del(self.items_amount[item.name])
                    self.items.remove(item)

        def drop_outfit_inv(self, item):
            if item.name in self.items_amount:
                self.items.remove(item)

        def buy(self, item):
            if item not in self.items:
                if self.money >= item.cost:
                    self.money -= item.cost
                    self.items.append(item)
                    self.items_amount[item.name] = 1
                    return True
                else:
                    return False
            else:
                if self.money >= item.cost:
                    self.money -= item.cost
                    self.items_amount[item.name] += 1
                    return True
                else:
                    return False

        def earn(self, amount):
            self.money += amount

        def has_item(self, item):
            if item in self.items:
                return True
            else:
                return False

        def inv_amount(self, item): # it will show the amount of an item
            #if not item.outfit:
            if item.name in self.items_amount:
                return inventory.items_amount[item.name]
            else:
                return 0
            #else:
            #    return inventory.items_amount[item.name]

        def count(item):
            return inventory.items.count(item)

    def item_accessories():
        item.accessories

    def item_use():
        item.use()

    def sorted_string():
        item.sorted_string

    def inv_items_amount():
        inventory.items_amount[item.name]

    inventory = NewInventory()
    #Tooltips:
    style.tips_top = Style(style.default)
    #style.title.font="gui/arial.ttf"
    style.tips_top.size = 20
    style.tips_top.color = "fff"
    style.tips_top.outlines = [(3, "6b7eef", 0,0)]
    style.tips_top.kerning = 5

    style.tips_bottom = Style(style.default)
    style.tips_bottom.size = 16
    style.tips_bottom.color = "fff"
    style.tips_bottom.outlines = [(0, "6b7eef", 1, 1), (0, "6b7eef", 2, 2)]
    style.tips_bottom.kerning = 2

    style.inventory_name = Style(style.default)
    style.inventory_name.size = 40
    style.inventory_name.bold = True
    style.inventory_name.color = "fff"
    style.inventory_name.outlines = [(0, "6b7eef", 1, 1), (0, "6b7eef", 2, 2)]
    style.inventory_name.kerning = 3

    style.money_show = Style(style.default)
    style.money_show.size = 25
    style.money_show.color = "fff"
    style.money_show.outlines = [(0, "6b7eef", 1, 1), (0, "6b7eef", 2, 2)]
    style.money_show.kerning = 2

    style.button.background = Frame("New_inventory/frame.png",25,25)
    style.button.yminimum = 52
    style.button.xminimum = 52
    style.button_text.color = "000"

    showitems = True #turn True to debug the inventory

####################################################################################################################################################
### Inventory init

init:

    transform inv_eff: # too lazy to make another version of each item, we just use ATL to make hovered items super bright
        zoom 0.5 xanchor 0.5 yanchor 0.5
        on idle:
            linear 0.2 alpha 2.5
        on hover:
            linear 0.2 alpha 0.5

    image information = Text("INFORMATION!", style="tips_top")
    #Tooltips-inventory:
    image tooltip_inventory_Cosplay_Outfit_Space_1=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("Lauren's first cosplay outfit, you can sell it online to make money."), style="tips_bottom"))
    image tooltip_inventory_Cosplay_Outfit_Space_2=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("Mandy's first cosplay outfit, you can sell it online to make money."), style="tips_bottom"))
    if persistent.patreonsafe:
        image tooltip_inventory_Jacky_bikini_1=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("Expensive, but the most stylish swimsuit for my mom."), style="tips_bottom"))
    else:
        image tooltip_inventory_Jacky_bikini_1=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("Expensive, but the most stylish swimsuit for my mom."), style="tips_bottom"))
    image tooltip_inventory_chocolate=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("Generic milk chocolate bar."), style="tips_bottom"))
    image tooltip_inventory_giftcard=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("hardnLong.com $25 Gift Card(s)."), style="tips_bottom"))
    image tooltip_inventory_flowers=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("Flowers for my ladies."), style="tips_bottom"))
    image tooltip_inventory_melatonin=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("Melatonin, the strongest over the counter sleep aid that I can buy. It's all natural... non addictive..."), style="tips_bottom"))
    image tooltip_inventory_spycam=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("Webcam(s), I can use this item to spy on the girls."), style="tips_bottom"))
    image tooltip_inventory_ball_gag=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("Ball Gag, a device used in sexual bondage and BDSM roleplay. Let's see how I can use it!"), style="tips_bottom"))
    image tooltip_inventory_camera=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("The best DSLR camera I can afford for now."), style="tips_bottom"))
    image tooltip_inventory_green_screen=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("A green screen will make us look more professional."), style="tips_bottom"))
    image tooltip_inventory_pro_lights=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("With this lights the photos will look better and we'll get more likes."), style="tips_bottom"))
    image tooltip_inventory_camera_accessories_1=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("This items helps you get more likes from images."), style="tips_bottom"))
    image tooltip_inventory_camera_accessories_2=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("This items helps you get more likes from images."), style="tips_bottom"))
    image tooltip_inventory_camera_accessories_3=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("This items helps you get more likes from images."), style="tips_bottom"))
    image tooltip_inventory_camera_accessories_4=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("This items helps you get more likes from images."), style="tips_bottom"))
    image tooltip_inventory_camera_accessories_5=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("This items helps you get more likes from images."), style="tips_bottom"))
    image tooltip_inventory_camera_accessories_6=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("This items is needed to make videos."), style="tips_bottom"))
    image tooltip_inventory_camera_accessories_7=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("This items helps you get more likes from videos."), style="tips_bottom"))
    image tooltip_inventory_camera_accessories_8=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("This items helps you get more likes from videos."), style="tips_bottom"))
    image tooltip_inventory_ph_book1=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("A childrens book that turned out to be full of hidden sexual themes and innuendos... Maybe it is my kind of book!"), style="tips_bottom"))
    image tooltip_inventory_ph_book2=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("Second book in the Perry Hotter Series."), style="tips_bottom"))
    image tooltip_inventory_ph_book3=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text(_("Third book in the Perry Hotter Series."), style="tips_bottom"))

####################################################################################################################################################
### Gallery screens
####################################################################################################################################################

screen inventory_screen():

    key "i" action [ Hide("inventory_screen"), Hide("gui_tooltip") ]

    add "bg Inventory" # the background
    modal True #prevent clicking on other stuff when inventory is shown

    textbutton _("Money:$[money]") text_style "money_show" xalign 0.525 yalign 0.12 action NullAction()

    textbutton _("INVENTORY") text_style "inventory_name" xalign 0.53 yalign 0.023 action NullAction()

    imagebutton auto "images/interface_images/close_button_%s.png" xpos 880 ypos 15 focus_mask True action [ Hide("inventory_screen"), Hide("gui_tooltip")]

    $ item_check = item_accessories

    $ x = 480 # coordinates of the top left item position
    $ y = 10
    $ i = 0
    #if item_check:
        #$ sorted_items = sorted(inventory.items, key = lambda x:"{}{}".format( attrgetter('permanent'), attrgetter('consumable') ), reverse=True)
    #else:
    $ sorted_items = sorted(inventory.items, key=attrgetter("sorted_string"), reverse=True) # we sort the items, so non-consumable items are listed first
    #$ sorted_items = sorted(inventory.items, key=attrgetter("permanent"), reverse=True) # we sort the items, so non-consumable items are listed first
    $ next_inv_page = inv_page + 1
    $ previous_inv_page = next_inv_page - 1
    if next_inv_page > int(len(inventory.items)/9):
        $ next_inv_page = 0
    for item in sorted_items:
        if i+1 <= (inv_page+1)*9 and i+1>inv_page*9:
            $ x += 177
            if i%3==0:
                $ y += 166
                $ x = 481
            $ amount = inventory.items_amount.get( item.name, 0 )
            #$ amount = inventory.items_amount[item.name]
            $ pic = item.image
            $ my_tooltip = "tooltip_inventory_" + pic.replace("images/interface_images/inventory_images/inv_", "").replace(".png", "") # we use tooltips to describe what the item does.
            if item.outfit:
                imagebutton idle pic hover pic xpos x ypos y action NullAction() hovered [ Play ("sound", "music/click.wav"), Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=645) ] unhovered [ Hide("gui_tooltip") ] at inv_eff
            else:
                imagebutton idle pic hover pic xpos x ypos y action NullAction() hovered [ Play ("sound", "music/click.wav"), Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=645)] unhovered [ Hide("gui_tooltip") ] at inv_eff#, Show("gui_tooltip_amount", my_picture=my_tooltip_amount, my_tt_ypos=645) ] at inv_eff
            text _("[amount]") xpos x+22 ypos y+20 style "inventory_name"
            #if player.outfit and (player.outfit == item.outfit): #indicate the selected item  #[Hide("gui_tooltip"), SetVariable("item", item), item_use]
            #    add "New_inventory/selected.png" xpos x ypos y anchor(.5,.5)
        $ i += 1
        if len(inventory.items) > 9:
            imagebutton auto "images/interface_images/Button_nextgal_%s.png" xpos .495 ypos .81 action [ SetVariable('inv_page', next_inv_page),
                Show("inventory_screen") ]
            if inv_page == 1:
                imagebutton auto "images/interface_images/Button_backgal_%s.png" xpos .445 ypos .81 action [ SetVariable('inv_page', 0),
                    Show("inventory_screen") ]
            else:
                imagebutton auto "images/interface_images/Button_backgal_%s.png" xpos .445 ypos .81 action [ SetVariable('inv_page', previous_inv_page),
                    Show("inventory_screen") ]

screen gui_tooltip (my_picture="", my_tt_xpos=58, my_tt_ypos=687):
    add my_picture xpos my_tt_xpos ypos my_tt_ypos

screen gui_tooltip_amount (my_picture="", my_tt_xpos=58, my_tt_ypos=687):
    add my_picture xpos my_tt_xpos ypos my_tt_ypos

####################################################################################################################################################
### After load label
####################################################################################################################################################

label after_load(): # If it exists, this label is called when a game is loaded. It can be use to fix data when the game is updated.
    #$ new_after_loads = [ k for k in renpy.get_all_labels() if k.startswith('after_load_') ]
    #while new_after_loads:
        #call expression new_after_loads[0]
        #$ new_after_loads = new_after_loads[1:]

    #$ all_after_loads = sorted(                                     #<== This sorts the after_loads labebels and loads them in revers
    #    [ k for k in renpy.get_all_labels()
    #      if k.startswith('after_load_') ], reverse=True )
    #while all_after_loads:
    #    call expression all_after_loads.pop()

    $ all_after_loads = sorted(                                     #<== This sorts the after_loads labebels and loads
        [ k for k in renpy.get_all_labels()
          if k.startswith('after_load_') ] )
    while all_after_loads:
        call expression all_after_loads.pop(0) from _call_expression

    $ _version = config.version

    return
