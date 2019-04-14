import pymysql

# SQL Login information.
ip = "140.115.35.44"
account  = "happy"
password = "happyobs"
database = "testdb"

class SQL:
    def __init__(self):
        pass
    def login(self, host=ip, username=account, passwd=password):
        self.db=pymysql.connect(host, username, passwd)
        self.cur=self.db.cursor()
        return self

if __name__=="__main__":
    sql = SQL().login(ip,account,password)