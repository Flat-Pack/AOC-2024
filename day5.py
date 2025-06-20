
#%%

rules, tests = {}, []

with open('day5.txt', "r") as file:
  for line in file:
    if "|" in line:
        x, y = line.split("|")
        rules[x] = rules[x].append(y) if rules[x] else [y]
    elif "," in line:
        tests.append(line.split())

def is_sorted(rules, test):
  for i in test:
    for j in test[i+1:]:
      if j in rules[i]:
        return False
  return test[len(test)//2]

total = 0

for t in tests:
  x = is_sorted(t)
  if x: total += x

print(total)
