import requests

res = requests.get("http://google.com")
res.raise_for_status()
# print("응답코드 :", res.status_code)#200이면 정상

# if res.status_code == requests.codes.ok:
#     print("Normal")
# else:
#     print("Error. [Error code", res.status_code, "]")

# res.raise_for_status()
# print("Start Web Scraping")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)