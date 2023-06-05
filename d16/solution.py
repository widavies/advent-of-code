import operator
from functools import reduce
import time

start = time.time()

# operator type ids
TID_SUM = 0
TID_MUL = 1
TID_MIN = 2
TID_MAX = 3
TID_LITERAL = 4
TID_GT = 5
TID_LT = 6
TID_EQ = 7

# length type ids
LTI_BITS = 0
LTI_PACKETS = 1
#
# Step 1: Load data
#
with open('input.txt') as f:
    packets = []

    transmission = f.readline()

    # bin(int(x, 16))[2:] translates the hex to binary, and strips the "0b" prefix
    # zfill(4) ensures that the binary string is at least 4 0s wide
    stack = list(''.join(list(map(lambda x: bin(int(x, 16))[2:].zfill(4), transmission))))

    # a helper function to pop multiple values at a time
    def pop(n):
        ret = stack[:n]
        del stack[:n]
        return ''.join(ret)

# Parsed will become an array of (version, tid, lti, val, pkt_size)
# where:
# 1. version - packet version
# 2. tid - type id
# 3. lti - length type id
# 4. val is
#   - literal value, when tid == TID_LITERAL
#   - number of sub packets when tid != TID_LITERAL and lti == LTI_PACKETS
#   - total bit count of all sub packets when tid != TID_LITERAL and lti == LTI_BITS
parsed = []

# Invariant: Beginning of "stack" is always start of a packet
while len(stack) >= 6:
    # First, extract packet header
    og = len(stack)
    version = int(pop(3), 2)
    tid = int(pop(3), 2)

    # not enough data for a full packet, return
    if len(stack) < 2:
        break

    if tid == TID_LITERAL:
        chunk = ''

        # keep extracting packets until there's no more
        while pop(1) == '1':
            chunk += pop(4)

        # don't forget the last packet
        chunk += pop(4)

        parsed.append((version, tid, -1, int(chunk, 2), og - len(stack)))
    else:
        # pop the length type id
        lti = int(pop(1), 2)

        if lti == 0:
            op = (version, tid, lti, int(pop(15), 2), og - len(stack))
        else:
            op = (version, tid, lti, int(pop(11), 2), og - len(stack))

        parsed.append(op)

# Part 1
print('Part #1: Version number sum:', sum(map(lambda x: x[0], parsed)))


# Part 2

def calculate(op_tid, op_args):
    if op_tid == TID_SUM:
        return sum(op_args)
    elif op_tid == TID_MUL:
        return reduce(operator.mul, op_args)
    elif op_tid == TID_MIN:
        return min(op_args)
    elif op_tid == TID_MAX:
        return max(op_args)
    elif op_tid == TID_GT:
        return int(op_args[0] > op_args[1])
    elif op_tid == TID_LT:
        return int(op_args[0] < op_args[1])
    elif op_tid == TID_EQ:
        return int(op_args[0] == op_args[1])

#
# This is the working space for the calculation.
#
# Each operation is pushed onto the stack as a (op, bit_size, [literals]) tuple.
# Each iteration, [literals] is checked to see if enough operands are
# present for calculation to run. When there are, the final result literal
# is pushed onto the parent tuple.
#
#
stack = [[parsed.pop(0), 0, []]]

while stack:
    [(_, tid, lti, val, pkt_size), bit_size, trying_for_vals] = stack[-1]

    # Are there enough operands to perform the calculation?
    if (lti == LTI_BITS and bit_size >= val) or (lti == LTI_PACKETS and len(trying_for_vals) >= val):
        stack.pop()

        if not stack:
            print('Part #2:', calculate(tid, trying_for_vals))
            break
        else:
            stack[-1][1] += val + pkt_size if LTI_BITS else bit_size + pkt_size
            stack[-1][2].append(calculate(tid, trying_for_vals))
            continue

    token = parsed.pop(0)

    (_, token_tid, _, token_val, token_pkt_size) = token

    if token_tid == TID_LITERAL:
        stack[-1][1] += token_pkt_size
        stack[-1][2].append(token_val)  # val, size
    else:
        stack.append([token, 0, []])

end = time.time()
print("Finish in", end - start, "sec")
