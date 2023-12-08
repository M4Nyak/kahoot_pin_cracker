import requests
import random
import string
sayi_kumesi= string.digits
while True:
 pin = str(random.choice(sayi_kumesi)) + str(random.choice(sayi_kumesi)) + str(random.choice(sayi_kumesi)) + str(random.choice(sayi_kumesi)) + str(random.choice(sayi_kumesi)) + str(random.choice(sayi_kumesi)) + str(random.choice(sayi_kumesi))
 rs= requests.session()
 rs.headers = {
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 7_1_1; en-US) AppleWebKit/602.31 (KHTML, like Gecko) Chrome/52.0.1856.275 Safari/537'


 }
 url= f"https://kahoot.it/reserve/session/{pin}/?1742051885232"
 a= rs.get(url).text
 rs.close()
 if 'Not found' == a:
    print("ders bulunamadi: ",pin)
 else:
    print("ders bulundu: ",pin)
    open("bulunandersler.txt","w").write(f"{pin} \n")
