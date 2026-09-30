# 202611839 임정아
# 작성일: 26.09.29

# 문제
# Person 클래스 작성.
# 인스턴스 변수: name [이름] / mobile [폰번호: 기본값을 가짐] / office [직장 번호: 기본값을 가짐] / email [이메일주소: 기본값을 가짐]
# 메소드: __init__(self, n, m, o, e) [생성자] / __str()__ [문자열 변환] / SetName(), getName()... [접근자와 설정자]

class Person():
    def __init__(self, n, m = None, o = None, e = None):
        self.name = n
        self.mobile = m
        self.office = o
        self.email = e

    def __str__(self):
        result = f"이름: {self.name}"

        if self.mobile is not None:
            result += f", 휴대폰: {self.mobile}"
        if self.office is not None:
            result += f", 직장 번호: {self.office}"
        if self.email is not None:
            result += f", 이메일: {self.email}"

        return result

    def setName(self, n):
        self.name = n
    def getName(self):
        return self.name

    def setMobile(self, m):
        self.mobile = m
    def getMobile(self):
        return self.mobile

    def setOffice(self, o):
        self.office = o
    def getOffice(self):
        return self.office

    def setEmail(self, e):
        self.email = e
    def getEmail(self):
        return self.email

def test_prob6():
    p1 = Person("Kim", o = "1234567", e = "kim@company.com")
    p2 = Person("Park", o = "2345678")
    p2.setEmail("park@company.com")

    print(p1)
    print(p2)

if __name__ == "__main__":
    test_prob6()