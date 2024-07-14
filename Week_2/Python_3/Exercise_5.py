from collections import Counter

s = input()
s = s.strip("[]")
s_list = s.split(",")

counter = Counter(s_list)

for item, count in counter.items():
    print(f"{item} = {count}")