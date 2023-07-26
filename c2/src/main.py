import random


# compare function
def compare_val(i1, rnd_val):
    if i1 == rnd_val:
        print('정답')
        return True
    elif i1 > rnd_val:
        print('다운')
        return False
    else:
        print('업')
        return False


# loop 3 times
def main():
    rnd_val = random.randint(1, 20)
    print('디버그', rnd_val)
    for i in range(3, 0, -1):
        i1 = int(input('숫자를 맞춰보세요 '))
        if compare_val(i1, rnd_val):
            break


if __name__ == "__main__":
    main()
