# 202611839 임정아
# 작성일: 26.09.29

# 문제
# 고양이를 클래스로 정의하고 인스턴스 생성. 접근자와 설정자 사용
# 인스턴스 변수: name[이름] / age[나이]
# 메소드: __init__(self, name, age)[생성자 함수] / __str__()[정보를 문자열로 변환] / setName(), getName().. [접근자와 설정자 함수]

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + " " + str(self.age)

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age

def test_prob1():
    missy = Cat('Missy', 3)
    lucky = Cat('Lucky', 5)
    print(missy)
    print(lucky)

if __name__ == "__main__":
    test_prob1()