name = input()

last_c = name[0]
new_name = name[0]
for c in name[1:]:
    if c == last_c:
        continue
    new_name += c
    last_c = c

print(new_name)
