for i in xrange(int(raw_input())):
    word = raw_input()
    n = len(word)
    sim = [0] * n
    sim[0] = n
    pos = 1
    left = 0
    while True:
        if pos + left < n and word[pos + left] == word[left]:
            left += 1
        else:
            if pos >= n:
                break
            if left == 0:
                pos += 1
                continue
            sim[pos] = left
            flag = left
            i = 1
            while i < left:
                if word[pos + i] == word[0]:
                    if sim[i] != left - i:
                        sim[pos + i] = min(left - i, sim[i])
                    else:
                        flag = i
                        break
                i += 1
            pos += flag
            left -= flag
    print sum(sim)