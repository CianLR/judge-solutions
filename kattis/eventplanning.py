
class Hotel:
    def __init__(self, price, beds):
        self.price = price
        self.beds = beds

def min_cost(people, hotels):
    min_cost = 500001
    for h in hotels:
        for w in h.beds:
            if w >= people:
                min_cost = min(min_cost, people * h.price)
    return min_cost

def main():
    N, B, H, W = map(int, input().split())
    hotels = []
    for _ in range(H):
        P = int(input())
        hotels.append(Hotel(P, [int(x) for x in input().split()]))
    mc = min_cost(N, hotels)
    print(mc if mc <= B else "stay home")

if __name__ == '__main__':
    main()

