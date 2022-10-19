'''
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.

'''
def high(x):
    val=dict()
    ar=range(1,27)
    alp=[chr(i) for i in range(97, 123)]
    w=dict(zip(alp,ar))
    for i in x.split():
        s=0
        for k in i:
            valu=w.get(k)
            s+=valu
        val.update({i:s})
    return max(val,key=val.get)