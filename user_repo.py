from user import User
class UserRepo():
    def __init__(self, conn):
        self.conn = conn

    def create(self, userpass_details):
        self.conn.execute("INSERT INTO users (username, password) VALUES (%s, %s)", [userpass_details['username'], userpass_details['password']])

