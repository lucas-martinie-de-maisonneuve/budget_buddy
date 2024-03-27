import pygame
from source.pygame_manager.Screen import Screen
from source.pygame_manager.Element import Element
from source.Controller import Controller

class Accounts(Element, Screen, Controller):
    def __init__(self): 
        Element.__init__(self)
        Screen.__init__(self)
        Controller.__init__(self)   


        self.image_paths = {
            "logout": "assets/image/Accounts/accounts_off1.png",
            "bell":"assets/image/Accounts/accounts_bell.png",
            "logo":"assets/image/Accounts/accounts_logo.png",
            "background":"assets/image/Accounts/accounts_background1.jpg",
            "help":"assets/image/Accounts/accounts_help.png",
            "pic":"assets/image/Accounts/accounts_pic.png"
        }

        self.images = {}
        for name, path in self.image_paths.items():
            self.images[name] = pygame.image.load(path)    
        
    def background(self): 
        self.img_background(400, 300, 1244, 830, self.images["background"])
        print(self.input_email)
     
    def top_bar(self):

        # Rect
        self.rect_full(self.green3, 500, 25, 1000, 30, 0) 
        self.rect_full(self.green1, 500, 75, 1000, 70, 0)
        self.rect_full(self.green3, 500, 125, 1000, 30, 0)

        # Lines v top bar
        pygame.draw.line(self.Window, self.green4, (850, 53), (850, 100), 1)
        pygame.draw.line(self.Window, self.green4, (930, 53), (930, 100), 1)

        # Lines h top bar
        pygame.draw.line(self.Window, self.green, (0, 40), (1000, 40), 1)
        pygame.draw.line(self.Window, self.green, (0, 110), (1000, 110), 1)

        # Brand
        self.text_not_center(self.font1, 18, "Wildcat Wealth Bank", self.white, 10, 85)
        self.img_center("Logo", 90, 65, 70, 40, self.images["logo"])
        
        # Account ID Number
       
        self.text_not_center(self.font3, 13, " Account ID number | ", self.white, 585, 75)
        self.text_not_center(self.font2, 13, "24121993", self.white, 755, 75)
        
        # Notification
        self.img_hover("bell", "bell", 890, 80, 40, 40,self.images["bell"],self.images["bell"])
        self.text_not_center(self.font1, 15, "17", self.yellow, 900, 50)

        # Log Out
        self.img_hover("Log Out", "Log Out", 970, 80, 40, 40,self.images["logout"],self.images["logout"])

    def side_bar(self):

        # Rect
        self.rect_full(self.grey, 140, 420, 250, 530, 5) 
        self.rect_border(self.green1, 140, 420, 250, 530, 2, 5)

        # User info
        self.img_not_center("Profil pic", 90, 170, 100, 100, self.images["pic"])
        self.text_not_center(self.font1, 15, "Hamza Lucas Vanny", self.grey3, 70, 260)
        self.button_hover_small("My Profil", 140, 320, 190, 40, self.green2, self.green2, self.green2, self.green2, "My Profil", self.font1, self.white,15, 0, 3
        )

        # Lines h top bar
        pygame.draw.line(self.Window, self.grey3, (100, 375), (180, 375), 3)
        pygame.draw.line(self.Window, self.grey3, (100, 535), (180, 535), 3)

        # Accounts
        self.button_hover_small("Checking Accounts", 140, 430, 190, 40, self.green2, self.green2, self.green2, self.green2, "Checking Accounts", self.font1, self.white,15, 0, 3
        )
        self.button_hover_small("Saving Account", 140, 480, 190, 40, self.green2, self.green2, self.green2, self.green2, "Saving Account", self.font1, self.white,15, 0, 3
        )

        # Saving Account
        self.button_hover_small("Transfer money", 140, 590, 190, 40, self.green2, self.green2, self.green2, self.green2, "Transfer money", self.font1, self.white,15, 0, 3
        )

        # Help
        self.img_hover("help", "help", 60, 650, 30, 30,self.images["help"],self.images["help"])
        self.text_not_center(self.font4, 12, "Need Help ?", self.grey2, 80, 645)

    def main_bar(self): 
        self.rect_full(self.grey, 630, 420, 700, 530, 5)
        self.rect_border(self.green2, 630, 420, 700, 530, 2, 5)  

    def accounts_run(self):
        accounts_running = True
        while accounts_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    accounts_running = False

        
  
            self.background()
            self.top_bar()
            self.side_bar()
            self.main_bar()
            self.update()


