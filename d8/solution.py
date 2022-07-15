from functools import reduce


# return a string where characters are in each
def fold_str(a, b):
    result = a

    for la in b:
        if la not in result:
            result += la

    return result

# returns characters abcdefg that aren't in string
def not_in(str):
    result = ''

    for l in 'abcdefg':
        if l not in str:
            result += l

    return result

truth = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg"
]

table = {
    7: [8],
    6: [0, 6, 9],
    5: [2, 3, 5],
    4: [4],
    3: [7],
    2: [1],
}

# Returns the matrix if valid, otherwise None
def return_valid(ttt, matrix):
    complete = set()

    # Test validity

    for row in range(7):
        if sum(matrix[row]) == 0:
            return None
        elif sum(matrix[row]) == 1:
            to = matrix[row].index(True)

            if to in complete:
                return None
            else:
                complete.add(matrix[row].index(True))

    # Test if matrix is complete

    if len(complete) == 7:
        mapped_solution = {}

        for row in range(7):
            mapped_solution[chr(ord('a') + row)] = chr(ord('a') + matrix[row].index(True))


        for t in ttt:
            if print_character(mapped_solution, t) is None:
                return None

        return matrix

    # Find a column that has two cols empty in the same row
    for row in range(7):
        if sum(matrix[row]) == 2:
            candidate_a = matrix[row].index(True)
            candidate_b = matrix[row].index(True, candidate_a + 1)

            # fill out matrix with valid
            matrix_a = [[x for x in row] for row in matrix]
            matrix_b = [[x for x in row] for row in matrix]

            for r in range(7):
                if r != row:
                    matrix_a[r][candidate_a] = False
                    matrix_b[r][candidate_b] = False

            matrix_a[row][candidate_b] = False
            matrix_b[row][candidate_a] = False

            # Propogate solved rows
            for r in range(7):
                if sum(matrix_a[r]) == 1:
                    solved = matrix_a[r].index(True)

                    for x in range(7):
                        if x != r:
                            matrix_a[x][solved] = False

            for r in range(7):
                if sum(matrix_b[r]) == 1:
                    solved = matrix_b[r].index(True)

                    for x in range(7):
                        if x != r:
                            matrix_b[x][solved] = False

            solution_a = return_valid(ttt, matrix_a)
            solution_b = return_valid(ttt, matrix_b)

            if solution_a is not None:
                return solution_a

            return solution_b

    assert "Limitations"

def output_mapped(solution, digits):
    number = 0
    multiplier = 1

    for d in reversed(digits):
        number += print_character(solution, d) * multiplier
        multiplier *= 10

    return number

def print_character(solution, digit):

    actual = ''

    for d in digit:
        actual += solution[d]

    for t in range(len(truth)):
        if list(sorted(truth[t])) == list(sorted(actual)):
            return t

    return None

def two(test):
    res = test[0].split()

    matrix = [[True for _ in range(7)] for _ in range(7)]

    for p in res:
        cant = not_in(reduce(fold_str, list(map(lambda x: truth[x], table[len(p)])), ''))

        for letter in p:
            for to in cant:
                matrix[ord(letter) - ord('a')][ord(to) - ord('a')] = False

    solution = return_valid(res, matrix)

    mapped_solution = {}

    for row in range(7):
        mapped_solution[chr(ord('a') + row)] = chr(ord('a') + solution[row].index(True))

    return output_mapped(mapped_solution, test[1].split())


def test_in(z):
    a = str(two(z))

    return a.count('1') + a.count('4') + a.count('7') + a.count('8')


if __name__ == '__main__':
    s = 0
    for x, y in [x.split('|') for x in open('input.txt', 'r')]:  # split signal and output
        l = {len(s): set(s) for s in x.split()}  # get number of segments

        n = ''
        for o in map(set, y.split()):  # loop over output digits
            match len(o), len(o & l[4]), len(o & l[2]):  # mask with known digits
                case 2, _, _:
                    n += '1'
                case 3, _, _:
                    n += '7'
                case 4, _, _:
                    n += '4'
                case 7, _, _:
                    n += '8'
                case 5, 2, _:
                    n += '2'
                case 5, 3, 1:
                    n += '5'
                case 5, 3, 2:
                    n += '3'
                case 6, 4, _:
                    n += '9'
                case 6, 3, 1:
                    n += '6'
                case 6, 3, 2:
                    n += '0'
        s += int(n)

    print(s)

    with open('input.txt', 'r') as f:
        data = list(map(lambda x: x.strip().split(' | '), f.read().splitlines()))

        # Solution part 1
        print(sum(map(lambda x: test_in(x), data)))

        # Solution part 2
        print(sum(map(lambda x: two(x), data)))
