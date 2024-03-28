from hashlib import sha256

from data.BudgetManager import BudgetManager
class Controller(BudgetManager):

    def __init__(self):
        super().__init__()

        # Home
        self.input_email = ""
        self.input_password = ""

        self.input_first_name_register = "First Name"
        self.input_last_name_register = "Last Name"

        self.input_email_register = "Email"
        self.input_password_register = "Password"

    def login_user(self):
        hashed_password = sha256(self.input_password.encode()).hexdigest()

        if self.check_credentials(self.input_email, hashed_password):
            self.user_info = self.get_user(self.input_email, hashed_password)
            self.connected = True
            return self.user_info
    
    # def user_info(self):
