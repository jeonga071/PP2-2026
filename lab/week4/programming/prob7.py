# 202611839 임정아
# 작성일: 26.09.29

# 문제
# 연락처를 저장하는 PhoneBook 클래스 작성. 딕셔너리를 이용하여 저장
# 인스턴스 변수: contacts[딕셔너리를 name, mobile, office, email로 구성]
# 메소드: __init__(self), __str__(), add(self, name, moblie=None, office=None, email=None)

class PhoneBook():
    def __init__(self):
        self.contacts = {}

    def __str__(self):
        result = ""
        for name, info in self.contacts.items():
            result += f"{name}\n"
            result += f"office phone: {info['office']}\n"
            result += f"email address: {info["email"]}\n"

        return result

    def add(self, name, moblie = None, office = None, email = None):
        self.contacts[name] = {"mobile": moblie, "office": office, "email": email}

def test_prob7():
    obj = PhoneBook()
    obj.add("Kim", office="1234567", email="kim@company.com")
    obj.add("Park", office="2345678", email="park@company.com")
    print(obj)

if __name__ == "__main__":
    test_prob7()