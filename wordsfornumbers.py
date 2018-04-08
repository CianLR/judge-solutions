from sys import stdin

smalls = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
]

tens = [
    None,
    None,
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety'
]

def digit_to_words(d):
    if d < len(smalls):
        return smalls[d]
    t, o = divmod(d, 10)
    return tens[t] + ('-' + smalls[o] if o else '')

def main():
    for line in stdin.readlines():
        tokens = line.split()
        for i in range(len(tokens)):
            if tokens[i].isdecimal():
                tokens[i] = digit_to_words(int(tokens[i]))
        print(' '.join(tokens).capitalize())

if __name__ == '__main__':
    main()

