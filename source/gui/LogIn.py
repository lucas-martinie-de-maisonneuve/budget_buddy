import pygame
from source.pygame_manager.Screen import Screen
from source.pygame_manager.Element import Element
from source.Controller import Controller

class LogIn(Element, Screen, Controller): 
    def __init__(self): 
        Element.__init__(self)
        Screen.__init__(self)
        Controller.__init__(self)
      
    def hover_sign(self):
        self.sign = (pygame.Rect(self.W//2+192, 590, 55, 20)) 
        if self.is_mouse_over_button(self.sign):
            self.text_center(self.font4, 13, "Sign-in options", self.white, self.W//2+220, 480)          
        else:
            self.text_center(self.font4, 12, "Sign-in options", self.white, self.W//2+220, 500)

    def gui_home(self): 
        self.screen_color(self.white)

        # self.img_background("background", 500, 350, 1200, 700, "LogIn/login3")

        # Rect principal
        self.rect_full(self.green3, self.W//2+220, 355, 400, 580, 10)
        self.rect_border(self.green3, self.W//2+220, 355, 400, 580, 2, 10)
        
        self.input_email_rect = self.button_hover("Email", self.W//2+220, 250, 350, 50, self.green2, self.green, self.green2, self.green, self.input_email, self.font1, self.white,15, 1, 5)

        self.input_password_rect = self.button_hover("Password", self.W//2+220, 320, 350, 50, self.green2, self.green, self.green2, self.green, self.input_password, self.font1, self.white, 15, 1, 5)

        self.login_rect = self.button_hover("Login", self.W//2+220, 390, 350, 50, self.green, self.green, self.green, self.green,"Log In", self.font1, self.white, 19, 1, 5) 
        

        # Lines
        self.text_center(self.font1, 15, "No account ? Create one!", self.white, self.W//2+220, 450)
        pygame.draw.line(self.Window, self.green, (545, 450), (625, 450), 1) 
        pygame.draw.line(self.Window, self.green, (815, 450), (895, 450), 1)
        pygame.draw.line(self.Window, self.green, (520, 575), (919, 575), 1)

        self.hover_sign()
      
    def login_run(self):
        login_running = True
        while login_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    login_running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_email_rect.collidepoint(event.pos): 
                        self.input_email = ""
                        self.entry = 1
                    elif self.input_password_rect.collidepoint(event.pos):
                        self.input_password = "" 
                        self.entry = 2

                    elif self.login_rect.collidepoint(event.pos):
                        pass

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if self.entry == 1: 
                            self.input_email = self.input_email[:-1]
                        elif self.entry == 2: 
                            self.input_password = self.input_password[:-1]
                    else:
                        if self.entry == 1: 

                            if event.unicode.islower():                    
                                self.input_email = self.input_email + event.unicode             
                        
                        elif self.entry == 2: 
                            self.input_password = self.input_password + event.unicode     

            self.gui_home()
            self.update()
