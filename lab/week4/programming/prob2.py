# 202611839 임정아
# 작성일: 26.09.29

# 문제
# 로켓 클래스 작성.
# 인스턴스 변수: x, y [로켓의 위치]
# 메소드: __init__(self, x, y) [생성자 함수] / __str__() [정보를 문자열로 변환] / moveUp(self) [y좌표가 1만큼 증가]

class Rocket:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"로켓의 높이: {self.y}"

    def moveUp(self):
        self.y = self.y + 1

def test_prob2():
    myRocket = Rocket(0, 0)
    print("로켓의 높이: ", myRocket.y)

    myRocket.moveUp()
    print("로켓의 높이: ", myRocket.y)

if __name__ == "__main__":
    test_prob2()