import pygame, random
from source.pygame_manager.Element import Element
from source.pygame_manager.Animation import Animation
from source.Controller import Controller
from source.gui.HomePage import HomePage

class LogIn(Element, Animation, Controller):
    def __init__(self):
        Element.__init__(self)
        Animation.__init__(self)
        Controller.__init__(self)

        self.entry = False
        self.switch = False
        self.checkbox = False
        self.current_account = False
        self.savings_account = False

        self.sort_code_un = self.random_sort_code()
        self.sort_code_deux = self.random_sort_code()
        self.sort_code_trois = self.random_sort_code()

        self.fixed_account_number = self.random_account_number()

        self.image_paths = {
            "twitter": "assets/image/LogIn/login_twitter.png",
            "instagram": "assets/image/LogIn/login_instagram.png",
            "facebook": "assets/image/LogIn/login_facebook.png",
            "background": "assets/image/LogIn/login_background.png"
        }

        self.images = {}
        for name, path in self.image_paths.items():
            self.images[name] = pygame.image.load(path)

    def random_sort_code(self):
        return random.randint(10, 99)

    def random_account_number(self):
        return random.randint(100000, 999999)

    def gui_home(self):

        # Background
        self.img_background(400, 300, 1244, 830, self.images["background"])

        # Rect principal
        self.rect_full(self.green3, self.W//2+220, self.H//2, 400, 580, 10)
        self.rect_border(self.white, self.W//2+220, self.H//2, 400, 580, 1, 10)
 
        # Bank Name
        self.text_center(self.font1, 35, "Wildcat Wealth Bank", self.white, self.W//2+220, 140)
        self.text_center(self.font4, 16, "Where Panthers Guard Your Fortune!", self.white, self.W//2+220, 180)

        # Email        
        self.input_email_rect = self.button_hover("Email", self.W//2+220, 250, 350, 50, self.green2, self.green2, self.green2, self.green2, self.input_email, self.font4, self.white,18, 1, 5)
        self.text_input(self.input_email_rect, self.input_email, "Email address", 720, 250, 350, 50, id="email_login")

        # Password
        self.input_password_rect = self.button_hover("Password", self.W//2+220, 320, 350, 50, self.green2, self.green2, self.green2, self.green2, self.input_password, self.font4, self.white, 18, 1, 5)
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
        self.signup_rect = pygame.draw.rect(self.Window, self.green3, [675, 490, 90, 20])
        self.sign = (pygame.Rect(675, 490, 90, 20))
        if self.is_mouse_over_button(self.sign):
            self.text_center(self.font4, 15, "Sign-in options", self.white, self.W//2+220, 500)
        else:
            self.text_center(self.font4, 13, "Sign-in options", self.white, self.W//2+220, 500)

    def gui_register(self):

        self.screen_color(self.white)

        # Rect principal
        self.rect_full(self.green3, self.W//2, self.H//2, 950, 650, 5)
        self.rect_border(self.green3, self.W//2, self.H//2, 950, 650, 15, 5)

        # About you
        self.text_center(self.font1, 25, "About you", self.white, self.W//2-400, self.H//2-300)

        self.input_first_name_register_rect = self.button_hover("", self.W//2-245, self.H//2-225, 350, 50, self.green2, self.green3, self.green2, self.green3, self.input_first_name_register, self.font1, self.white,15, 1, 5)
        self.text_center(self.font1, 15, "First Name", self.white, self.W//2-380, self.H//2-265)

        self.input_last_name_register_rect = self.button_hover("", self.W//2-245, self.H//2-140, 350, 50, self.green2, self.green3, self.green2, self.green3, self.input_last_name_register, self.font1, self.white,15, 1, 5)
        self.text_center(self.font1, 15, "Last Name", self.white, self.W//2-380, self.H//2-180)

        self.input_email_register_rect = self.button_hover("", self.W//2-245, self.H//2-55, 350, 50, self.green2, self.green3, self.green2, self.green3, self.input_email_register, self.font1, self.white,15, 1, 5)
        self.text_center(self.font1, 15, "Email", self.white, self.W//2-400, self.H//2-95)

        self.input_password_register_rect = self.button_hover("", self.W//2-245, self.H//2+30, 350, 50, self.green2, self.green3, self.green2, self.green3, self.input_password_register, self.font1, self.white, 15, 1, 5)
        self.text_center(self.font1, 15, "Password", self.white, self.W//2-385, self.H//2-10)

        # Your account
        self.text_center(self.font1, 25, "Your account", self.white, self.W//2+100, self.H//2-300)
        self.text_center(self.font1, 15, "Your account type", self.white, self.W//2+125, self.H//2-270)

        if self.current_account:
            self.input_account_Current = self.button_hover("Current Account", self.W//2+240, self.H//2-212, 350, 50, self.green, self.green3, self.green, self.green, "Current Account", self.font1, self.white, 15, 1, 5)
        else:
            self.input_account_Current = self.button_hover("Current Account", self.W//2+240, self.H//2-212, 350, 50, self.green2, self.green3, self.green2, self.green3, "Current Account", self.font1, self.white, 15, 1, 5)

        if self.savings_account:
            self.input_account_Savings = self.button_hover("Savings Account", self.W//2+240, self.H//2-158, 350, 50, self.green, self.green3, self.green, self.green, "Savings Account", self.font1, self.white, 15, 1, 5)
        else:
            self.input_account_Savings = self.button_hover("Savings Account", self.W//2+240, self.H//2-158, 350, 50, self.green2, self.green3, self.green2, self.green3, "Savings Account", self.font1, self.white, 15, 1, 5)


        self.text_center(self.font1, 15, "Sort Code", self.white, self.W//2+100, self.H//2-95)
        self.input_account_number_rect1 = self.button_hover("", self.W//2+122, self.H//2-55, 114, 50, self.green2, self.green3, self.green2, self.green3, str(self.sort_code_1), self.font1, self.white, 15, 1, 5)
        self.input_account_number_rect2 = self.button_hover("", self.W//2+240, self.H//2-55, 114, 50, self.green2, self.green3, self.green2, self.green3, str(self.sort_code_2), self.font1, self.white, 15, 1, 5)
        self.input_account_number_rect3 = self.button_hover("", self.W//2+358, self.H//2-55, 114, 50, self.green2, self.green3, self.green2, self.green3, str(self.sort_code_3), self.font1, self.white, 15, 1, 5)

        self.text_center(self.font1, 15, "Account Number", self.white, self.W//2+125, self.H//2-10)
        self.input_account_number_rect = self.button_hover("", self.W//2+240, self.H//2+30, 350, 50, self.green2, self.green3, self.green2, self.green3, str(self.account_number), self.font1, self.white, 15, 1, 5)

        # Terms & conditions
        self.text_center(self.font1, 20, "Terms and Conditions", self.white, self.W//2, self.H//2+145)
        self.text_center(self.font1, 15, "Please read the Internet Banking terms and conditions and our Data Privacy Notice.", self.white, self.W//2, self.H//2+175)
        self.checkbox_rect_rect = self.rect_full(self.green1, self.W//2, self.H//2+200, 500, 25, 2)
        self.text_center(self.font1, 15, "I agree to the Internet Banking terms and conditions", self.white, self.W//2, self.H//2+200)
        self.checkbox_rect = self.rect_full(self.green3, self.W//2-200, self.H//2+200, 15, 15, 2)

        # Register button
        self.register_rect = self.button_hover("Register", self.W//2, self.H//2+250, 350, 50, self.green, self.green, self.green, self.green,"Register", self.font1, self.white, 19, 1, 5)

        # Lines v top bar
        pygame.draw.line(self.Window, self.green, (self.W//2, self.H//2-250), (self.W//2, self.H//2+50), 2)
        pygame.draw.line(self.Window, self.green, (self.W//2-80, self.H//2+160), (self.W//2+80, self.H//2+160), 2)
        if self.checkbox:
            pygame.draw.line(self.Window, self.green, (self.W//2 - 200 - 6, self.H//2 + 200 - 6), (self.W//2 - 200 + 2, self.H//2 + 200 + 7), 4)
            pygame.draw.line(self.Window, self.green, (self.W//2 - 200 + 1, self.H//2 + 200 + 7), (self.W//2 - 200 + 8, self.H//2 + 200 - 12), 4)

    def login_run(self):
        login_running = True
        while login_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    login_running = False

                if not self.switch:
                    self.gui_home()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.input_email_rect.collidepoint(event.pos):
                            self.input_email = ""
                            self.entry = 1

                        elif self.input_password_rect.collidepoint(event.pos):
                            self.input_password = ""
                            self.entry = 2

                        elif self.login_rect.collidepoint(event.pos):
                            self.user = self.login_user()
                            if self.connected:
                                hp = HomePage(self.user)
                                hp.homepage_run()
                                self.connected = False

                        elif self.signup_rect.collidepoint(event.pos):
                            self.switch = True

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            if self.entry == 1:
                                self.input_email = self.input_email[:-1]
                            elif self.entry == 2:
                                self.input_password = self.input_password[:-1]
                        else:
                            if self.entry == 1:
                                if event.unicode:
                                    self.input_email += event.unicode

                            elif self.entry == 2:
                                self.input_password += event.unicode

                if self.switch:
                    self.gui_register()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.input_first_name_register_rect.collidepoint(event.pos):
                            self.input_first_name_register =""
                            self.entry = 3

                        elif self.input_last_name_register_rect.collidepoint(event.pos):
                            self.input_last_name_register = ""
                            self.entry = 4

                        elif self.input_email_register_rect.collidepoint(event.pos):
                            self.input_email_register = ""
                            self.entry = 5

                        elif self.input_password_register_rect.collidepoint(event.pos):
                            self.input_password_register = ""
                            self.entry = 6

                        elif self.input_account_Current.collidepoint(event.pos):
                            self.current_account = not self.current_account

                        elif self.input_account_Savings.collidepoint(event.pos):
                            self.savings_account = not self.savings_account

                        elif self.register_rect.collidepoint(event.pos):
                            self.switch = False

                        elif self.checkbox_rect.collidepoint(event.pos):
                            self.checkbox = not self.checkbox
                            if self.checkbox:
                                self.sort_code_1 = self.sort_code_un
                                self.sort_code_2 = self.sort_code_deux
                                self.sort_code_3 = self.sort_code_trois
                                self.account_number = self.fixed_account_number
                            else:
                                self.sort_code_1 = ""
                                self.sort_code_2 = ""
                                self.sort_code_3 = ""
                                self.account_number = ""

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            if self.entry == 3:
                                self.input_first_name_register = self.input_first_name_register[:-1]
                            elif self.entry == 4:
                                self.input_last_name_register = self.input_last_name_register[:-1]
                            elif self.entry == 5:
                                self.input_email_register = self.input_email_register[:-1]
                            elif self.entry == 6:
                                self.input_password_register = self.input_password_register[:-1]
                        else:
                            if self.entry == 3:
                                self.input_first_name_register += event.unicode
                            elif self.entry == 4:
                                self.input_last_name_register += event.unicode
                            elif self.entry == 5:
                                if event.unicode.islower():
                                    self.input_email_register +=  event.unicode
                            elif self.entry == 6:
                                self.input_password_register += event.unicode
                
                self.update()
