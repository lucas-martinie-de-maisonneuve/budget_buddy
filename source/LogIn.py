import pygame
from pygame_manager.Screen import Screen
from pygame_manager.Element import Element

class LogIn(Element, Screen): 
    def __init__(self): 
        Element.__init__(self)
        Screen.__init__(self)
        pygame.init()   


    def hover_sign(self):
        self.sign = (pygame.Rect(967, 594, 45, 13))    
        if self.is_mouse_over_button(self.sign):
            self.text_center(self.font1, 17, "Sign Up", self.black, self.W//2+220, 600)          
        else:
            self.text_center(self.font1, 15, "Sign Up", self.white, self.W//2+220, 600)

    def gui_home(self): 
        self.screen_color(self.white)

        # self.img_background("background", 500, 350, 1200, 700, "LogIn/login3")

        # Rect principal
        self.rect_full(self.green3, self.W//2+220, 355, 400, 580, 5)
        self.rect_border(self.green3, self.W//2+220, 355, 400, 580, 2, 5)
        
        self.button_hover("Email", self.W//2+220, 250, 350, 50, self.green2, self.green, self.green2, self.green, "Email", self.font1, self.white,15, 1, 5)

        self.button_hover("Password", self.W//2+220, 320, 350, 50, self.green2, self.green, self.green2, self.green,"Password", self.font1, self.white, 15, 1, 5)

        # Lines
        pygame.draw.line(self.Window, self.green, (520, 575), (919, 575), 1)

        self.hover_sign()

 
      


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
    