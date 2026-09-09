#
# 생일 축하 함수
#

def say_happy_birthday(name:str) -> None:
    print("안녕하세요")
    print(name + "님의 생일을 축하합니다.")
    return None

def test_happy_birthday():
    say_happy_birthday("임정아")
    say_happy_birthday("송영준")
    say_happy_birthday("김민재")
    say_happy_birthday("윤완")

def test_happy_birthday2():
    names = ["임정아", "송영준", "김민재", "윤완"]
    for name in names:
        say_happy_birthday(name)

def test_happy_birthday3():
    say_happy_birthday(3.14159)
    say_happy_birthday(100)
    say_happy_birthday([1,2,3])

if __name__ == "__main__":  #이 파일이 메인으로 사용할 때 실행
    #test_happy_birthday1()
    #test_happy_birthday2()
    test_happy_birthday3()
