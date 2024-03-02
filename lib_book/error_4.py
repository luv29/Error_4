import mysql.connector as ms
import requests


    

def re():
    con = False
    mycon=ms.connect(host='localhost',user='root',passwd='@Piyush185251',database='e_4',charset='utf8')
    if mycon.is_connected()==False:
        print("error connecting to database")
        con = False
    else:
        con = True
    if con:
        url="https://gutendex.com/books/?page=1234"

        res=requests.get(url)
        if not res.status_code==200:
            print("error");
        else:
            c=0
            while url!=None and c<200:
                pa=res.json()
                for pas in pa["results"]:
                    cur=mycon.cursor()
                    s="INSERT INTO data (id, title, name, lang, txt, epub) VALUES ({},'{}','{}','{}','{}','{}');".format(pas["id"],pas["title"],pas["authors"][0]["name"],pas["languages"][0],pas["formats"]["text/html"],pas["formats"]["application/epub+zip"])
                    try:
                        cur.execute(s)
                        mycon.commit()
                    except ms.errors.ProgrammingError:
                        continue
                    cur.close()
                    c+=1
                url=pa["next"]
                res=requests.get(url)

    mycon.close()
            


                
                
    
