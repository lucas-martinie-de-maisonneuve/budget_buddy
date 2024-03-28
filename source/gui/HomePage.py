import pygame
from source.pygame_manager.Element import Element
from source.Controller import Controller

class HomePage(Element, Controller):
    def __init__(self, user_info): 
        Element.__init__(self)
        Controller.__init__(self)
        self.user = user_info
        self.user_id = self.user[0]
        self.transactions = self.display_transaction(self.user_id)
        self.scroll = 0
        self.image_paths = {
            "logout": "assets/image/Accounts/accounts_off1.png",
            "bell":"assets/image/Accounts/accounts_bell.png",
            "logo":"assets/image/Accounts/accounts_logo.png",
            "background":"assets/image/Accounts/accounts_background1.jpg",
            "background_top":"assets/image/Accounts/accounts_background_top.jpg",
            "help":"assets/image/Accounts/accounts_help.png",
            "pic":"assets/image/Accounts/accounts_pic.png", 
            "date":"assets/image/Account/account_1.png",
            "income":"assets/image/Account/account_2.png",
            "expense":"assets/image/Account/account_3.png",
            "descending":"assets/image/Account/account_5.png",
            "ascending":"assets/image/Account/account_7.png",
            "calendar":"assets/image/Account/account_6.png",
            "type":"assets/image/Account/account_4.png",
        }

        self.images = {}
        for name, path in self.image_paths.items():
            self.images[name] = pygame.image.load(path)    
        
    def background(self): 
        self.img_background(400, 300, 1244, 830, self.images["background"])
     
    def top_bar(self):
        self.img_background(500, 76.5, 1000, 153, self.images["background_top"])
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
        self.rect_radius_top(self.green3, 140, 175, 250, 45, 5)


        # User info
        self.img_not_center("Profil pic", 90, 160, 90, 90, self.images["pic"])
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

    def main_block(self):
        self.rect_full(self.grey, 630, 420, 700, 530, 5)
        self.filter_options()
        y = 0

        for transaction in self.transactions:
            self.pos_y = y + self.scroll

            if self.pos_y < 425:
                self.text_not_center(self.font3, 10,f"{str(transaction[5].day)}/{str(transaction[5].month)}/{str(transaction[5].year)}", self.black, 460, self.pos_y + 252.5)
                self.text_not_center(self.font3, 15, str(transaction[2]), self.black, 530, self.pos_y + 250)
                self.text_not_center(self.font3, 12, str(transaction[3]), self.black, 750, self.pos_y + 251.5)
                self.text_not_center(self.font3, 12, str(transaction[4]), self.black, 938, self.pos_y + 250)
                self.text_not_center(self.font3, 12, "£", self.black, 930, self.pos_y + 250)
                y += 25
        
        self.rect_radius_top(self.green3, 630, 175, 700, 45, 5)
        self.rect_border(self.green2, 630, 420, 700, 530, 2, 5) 

    def filter_options(self): 

        self.img_txt_hover("date", "Date", 320, 350, 35, 35, self.images["date"], self.images["date"], self.font3, 15, self.grey3,345, 340)
        self.img_txt_hover("income", "Income", 320, 400, 35, 35, self.images["income"], self.images["income"], self.font3, 15, self.grey3,345, 390)
        self.img_txt_hover("expense", "Expense", 320, 450, 35, 35, self.images["expense"], self.images["expense"], self.font3, 15, self.grey3,345, 440)
        self.img_txt_hover("descending", "Descending", 320, 500, 35, 35, self.images["descending"], self.images["descending"], self.font3, 15, self.grey3,345, 490)
        self.img_txt_hover("ascending", "Ascending", 320, 550, 35, 35, self.images["ascending"], self.images["ascending"], self.font3, 15, self.grey3,345, 540)
        self.img_txt_hover("calendar", "Calendar", 320, 600, 35, 35, self.images["calendar"], self.images["calendar"], self.font3, 15, self.grey3,345, 590)
        self.img_txt_hover("type", "Type", 320, 650, 35, 35, self.images["type"], self.images["type"], self.font3, 15, self.grey3,345, 640)

    def homepage_run(self):
        accounts_running = True
        while accounts_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    accounts_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4 and self.scroll < 0 :
                        self.scroll += 15

                    elif event.button == 5:
                        self.scroll -= 15
                   
                  
            self.background()
            self.side_bar()
            self.main_block()
            self.top_bar()

            self.update()
