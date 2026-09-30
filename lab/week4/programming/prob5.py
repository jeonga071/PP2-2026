# 202611839 임정아
# 작성일: 26.09.29

# 문제
# Triangle 클래스 작성.
# 인스턴스 변수: angle1, angle2, angle3 [각도] / numberofSides [변의 개수(기본값 3)]
# 메소드: __init__(self, a1, a2, a3) [매개변수 생성자] / __str__() [문자열 변환] / setAngle1(), getAngle1()... [접근자와 설정자] / checkAngles() [내각의 합 확인]

class Triangle:
    def __init__(self, a1, a2, a3, numberOfSides = 3) :
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.numberOfSides = numberOfSides
    def __str__(self):
        return f"삼각형의 각도: {self.a1}도, {self.a2}도, {self.a3}도"

    def setAngle1(self, a1):
        self.a1 = a1
    def getAngle1(self):
        return self.a1

    def setAngle2(self, a2):
        self.a2 = a2
    def getAngle2(self):
        return self.a2

    def setAngle3(self, a3):
        self.a3 = a3
    def getAngle3(self):
        return self.a3

    def checkAngles(self):
        return self.a1 + self.a2 + self.a3

def test_prob5():
    triangle = Triangle(90, 30, 60)
    print(triangle.checkAngles())

if __name__ == "__main__":
    test_prob5()