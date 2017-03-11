N = int(input())
for _ in range(N):
    name, post_sec, dob, courses = input().split(' ')
    if int(post_sec[:4]) > 2009 or int(dob[:4]) > 1990:
        print(name, 'eligible')
    elif int(courses) > 40:
        print(name, 'ineligible')
    else:
        print(name, 'coach petitions')
