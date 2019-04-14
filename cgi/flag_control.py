#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer) # 中文編碼問題

import SQL_controller
import cgi, cgitb

# get information form html
form = cgi.FieldStorage() 
site_SN = form.getvalue('SN')
site_flag  = form.getvalue('flag')

sql=SQL_controler.SQL().login()
txt = "UPDATE testdb.flag_table SET flag1={0} WHERE SN={1};".format(site_flag, site_SN)
sql.cur.execute(txt)
sql.db.commit()

txt = "select * from testdb.flag_table;"
sql.cur.execute(txt)
result=sql.cur.fetchall()


sql.db.close()

print("Content-type: text/html")
print("")
print("test<br>")
print(txt+"<br>")
print(site_SN+"  "+site_flag+"<br>")
print(result)