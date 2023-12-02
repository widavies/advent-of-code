
def p1():
    with open('input.txt') as f:
        positions = list(map(int, f.readline().split(',')))
        positions.sort()

        # python, defaults to decimal if not //
        # lower median taken if odd amount
        # True because of optimality property https://en.wikipedia.org/wiki/Median#Optimality_property
        median = positions[len(positions) // 2]

        cost = sum(list(map(lambda x: abs(x - median), positions)))

        print("Align to:", median)
        print("Cost:", cost)

def p2():
    with open('input.txt') as f:
        positions = list(map(int, f.readline().split(',')))

        # If you double the distance, need more than double the fuel, so optimality property is not preserved
        avg = sum(positions) // len(positions)

        cost = round(sum(list(map(lambda x: abs(abs(x - avg) * (abs(x - avg) + 1) / 2), positions))))

        print("Align to:", avg)
        print("Cost:", cost)


p1()
p2()