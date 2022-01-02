init python:

    class getMousePosition(renpy.Displayable):

        def __init__(self):
            renpy.Displayable.__init__(self)

        def event(self, ev, x, y, st):
            import pygame

            if ev.type == pygame.MOUSEMOTION: # Updates the position of the mouse every time the player moves it
                store.mousex = x
                store.mousey = y

        def render(self, width, height, st, at):
            return renpy.Render(1, 1)

    store.mousePosition= getMousePosition()

    def checkEvent():
        ui.add(mousePosition)
    config.overlay_functions.append(checkEvent) # This adds a 1*1 displayable on every screen