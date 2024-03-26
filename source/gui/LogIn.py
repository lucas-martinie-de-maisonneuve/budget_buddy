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

    def gui_register(self):

        self.screen_color(self.white)

        # Rect principal
        self.rect_full(self.green3, self.W//2, self.H//2, 950, 650, 10)
        self.rect_border(self.green3, self.W//2, self.H//2, 950, 650, 2, 10)

        # About you
        self.text_center(self.font1, 15, "About you", self.white, self.W//2-425, self.H//2-300)

        self.text_center(self.font1, 15, "First Name", self.white, self.W//2-415, self.H//2-265)
        self.input_first_name_register_rect = self.button_hover("First Name", self.W//2-280, self.H//2-225, 350, 50, self.green2, self.green, self.green2, self.green, self.input_first_name_register, self.font1, self.white,15, 1, 5)
        self.text_center(self.font1, 15, "Last Name", self.white, self.W//2-415, self.H//2-180)
        self.input_last_name_register_rect = self.button_hover("Last Name", self.W//2-280, self.H//2-140, 350, 50, self.green2, self.green, self.green2, self.green, self.input_last_name_register, self.font1, self.white,15, 1, 5)

        self.text_center(self.font1, 15, "Email", self.white, self.W//2-430, self.H//2-95)
        self.input_email_register_rect = self.button_hover("Email", self.W//2-280, self.H//2-55, 350, 50, self.green2, self.green, self.green2, self.green, self.input_email_register, self.font1, self.white,15, 1, 5)
        self.text_center(self.font1, 15, "Password", self.white, self.W//2-415, self.H//2-10)
        self.input_password_register_rect = self.button_hover("Password", self.W//2-280, self.H//2+30, 350, 50, self.green2, self.green, self.green2, self.green, self.input_password_register, self.font1, self.white, 15, 1, 5)

        # Your account
        self.text_center(self.font1, 15, "Your account", self.white, self.W//2, self.H//2-300)
        self.text_center(self.font1, 15, "Your account type", self.white, self.W//2+15, self.H//2-265)

        # self.input_account_number_rect = self.button_hover("Account Number", self.W//2+220, 320, 350, 50, self.green2, self.green, self.green2, self.green, self.input_password, self.font1, self.white, 15, 1, 5)

        # # Terms & conditions
        # self.text_center(self.font1, 15, "Please read the Internet Banking terms and conditions and our Data Privacy Notice.", self.white, self.W//2+220, 450)
        # self.text_center(self.font1, 15, "I agree to the Internet Banking terms and conditions", self.white, self.W//2+220, 450)
        # self.checkbox_rect = self.rect_full(self.green3, self.W//2, self.H//2, 950, 650, 2)

        # # Register button
        # self.register_rect = self.button_hover("Register", self.W//2+220, 390, 350, 50, self.green, self.green, self.green, self.green,"Register", self.font1, self.white, 19, 1, 5)


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

            self.gui_register()
            self.update()
