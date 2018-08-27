played = input()
counts = {
    'T': played.count('T'),
    'G': played.count('G'),
    'C': played.count('C'),
}

print(sum([v**2 for v in counts.values()]) + min(counts.values()) * 7)
