# Segment reference:
#  1 
# 2 3
#  4
# 5 6
#  7

num_segments = {
    frozenset([1, 2, 3, 5, 6, 7]): 0,
    frozenset([3, 6]): 1,
    frozenset([1, 3, 4, 5, 7]): 2,
    frozenset([1, 3, 4, 6, 7]): 3,
    frozenset([2, 3, 4, 6]): 4,
    frozenset([1, 2, 4, 6, 7]): 5,
    frozenset([1, 2, 4, 5, 6, 7]): 6,
    frozenset([1, 3, 6]): 7,
    frozenset([1, 2, 3, 4, 5, 6, 7]): 8,
    frozenset([1, 2, 3, 4, 6, 7]): 9,
}

class Number:
    def __init__(self, segs_lit, segs_unsure, is_first=False):
        lit_set = frozenset(segs_lit)
        total_set = frozenset(segs_lit + segs_unsure)
        self.possibilities = set([0] if len(segs_lit) == 0 and is_first else [])
        for seg_set in num_segments:
            if lit_set.issubset(seg_set) and seg_set.issubset(total_set):
                # If everything lit is in the num and
                # all the required segs are available
                self.possibilities.add(num_segments[seg_set])


class Time:
    def __init__(self, str_list):
        nums = ['']*4
        for line in str_list:
            nums[0] += line[:3]
            nums[1] += line[5:8]
            nums[2] += line[12:15]
            nums[3] += line[17:20] + (' ' if len(line) == 19 else '')
        seg_indicies = {
            1: 1,
            2: 3, 3: 5,
            4: 7,
            5: 9, 6: 11,
            7: 13,
        }
        self.numbers = []
        for i, num_str in enumerate(nums):
            lit_segs = []
            unsure_segs = []
            for seg in seg_indicies:
                if num_str[seg_indicies[seg]] == '.':
                    continue
                elif num_str[seg_indicies[seg]] == '?':
                    unsure_segs.append(seg)
                else:
                    lit_segs.append(seg)
            self.numbers.append(
                Number(lit_segs, unsure_segs, is_first=i==0))

    def get_unambigious_time(self):
        time = []
        for n in self.numbers:
            if len(n.possibilities) != 1:
                return None
            time.append(list(n.possibilities)[0])

    def could_be_time(self, num_list):
        assert(len(num_list) == 4)
        for pos, n in zip(num_list, self.numbers):
            if pos not in n.possibilities:
                return False
        return True

    def get_all_posibilities(self):
        pos = set()
        for p1 in self.numbers[0].possibilities:
            for p2 in self.numbers[1].possibilities:
                for p3 in self.numbers[2].possibilities:
                    for p4 in self.numbers[3].possibilities:
                        if is_valid_time((p1, p2, p3, p4)):
                            pos.add((p1, p2, p3, p4))
        return pos


def is_valid_time(tl):
    return (0 <= tl[0]*10 + tl[1] < 24) and (0 <= tl[2]*10 + tl[3] < 60)

def print_time_list(tl):
    s = '{}{}:{}{}'.format(*tl)
    if tl[0] == 0:
        s = s[1:]
    print(s)

def tl_difference(tlb, tla):
    # Early, late
    hrsa = tla[0]*10 + tla[1]
    minsa = tla[2]*10 + tla[3]
    hrsb = tlb[0]*10 + tlb[1]
    minsb = tlb[2]*10 + tlb[3]

    diff = (hrsa - hrsb) * 60
    diff += minsa - minsb
    return diff % (24 * 60)

def add_time_list(tl, add_mins):
    hrs = tl[0]*10 + tl[1]
    mins = tl[2]*10 + tl[3]

    carry = (mins + add_mins)//60
    mins = (mins + add_mins) % 60
    hrs = (hrs + carry) % 24
    return hrs//10, hrs%10, mins//10, mins%10

if __name__ == '__main__':
    N = int(input())
    while N:
        times = [Time([input() for _ in range(5)])]
        differences = []
        for _ in range(1, N):
            s, e = map(int, input().split())
            differences.append((s, e))
            times.append(Time([input() for _ in range(5)]))
        
        possibles = []
        for i in range(N):
            all_posses = times[i].get_all_posibilities()
            reachable_posses = set()
            if i == 0:
                reachable_posses = all_posses
            else:
                s, e = differences[i - 1]
                for prev_pos in possibles[-1]:
                    for pos in (all_posses - reachable_posses):
                        if s <= tl_difference(prev_pos, pos) <= e:
                            reachable_posses.add(pos)
            
            possibles.append(reachable_posses)

        # Propigate the knowledge backwards
        new_posses = [possibles[-1]]
        for i in range(N - 1, 0, -1):
            # Eg. 5 -> 4 -> 3 -> 2 -> 1
            s, e = differences[i - 1]
            new_previous_posses = set()
            for curr_pos in possibles[i]:
                for back_pos in (possibles[i - 1] - new_previous_posses):
                    diff = tl_difference(back_pos, curr_pos)
                    if s <= diff <= e:
                        new_previous_posses.add(back_pos)
            new_posses.append(new_previous_posses)

        for pos in new_posses[::-1]:
            if len(pos) == 1:
                print_time_list(list(pos)[0])
            else:
                print("ambiguous, {} possibilities".format(len(pos)))
        
        print()
        N = int(input())
