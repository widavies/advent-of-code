import math
import re

with open('input.txt') as f:
    content = f.read()

expr = re.compile(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))")

enabled = True
result_all = 0
result_enabled = 0

for op, *rest in expr.findall(content):
    mult = math.prod(map(lambda x: int(x or 0), rest))
    result_all += mult
    result_enabled += int(enabled) * mult
    enabled = enabled if 'mul' in op else op == "do()"

print('Part 1', result_all)
print('Part 2', result_enabled)