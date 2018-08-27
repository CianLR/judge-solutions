N = int(input())
pre_nums = [int(input()) for _ in range(N)]
post_nums = [(x//10)**(x%10) for x in pre_nums]
print(sum(post_nums))
