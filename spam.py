from random import shuffle

liste = " amazing gorgeous blazing stunning bold stunning tremendous \
          fantastic phenomenal delightful ambitious exciting staggering \
          outstanding magical revolutionary incredible amazing intuitive \
          beautiful jaw-dropping".upper().split()

shuffle(liste)

for strophe in range(5):
    for n in range(2):
        for i in range(4):
            print('SPAM ',end='')
        print()

    el1 = liste.pop()
    el2 = liste.pop()
    print( '{} SPAM, {} SPAM'.format(el1, el2))
    #print(liste.pop()+ ' SPAM, ' + liste.pop()+ ' SPAM') 
    print()   
