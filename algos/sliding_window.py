# Sliding window algorithm, useful for having to compare array slices
# and similar things

# Reduces time-complexity of brute-force approach, so it's also probably
# good to know for just general usage.

def find_max_sum(a, k): 
    '''
    `a` is the input. It can be any iterable. If it is a string, as
    I the leetcode examples can be, it still has iterable properties, but
    as this is summing, it won't work.

    `k` is the size of the window
    '''
    n = len(a)

    current = 0 #set the current size to 0

    maximum = 0 #set the max to 0 to start with

    #sum of the first window
    for i in range(0, k):
        current += a[i]

    maximum = current

    for i in range(k, n):
        #account for left element
        current -= a[i-k]

        #add in current element
        current += a[i]

        if maximum < current:
            maximum = current
    return maximum

a = [2, 3, 4,6, 7, 1, 19, 24, 3]
k = 2
print(find_max_sum(a, k))


class Substring_Window:
    #basically a regexer
    def areCountsEqual(self, t:iter, p:iter) -> iter:
        #t = text
        #p = pattern
        for i in range(0,256):
            if t[i] != p[i]:
                return False
        return True

    def indexer(self, t, p):
        #t = text
        #p = pattern

        n = len(t)
        m = len(p)

        #blank index array to hold patterns
        index = []

        #frequency arrays
        #assumption is 256 characters, adjust if necessary
        t_count = [0] * 256 
        p_count = [0] * 256

        #loop through first m characters
        for i in range(0,m):
            t_count[ord(t[i])] += 1
            p_count[ord(p[i])] += 1

        for i in range(m, n):
            if self.areCountsEqual(t_count, p_count):
                index.append(i-m)
            
            #discard leftmost
            t_count[ord(t[i-m])] -= 1
            #add current
            t_count[ord(t[i])] += 1
        
        if self.areCountsEqual(t_count, p_count):
            index.append(n-m)
        return index

t = "ABCABCDABCDABCDEDFADCABC"
p = "ABC"


print(Substring_Window().indexer(t, p))
class LongestSubstring:
    #kind of a combination of the two above

    def findLengthCommonSubstring(self, s:str) -> int:
        
        if s == "":
            return 0
        #pointers
        start = 0
        end = 0
        
        uniques = set()

        maxLength = 0

        while end < len(s):
            if s[end] not in uniques:
                uniques.add(s[end])
                end += 1
                maxLength = max(maxLength, len(uniques))
            else:
                uniques.remove(s[start])
                start += 1

        return maxLength

s = "abcaabcdabcd"
print(LongestSubstring().findLengthCommonSubstring(s))
