from datetime import datetime
from data.Database import Database

class UserRepository(Database):
    def __init__(self):
        passwords = ['VannyLamorte25!', 'Oleg4342758@!','$~Bc4gB9']
        for password in passwords:
            try:
                Database.__init__(self, 'localhost', 'root', password, 'bank')
                self.connect()
                break
            except:
                pass


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
    