# 문제

# 여러 학생들의 키와 몸무게를 리스트로 입력 받아 BMI 리스트를 출력하는
# 함수와 테스트하는 함수를 작성하시오.
# BMI 함수는 지난 시간에 작성한 get_bmi 함수를 이용하여 작성하시오.

def get_bmi(kg: float, cm:float) -> float:
    bmi = kg / (cm/100) ** 2
    return bmi

def main():
    lst = [];
    while True:
        kg = input("몸무게(kg):");
        cm = input("키(cm):");
        lst.append((float(kg), float(cm)));

        stop = input("더 입력하시겠습니까?(y/n):");
        if stop == "n":
            break
    print_bmi(lst)

def print_bmi(lst):
    for i in range(len(lst)):
        kg = lst[i][0]
        cm = lst[i][1]
        bmi = get_bmi(kg, cm)
        print(f"학생 {i + 1}의 bmi는 {bmi}입니다.")

main()