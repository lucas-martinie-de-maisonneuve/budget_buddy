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

        self.sort_code_1 = ""
        self.sort_code_2 = ""
        self.sort_code_3 = ""
        self.country = "GB"
        self.check_digits = ""
        self.bank_code = "PANT"
        self.account_number = ""
        self.iban = ""

        # Homepage Transfer Money
        self.input_description = "Description"
        self.category = "Category"
        self.input_number_category = "1-7"
        self.input_amount = "Amount"

        self.input_name_receiver = "Name"
        self.input_surname_receiver = "Surname"
        self.input_iban_receiver = "IBAN"

        self.register = False
        self.connected = False

    def login_user(self):
        hashed_password = sha256(self.input_password.encode()).hexdigest()

        if self.check_credentials(self.input_email, hashed_password):
            self.user = self.get_user(self.input_email, hashed_password)
            self.connected = True
            return self.user
        
    def register_user(self):
        hashed_password_register = sha256(self.input_password_register.encode()).hexdigest()
        self.new_user = self.add_user(self.input_first_name_register,self.input_last_name_register, self.input_email_register, hashed_password_register, self.iban, self.account_number, self.account_type_number)
        return self.new_user
        
    # Notification
        
    def save_last_co(self,user_id):
        self.save_last_transaction (user_id)

    def load_info_last_co(self, user): 
        self.last_login_date = self.get_last_co_time(user)
        return self.last_login_date 

    # Saving & Checking 

    def catch_phrase(self, account_nb):
        return self.description_account([account_nb])  
    
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
    
    # Main Page

    def display_total_amount(self, account_id, user_id):
        total_amount_r =  self.sum_account_r(account_id, user_id)[0][0]  
        total_amount_s =  self.sum_account_s(account_id, user_id)[0][0]   
        if total_amount_r == None:
            total_amount_r = 0
        if total_amount_s ==  None:
            total_amount_s = 0

        total = total_amount_r -  total_amount_s
        return total
    
 







    

