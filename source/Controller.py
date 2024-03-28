from hashlib import sha256

from data.UserRepository import UserRepository
class Controller(UserRepository):

    def __init__(self):
        UserRepository.__init__(self)

        # Home
        self.input_email = ""
        self.input_password = ""

        self.input_first_name_register = ""
        self.input_last_name_register = ""

        self.input_email_register = ""
        self.input_password_register = ""

        self.account_number = ""

        self.sort_code_1 = ""
        self.sort_code_2 = ""
        self.sort_code_3 = ""

        self.connected = False

    def login_user(self):
        hashed_password = sha256(self.input_password.encode()).hexdigest()

        if self.check_credentials(self.input_email, hashed_password):
            self.user = self.get_user(self.input_email, hashed_password)
            self.connected = True
            return self.user
