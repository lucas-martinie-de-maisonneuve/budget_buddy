from datetime import datetime
from data.Database import Database

class TransactionRepository(Database):
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

    def transaction_info(self, user_id):
        sql = "SELECT * FROM transaction WHERE id_receiver = %s OR id_sender = %s"
        values = (user_id, user_id)
        return self.fetch(sql, values)

    # ACCOUNTS
    
    def description_account(self, account_nb):
        sql = "SELECT tagline FROM description WHERE id = %s"
        values = (account_nb)
        return self.fetch(sql, values)    
    
    def income_filter(self, user_id):
        sql = "SELECT * FROM transaction WHERE transaction_re = 1  AND (id_receiver = %s OR id_sender = %s)"
        values = (user_id, user_id)
        return self.fetch(sql, values)

    def expense_filter (self, user_id):
        sql = "SELECT * FROM transaction WHERE transaction_re = 2 AND (id_receiver = %s OR id_sender = %s)"
        values = (user_id, user_id)
        return self.fetch(sql, values)

    def ascending_date_filter(self, user_id):
        sql = "SELECT * FROM transaction WHERE id_receiver = %s OR id_sender = %s ORDER BY date ASC"
        values = (user_id, user_id)
        return self.fetch(sql, values)

    def descending_date_filter (self, user_id):
        sql = "SELECT * FROM transaction WHERE id_receiver = %s OR id_sender = %s ORDER BY date DESC"
        values = (user_id, user_id)
        return self.fetch(sql, values)

    def calendar_filter(self, start_date, end_date, user_id):
        start_date = datetime.strptime(start_date, '%d/%m/%Y').strftime('%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%d/%m/%Y').strftime('%Y-%m-%d')
        sql = "SELECT * FROM transaction WHERE (id_receiver = %s OR id_sender = %s ) AND date BETWEEN %s AND %s ORDER BY date "
        values = (user_id, user_id, start_date, end_date, )
        return self.fetch(sql, values)

    def amount_asc_filter (self, user_id):
        sql = "SELECT * FROM transaction WHERE id_receiver = %s OR id_sender = %s ORDER BY amount ASC "
        values = (user_id, user_id)
        return self.fetch(sql, values)

    def amount_desc_filter (self, user_id):
        sql = "SELECT * FROM transaction WHERE id_receiver = %s OR id_sender = %s ORDER BY amount DESC"
        values = (user_id, user_id)
        return self.fetch(sql, values)

    def category_filter (self, user_id, id_categ):
        sql = "SELECT * FROM transaction WHERE (id_sender = %s OR id_receiver = %s) AND id_category  = %s"
        values = (user_id, user_id, id_categ)
        return self.fetch(sql, values)    
    
    def sum_account_r(self, account_id, user_id  ):
        sql = "SELECT SUM(amount) AS total_amount FROM transaction WHERE account_id = %s AND id_receiver = %s"
        values = (account_id, user_id)
        return self.fetch(sql, values)
    
    def sum_account_s(self, account_id, user_id  ):
        sql = "SELECT SUM(amount) AS total_amount FROM transaction WHERE account_id = %s AND id_sender = %s"
        values = (account_id, user_id)
        return self.fetch(sql, values)
      

    # Notification
    def last_notif (self, id_user):
        current_time = datetime.now()
        sql = "INSERT INTO notificaton = %s WHERE id = %s"
        values = (current_time, id_user,)
        self.execute_query(sql, values)

    def save_last_transaction (self, id_user):
        current_time = datetime.now()
        sql = "UPDATE user SET date_last_co = %s WHERE id = %s"
        values = (current_time, id_user,)
        self.execute_query(sql, values)

    def get_last_co_time(self, id_user):
        sql = "SELECT date_last_co FROM user WHERE id = %s"
        values = (id_user)
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