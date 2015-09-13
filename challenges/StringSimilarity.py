def compute_prefix_array(prefix):
    result = [0] * len(prefix)
    matched = 0
    for i in xrange(1, len(prefix)):
        while matched > 0 and prefix[matched] != prefix[i]:
            matched = result[matched - 1]
        if prefix[matched] == prefix[i]:
            matched += 1
        result[i] = matched
    return result

def  StringSimilarity( inputs):
    result = []
    for s in inputs:
        prefix_array = compute_prefix_array(s)
        sum_array = []
        count = len(s)
        for i in xrange(len(s)):
            if prefix_array[i]:
                prefix_array[i] = prefix_array[prefix_array[i] - 1] + 1
            sum_array.append(prefix_array[i])
            count += sum_array[-1]
        result.append(count)
    return result