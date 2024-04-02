import pygame
from source.pygame_manager.Element import Element
from source.Controller import Controller

class HomePage(Element, Controller):
    def __init__(self, user_info): 
        Element.__init__(self)
        Controller.__init__(self)
        self.user = user_info
        self.user_id, self.user_fisrt_name, self.user_last_name, self.user_email, self.user_iban, self.user_account_number, self.last_login_date = self.user[0], self.user[1], self.user[2], self.user[3], self.user[5], self.user[6], self.user[9]

        self.transactions = self.display_transaction(self.user_id, 1)
        self.date_sort = False

        self.checking_sender = False
        self.saving_sender = False
        self.checking_receiver = False
        self.saving_receiver = False

        self.not_conform = False
        self.transaction_event = False


        self.checking_saving_event = False
        self.scroll = 0
        self.accounts_running = True
        self.transaction_running = True
        self.disconnected = True

        self.entry = False

        # Main Page
        self.welcome_message = ""
        self.coin_angle = 0
        self.rotation_speed = 2    
        self.total_saving = str(self.display_total_amount(2, self.user_id))
        self.total_checking = str(self.display_total_amount(1, self.user_id))  
        self.total_account = str(int(self.total_saving) + int(self.total_checking))

        # Notification
        self.display_notif = self.notification()

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
        }

        self.images = {}
        for name, path in self.image_paths.items():
            self.images[name] = pygame.image.load(path)

        self.profile_display, self.checking_saving_display, self.transfer_display = False, False, False

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
        self.text_not_center(self.font2, 13, self.user[7], self.white, 765, 75)

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
        self.text_not_center(self.font1, 15, f"{self.user[1]} { self.user[2]}", self.grey3, 70, 270)
        self.profile_rect = self.button_hover_small("My Profil", 140, 320, 190, 40, self.green2, self.green2, self.green2, self.green2, "My Profil", self.font1, self.white,15, 0, 3
        )

        # Lines h top bar
        pygame.draw.line(self.Window, self.grey3, (100, 375), (180, 375), 3)
        pygame.draw.line(self.Window, self.grey3, (100, 535), (180, 535), 3)

        # Accounts
        self.checking_rect = self.button_hover_small("Checking Accounts", 140, 430, 190, 40, self.green2, self.green2, self.green2, self.green2, "Checking Accounts", self.font1, self.white,15, 0, 3
        )
        # Saving Account
        self.saving_rect = self.saving_rect = self.button_hover_small("Saving Account", 140, 480, 190, 40, self.green2, self.green2, self.green2, self.green2, "Saving Account", self.font1, self.white,15, 0, 3
        )

        self.transfer_rect = self.button_hover_small("Transfer money", 140, 590, 190, 40, self.green2, self.green2, self.green2, self.green2, "Transfer money", self.font1, self.white,15, 0, 3
        )

        # Help
        self.img_hover("help", "help", 60, 650, 30, 30,self.images["help"],self.images["help"])
        self.text_not_center(self.font4, 12, "Need Help ?", self.grey2, 80, 645)

    def main_section (self):
        self.rect_full(self.grey, 630, 420, 700, 530, 5)
        self.rect_border(self.green2, 630, 420, 700, 530, 2, 5)
        self.rect_radius_top(self.green3, 630, 175, 700, 45, 5)

    def all_accounts(self):

        pygame.draw.line(self.Window, self.grey3, (315, 280), (605, 280), 1)
        self.text_not_center(self.font1, 35, self.total_account, self.green1, 405, 230)
        self.text_not_center(self.font1, 18, "Total Balance", self.grey2, 405, 290)

        # Checking Account
        self.rect_full(self.green1, 460, 410, 300, 150, 5)
        self.img_hover("Circle", "Circle", 530, 410, 110, 110,self.images["circle"],self.images["circle"])
        self.text_not_center(self.font4, 15, self.total_checking, self.white, 500, 405)
        self.text_not_center(self.font1, 14, "CHECKING ACCOUNT", self.white, 330, 370)
        self.text_not_center(self.font4, 12,f"Sort Code  — {self.user[5]}", self.white, 330, 400)
        self.text_not_center(self.font4, 12, f"Account ID — { self.user[7]}", self.white, 330, 430)
        self.text_not_center(self.font4, 12, f"{self.user[1]} { self.user[2]}", self.white, 330, 460)

        # Saving Account
        self.rect_full(self.green1, 460, 580, 300, 150, 5)
        self.img_hover("Circle", "Circle", 530, 580, 110, 110,self.images["circle"],self.images["circle"])
        self.text_not_center(self.font4, 15, self.total_saving, self.white, 500, 575)
        self.text_not_center(self.font1, 14, "SAVING ACCOUNT", self.white, 330, 540)
        self.text_not_center(self.font4, 12, f"Sort Code — {self.user[5]}", self.white, 330, 570)
        self.text_not_center(self.font4, 12,f"Account ID  — { self.user[7]}", self.white, 330, 600)
        self.text_not_center(self.font4, 12,f"{self.user[1]} { self.user[2]}", self.white, 330, 630)

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

    # Diagramme
    def diagram(self):
        pass     
      
    
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

            if self.pos_y < 425:
                self.text_not_center(self.font3, 10,str(transaction[6]), self.black, 450, self.pos_y + 252.5)
                self.text_not_center(self.font3, 10,f"{str(transaction[5].day)}/{str(transaction[5].month)}/{str(transaction[5].year)}", self.black, 460, self.pos_y + 252.5)
                self.text_not_center(self.font3, 15, str(transaction[2]), self.black, 530, self.pos_y + 250)
                self.text_not_center(self.font3, 12, str(transaction[3]), self.black, 750, self.pos_y + 251.5)
                self.text_not_center(self.font3, 12, str(transaction[4]), self.black, 938, self.pos_y + 250)
                self.text_not_center(self.font3, 12, "£", self.black, 930, self.pos_y + 250)
                if transaction[8] == self.user_id:
                    self.text_not_center(self.font1, 18, "-", self.red, 920, self.pos_y + 250)
                elif transaction[9] == self.user_id:
                    self.text_not_center(self.font1, 18, "+", self.green, 920, self.pos_y + 250)

                y += 25

        self.rect_full(self.grey, 630, 220, 700, 50, 0)
        self.rect_border(self.green2, 630, 420, 700, 530, 2, 5)
        self.rect_radius_top(self.green3, 630, 175, 700, 45, 5)
        self.text_not_center(self.font2, 17,"Date", self.black, 464, 210)
        self.text_not_center(self.font2, 17,"To / From", self.black, 535, 210)
        self.text_not_center(self.font2, 17, "Description", self.black, 740, 210)
        self.text_not_center(self.font2, 17, "Amount", self.black, 910, 210)

        if not self.checking_saving_event:
            self.checking_saving_event = True

        self.text_not_center(self.font1, 14, str(self.welcome_message[0][0]), self.white, 295, 170)

    def profile_design(self):

        # Name
        self.text_not_center(self.font1, 16, "Name", self.grey1, 330, 300)
        self.text_not_center(self.font2, 16, self.user[1], self.grey1, 390, 300)
        pygame.draw.line(self.Window, self.green4, (330, 330), (750, 330), 1)

        # Surname
        self.text_not_center(self.font1, 16, "Surname", self.grey1, 330, 350)
        self.text_not_center(self.font2, 16,self.user[2], self.grey1, 420, 350)
        pygame.draw.line(self.Window, self.green4, (330, 380), (750, 380), 1)

        # Email
        self.text_not_center(self.font1, 16, "Email", self.grey1, 330, 400)
        self.text_not_center(self.font2, 16, self.user[3], self.grey1, 400, 400)
        pygame.draw.line(self.Window, self.green4, (330, 430), (750, 430), 1)

        # Account ID
        self.text_not_center(self.font1, 16, "Account ID Number", self.grey1, 330, 450)
        self.text_not_center(self.font2, 16, self.user[7], self.grey1,500, 450)
        pygame.draw.line(self.Window, self.green4, (330, 480), (750, 480), 1)

        # SORT CODE
        self.text_not_center(self.font1, 16, "Sort Code", self.grey1, 330, 500)
        self.text_not_center(self.font2, 16, str(self.user[5]), self.grey1, 480, 500)
        pygame.draw.line(self.Window, self.green4, (330, 530), (750, 530), 1)

        # IBAN
        self.text_not_center(self.font1, 16, "IBAN", self.grey1, 330, 550)
        self.text_not_center(self.font2, 16, self.user[6], self.grey1, 380, 550)
        pygame.draw.line(self.Window, self.green4, (330, 580), (750, 580), 1)

    def filter_options(self):

        # Filter by date
        self.text_not_center(self.font3, 18, "Sort by", self.grey2, 305, 290)
        self.date_rect = self.img_txt_hover("date", "Date", 320, 350, 35, 35, self.images["date"], self.images["date"], self.font3, 15, self.grey3,345, 340)
        # Filter by income
        self.income_rect = self.img_txt_hover("income", "Income", 320, 400, 35, 35, self.images["income"], self.images["income"], self.font3, 15, self.grey3,345, 390)
        # Filter by expense
        self.expense_rect = self.img_txt_hover("expense", "Expense", 320, 450, 35, 35, self.images["expense"], self.images["expense"], self.font3, 15, self.grey3,345, 440)
        # Filter by amount descending
        self.descending_rect = self.img_txt_hover("descending", "Descending", 320, 500, 35, 35, self.images["descending"], self.images["descending"], self.font3, 15, self.grey3,345, 490)
        # Filter by amount ascending
        self.ascending_rect = self.img_txt_hover("ascending", "Ascending", 320, 550, 35, 35, self.images["ascending"], self.images["ascending"], self.font3, 15, self.grey3,345, 540)
        # Filter by period
        self.calendar_rect = self.img_txt_hover("calendar", "Calendar", 320, 600, 35, 35, self.images["calendar"], self.images["calendar"], self.font3, 15, self.grey3,345, 590)
        # Filter by type
        self.category_rect = self.img_txt_hover("type", "Type", 320, 650, 35, 35, self.images["type"], self.images["type"], self.font3, 15, self.grey3,345, 640)

    def transaction_design(self):

        # Sender
        self.text_not_center(self.font1, 18, "Sender", self.grey2, 450, 225)
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
        self.text_not_center(self.font1, 18, "Receiver", self.grey2, 780, 225)
        self.input_name_receiver_rect = self.button_hover("Name",720, 290, 150, 40, self.grey, self.green1, self.grey, self.green1, self.input_name_receiver, self.font3, self.grey2, 14, 2, 5)
        self.input_surname_receiver_rect = self.button_hover("Surname", 880, 290, 150, 40, self.grey, self.green1, self.grey, self.green1, self.input_surname_receiver, self.font3, self.grey2, 14, 2, 5) 
        self.input_iban_receiver_rect = self.button_hover("IBAN", 800, 360, 310, 40, self.grey, self.green1, self.grey, self.green1, self.input_iban_receiver, self.font3, self.grey2, 14, 2, 5)

        # Send money to yourself
        self.text_not_center(self.font1, 18, "Transfer to yourself", self.grey2, 700, 430)

        if self.checking_receiver:
            self.checking_receiver_rect = self.button_hover("Checking Account", 720, 500, 150, 40, self.green1, self.green1, self.green1, self.green1, "Checking Account", self.font3, self.white, 14, 2, 5)
        else:
            self.checking_receiver_rect = self.button_hover("Checking Account", 720, 500, 150, 40, self.grey, self.green1, self.grey, self.green1, "Checking Account", self.font3, self.grey2, 14, 2, 5)

        if self.saving_receiver:
            self.saving_receiver_rect = self.button_hover("Saving Account", 880, 500, 150, 40, self.green1, self.green1, self.green1, self.green1, "Saving Account", self.font3, self.white, 14, 2, 5)
        else:
            self.saving_receiver_rect = self.button_hover("Saving Account", 880, 500, 150, 40, self.grey, self.green1, self.grey, self.green1, "Saving Account", self.font3, self.grey2, 14, 2, 5)

        # Validation button
        self.confirm_button_rect = self.button_hover("validation", 855, 600, 200, 40, self.green2, self.green2, self.green1, self.green1, "CONFIRM BANK TRANSFER", self.font3, self.white, 14, 2, 5)

        # Error Message
        if self.not_conform:
            self.text_not_center(self.font1, 12, "Oops, something has gone wrong ", self.red, 770, 630)

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
                        self.profile_display, self.checking_saving_display, self.checking_saving_event, self.transfer_display, self.transaction_event = False, False, False, True, False

                    elif self.checking_rect.collidepoint(event.pos):
                        self.welcome_message = self.catch_phrase(1)
                        self.profile_display, self.checking_saving_display, self.transfer_display = False, True, False

                    elif self.saving_rect.collidepoint(event.pos):
                        self.welcome_message = self.catch_phrase(2)
                        self.profile_display, self.checking_saving_display, self.transfer_display, self.transaction_event = False, True, False, False
                    
                    elif self.profile_rect.collidepoint(event.pos):
                        self.profile_display, self.checking_saving_display, self.transfer_display, self.checking_saving_event, self.transaction_event = True, False, False, False, False

                    elif self.log_out_rect.collidepoint(event.pos):
                        self.disconnected = True
                        self.accounts_running = False

                    if self.checking_saving_event:
                        if event.button == 4 and self.scroll < 0 :
                            self.scroll += 15
                        elif event.button == 5:
                            self.scroll -= 15
                        else:
                            if self.date_rect.collidepoint(event.pos):
                                if self.date_sort:
                                    self.transactions = self.display_transaction(self.user_id,1)
                                    self.date_sort = False
                                else:
                                    self.transactions = self.display_transaction(self.user_id,2)
                                    self.date_sort = True
                            elif self.income_rect.collidepoint(event.pos):
                                self.transactions = self.display_transaction(self.user_id,3)

                            elif self.expense_rect.collidepoint(event.pos):
                                self.transactions = self.display_transaction(self.user_id,4)

                            elif self.ascending_rect.collidepoint(event.pos):
                                self.transactions = self.display_transaction(self.user_id,5)

                            elif self.descending_rect.collidepoint(event.pos):
                                self.transactions = self.display_transaction(self.user_id,6)

                            # elif self.calendar_rect.collidepoint(event.pos):
                            #     self.transactions = self.display_transaction(self.user_id,7)

                            elif self.calendar_rect.collidepoint(event.pos):
                                self.transactions = self.display_transaction(self.user_id,8)

                    if self.transaction_event:
                        if self.checking_sender_rect.collidepoint(event.pos):
                            self.checking_sender = not self.checking_sender

                        elif self.saving_sender_rect.collidepoint(event.pos):
                            self.saving_sender = not self.saving_sender

                        elif self.input_description_rect.collidepoint(event.pos):
                            if self.input_description == "Description":
                                self.input_description = ""
                            self.entry = 3

                        elif self.input_number_category_rect.collidepoint(event.pos):
                            if self.input_number_category == "1-7":
                                self.input_number_category = ""
                            self.entry = 4

                        elif self.input_amont_rect.collidepoint(event.pos):
                            if self.input_amount == "Amount":
                                self.input_amount = ""
                            self.entry = 5

                        elif self.input_name_receiver_rect.collidepoint(event.pos):
                            if self.input_name_receiver == "Name":
                                self.input_name_receiver = ""
                            self.entry = 6

                        elif self.input_surname_receiver_rect.collidepoint(event.pos):
                            if self.input_surname_receiver == "Surname":
                                self.input_surname_receiver = ""
                            self.entry = 7

                        elif self.input_iban_receiver_rect.collidepoint(event.pos):
                            if self.input_iban_receiver  == "IBAN":
                                self.input_iban_receiver = ""
                            self.entry = 8

                        elif self.checking_receiver_rect.collidepoint(event.pos):
                            self.checking_receiver = not self.checking_receiver

                        elif self.saving_receiver_rect.collidepoint(event.pos):
                            self.saving_receiver = not self.saving_receiver

                        elif self.confirm_button_rect.collidepoint(event.pos):
                            pass
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
                                    if event.unicode.isupper():
                                        self.input_iban_receiver += event.unicode