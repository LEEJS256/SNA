# -*- coding: utf-8 -*-

import ps_config2 as cfg
import pymysql

count=1

    
def main():
    conn=pymysql.connect(host=cfg.DB_host,user=cfg.DB_user,password=cfg.DB_password,db=cfg.DB_db,charset='utf8')
    
    curs=conn.cursor()
    global count
    sql='insert into EEE(c,DD,cpu,memory,disk,ip) values (%s,%s,%s,%s,%s,%s)'
    #sql='insert into EEE(c,DD,cpu,memory,disk,ip) values (%s,%s,%s,%s,%s,%s)'
    
    curs.execute(sql,(count,cfg.nowDatetime,cfg.cpu,cfg.memory,cfg.disk,cfg.ip))
    count+=1
    #count()
    sql='select * from EEE'
    curs.execute(sql)
    rows=curs.fetchall()
    print(rows)
    conn.commit()
    conn.close()
    
    
    
    
    
    
    
    
if __name__=="__main__":
   main()
   