S = raw_input()
K = input()

suffixes = dict()
for i in xrange(len(S)):
    idx = i + 1
    for j in xrange(idx, (len(S))+1):
        if len(S[i:j]) > len(S) / K:
            break
        if not suffixes.get(S[i:j], None):
            suffixes[S[i:j]] = []
        if suffixes[S[i:j]] and suffixes[S[i:j]][-1] + len(S[i:j]) >= i:
            del(suffixes[S[i:j]][-1])
        suffixes[S[i:j]].append(i)

count = 0
for suff, lst in suffixes.iteritems():
    if len(lst) == K:
        count += 1
print count