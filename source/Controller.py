from hashlib import sha256

from data.UserRepository import UserRepository
from data.TransactionRepository import TransactionRepository

# Controller
class Controller(UserRepository,TransactionRepository):

    def __init__(self):
        UserRepository.__init__(self)

        # Home
        self.input_email = ""
        self.input_password = ""

        # Signup
        self.input_first_name_register = ""
        self.input_last_name_register = ""

        self.input_email_register = ""
        self.input_password_register = ""

        self.account_number = ""

        self.sort_code_1 = ""
        self.sort_code_2 = ""
        self.sort_code_3 = ""

        # Homepage Transfer Money
        self.input_descrition = "Description"
        self.input_number_category = "1-7"
        self.input_amount = "Amount"

        self.input_name_receiver = "Name"
        self.input_surname_receiver = "Surname"
        self.input_iban_receiver = "IBAN"


        self.connected = False

    def login_user(self):
        hashed_password = sha256(self.input_password.encode()).hexdigest()

        if self.check_credentials(self.input_email, hashed_password):
            self.user = self.get_user(self.input_email, hashed_password)
            self.connected = True
            return self.user
        
     
    
    def display_transaction(self, user_id, filter):
        if filter == 1: 
            transactions = self.descending_date_filter(user_id)
            
        elif filter == 2: 
            transactions = self.ascending_date_filter(user_id)
        
        elif filter == 3: 
            transactions = self.income_filter(user_id)

        elif filter == 4: 
            transactions = self.expense_filter(user_id)

        elif filter == 5: 
            transactions = self.amount_desc_filter(user_id)

        elif filter == 6: 
            transactions = self.amount_asc_filter(user_id)

        # elif filter == 7: 
        #     transactions = self.amount_desc_filter(user_id)

        elif filter == 8: 
            transactions = self.category_filter(user_id)
   
        return transactions


    

