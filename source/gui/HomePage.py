import pygame
from source.pygame_manager.Element import Element
from source.Controller import Controller
from datetime import datetime

class HomePage(Element, Controller):
    def __init__(self, user_info): 
        Element.__init__(self)
        Controller.__init__(self)
        self.user = user_info
        self.user_id, self.user_fisrt_name, self.user_last_name, self.user_email, self.sort_code, self.user_iban, self.user_account_number, self.last_login_date = self.user[0], self.user[1], self.user[2], self.user[3], self.user[5], self.user[6], self.user[7], self.user[9]

        self.current_date = ""
        self.transactions = self.display_transaction(self.user_id, 1, None, None, None)
        self.account_type = None
        self.date_sort = False

        self.checking_sender = False
        self.saving_sender = False
        self.checking_receiver = False
        self.saving_receiver = False
        self.home_event = True

        self.sort_code_1 = str(self.sort_code)[:2]
        self.sort_code_2 = str(self.sort_code)[2:4]
        self.sort_code_3 = str(self.sort_code)[4:]
        self.sort_code_final = '-'.join([self.sort_code_1, self.sort_code_2, self.sort_code_3])

        self.not_conform = False
        self.transaction_event = False

        self.sort_category = 0
        self.category_list = ["income", "Living Expenses", "Transportation Costs" ,"Food and Grocery Expenditures", "Personal Expenses", "Financial Obligations"]
        self.display_category_description = False

        self.checking_saving_event = False
        self.scroll = 0
        self.accounts_running = True
        self.transaction_running = True
        self.disconnected = True

        self.entry = False

        self.error_de = False
        self.error_nc = False
        self.error_at = False
        self.error_ne = False
        self.error_se = False
        self.error_ib = False
        self.transfer_money_message = False

        self.checking_sender = False
        self.saving_sender = False
        self.checking_receiver = False
        self.saving_receiver = False


        self.error_ops = False
        self.error_opr = False

        # Main Page
        self.coin_angle = 0
        self.rotation_speed = 2
        self.total_saving = str(self.display_total_amount(2, self.user_id))
        self.total_checking = str(self.display_total_amount(1, self.user_id))
        self.total_account = str(int(self.total_saving) + int(self.total_checking))

        # Notification
        self.display_notif = self.notification()

        # Sort by
        self.calendar_error = False
        self.display_start_end_date = False
        self.input_start_date = "00/00/0000"
        self.input_end_date = "00/00/0000"

        self.image_paths = {
            # Main page
            "logout": "assets/image/MainPage/mainpage_off.png",
            "bell":"assets/image/MainPage/mainpage_bell.png",
            "background":"assets/image/MainPage/mainpage_background1.jpg",
            "background_top":"assets/image/MainPage/mainpage_background_top.jpg",
            "help":"assets/image/MainPage/mainpage_help.png",
            "profile":"assets/image/MainPage/mainpage_profile.png",
            "coin":"assets/image/MainPage/mainpage_coin.png",
            "circle":"assets/image/MainPage/mainpage_circle.png",
            # Checking & Saving
            "date":"assets/image/Account/account_1.png",
            "income":"assets/image/Account/account_2.png",
            "expense":"assets/image/Account/account_3.png",
            "descending":"assets/image/Account/account_5.png",
            "ascending":"assets/image/Account/account_7.png",
            "calendar":"assets/image/Account/account_6.png",
            "type":"assets/image/Account/account_4.png",
            # Profile
            "pen":"assets/image/Profile/profile_pen.png",
            # Transaction
            "question":"assets/image/Transaction/transaction_question.png",
            # Logo diagram
            "income_logo":"assets/image/MainPage/income_logo.png",
            "living":"assets/image/MainPage/house_logo.png",
            "personal":"assets/image/MainPage/clothing_logo.png",
            "obligation":"assets/image/MainPage/document_logo.png",
            "grocery":"assets/image/MainPage/grocery_logo.png",
            "transportation":"assets/image/MainPage/transport_logo.png",
        }


        self.images = {}
        for name, path in self.image_paths.items():
            self.images[name] = pygame.image.load(path)

        self.profile_display, self.checking_saving_display, self.transfer_display = False, False, False

        self.welcome_message_list = ["Welcome to your profile! Here, you can view all the details and information pertinent to you",
        "Welcome! You are currently on the homepage where you can view the total details of all accounts",
        "Welcome to your checking account! Let's manage your finances together",
        "Welcome back to your savings account! Let's continue growing your financial goals together",
        "Transfer Money Now with Ease!"
        ]
        self.welcome_message = self.welcome_message_list[1]                      

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
        self.text_not_center(self.font3, 13, " Account ID number | ", self.white, 600, 75)
        self.text_not_center(self.font2, 13, self.user_account_number, self.white, 770, 76)

        # Notification
        self.img_hover("bell", "bell", 890, 80, 40, 40,self.images["bell"],self.images["bell"])
        self.text_not_center(self.font1, 15, str(self.display_notif), self.yellow, 900, 50)

        # Log Out
        self.log_out_rect = self.img_hover("Log Out", "Log Out", 970, 80, 40, 40,self.images["logout"],self.images["logout"])

    def side_bar(self):

        # Rect
        self.rect_full(self.grey, 140, 420, 250, 530, 5)
        self.rect_border(self.green1, 140, 420, 250, 530, 2, 5)
        self.rect_radius_top(self.green3, 140, 175, 250, 45, 5)

        # User info
        self.img_not_center("Profil pic", 90, 160, 90, 90, self.images["profile"])
        self.text_not_center(self.font1, 15, f"{self.user_fisrt_name} {self.user_last_name}", self.grey3, 70, 260)
        self.profile_rect = self.button_hover_small("My Profil", 140, 310, 190, 40, self.green2, self.green2, self.green2, self.green2, "My Profil", self.font1, self.white,15, 0, 3
        )

        # Home
        self.home_rect = self.button_hover_small("Home", 140, 360, 190, 40, self.green2, self.green2, self.green2, self.green2, "Home", self.font1, self.white,15, 0, 3        )


        # Lines h top bar
        pygame.draw.line(self.Window, self.grey3, (100, 405), (180, 405), 3)
        pygame.draw.line(self.Window, self.grey3, (100, 545), (180, 545), 3)

        if self.user[8] == 1:
            # Accounts
            self.checking_rect = self.button_hover_small("Checking Accounts", 140, 450, 190, 40, self.green2, self.green2, self.green2, self.green2, "Checking Accounts", self.font1, self.white,15, 0, 3)
            # Saving Account
            self.saving_rect = self.saving_rect = self.button_hover_small("Saving Account", 140, 500, 190, 40, self.grey1, self.grey1, self.grey1, self.grey1, "Saving Account", self.font1, self.white,15, 0, 3)
        if self.user[8] == 2:
             # Accounts
            self.checking_rect = self.button_hover_small("Checking Accounts", 140, 450, 190, 40, self.grey1, self.grey1, self.grey1, self.grey1, "Checking Accounts", self.font1, self.white,15, 0, 3)
            # Saving Account
            self.saving_rect = self.saving_rect = self.button_hover_small("Saving Account", 140, 500, 190, 40, self.green2, self.green2, self.green2, self.green2, "Saving Account", self.font1, self.white,15, 0, 3)
        if self.user[8] == 3:
             # Accounts
            self.checking_rect = self.button_hover_small("Checking Accounts", 140, 450, 190, 40, self.green2, self.green2, self.green2, self.green2, "Checking Accounts", self.font1, self.white,15, 0, 3)
            # Saving Account
            self.saving_rect = self.saving_rect = self.button_hover_small("Saving Account", 140, 500, 190, 40, self.green2, self.green2, self.green2, self.green2, "Saving Account", self.font1, self.white,15, 0, 3)

        self.transfer_rect = self.button_hover_small("Transfer money", 140, 590, 190, 40, self.green2, self.green2, self.green2, self.green2, "Transfer money", self.font1, self.white,15, 0, 3)

        # Help
        self.img_hover("help", "help", 60, 650, 30, 30,self.images["help"],self.images["help"])
        self.text_not_center(self.font4, 12, "Need Help ?", self.grey2, 80, 645)

    def main_section (self):
        self.rect_full(self.grey, 630, 420, 700, 530, 5)
        self.rect_border(self.green2, 630, 420, 700, 530, 2, 5)
        self.rect_radius_top(self.green3, 630, 175, 700, 45, 5)

        # Welcome message
        self.text_not_center(self.font1, 14, self.welcome_message, self.white, 295, 170) 

    def all_accounts(self):

        pygame.draw.line(self.Window, self.grey3, (315, 280), (605, 280), 1)
        self.text_not_center(self.font1, 35, self.total_account, self.green1, 405, 230)
        self.text_not_center(self.font1, 18, "Total Balance", self.grey2, 405, 290)

        # Checking Account
        self.rect_full(self.green1, 460, 410, 300, 150, 5)
        self.img_hover("Circle", "Circle", 530, 410, 110, 110,self.images["circle"],self.images["circle"])
        self.text_not_center(self.font4, 15, self.total_checking, self.white, 500, 405)
        self.text_not_center(self.font1, 14, "CHECKING ACCOUNT", self.white, 330, 370)
        self.text_not_center(self.font4, 12,f"Sort Code {self.sort_code_final}", self.white, 330, 400)
        self.text_not_center(self.font4, 12, f"Account ID {self.user_account_number}", self.white, 330, 430)
        self.text_not_center(self.font4, 12, f"{self.user_fisrt_name} {self.user_last_name}", self.white, 330, 460)

        # Saving Account
        self.rect_full(self.green1, 460, 580, 300, 150, 5)
        self.img_hover("Circle", "Circle", 530, 580, 110, 110,self.images["circle"],self.images["circle"])
        self.text_not_center(self.font4, 15, self.total_saving, self.white, 500, 575)
        self.text_not_center(self.font1, 14, "SAVING ACCOUNT", self.white, 330, 540)
        self.text_not_center(self.font4, 12, f"Sort Code {self.sort_code_final}", self.white, 330, 570)
        self.text_not_center(self.font4, 12,f"Account ID {self.user_account_number}", self.white, 330, 600)
        self.text_not_center(self.font4, 12,f"{self.user_fisrt_name} {self.user_last_name}", self.white, 330, 630)

        # Animation
        rotated_coin = pygame.transform.rotate(self.images["coin"], self.coin_angle)
        resized_rotated_coin = pygame.transform.scale(rotated_coin, (90, 90))
        resized_rotated_coin_rect = resized_rotated_coin.get_rect(center=(350, 240))

        self.Window.blit(resized_rotated_coin, resized_rotated_coin_rect)
     
        self.coin_angle += self.rotation_speed
        if self.coin_angle >= 360:
            self.coin_angle -= 360
        elif self.coin_angle < 0:
            self.coin_angle += 360
        self.diagram()

    # Diagramme
    def diagram(self):
        income_size, obligation_size, grocery_size, living_size, personal_size, transport_size = 0, 0, 0, 0, 0, 0 
        income_total, obligation_total, grocery_total, living_total, personal_total, transport_total = 0, 0, 0, 0, 0, 0 
        for transaction in self.transactions:
            if transaction[6] == 0:
                income_total += transaction[4]
            elif transaction[6] == 5:
                obligation_total += transaction[4]
            elif transaction[6] == 3:
                grocery_total += transaction[4]
            elif transaction[6] == 1:
                living_total += transaction[4]
            elif transaction[6] == 4:
                personal_total += transaction[4]
            elif transaction[6] == 2:
                transport_total += transaction[4]

        pygame.draw.line(self.Window, self.grey3, (625, 450), (970, 450), 2)

        total = obligation_total + grocery_total + living_total + personal_total + transport_total + income_total
        if total == 0:
            total = 1
        obligation_size = 215 * obligation_total / total
        grocery_size = 215 * grocery_total / total
        living_size = 215 * living_total / total
        personal_size = 215 * personal_total / total
        transport_size = 215 * transport_total / total
        income_size = 215 * income_total / total

        self.img_center("Income", 650, 650, 40, 40, self.images["income_logo"])
        self.rect_full_not_centered(self.black, 670, 452, 40, income_size, 0)
        self.text_center(self.font2, 12, f"+{income_total}€",self.green2, 650, 442 - (income_size))

        self.img_center("obligation", 710, 650, 40, 40, self.images["obligation"])
        self.rect_full_not_centered(self.black, 730, 450 + obligation_size, 40, obligation_size, 0)
        self.text_center(self.font2, 12, f"-{obligation_total}€",self.red2, 710, 460 + obligation_size)

        self.img_center("grocery", 770, 650, 40, 40, self.images["grocery"])
        self.rect_full_not_centered(self.black, 790, 450 + grocery_size, 40, grocery_size, 0)
        self.text_center(self.font2, 12, f"-{grocery_total}€",self.red2, 770, 460 + grocery_size)

        self.img_center("living", 830, 650, 40, 40, self.images["living"])
        self.rect_full_not_centered(self.black, 850, 450 + living_size, 40, living_size, 0)
        self.text_center(self.font2, 12, f"-{living_total}€",self.red2, 830, 460 + living_size)

        self.img_center("personal", 890, 650, 40, 40, self.images["personal"])
        self.rect_full_not_centered(self.black, 910, 450 + personal_size, 40, personal_size, 0)
        self.text_center(self.font2, 12, f"-{personal_total}€",self.red2, 890, 460 + personal_size)

        self.img_center("transportation", 950, 650, 40, 40, self.images["transportation"])
        self.rect_full_not_centered(self.black, 970, 450 + transport_size, 40, transport_size, 0)
        self.text_center(self.font2, 12, f"-{transport_total}€",self.red2, 950, 460 + transport_size)

        self.last_month = self.button_hover_small("1month ", 650, 210, 85, 20, self.grey2, self.grey3, self.grey1, self.grey3, "Last month", self.font3, self.white, 12, 2, 5)
        self.three_last_month = self.button_hover_small("3month ", 740, 210, 85, 20, self.grey2, self.grey3, self.grey1, self.grey3, "Three month", self.font3, self.white, 12, 2, 5)
        self.last_year = self.button_hover_small("lastyear ", 830, 210, 85, 20, self.grey2, self.grey3, self.grey1, self.grey3, "Last year", self.font3, self.white, 12, 2, 5)
        self.all_time = self.button_hover_small("alltime ", 920, 210, 85, 20, self.grey2, self.grey3, self.grey1, self.grey3, "All Time", self.font3, self.white, 12, 2, 5)

    def main_page_design(self):

        self.background()
        self.top_bar()
        self.side_bar()
        self.main_section()

    def saving_checking_design(self):
        self.filter_options()
        y = 0

        for transaction in self.transactions:
            self.pos_y = y + self.scroll
            if transaction[7] == self.account_type:
                if self.pos_y < 425:
                    self.text_not_center(self.font3, 10,('['+ str(transaction[6])+']'), self.black, 440, self.pos_y + 252.5)
                    self.text_not_center(self.font3, 10, f"{transaction[5].day:02d}/{transaction[5].month:02d}/{transaction[5].year}", self.black, 460, self.pos_y + 252.5)
                    self.text_not_center(self.font3, 15, str(transaction[2]), self.black, 530, self.pos_y + 250)
                    self.text_not_center(self.font3, 12, str(transaction[3]), self.black, 750, self.pos_y + 251.5)
                    self.text_not_center(self.font3, 12, str(transaction[4]), self.black, 938, self.pos_y + 250)
                    self.text_not_center(self.font3, 12, "£", self.black, 930, self.pos_y + 250)
                    if transaction[9] == self.user_id:
                        self.text_not_center(self.font1, 18, "+", self.green, 920, self.pos_y + 250)
                    elif transaction[8] == self.user_id:
                        self.text_not_center(self.font1, 18, "-", self.red, 920, self.pos_y + 250)

                    y += 25

        self.rect_full(self.grey, 630, 220, 700, 50, 0)
        self.rect_border(self.green2, 630, 420, 700, 530, 2, 5)
        self.rect_radius_top(self.green3, 630, 175, 700, 45, 5)
        self.text_not_center(self.font2, 17, "Sort by", self.black, 305, 210)
        self.text_not_center(self.font2, 17,"Date", self.black, 464, 210)
        self.text_not_center(self.font2, 17,"To / From", self.black, 535, 210)
        self.text_not_center(self.font2, 17, "Description", self.black, 740, 210)
        self.text_not_center(self.font2, 17, "Amount", self.black, 910, 210)

        if not self.checking_saving_event:
            self.checking_saving_event = True

        # Welcome message
        self.text_not_center(self.font1, 14, self.welcome_message, self.white, 295, 170) 

        if self.calendar_error: 
            self.text_not_center(self.font4, 12, "Invalid", self.red, 345, 582)

    def profile_design(self):

        # Name
        self.text_not_center(self.font1, 16, "Name", self.grey1, 330, 300)
        self.text_not_center(self.font2, 16, self.user_fisrt_name, self.grey1, 390, 300)
        pygame.draw.line(self.Window, self.green4, (330, 330), (750, 330), 1)

        # Surname
        self.text_not_center(self.font1, 16, "Surname", self.grey1, 330, 350)
        self.text_not_center(self.font2, 16, self.user_last_name, self.grey1, 420, 350)
        pygame.draw.line(self.Window, self.green4, (330, 380), (750, 380), 1)

        # Email
        self.text_not_center(self.font1, 16, "Email", self.grey1, 330, 400)
        self.text_not_center(self.font2, 16, self.user_email, self.grey1, 380, 400)
        pygame.draw.line(self.Window, self.green4, (330, 430), (750, 430), 1)

        # Account ID
        self.text_not_center(self.font1, 16, "Account ID Number", self.grey1, 330, 450)
        self.text_not_center(self.font2, 16, self.user_account_number, self.grey1,480, 450)
        pygame.draw.line(self.Window, self.green4, (330, 480), (750, 480), 1)

        # Sort Code
        self.text_not_center(self.font1, 16, "Sort Code", self.grey1, 330, 500)
        self.text_not_center(self.font2, 16, self.sort_code_final, self.grey1, 420, 500)
        pygame.draw.line(self.Window, self.green4, (330, 530), (750, 530), 1)

        # IBAN
        self.text_not_center(self.font1, 16, "IBAN", self.grey1, 330, 550)
        self.text_not_center(self.font2, 16, self.user_iban, self.grey1, 380, 550)
        pygame.draw.line(self.Window, self.green4, (330, 580), (750, 580), 1)

    def filter_options(self):

        # Filter by date
        self.date_rect = self.img_txt_hover("date", "Date", 320, 270, 35, 35, self.images["date"], self.images["date"], self.font3, 15, self.grey3,345, 260)
        # Filter by income
        self.income_rect = self.img_txt_hover("income", "Income", 320, 320, 35, 35, self.images["income"], self.images["income"], self.font3, 15, self.grey3,345, 310)
        # Filter by expense
        self.expense_rect = self.img_txt_hover("expense", "Expense", 320, 370, 35, 35, self.images["expense"], self.images["expense"], self.font3, 15, self.grey3,345, 360)
        # Filter by amount descending
        self.descending_rect = self.img_txt_hover("descending", "Descending", 320, 420, 35, 35, self.images["descending"], self.images["descending"], self.font3, 15, self.grey3,345, 410)
        # Filter by amount ascending
        self.ascending_rect = self.img_txt_hover("ascending", "Ascending", 320, 470, 35, 35, self.images["ascending"], self.images["ascending"], self.font3, 15, self.grey3,345, 460)

        # Filter by type
        if self.display_category_description:
            type_text = self.category_list[self.sort_category - 1]
        else: type_text = "Type"
        self.type_rect = self.img_txt_hover("type", type_text, 320, 520, 35, 35, self.images["type"], self.images["type"], self.font3, 15, self.grey3,345, 510)

        # Filter by period
        self.calendar_rect = self.img_txt_hover("calendar", "Calendar", 320, 570, 35, 35, self.images["calendar"], self.images["calendar"], self.font3, 15, self.grey3, 345, 560)

        if self.display_start_end_date:
            self.input_start_date_rect = self.button_hover("start", 350, 605, 80, 25, self.grey, self.grey3, self.grey, self.grey3, self.input_start_date, self.font3, self.black, 10, 2, 5) 

            self.input_end_date_rect = self.button_hover("end", 350, 637, 80, 25, self.grey, self.grey3, self.grey, self.grey3, self.input_end_date, self.font3, self.black, 10, 2, 5)
            self.validate_rect = self.button_hover("Validate", 350, 665, 80, 20, self.grey, self.grey3, self.green4, self.green4, "Validate", self.font3, self.black, 10, 2, 5)

    def transaction_design(self):

        # Sender
        self.text_not_center(self.font1, 18, "Sender", self.grey2, 435, 225)
        self.input_name_sender_rect = self.button_hover("Name", 380, 290, 150, 40, self.grey, self.green1, self.grey, self.green1, self.user_fisrt_name, self.font3, self.grey2, 14, 2, 5)
        self.input_surname_sender_rect = self.button_hover("Surname", 540, 290, 150, 40, self.grey, self.green1, self.grey, self.green1, self.user_last_name, self.font3, self.grey2, 14, 2, 5)

        if self.checking_sender:
            self.checking_sender_rect = self.button_hover("Checking Account", 380, 360, 150, 40, self.green1, self.green1, self.green1, self.green1, "Checking Account", self.font3, self.white, 14, 2, 5)
        else:
            self.checking_sender_rect = self.button_hover("Checking Account", 380, 360, 150, 40, self.grey, self.green1, self.grey, self.green1, "Checking Account", self.font3, self.grey2, 14, 2, 5)

        if self.saving_sender:
            self.saving_sender_rect = self.button_hover("Saving Account", 540, 360, 150, 40, self.green1, self.green1, self.green1, self.green1, "Saving Account", self.font3, self.white, 14, 2, 5)
        else:
            self.saving_sender_rect = self.button_hover("Saving Account", 540, 360, 150, 40, self.grey, self.green1, self.grey, self.green1, "Saving Account", self.font3, self.grey2, 14, 2, 5)

        self.input_description_rect = self.button_hover("Description", 460, 430, 310, 40, self.grey, self.green1, self.grey, self.green1, self.input_description, self.font3, self.grey2, 14, 2, 5)

        self.input_amont_rect = self.button_hover("Amount", 460, 570, 310, 40, self.grey, self.green1, self.grey, self.green1, self.input_amount, self.font3, self.grey2, 14, 2, 5)

        # Category
        if self.input_number_category == "1":
            self.category = "Living Expenses"
        elif self.input_number_category == "2":
            self.category = "Transportation Costs"
        elif self.input_number_category == "3":
            self.category = "Food and Grocery Expense"
        elif self.input_number_category == "4":
            self.category = "Personal Expenses"
        elif self.input_number_category == "5":
            self.category = "Financial Obligations"
        else:
            self.category = "Category"

        self.button_hover("Category", 420, 500, 220, 40, self.grey, self.green1, self.grey, self.green1, self.category, self.font3, self.grey2, 14, 2, 5)
        self.input_number_category_rect = self.button_hover("number", 560, 500, 40, 40, self.grey, self.green1, self.grey, self.green1, self.input_number_category, self.font3, self.grey2, 14, 2, 5)
        self.question_rect = self.img_not_center("question", 585, 490, 25, 25, self.images["question"])

        if self.is_mouse_over_button(self.question_rect ):
            self.text_not_center(self.font4, 12, "1 = Living Expenses", self.grey2, 320, 605)
            self.text_not_center(self.font4, 12, "2 = Transportation Costs", self.grey2, 320, 625)
            self.text_not_center(self.font4, 12, "3 = Food and Grocery Expense", self.grey2, 320, 645)
            self.text_not_center(self.font4, 12, "4 = Personal Expenses", self.grey2, 520, 605)
            self.text_not_center(self.font4, 12, "5 = Financial Obligations", self.grey2, 520, 625)

        # Receiver
        self.text_not_center(self.font1, 18, "Receiver", self.grey2, 765, 225)

        self.input_name_receiver_rect = self.button_hover("Name",720, 290, 150, 40, self.grey, self.green1, self.grey, self.green1, self.input_name_receiver, self.font3, self.grey2, 14, 2, 5)

        self.input_surname_receiver_rect = self.button_hover("Surname", 880, 290, 150, 40, self.grey, self.green1, self.grey, self.green1, self.input_surname_receiver, self.font3, self.grey2, 14, 2, 5) 

        self.input_iban_receiver_rect = self.button_hover("IBAN", 800, 360, 310, 40, self.grey, self.green1, self.grey, self.green1, self.input_iban_receiver, self.font3, self.grey2, 14, 2, 5)

        # Send money to yourself
        self.text_not_center(self.font1, 18, "Transfer to yourself", self.grey2, 720, 430)

        if self.checking_receiver:
            self.checking_receiver_rect = self.button_hover("Checking Account", 720, 500, 150, 40, self.green1, self.green1, self.green1, self.green1, "Checking Account", self.font3, self.white, 14, 2, 5)
        else:
            self.checking_receiver_rect = self.button_hover("Checking Account", 720, 500, 150, 40, self.grey, self.green1, self.grey, self.green1, "Checking Account", self.font3, self.grey2, 14, 2, 5)

        if self.saving_receiver:
            self.saving_receiver_rect = self.button_hover("Saving Account", 880, 500, 150, 40, self.green1, self.green1, self.green1, self.green1, "Saving Account", self.font3, self.white, 14, 2, 5)
        else:
            self.saving_receiver_rect = self.button_hover("Saving Account", 880, 500, 150, 40, self.grey, self.green1, self.grey, self.green1, "Saving Account", self.font3, self.grey2, 14, 2, 5)
        if self.error_ops:
            self.text_center(self.font4, 15, "Choose an option", self.red2, 455, 326)
        if self.error_de:
            self.text_center(self.font4, 15, "Invalid Input", self.red2, 575, 400)
        if self.error_nc:
            self.text_center(self.font4, 15, "Invalid Input", self.red2, 575, 470)
        if self.error_at:
            self.text_center(self.font4, 15, "Invalid Input", self.red2, 575, 540)
        if self.error_ne:
            self.text_center(self.font4, 15, "Invalid Input", self.red2, 755, 260)
        if self.error_se:
            self.text_center(self.font4, 15, "Invalid Input", self.red2,  915, 260)
        if self.error_ib:
            self.text_center(self.font4, 15, "Invalid Input", self.red2,  915, 330)
        if self.error_opr:
            self.text_center(self.font4, 15, "Choose an option", self.red2,  795, 466)
        if self.transfer_money_message:
            self.text_center(self.font4, 15, "Transaction successful!", self.green, 855, 640)

        # Validation button
        self.confirm_button_rect = self.button_hover("validation", 855, 600, 200, 40, self.green2, self.green2, self.green1, self.green1, "CONFIRM BANK TRANSFER", self.font3, self.white, 14, 2, 5)

        self.transaction_event = True

    def notification(self):
        new_notif = 0
        for transaction in self.transactions:
            if transaction[5] > self.last_login_date:
                new_notif = new_notif + 1
        return new_notif

    def homepage_run(self):
        if self.accounts_running:
            self.background()
            self.side_bar()
            self.main_page_design()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pass
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.transfer_rect.collidepoint(event.pos):
                        self.profile_display, self.checking_saving_display, self.checking_saving_event, self.transfer_display, self.transaction_event, self.home_event = False, False, False, True, False, False
                        self.welcome_message = self.welcome_message_list[4] 

                    elif self.home_rect.collidepoint(event.pos):
                        self.profile_display, self.checking_saving_display, self.transfer_display, self.checking_saving_event, self.transaction_event, self.home_event = False, False, False, False, False, True 
                        self.welcome_message = self.welcome_message_list[1]                      
                        self.transactions = self.display_transaction(self.user_id,1, None, None, None)

                    elif self.checking_rect.collidepoint(event.pos):
                        self.welcome_message = self.catch_phrase(1)
                        self.account_type = 1
                        self.profile_display, self.checking_saving_display, self.home_event, self.transaction_event = False, True, False, False
                        self.welcome_message = self.welcome_message_list[2] 

                    elif self.saving_rect.collidepoint(event.pos):
                        self.account_type = 2
                        self.profile_display, self.checking_saving_display, self.transfer_display, self.transaction_event, self.home_event = False, True, False, False, False
                        self.welcome_message = self.welcome_message_list[3] 

                    elif self.profile_rect.collidepoint(event.pos):
                        self.profile_display, self.checking_saving_display, self.transfer_display, self.checking_saving_event, self.transaction_event, self.home_event = True, False, False, False, False, False
                        self.welcome_message = self.welcome_message_list[0] 

                    elif self.log_out_rect.collidepoint(event.pos):
                        self.disconnected = True
                        self.accounts_running = False
                        self.save_last_co(self.user_id)

                    # Event Saving & Checking
                    if self.checking_saving_event:
                        if event.button == 4 and self.scroll < 0 :
                            self.scroll += 15
                        elif event.button == 5:
                            self.scroll -= 15
                        else:
                            if self.date_rect.collidepoint(event.pos):
                                self.display_category_description = False
                                self.scroll = 0
                                if self.date_sort:
                                    self.transactions = self.display_transaction(self.user_id,1, None, None, None)
                                    self.date_sort = False
                                else:
                                    self.transactions = self.display_transaction(self.user_id,2, None, None, None)
                                    self.date_sort = True
                            elif self.income_rect.collidepoint(event.pos):
                                self.scroll = 0
                                self.display_category_description = False
                                self.transactions = self.display_transaction(self.user_id,3, None, None, None)

                            elif self.expense_rect.collidepoint(event.pos):
                                self.scroll = 0
                                self.display_category_description = False
                                self.transactions = self.display_transaction(self.user_id,4, None, None, None)

                            elif self.ascending_rect.collidepoint(event.pos):
                                self.scroll = 0
                                self.display_category_description = False
                                self.transactions = self.display_transaction(self.user_id,5, None, None, None)

                            elif self.descending_rect.collidepoint(event.pos):
                                self.scroll = 0
                                self.display_category_description = False
                                self.transactions = self.display_transaction(self.user_id, 6, None, None, None)

                            elif self.calendar_rect.collidepoint(event.pos): 
                                self.scroll = 0
                                self.ddisplay_start_end_date = False
                                if self.display_start_end_date:
                                    self.display_start_end_date = False
                                else:
                                    self.display_start_end_date= True  

                            elif self.display_start_end_date:    

                                if self.validate_rect.collidepoint(event.pos) :
                                    try:
                                        self.display_category_description = False
                                        self.transactions = self.display_transaction(self.user_id, 7, None, self.input_start_date, self.input_end_date)
                                    except: 
                                        self.calendar_error = True

                            elif self.type_rect.collidepoint(event.pos):
                                self.scroll = 0
                                self.display_category_description = True
                                self.transactions = self.display_transaction(self.user_id,8, self.sort_category, None, None)
                                if self.sort_category < 5:
                                    self.sort_category += 1
                                else:
                                    self.sort_category = 0

                        if self.display_start_end_date: 
                            try:
                                if self.input_start_date_rect.collidepoint(event.pos):
                                    self.input_start_date = ""
                                    self.entry = 9
                                    self.calendar_error = False
                                

                                elif self.input_end_date_rect.collidepoint(event.pos):
                                    self.input_end_date = ""
                                    self.entry = 10
                                    self.calendar_error = False
                            except:
                                pass
                

                    # Event Transaction
                    if self.transaction_event:
                        if self.checking_sender_rect.collidepoint(event.pos):
                            self.checking_sender = not self.checking_sender
                            self.saving_sender = False
                            self.error_ops = False
                            self.transfer_money_message = False

                        elif self.saving_sender_rect.collidepoint(event.pos):
                            self.saving_sender = not self.saving_sender
                            self.checking_sender = False
                            self.error_ops = False
                            self.transfer_money_message = False

                        elif self.input_description_rect.collidepoint(event.pos):
                            if self.input_description == "Description":
                                self.input_description = ""
                            self.error_de = False
                            self.entry = 3
                            self.transfer_money_message = False

                        elif self.input_number_category_rect.collidepoint(event.pos):
                            if self.input_number_category == "1-5":
                                self.input_number_category = ""
                            self.error_nc = False
                            self.entry = 4
                            self.transfer_money_message = False

                        elif self.input_amont_rect.collidepoint(event.pos):
                            if self.input_amount == "Amount":
                                self.input_amount = ""
                            self.error_at = False
                            self.entry = 5
                            self.transfer_money_message = False

                        elif self.input_name_receiver_rect.collidepoint(event.pos):
                            if self.input_name_receiver == "Name":
                                self.input_name_receiver = ""
                            self.error_ne = False
                            self.entry = 6
                            self.transfer_money_message = False

                        elif self.input_surname_receiver_rect.collidepoint(event.pos):
                            if self.input_surname_receiver == "Surname":
                                self.input_surname_receiver = ""
                            self.error_se = False
                            self.entry = 7
                            self.transfer_money_message = False

                        elif self.input_iban_receiver_rect.collidepoint(event.pos):
                            if self.input_iban_receiver  == "IBAN":
                                self.input_iban_receiver = ""
                            self.error_ib = False
                            self.entry = 8
                            self.transfer_money_message = False

                        elif self.checking_receiver_rect.collidepoint(event.pos):
                            self.checking_receiver = not self.checking_receiver
                            self.saving_receiver = False
                            self.error_opr = False
                            self.transfer_money_message = False

                        elif self.saving_receiver_rect.collidepoint(event.pos):
                            self.saving_receiver = not self.saving_receiver
                            self.checking_receiver = False
                            self.error_opr = False
                            self.transfer_money_message = False

                        elif self.confirm_button_rect.collidepoint(event.pos):
                            if (not self.input_description or
                                not self.input_number_category or
                                not self.input_amount or
                                not self.input_name_receiver or
                                not self.input_surname_receiver or
                                not self.input_iban_receiver or
                                not self.checking_sender and
                                not self.saving_sender or
                                not self.checking_receiver and
                                not self.saving_receiver):
                                if self.input_description == "Description" or self.input_description == "":
                                    self.error_de = True
                                if self.input_number_category == "1-5" or self.input_number_category == "":
                                    self.error_nc = True
                                if self.input_amount == "Amount" or self.input_amount == "":
                                    self.error_at = True
                                if self.input_name_receiver == "Name" or self.input_name_receiver == "":
                                    self.error_ne = True
                                if self.input_surname_receiver == "Surname" or self.input_surname_receiver == "":
                                    self.error_se = True
                                if self.input_iban_receiver == "IBAN" or self.input_iban_receiver == "":
                                    self.error_ib = True
                                if not self.checking_sender and not self.saving_sender:
                                    self.error_ops = True
                                if not self.checking_receiver and not self.saving_receiver:
                                    self.error_opr = True
                            else:
                                self.current_date = datetime.now()
                                if not self.checking_receiver and not self.saving_receiver:
                                    self.id_receiver  = self.get_id_receiver()
                                    self.new_transaction_account_id = 1
                                    self.transfer_money()
                                else:
                                    self.id_receiver = self.user_id

                                    if self.checking_receiver and not self.saving_receiver:
                                        self.new_transaction_account_id = 1
                                    if self.saving_receiver and not self.checking_receiver:
                                        self.new_transaction_account_id = 2
                                    self.transfer_money()
                                    self.transactions = self.display_transaction(self.user_id, 1, None, None, None)
                                    self.display_notif = self.notification()

                                self.error_de = False
                                self.error_nc = False
                                self.error_at = False
                                self.error_ne = False
                                self.error_se = False
                                self.error_ib = False
                                self.error_ops = False
                                self.error_opr = False
                                self.transfer_money_message = True
                                self.checking_sender = False
                                self.saving_sender = False
                                self.checking_receiver = False
                                self.saving_sender = False
                                self.input_description = "Description"
                                self.input_number_category = "1-5"
                                self.input_amount = "Amount"
                                self.input_name_receiver = "Name"
                                self.input_surname_receiver  = "Surname"
                                self.input_iban_receiver = "IBAN"
                    if self.home_event:
                        if self.last_month.collidepoint(event.pos):
                            self.transactions = self.display_transaction(self.user_id, 9, 30, None, None)
                        elif self.three_last_month.collidepoint(event.pos):
                            self.transactions = self.display_transaction(self.user_id, 9, 90, None, None)
                        elif self.last_year.collidepoint(event.pos):
                            self.transactions = self.display_transaction(self.user_id, 9, 365, None, None)
                        elif self.all_time.collidepoint(event.pos):
                            self.transactions = self.display_transaction(self.user_id, 1, None, None, None)

                if self.transaction_event:
                    if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_BACKSPACE:
                                if self.entry == 3:
                                    self.input_description = self.input_description[:-1]
                                elif self.entry == 4:
                                    self.input_number_category = self.input_number_category[:-1]
                                elif self.entry == 5:
                                    self.input_amount = self.input_amount[:-1]
                                elif self.entry == 6:
                                    self.input_name_receiver = self.input_name_receiver[:-1]
                                elif self.entry == 7:
                                    self.input_surname_receiver = self.input_surname_receiver[:-1]
                                elif self.entry == 8:
                                    self.input_iban_receiver = self.input_iban_receiver[:-1]
                            else:
                                if self.entry == 3 and len(self.input_description) < 32:
                                    self.input_description += event.unicode

                                elif self.entry == 4 and len(self.input_number_category) < 1:
                                    if event.unicode.isdigit():
                                        self.input_number_category += event.unicode

                                elif self.entry == 5 and len(self.input_amount) < 6:
                                    if event.unicode.isdigit():
                                        self.input_amount += event.unicode

                                elif self.entry == 6 and len(self.input_name_receiver) < 16:
                                    self.input_name_receiver += event.unicode

                                elif self.entry == 7 and len(self.input_surname_receiver) < 16:
                                    self.input_surname_receiver += event.unicode

                                elif self.entry == 8 and len(self.input_iban_receiver) < 22:
                                    if event.unicode.isupper() or event.unicode.isdigit():
                                        self.input_iban_receiver += event.unicode

                    # Saving & Checking
                    elif self.checking_saving_event:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_BACKSPACE:
                                if self.entry == 9:
                                    self.input_start_date = self.input_start_date[:-1]
                                elif self.entry == 10:
                                    self.input_end_date = self.input_end_date[:-1]
                            else:
                                if self.entry == 9 and len(self.input_start_date) < 10:
                                    self.input_start_date += event.unicode

                                elif self.entry == 10 and len(self.input_end_date) < 10:
                                    self.input_end_date += event.unicode
