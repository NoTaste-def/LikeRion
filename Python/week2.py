def func(a):
  return 3*a+1

print(func(1))


class User:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
class Seo(User):
  def greeting():
    print('나는 스민재')

# user1 = User("스민재", 24)
# print(type(user1))
# print(user1.name, user1.age)

user2 = Seo("스민재", 24)
print(user2.name, user2.age)
user2.greeting

# 파이썬은 다중 상속이 가능하다.


###########################################################################

# 웹 : 인터넷 기반 http를 이용한 정보 공유 서비스
# http : 서버와 클라이언트의 데이터 교환을 요청(Req)과 응답(Res) 형식으로 정의한 프로토콜
# https : http에서 tls 프로토콜을 도입한 것. => 도청과 변조에 강해짐. 보안성 향상.
