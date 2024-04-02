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
    def add_user(self, first_name, last_name, email, password, sort_code, iban, account_number, account_type):
        sql = "INSERT INTO user (first_name, last_name, email, password, sort_code, iban, account_number, account_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = ( first_name, last_name, email, password, sort_code, iban, account_number, account_type)
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

    # A revoir
    def get_last_message_time(self, id_user):
        sql = "SELECT date_last_message FROM user WHERE id = %s"
        values = (id_user,)
        result = self.fetch(sql, values)
        if result:
                return result[0][0]
        else:
            return None

    def first_name_user(self):
        sql = "SELECT first_name FROM user"
        return self.fetch(sql)