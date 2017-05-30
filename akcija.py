N = int(input())
books = sorted([int(input()) for _ in range(N)], reverse=True)

print(sum(books) - sum(books[2::3]))
