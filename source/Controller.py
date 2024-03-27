from hashlib import sha256

from data.BudgetManager import BudgetManager
class Controller(BudgetManager):

    def __init__(self):        
        BudgetManager.__init__(self)

        # Home
        self.input_email = ""
        self.input_password = ""

        self.input_first_name_register = "First Name"
        self.input_last_name_register = "Last Name"

        self.input_email_register = "Email"
        self.input_password_register = "Password"

        self.first_name = "Lucy"
        self.last_name = "Madec"
        self.email = "lucy.madecm@laplateforme.io"
        self.p = "$2y$10$qIBQqkFGuABUzh8HIv2m2ujXi/oebdIBtChVGz1P0ixyWudg01sDG"
        self.iban = "GB10abcd10203012345678"
        self.account_number = "523"

    def login_user(self):
        hashed_password = sha256(self.input_password.encode()).hexdigest()

        if self.check_credentials(self.input_email, hashed_password):
            self.user_info = self.get_user(self.input_email, hashed_password)
            self.connected = True
            return self.user_info
    
 