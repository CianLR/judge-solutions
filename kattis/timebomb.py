import sys

numbers = '''
***  ******** ****************
* *  *  *  ** **  *    ** ** *
* *  ****************  *******
* *  **    *  *  ** *  ** *  *
***  *******  *******  *******
'''.split('\n')

num_list = []
for i in range(10):
    num_list.append(
        ''.join([l[i*3:(i+1)*3] for l in numbers])
    )

in_num = sys.stdin.readlines()
in_num_list = []
for i in range(len(in_num[0])//4):
    in_num_list.append(
        ''.join(l[i*4:((i+1)*4)-1] for l in in_num)
    )

final_num = 0
for num in in_num_list:
    if num not in num_list:
        print("BOOM!!")
        sys.exit()
    final_num *= 10
    final_num += num_list.index(num)

print("BOOM!!" if final_num % 6 else 'BEER!!')
