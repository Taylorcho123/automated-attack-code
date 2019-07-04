from requests_toolbelt import MultipartEncoder
import requests

url = "http://192.168.0.29:8080/ShotPlace/bbs/write?boardCd=free&curPage=1&searchWord="

for i in range(1, 101) : 
	m = MultipartEncoder (
	    fields = {
	            "boardCd" : "free",
	            "title" : "auto : "+str(i),
	            "content" : "python3 requests module",
	    }
	)

	res = requests.post(url, data=m, headers={"Content-Type" : m.content_type})

	print(str(i)+"th article's status code : ", res.status_code)

