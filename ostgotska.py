
def main():
    words = raw_input().split()
    ae_in = sum(map(lambda w: 'ae' in w, words))
    if ae_in / float(len(words)) >= 0.4:
        print "dae ae ju traeligt va"
    else:
        print "haer talar vi rikssvenska"

if __name__ == '__main__':
    main()

