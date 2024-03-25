import pygame

from source.pygame_manager.Screen import Screen
from source.pygame_manager.Element import Element

class LogIn(Screen, Element): 
    def __init__(self): 
        Element.__init__(self)
        Screen.__init__(self)
        pygame.init()
   
    
    def gui_home(self): 
        self.screen_color(self.white)

        # Rect principal
        self.rect_full(self.grey1, self.W//2, 355, 400, 580, 5)
        self.rect_border(self.grey2, self.W//2, 355, 400, 580, 2, 5)

    def login_run(self):
        login_running = True
        while login_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    login_running = False

            self.gui_home()
            self.update()
h = LogIn()
h.login_run()
    