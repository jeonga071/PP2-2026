# 202611839 임정아
# 작성일: 26.09.30

# 문제
# printSong 클래스 작성.
# printSong: 노래 가사를 리스트로 받아 내부에 저장.
# sing(): 한 줄에 한 항목씩 출력

class printSong:
    def __init__(self, song):
        self.song = song

    def sing(self):
        for line in self.song:
            print(line)

def test_prob8():
    aSong = printSong(["TWINKLE, twinkle, little star",
                  "How I wonder what you are!",
                  "Up above the world so high,",
                  "Like a diamond in the sky."])
    aSong.sing()

if __name__ == "__main__":
    test_prob8()