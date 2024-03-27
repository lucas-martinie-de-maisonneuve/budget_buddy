from datetime import datetime
from data.Database import Database

class BudgetManager(Database):
    def __init__(self):
        # Database.__init__(self, 'localhost', 'root', '$~Bc4gB9', 'bank')
        Database.__init__(self, 'localhost', 'root', 'VannyLamorte25!', 'bank')
        # Database.__init__(self, 'localhost', 'root', 'Oleg4342758@!', 'bank')
        self.connect()
           
    def check_credentials(self, email, password):
        sql = "SELECT * FROM user WHERE email = %s AND password = %s"
        values = (email, password)
        user = self.fetch_one(sql, values)
        return user is not None
    
    def get_user(self, email, password):
        sql = "SELECT * FROM user WHERE email = %s AND password = %s"
        values = (email, password)
        user = self.fetch_one(sql, values)
        return user
    
    # TABLE USER
    
    def add_user(self, first_name, last_name, email, password, iban, account_number):
        sql = "INSERT INTO user (first_name, last_name, email, password, iban, account_number) VALUES (%s, %s, %s, %s, %s, %s)"
        values = ( first_name, last_name, email, password, iban, account_number)
        self.execute_query(sql, values)

    def user_info(self):
        sql = "SELECT * user"
        return self.fetch(sql)

    def first_name_user(self):
        sql = "SELECT first_name FROM user"
        return self.fetch(sql)
    
    def last_name_user(self):
        sql = "SELECT last_name FROM user"
        return self.fetch(sql)
    
    def iban_user(self):
        sql = "SELECT iban FROM user"
        return self.fetch(sql)
    
    def account_number_user(self):
        sql = "SELECT iban FROM user"
        return self.fetch(sql)
    
    def update_user(self,email):
        sql = 'UPDATE user SET pseudo=%s'
        params = (email,)        
        self.execute_query(sql, params) 

    # TRANSACTION

    def add_transaction(self, transaction_re, transaction_name, description, amount, date, id_category, id_user,  account_id ):
        sql = "INSERT INTO transaction (transaction_re, transaction_name, description, amount, date, id_category, id_user,  account_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (transaction_re, transaction_name, description, amount, date, id_category, id_user,  account_id )
        self.cursor.execute(sql, values)
        self.connection.commit()

    def transaction_info(self):
        sql = "SELECT * FROM transaction"
        return self.fetch(sql)

    # ACCOUNTS
        
    def account_type(self):
        sql = "SELECT ad_description FROM account"
        return self.fetch(sql)
        
    def ad_description_account(self):
        sql = "SELECT ad_description FROM account"
        return self.fetch(sql)
    
    def general_description_account(self):
        sql = "SELECT _description FROM account"
        return self.fetch(sql)

    # Notification    
        
    def last_notif (self, id_user): 
        current_time = datetime.now()
        sql = "INSERT INTO notificaton = %s WHERE id = %s"
        values = (current_time, id_user,)
        self.execute_query(sql, values)        

    def save_last_transaction (self, id_user): 
        current_time = datetime.now()
        sql = "UPDATE user SET date_last_transaction = %s WHERE id = %s"
        values = (current_time, id_user,)
        self.execute_query(sql, values)

    # A revoir
    def get_last_message_time(self, id_user):
        sql = "SELECT date_last_message FROM user WHERE id = %s"
        values = (id_user,)
        result = self.fetch(sql, values)
        if result: 
                return result[0][0]
        else: 
            return None   
        
    def add_notification(self):
        user = "fist_name_user"
        amount = "50"
        value = f"{user} transferred you the amount of {amount}£"
        sql = "INSERT INTO notification(notif_message) VALUES (%s)"
        values = (value,)
        self.execute_query(sql, values)

    def display_notification(self, id_user):
        sql = "SELECT notif_message FROM notification WHERE id = %s"
        values = (id_user)
        self.execute_query(sql, values)
    
    def first_name_user(self):
        sql = "SELECT first_name FROM user"
        return self.fetch(sql)
