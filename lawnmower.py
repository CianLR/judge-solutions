
ADD = 0
END = 1

def generate_events(passes, width):
    events = []
    for p in passes:
        events.append((p - (width / 2), ADD))
        events.append((p + (width / 2), END))
    return sorted(events)

def full_coverage(passes, width, size):
    events = generate_events(passes, width)
    if events[0][0] > 0 or events[-1][0] < size:
        return False

    cuts = 1
    for _, event_type in events[1:-1]:
        cuts += 1 if event_type == ADD else -1
        if cuts == 0:
            return False
    return True

def main():
    nx, ny, w = [float(x) for x in input().split()]
    while nx or ny or w:
        x_passes = [float(x) for x in input().split()]
        y_passes = [float(x) for x in input().split()]
        if full_coverage(x_passes, w, 75) and full_coverage(y_passes, w, 100):
            print("YES")
        else:
            print("NO")
        
        nx, ny, w = [float(x) for x in input().split()]


if __name__ == '__main__':
    main()

