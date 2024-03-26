from hashlib import sha256

from data.BudgetManager import BudgetManager
class Controller(BudgetManager):

    def __init__(self):
        super().__init__()

        # Home
        self.input_email = "Email"
        self.input_password = "Password" 

def login_user(self):
        
    hashed_password = sha256(self.input_password.encode()).hexdigest()

    if self.check_credentials(self.input_email, hashed_password):
        self.user_info = self.get_user(self.input_email, hashed_password)
        self.connected = True
        return self.user_info