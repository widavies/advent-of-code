from statistics import median

opening = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>'
}

closing = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137
}

closing2 = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4
}

with open(0) as f:
  score = 0
  scores2 = []

  for input in f:
    stack = []

    for letter in input.rstrip():
      if letter in opening:
        stack.append(opening[letter])
      elif letter != stack.pop():
        score += closing[letter]
        stack.clear()
        break
    else:
      score2 = 0

      while stack:
        score2 = closing2[stack.pop()] + 5 * score2

      scores2.append(score2)

  # Part 1
  print(score)

  # Part 2
  print(median(scores2))

  # Improvements: for else statement comes in handy here
