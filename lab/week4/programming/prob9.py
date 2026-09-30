# 202611839 임정아
# 작성일: 26.09.30

# 문제
# 2개의 거북이를 생성해서 서로 다른 방향으로 움직이도록 하라.

def test_prob9():
    import turtle

    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t1.shape("turtle")
    t2.shape("circle")

    t1.setheading(0) #각도(오른쪽)
    t2.setheading(180) #(왼쪽)
    t1.forward(100)
    t2.forward(100)

    t1.setheading(270) # (아래)
    t2.setheading(90) # (위)
    t1.forward(50)
    t2.forward(50)

    t1.setheading(0)
    t2.setheading(180)
    t1.forward(100)
    t2.forward(100)

    turtle.done()

if __name__ == "__main__":
    test_prob9()