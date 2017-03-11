curr_dir = int(input())
true_dir = int(input())

clock_spin = (true_dir - curr_dir) % 360
counter_spin = (curr_dir - true_dir) % 360

if clock_spin <= counter_spin:
    print(clock_spin)
else:
    print(-counter_spin)
