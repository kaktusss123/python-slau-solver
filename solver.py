"""
Данные в файл записываются в иде матрицы коэффициентов
1 2 3
4 5 6
, где 1 2 4 5 - коэффициенты, 3 6 - свободные члены
"""


def read_input(filename: str = 'input.txt') -> tuple:
    """
    Читает файл в 2 списка вида [[], []], []: матрица коэффициентов и свободных членов
    """
    A = []
    B = []
    with open(filename) as file:
        for line in file:
            line = line.strip().split()
            A.append(list(map(lambda x: float(x), line[:-1])))
            B.append(float(line[-1]))
    return A, B


def mult_row(A, B, ind, coef):
    """
    Умножает строку матриц [ind] на coef
    """
    row = A[ind]
    for i in range(len(row)):
        row[i] *= coef
    A[ind] = row
    B[ind] *= coef


def sub_row(A, B, ind):
    """
    Вычитает строку [ind + 1] из строки [ind]
    """
    for c in range(len(A[0])):
        A[ind][c] -= A[ind+1][c]
    B[ind] -= B[ind+1]


def gauss(A, B):
    """
    Выполняет решение СЛАУ методом Гаусса
    """
    r = len(A[0]) - 1
    # Сначала приводим к нижнетреугольному виду методом Гаусса
    for c in range(len(A) - 1, 0, -1):
        multiplier = A[r][c] / A[r-1][c]
        mult_row(A, B, r-1, multiplier)
        sub_row(A, B, r-1)
        r -= 1
    r = 0
    # Затем нижнетреугольную матрицу приводим к диагонально все тем же методом Гаусса
    for c in range(len(A)-1):
        multiplier = A[r+1][c] / A[r][c]
        mult_row(A, B, r, multiplier)
        sub_row(A, B, r-1)
    answer = []
    # Ответ считаем как {свободный член} / {соответствующий элемент диагонали}
    for i in range(len(A)):
        answer.append(B[i] / A[i][i])
    return answer


l, b = read_input()
ans = gauss(l, b)
print(l, b, sep='\n')
print('Answer:', ans)
