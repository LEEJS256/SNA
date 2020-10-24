# -*- coding: utf-8 -*-

import ps_config2 as cfg
import pymysql

count=1
def main():
    conn=pymysql.connect(host=cfg.DB_host,user=cfg.DB_user,password=cfg.DB_password,db=cfg.DB_db,charset='utf8')
    #conn=pymysql.connect(host='192.168.0.8',user='SNA',password='smart123',db='test',charset='utf8')
    curs=conn.cursor()
    
    #sql='insert into equipment(eq_ip,name,
    global count
    sql='insert into EEE(c,DD,cpu,memory,disk,ip) values (%s,%s,%s,%s,%s,%s)'
    #sql='insert into equip_performance(eq_pe_num,eq_ip,record_date,cpu_user,memory_use,disk_use) values (%s,%s,%s,%s,%s,%s)'
    curs.execute(sql,(count,cfg.nowDatetime,cfg.cpu,cfg.memory,cfg.disk,cfg.ip))
    count+=1


    
    sql='select * from EEE'
    curs.execute(sql)
    rows=curs.fetchall()
    print(rows)
    conn.commit()
    conn.close()
    
    
    
    
    
    
    
    
if __name__=="__main__":
   # count=0
              
    main()
   # print("select * from EEE")
   # while count<4: