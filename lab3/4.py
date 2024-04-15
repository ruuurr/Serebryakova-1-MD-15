import random


def rand():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    operator = random.choice(['+', '-',])
    exp = f"{a} {operator} {b}"
    return exp, eval(exp)
def main():
    prav = 0
    neprav = 0
    max_prav = 3

    while neprav < max_prav:
        exp, prav_result = rand()
        answer = input(f"{exp} = ")

        try:
            answer = int(answer)
            if answer == prav_result:
                print("правильный ответ")
            else:
                print("ответ неверный")
                neprav += 1
        except ValueError:
            print("введите целое число")

    print(f"игра окончена. Правильных ответов:{prav}")


if __name__ == "__main__":
    main()