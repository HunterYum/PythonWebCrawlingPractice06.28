import re
#ca?e = care or cafe or cave or cave

p = re.compile("ca.e") 
#.(ca.e) : 하나의 문자를 의미 > care, cafe, case (o) | caffe (x)
# ^(^de) : 문자열의 시작 > desk, destination (o) | fade (x)
# $ (se$) : 문자열의 끝 > case, base (o) | face(x)

def print_match(m):

# print(m.group())
   if m:
       print("m.group():", m.group()) #일치하는 문자열
       print("m.string:", m.string) # 입력받은 문자열
       print("m.start():", m.start())
       print("m.end():", m.end())
       print("m.span():", m.span())
   else:
       print("No Matching")

# m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m = p.search("good care") #search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

# t = p.findall("careless") #findall : 일치하는 모든 것을 리스트 형태로 반환
# print(t)

#1. p = re.compile("원하는 형태")
#2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
#3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
#4. t = p.findall("비교할 문자열") : 일치하는 모든 것을 리스트 형태로 반환

#원하는 형태 : 정규식
#.(ca.e) : 하나의 문자를 의미 > care, cafe, case (o) | caffe (x)
# ^(^de) : 문자열의 시작 > desk, destination (o) | fade (x)
# $ (se$) : 문자열의 끝 > case, base (o) | face(x)