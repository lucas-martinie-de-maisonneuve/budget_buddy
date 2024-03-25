import pygame

from source.pygame_manager.Screen import Screen
from source.pygame_manager.Element import Element

class Home(Screen, Element): 
    def __init__(self): 
        Element.__init__(self)
        Screen.__init__(self)
        pygame.init()
   
    
    def gui_home(self): 
        self.screen_color(self.white)

        # Rect principal
        self.rect_full(self.grey1, self.W//2, 355, 400, 580, 5)
        self.rect_border(self.grey2, self.W//2, 355, 400, 580, 2, 5)

    def home_run(self):
        home_running = True
        while home_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    home_running = False

            self.gui_home()
            self.update()
h = Home()
h.home_run()
    