def euclideanAlgorithm(a: int, b: int, returnQ=False):
    r = 1
    q = 1
    sr = 0
    q_list = []

    while r != 0:
        r = a % b
        q = int((a - r) / b)
        q_list.append(q)
        a = b
        b = r
        if r != 0:
            sr = r

    if returnQ:
        return q_list
    else:
        return sr


def extendedEuclideanAlgorithm(a: int, b: int):
    new_q_list = []

    q_list = euclideanAlgorithm(a, b, True)

    for y in range(0, len(q_list)):
        new_q_list.append(q_list[(len(q_list)-1)-y])

    q_list = new_q_list
    x_list = [0]
    y_list = [1]

    for i in range(1, len(q_list)):
        x_list.append(y_list[i-1])
        y_list.append(x_list[i-1] - q_list[i] * y_list[i-1])

    print(f"Q: {q_list}")
    print(f"X: {x_list}")
    print(f"Y: {y_list}")

    return y_list[len(y_list)-1]


def phi(n: int):
    num = 0

    for i in range(1, n):
        if ggT(i, n) == 1:
            num += 1

    return num


def factorial(n: int):
    p = 1
    for i in range(1, n+1):
        p *= i
    return p