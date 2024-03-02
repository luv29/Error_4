import mysql.connector as ms

def extract_data(key):
    mycon=ms.connect(host='localhost',user='root',passwd='@Piyush185251',database='e_4',charset='utf8')
    if  not mycon.is_connected():
        print("error")
    else:
        cur=mycon.cursor()
        if type(key)==int:
            q="select * from data where (id={});".format(eval(key))
        else:
            q="select * from data where(title like '%{}%' or name like '%{}%');".format(key,key)

        cur.execute(q)
    
        var=cur.fetchall()
        mycon.commit()
        cur.close()
        mycon.close()
        return var
        
        
