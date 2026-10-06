# 202611839 임정아
# 작성일: 26.09.29

# 문제
# Rectangle 클래스 작성.
# 인스턴스 변수: x, y [좌측 상단 좌표] / width, height [너비와 높이]
# 메소드: __init__(self, x, y, w, h) / __str__() [사각형의 좌표와 크기를 문자열로 변환] / setX(), get()... [접근자와 설정자] / getArea() [면적 계산] / overlap(r) [사각형과 전달된 사각형이 겹치면 True, 아니면 False]

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def __str__(self):
        return f"위치: {self.x}, {self.y} / 크기: {self.width}, {self.height}"

    def setX(self, x):
        self.x = x
    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y
    def getY(self):
        return self.y

    def setWidth(self, w):
        self.width = w
    def getWidth(self):
        return self.width

    def setHeight(self, h):
        self.height = h
    def getHeight(self):
        return self.height

    def getArea(self):
        return self.width * self.height

    def overlap(self, r):
        if self.x + self.width < r.x:
            return False

        if r.x + r.width < self.x:
            return False

        if self.y + self.height < r.y:
            return False

        if r.y + r.height < self.y:
            return False

        return True

def test_prob4():
    r1 = Rectangle(0, 0, 100, 100)
    r2 = Rectangle(10, 10, 100, 100)
    if r1.overlap(r2):
        print("r1과 r2는 서로 W겹칩니다.")
    else:
        print("r1과 r2는 서로 겹치지 않습니다.")

if __name__ == "__main__":
    test_prob4()