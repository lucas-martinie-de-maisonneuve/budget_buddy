from datetime import datetime
from data.Database import Database

class DiscordManager(Database):
    def __init__(self):
        Database.__init__(self, 'localhost', 'root', '$~Bc4gB9', 'discord')
        # Database.__init__(self, 'localhost', 'root', 'VannyLamorte25!', 'discord')
        # Database.__init__(self, 'localhost', 'root', 'azerty', 'discord') <-- Hamza
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
    
    def add_user(self, surname, name, pseudo, email, password, photo, id_role):
        sql = "INSERT INTO user (surname, name, pseudo, email, password, photo, id_role) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (surname, name, pseudo, email, password, photo, id_role)
        self.execute_query(sql, values)

    def surname_user(self):
        sql = "SELECT surname FROM user"
        return self.fetch(sql)

    def display_user(self):
        sql = "SELECT * FROM user"
        return self.fetch(sql)
    
    def display_admin_request(self):
        sql = "SELECT * FROM user WHERE change_role=1"
        return self.fetch(sql)
    
    def display_role_name(self):
        sql = "SELECT role.name FROM role LEFT JOIN user ON user.id_role = role.id"
        return self.fetch(sql)

    def add_category(self, name, intro):
        sql = "INSERT INTO category (name, intro) VALUES (%s, %s)"
        values = (name, intro)
        self.cursor.execute(sql, values)
        self.connection.commit()

    # Toutes Categories
    def display_category(self):
        sql = "SELECT * FROM category"
        return self.fetch(sql)

    def display_channel(self):
        sql = "SELECT * FROM channel"
        return self.fetch(sql)

    def display_message(self):
        sql = "SELECT * FROM message"
        return self.fetch(sql)

    def count_category(self):
        sql = "SELECT COUNT(*) AS nb FROM category"
        return self.fetch_one(sql)

    def id_category(self):
        sql = "SELECT id FROM category"
        self.cursor.execute(sql)
        self.categorys = self.cursor.fetchall()
        return self.categorys

    def name_category(self):
        sql = "SELECT name FROM category"
        return self.fetch(sql)

    # Ajout Channel
    def add_channel(self,name,status,communication,id_category):
        sql = "INSERT INTO channel (name,status,communication,id_category) VALUES (%s, %s,%s, %s)"
        values = (name,status,communication,id_category)
        self.cursor.execute(sql, values)
        self.connection.commit()

    def name_channel(self,id):
        sql = "SELECT name FROM channel WHERE id_category = %s"
        values = (id,)
        return self.fetch(sql, values)

    def count_channel(self,id):
        sql = "SELECT COUNT(*) AS nb FROM channel WHERE id_category = %s"
        values = (id,)
        return self.fetch_one(sql,values)
            
    def id_channel(self):
        sql = "SELECT id_category FROM channel"
        self.cursor.execute(sql)
        self.channels = self.cursor.fetchall()
        return self.channels

    def communication_channel(self, id):
        sql = "SELECT communication FROM channel WHERE id_category = %s"
        values = (id,)
        return self.fetch(sql, values) 
    
    # Update
    def update_user(self, pseudo, email, password, photo, id):
        sql = 'UPDATE user SET pseudo=%s, email=%s, password=%s, photo=%s WHERE id=%s'
        params = (pseudo, email, password, photo, id)
        self.execute_query(sql, params)     

    def update_message_author(self, name, user):
        sql = 'UPDATE message SET name=%s WHERE name=%s'
        params = (name, user)
        self.execute_query(sql, params)
    
    def update_abc_password(self, password, id_user): 
        sql = 'UPDATE password SET password=%s WHERE id_user=%s'
        params = (password, id_user)
        self.execute_query(sql, params)
    
    def update_role_request(self, email):
        sql = 'UPDATE user SET change_role=1 WHERE email=%s'
        params = (email,)
        self.execute_query(sql, params)

    def upgrade_role(self, id_user):
        sql = 'UPDATE user SET change_role=0, id_role=1 WHERE id =%s'
        values = (id_user,)
        self.execute_query(sql, values)

    def deny_upgrade_role(self, id_user):
        sql = 'UPDATE user SET change_role=0 WHERE id =%s'
        values = (id_user,)
        self.execute_query(sql, values)

    # Delete User
    def delete_user(self, id):
        sql = "DELETE FROM user WHERE id = %s"
        values = (id,)
        self.execute_query(sql, values)

    def delete_category(self, id):
        sql = "DELETE FROM category WHERE id = %s"
        values = (id,)
        self.execute_query(sql, values)

    def delete_channel(self, id):
        sql = "DELETE FROM channel WHERE id = %s"
        values = (id,)
        self.execute_query(sql, values)

    def delete_channel_message(self, id):
        sql = "DELETE FROM message WHERE id_channel = %s"
        values = (id,)
        self.execute_query(sql, values)

    def save_message(self, name, message, id_channel):
        actual_time = datetime.now()
        sql = "INSERT INTO message (name, time, message, id_channel) VALUES (%s, %s, %s, %s)"
        values = (name, actual_time, message, id_channel)
        self.execute_query(sql, values)
        
    def count_message(self,id):
        sql = "SELECT COUNT(*) AS nb FROM message WHERE id_channel = %s"
        values = (id,)
        return self.fetch_one(sql,values)
    
    def get_message(self,id):
        sql = "SELECT * FROM message WHERE id_channel = %s"
        values = (id,)
        return self.fetch(sql,values)

    def name_message(self,id):
        sql = "SELECT name FROM message WHERE id_channel = %s"
        values = (id,)
        return self.fetch(sql,values)
    
    def get_profile_picture(self, id):
        sql = "SELECT photo FROM user WHERE pseudo = %s"
        values = (id,)
        return self.fetch(sql,values)

    def time_message(self,id):
        sql = "SELECT time FROM message WHERE id_channel = %s"
        values = (id,)
        return self.fetch(sql,values)

    def message_message(self,id):
        sql = "SELECT message FROM message WHERE id_channel = %s"
        values = (id,)
        return self.fetch(sql,values)

    def id_channel_message(self):
        sql = "SELECT id_channel FROM message"
        return self.fetch(sql)
    
    def get_password(self, user_id):
        sql = "SELECT password FROM password WHERE id_user = %s"
        values = (user_id,)
        return self.fetch(sql, values)

    def close_connection(self):
        self.disconnect()
    
    def add_emoji(self, id_mes,nb_react):
        sql = 'UPDATE message SET react=%s WHERE id=%s'
        values = (nb_react, id_mes)
        self.execute_query(sql, values)

    def add_abc_password (self, password, id_user):
        sql = "INSERT INTO password (password, id_user) VALUES (%s, %s)"
        values = (password, id_user)
        self.execute_query(sql, values)

    # Notification   
    def save_last_message (self, user_id): 
        current_time = datetime.now()
        sql = "UPDATE user SET last_message = %s WHERE id = %s"
        values = (current_time, user_id,)
        self.execute_query(sql, values)

    def get_last_message_time(self, user_id):
        sql = "SELECT last_message FROM user WHERE id = %s"
        values = (user_id,)
        result = self.fetch(sql, values)
        if result: 
                return result[0][0]
        else: 
            return None        

    def get_user_role(self, user_status):
        sql = "SELECT id_role FROM user WHERE id = %s"
        values = (user_status,)
        return self.fetch(sql,values)

    def get_channel_status(self, channel_id):
        sql = "SELECT status FROM channel WHERE id = %s"
        values = (channel_id,)
        return self.fetch(sql,values)
        
    # Audio 
    def save_to_database (self, name, id_channel):
        with open("source/pyaudio/audio_liv.wav", 'rb') as f:
            audio_blob = f.read()

        time = datetime.now()
        sql = "INSERT INTO audio(name, time, audio_blob, id_channel) VALUES (%s, %s, %s, %s)"
        params = (name, time, audio_blob, id_channel)
        self.execute_query(sql, params)

    def retrieve_audio_database(self, id_channel): 
        query = "SELECT audio_blob FROM audio WHERE id = %s"
        values = (3,)
        save = self.fetch(query, values)[0][0]
        with open(f"source/pyaudio/output3.wav", 'wb') as f:
            f.write(save)


manager = DiscordManager()
manager.close_connection()