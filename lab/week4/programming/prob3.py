# 202611839 임정아
# 작성일: 26.09.29

# 문제
# Box 클래스 작성. 가로길이, 세로길이, 높이를 나타내는 인스턴스 변수를 가짐.
# 인스턴스 변수: length, height depth [가로, 세로, 높이]
# 메소드: __init__(self, l, h, d) [매개변수 l, h, d를 가지는 생성자 함수] / __str__() [정보를 문자열로 변환] / setLength(), getLength()... [각 속성에 대한 접근자와 설정자 함수]

class Box:
    def __init__(self, l, h, d):
        self.length = l
        self.height = h
        self.depth = d

    def __str__(self):
        return f"({self.height}, {self.length}, {self.depth})"

    def setLength(self, l):
        self.length = l
    def getLength(self):
        return self.length
    
    def setHeight(self, h):
        self.height = h
    def getHeight(self):
        return self.height

    def setDepth(self, d):
        self.depth = d
    def getDepth(self):
        return self.depth

def test_prob3():
    b1 = Box(100, 100, 100)
    print(b1)
    print("상자의 부피는", b1.getHeight()*b1.getLength()*b1.getDepth())

if __name__ == "__main__":
    test_prob3()