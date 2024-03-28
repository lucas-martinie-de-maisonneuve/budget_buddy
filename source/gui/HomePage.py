import pygame
from source.pygame_manager.Element import Element
from source.Controller import Controller

class HomePage(Element, Controller):
    def __init__(self, user_info): 
        Element.__init__(self)
        Controller.__init__(self)
        self.user = user_info


        self.image_paths = {
            "logout": "assets/image/Accounts/accounts_off1.png",
            "bell":"assets/image/Accounts/accounts_bell.png",
            "logo":"assets/image/Accounts/accounts_logo.png",
            "background":"assets/image/Accounts/accounts_background1.jpg",
            "help":"assets/image/Accounts/accounts_help.png",
            "pic":"assets/image/Accounts/accounts_pic.png", 
            "date":"assets/image/Account/account_1.png",
            "income":"assets/image/Account/account_2.png",
            "expense":"assets/image/Account/account_3.png",
            "descending":"assets/image/Account/account_5.png",
            "ascending":"assets/image/Account/account_7.png",
            "calendar":"assets/image/Account/account_6.png",
            "type":"assets/image/Account/account_4.png",
            "modify":"assets/image/Profile/profile1.png",
            "question":"assets/image/Transaction/transaction1.png",
        }

        self.images = {}
        for name, path in self.image_paths.items():
            self.images[name] = pygame.image.load(path)    
        
    def background(self): 
        self.img_background(400, 300, 1244, 830, self.images["background"])
     
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

    def main_section (self):
        self.rect_full(self.grey, 630, 420, 700, 530, 5)
        self.rect_border(self.green2, 630, 420, 700, 530, 2, 5) 
        self.rect_radius_top(self.green3, 630, 175, 700, 45, 5)

    def main_page_design(self):
        self.background()
        self.top_bar()
        self.side_bar()
        self.main_section ()

    def profile_design(self):

        # Name
        self.text_not_center(self.font3, 16, "Name", self.grey1, 330, 300)
        self.text_not_center(self.font2, 16, "Lucas", self.grey1, 390, 300)
        pygame.draw.line(self.Window, self.green4, (330, 330), (700, 330), 1)

        # Surname
        self.text_not_center(self.font3, 16, "Surname", self.grey1, 330, 350)
        self.text_not_center(self.font2, 16, "Martinie", self.grey1, 420, 350)
        pygame.draw.line(self.Window, self.green4, (330, 380), (700, 380), 1)

        # Email
        self.text_not_center(self.font3, 16, "Email", self.grey1, 330, 400)
        self.text_not_center(self.font2, 16, "lucas.martinie@laplateforme.io", self.grey1, 400, 400)
        pygame.draw.line(self.Window, self.green4, (330, 430), (700, 430), 1)
        
        # Account ID
        self.text_not_center(self.font3, 16, "Account ID Number", self.grey1, 330, 450)
        self.text_not_center(self.font2, 16, "HAHAHAHIHIHOHO", self.grey1,520, 450)

        # IBAN
        self.text_not_center(self.font3, 16, "IBAN", self.grey1, 330, 500)
        self.text_not_center(self.font2, 16, "MOUHAHAHAHAHAHA!!!!", self.grey1, 390, 500)
        pygame.draw.line(self.Window, self.green4, (330, 530), (700, 530), 1)

    def saving_checking_design(self): 

        # Filter for income and expense
        self.text_not_center(self.font3, 18, "Sort by", self.grey2, 305, 290)
        self.img_txt_hover("date", "Date", 320, 350, 35, 35, self.images["date"], self.images["date"], self.font3, 15, self.grey3,345, 340)
        self.img_txt_hover("income", "Income", 320, 400, 35, 35, self.images["income"], self.images["income"], self.font3, 15, self.grey3,345, 390)
        self.img_txt_hover("expense", "Expense", 320, 450, 35, 35, self.images["expense"], self.images["expense"], self.font3, 15, self.grey3,345, 440)
        self.img_txt_hover("descending", "Descending", 320, 500, 35, 35, self.images["descending"], self.images["descending"], self.font3, 15, self.grey3,345, 490)
        self.img_txt_hover("ascending", "Ascending", 320, 550, 35, 35, self.images["ascending"], self.images["ascending"], self.font3, 15, self.grey3,345, 540)
        self.img_txt_hover("calendar", "Calendar", 320, 600, 35, 35, self.images["calendar"], self.images["calendar"], self.font3, 15, self.grey3,345, 590)
        self.img_txt_hover("type", "Type", 320, 650, 35, 35, self.images["type"], self.images["type"], self.font3, 15, self.grey3,345, 640)

    def transaction_design(self): 

        # Sender
        self.text_not_center(self.font1, 18, "Sender", self.grey2, 450, 225)
        self.button_hover("Name", 380, 290, 150, 40, self.grey, self.green1, self.grey, self.green1, "Name", self.font3, self.grey2, 14, 2, 5)
        self.button_hover("Surname", 540, 290, 150, 40, self.grey, self.green1, self.grey, self.green1, "Surname", self.font3, self.grey2, 14, 2, 5)
        self.button_hover("Checking Account", 380, 360, 150, 40, self.grey, self.green1, self.grey, self.green1, "Checking Account", self.font3, self.grey2, 14, 2, 5)
        self.button_hover("Saving Account", 540, 360, 150, 40, self.grey, self.green1, self.grey, self.green1, "Saving Account", self.font3, self.grey2, 14, 2, 5)
        self.button_hover("Description", 460, 430, 310, 40, self.grey, self.green1, self.grey, self.green1, "Description", self.font3, self.grey2, 14, 2, 5)
        self.button_hover("+/-", 325, 570, 40, 40, self.grey, self.green1, self.grey, self.green1, "+/-", self.font3, self.grey2, 14, 2, 5)
        self.button_hover("Amont", 485, 570, 260, 40, self.grey, self.green1, self.grey, self.green1, "Amount", self.font3, self.grey2, 14, 2, 5)

        # Category      
        self.button_hover("Category", 420, 500, 220, 40, self.grey, self.green1, self.grey, self.green1, "Category", self.font3, self.grey2, 14, 2, 5)
        self.button_hover("number", 560, 500, 40, 40, self.grey, self.green1, self.grey, self.green1, "7", self.font3, self.grey2, 14, 2, 5)
        self.question_rect = self.img_not_center("question", 585, 490, 25, 25, self.images["question"])

        if self.is_mouse_over_button(self.question_rect ):
            self.text_not_center(self.font4, 12, "1 = Living Expenses", self.grey2, 320, 605)
            self.text_not_center(self.font4, 12, "2 = Transportation Costs", self.grey2, 320, 625)
            self.text_not_center(self.font4, 12, "3 = Food and Grocery Expense", self.grey2, 320, 645)
            self.text_not_center(self.font4, 12, "4 = Personal Expenses", self.grey2, 520, 605)
            self.text_not_center(self.font4, 12, "5 = Financial Obligations", self.grey2, 520, 625)      

        # Receiver
        self.text_not_center(self.font1, 18, "Receiver", self.grey2, 780, 225)
        self.button_hover("Name",720, 290, 150, 40, self.grey, self.green1, self.grey, self.green1, "Name", self.font3, self.grey2, 14, 2, 5)
        self.button_hover("Surname", 880, 290, 150, 40, self.grey, self.green1, self.grey, self.green1, "Surname ", self.font3, self.grey2, 14, 2, 5) 
        self.button_hover("IBAN", 800, 360, 310, 40, self.grey, self.green1, self.grey, self.green1, "IBAN", self.font3, self.grey2, 14, 2, 5)

        # Send money to yourself
        self.text_not_center(self.font1, 18, "Transfer to yourself", self.grey2, 700, 430)
        self.button_hover("Checking Account", 720, 500, 150, 40, self.grey, self.green1, self.grey, self.green1, "Checking Account", self.font3, self.grey2, 14, 2, 5)
        self.button_hover("Saving Account", 880, 500, 150, 40, self.grey, self.green1, self.grey, self.green1, "Saving Account", self.font3, self.grey2, 14, 2, 5)

        # Validation button
        self.button_hover("validation", 855, 600, 200, 40, self.green2, self.green2, self.green1, self.green1, "CONFIRM BANK TRANSFER", self.font3, self.white, 14, 2, 5)       

    def homepage_run(self):
        accounts_running = True
        while accounts_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    accounts_running = False   
  
            self.main_page_design()
            # self.profile_design()
            # self.saving_checking_design()
            self.transaction_design()
            self.update()