#
# bmi 계산 함수
# Body Mass Index (BMI) 계산 함수
#

def get_bmi(kg: float, cm:float) -> float:
    bmi = kg / (cm/100) ** 2
    return bmi

def test_get_bmi():
    height = 175
    weight = 70
    b = get_bmi(weight, height)
    print(f"키({height}cm) 몸무게({weight}kg)의 BMI는 {b}입니다.")

if __name__ == "__main__":
    test_get_bmi()