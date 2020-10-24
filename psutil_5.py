# -*- coding: utf-8 -*-

import ps_config as cfg
import pymysql

count=1
def main():
    #conn=pymysql.connect(host=cfg.DB_host,user=cfg.DB_user,password=cfg.DB_password,db=cfg.DB_db,charset='utf8')
    
    conn=pymysql.connect(host='cfg.DB_host',user='cfg.DB_user',password='cfg.DB_password',db='cfg.DB_db',charset='utf8')
    #conn=pymysql.connect(host='192.168.0.8',user='SNA',password='smart123',db='test',charset='utf8')
    curs=conn.cursor()
    
    #sql='insert into equipment(eq_ip,name,
    global count
    #sql='insert into equip_performance(eq_pe_num,record_date,cpu_user,memory_use,disk_use) values (%s,%s,%s,%s,%s)'
    sql='insert into equip_performance(eq_pe_num,eq_ip,record_date,cpu_use,memory_use,disk_use) values (%s,NULL,%s,%s,%s,%s)'
    #curs.execute(sql,(count,cfg.ip,cfg.nowDatetime,cfg.cpu,cfg.memory,cfg.disk))
    curs.execute(sql,(count,cfg.nowDatetime,cfg.cpu,cfg.memory,cfg.disk))

    count+=1
    
    sql='select * from equip_performance'
    curs.execute(sql)   
    rows=curs.fetchall()
    print(rows)
    conn.commit()
    conn.close()
    
    
    
    
    
    
    
    
    
if __name__=="__main__":
    # while count < :
    # count=0
    main()