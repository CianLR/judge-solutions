
def gen_digits():
    digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    digits += ["eleven", "twelve", "thirteen", "fourteen", "fifteen",
               "sixteen", "seventeen", "eighteen", "nineteen"]
    for t in ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]:
        for i in xrange(10):
            digits.append(t + digits[i])
    for h in ["onehundred", "twohundred", "threehundred", "fourhundred", "fivehundred",
              "sixhundred", "sevenhundred", "eighthundred", "ninehundred"]:
        for i in xrange(100):
            digits.append(h + digits[i])
    return digits


def main():
    digits = gen_digits()
    len_to_word = {}
    for i in xrange(len(digits) - 1, 0, -1):
        len_to_word[i - len(digits[i])] = digits[i]
    N = int(raw_input())
    words = [raw_input() for _ in xrange(N)]
    chars = sum(map(len, words)) - 1
    sentence = ' '.join(words)
    print sentence.replace('$', len_to_word[chars])
    

if __name__ == '__main__':
    main()

