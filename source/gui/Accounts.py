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
            "background":"assets/image/Accounts/accounts_background1.jpg"
        }

        self.images = {}
        for name, path in self.image_paths.items():
            self.images[name] = pygame.image.load(path)    
        
    def gui_accounts(self): 
        self.screen_color(self.white)

        # Background
        self.img_background(400, 300, 1244, 830, self.images["background"])

     
        # Top bar
        self.rect_full(self.green3, 500, 25, 1000, 40, 0) 
        self.rect_full(self.green1, 500, 75, 1000, 70, 0)
        self.rect_full(self.green3, 500, 130, 1000, 40, 0)
        
        # User info
        self.text_not_center(self.font1, 15, "Hamza Lucas Vanny", self.white, 595, 55)
        self.text_not_center(self.font3, 13, " Account ID number | ", self.white, 585, 75)
        self.text_not_center(self.font2, 13, "24121993", self.white, 755, 75)

        # Side bar
        self.rect_full(self.grey, 140, 425, 250, 520, 5) 
        self.rect_border(self.green1, 140, 425, 250, 520, 2, 5)

        # Main bar
        self.rect_full(self.grey, 630, 425, 700, 520, 5)
        self.rect_border(self.green2, 630, 425, 700, 520, 2, 5)

        # Lines v
        pygame.draw.line(self.Window, self.green4, (850, 53), (850, 100), 1)
        pygame.draw.line(self.Window, self.green4, (930, 53), (930, 100), 1)

        # Lines h
        pygame.draw.line(self.Window, self.green, (0, 40), (1000, 40), 1)
        pygame.draw.line(self.Window, self.green, (0, 110), (1000, 110), 1)

        self.text_not_center(self.font1, 18, "Wildcat Wealth Bank", self.white, 10, 85)

        self.img_center("Logo", 90, 65, 70, 40, self.images["logo"])

        # Notification
        self.img_hover("bell", "bell", 890, 80, 40, 40,self.images["bell"],self.images["bell"])
        self.text_not_center(self.font1, 15, "17", self.yellow, 900, 50)

        # Log Out
        self.img_hover("Log Out", "Log Out", 970, 80, 40, 40,self.images["logout"],self.images["logout"])
        
    def accounts_run(self):
        accounts_running = True
        while accounts_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    accounts_running = False
  

            self.gui_accounts()
            self.update()


