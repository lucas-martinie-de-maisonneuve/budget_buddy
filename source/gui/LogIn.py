import pygame
from source.pygame_manager.Screen import Screen
from source.pygame_manager.Element import Element
from source.Controller import Controller

class LogIn(Element, Screen, Controller): 
    def __init__(self): 
        Element.__init__(self)
        Screen.__init__(self)
        Controller.__init__(self)

        self.entry = False

        self.img_twitter = pygame.image.load("assets/image/LogIn/login_twitter.png")
        self.img_instagram = pygame.image.load("assets/image/LogIn/login_instagram.png")
        self.img_facebook = pygame.image.load("assets/image/LogIn/login_facebook.png")
        self.img_logo = pygame.image.load("assets/image/LogIn/login_logo.png")
      
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
        
        self.input_email_rect = self.button_hover("Email", self.W//2+220, 250, 350, 50, self.green2, self.green, self.green2, self.green, self.input_email, self.font1, self.white,18, 1, 5)

        self.input_password_rect = self.button_hover("Password", self.W//2+220, 320, 350, 50, self.green2, self.green, self.green2, self.green, self.input_password, self.font1, self.white, 18, 1, 5)

        self.login_rect = self.button_hover("Login", self.W//2+220, 390, 350, 50, self.green, self.green, self.green, self.green,"Log In", self.font1, self.white, 18, 1, 5) 
        
        self.text_center(self.font1, 13, "No account ?", self.white, self.W//2+190, 450)
        self.text_center(self.font4, 13, "Create one!", self.white, self.W//2+265, 450)
        # Lines
        pygame.draw.line(self.Window, self.green, (550, 450), (640, 450), 1) 
        pygame.draw.line(self.Window, self.green, (805, 450), (895, 450), 1)
        pygame.draw.line(self.Window, self.green, (520, 575), (919, 575), 1)

        # Social Media
        self.img_hover("Twitter", "Twitter", self.W//2+160, 610, 35, 35, self.img_twitter, self.img_twitter)
        self.img_hover("Instagram", "Instagram", self.W//2+220, 610, 35, 35, self.img_instagram, self.img_instagram)
        self.img_hover("Facebook", "Facebook", self.W//2+280, 610, 35, 35, self.img_facebook, self.img_facebook)
        
        self.img_center("logo", self.W//2+220, 140, 200, 110, self.img_logo)



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
