import pygame
from source.pygame_manager.Element import Element
from source.pygame_manager.Animation import Animation
from source.Controller import Controller

class LogIn(Element, Animation, Controller): 
    def __init__(self): 
        Element.__init__(self)
        Animation.__init__(self)
        Controller.__init__(self)

        self.entry = False

        self.image_paths = {
            "twitter": "assets/image/LogIn/login_twitter.png",
            "instagram": "assets/image/LogIn/login_instagram.png",
            "facebook": "assets/image/LogIn/login_facebook.png",
            "background": "assets/image/LogIn/login_background.png"
        }

        self.images = {}
        for name, path in self.image_paths.items():
            self.images[name] = pygame.image.load(path)    
         
    def gui_home(self): 

        self.img_background(400, 300, 1244, 830, self.images["background"])

        # Rect principal
        self.rect_full(self.green3, self.W//2+220, self.H//2, 400, 580, 10)
        self.rect_border(self.white, self.W//2+220, self.H//2, 400, 580, 1, 10)

        # Logo
        self.text_center(self.font1, 35, "Wildcat Wealth Bank", self.white, self.W//2+220, 140)
        self.text_center(self.font4, 16, "Where Panthers Guard Your Fortune!", self.white, self.W//2+220, 180)

        # Email        
        self.input_email_rect = self.button_hover("Email", self.W//2+220, 250, 350, 50, self.green2, self.green, self.green2, self.green, self.input_email, self.font4, self.white,18, 1, 5)
        self.text_input(self.input_email_rect, self.input_email, "Email address", 720, 250, 350, 50, id="email_login")
    
        # Password
        self.input_password_rect = self.button_hover("Password", self.W//2+220, 320, 350, 50, self.green2, self.green, self.green2, self.green, self.input_password, self.font4, self.white, 18, 1, 5)
        self.text_input(self.input_password_rect, self.input_password, "Password", 720, 320, 350, 50, id="email_login")

        # Login
        self.login_rect = self.button_hover("Login", self.W//2+220, 390, 350, 50, self.green, self.green, self.green, self.green,"Log In", self.font1, self.white, 18, 1, 5) 
        
        # No Account
        self.text_center(self.font1, 13, "No account ?", self.white, self.W//2+190, 450)
        self.text_center(self.font4, 13, "Create one!", self.white, self.W//2+265, 450)
        
        # Lines
        pygame.draw.line(self.Window, self.green, (550, 450), (640, 450), 1) 
        pygame.draw.line(self.Window, self.green, (805, 450), (895, 450), 1)
        pygame.draw.line(self.Window, self.green, (520, 575), (919, 575), 1)

        # Social Media
        self.img_hover("Twitter", "Twitter", self.W//2+160, 610, 35, 35,self.images["twitter"],self.images["twitter"])
        self.img_hover("Instagram", "Instagram", self.W//2+220, 610, 35, 35,self.images["instagram"],self.images["instagram"])
        self.img_hover("Facebook", "Facebook", self.W//2+280, 610, 35, 35, self.images["facebook"], self.images["facebook"])        
       
        # Sign In


        # pygame.draw.rect(self.Window, self.black, [675, 490, 90, 20])
        self.sign = (pygame.Rect(675, 490, 90, 20)) 
        if self.is_mouse_over_button(self.sign):
            self.text_center(self.font4, 15, "Sign-in options", self.white, self.W//2+220, 500)          
        else:
            self.text_center(self.font4, 13, "Sign-in options", self.white, self.W//2+220, 500)
      

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