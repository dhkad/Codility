def binary_gap(n):
    return len(max(format(n, 'b').strip('0').split('1')))


def circu_array(k, a):
    if k < len(a):
        out = a[-k:]
        tem = a[:-k]
        out.extend(tem)
    elif len(a) == k:
        out = a
    elif len(a) == 0:
        out = []
    else:
        k = k % len(a)
        out = a[-k:]
        tem = a[:-k]
        out.extend(tem)
    return out


def odd_ocu_in_array(A):

    unpaired = 0

    for item in A:
        unpaired ^= item

    return unpaired


import math


def frog_jump(X, Y, D):
    num = Y - X
    den = D
    jumps = math.ceil(num / den)

    return jumps


# A permutation is a sequence containing each element from 1 to N once, and only once.
def solution_PermCheck(A):
    if set(A) == set(range(1, 1 + len(A))):
        return 1
    else:
        return 0


def solution_min_no_not_exist(A):
    return min(set(range(1, len(A) + 2)).difference(set(A)))

'''
Detected time complexity:
O(N)
'''
def solution_tape(a):
    dmin = float('Inf')
    sum_a = sum(a)
    isums = 0
    for i in range(1,len(a)):
        isums += a[i-1]
        tsum = sum_a -isums
        d = abs(isums-tsum)
        if d<dmin:
            dmin=d
    return dmin



def solution_frogriverone(X, A):
    # write your code in Python 3.6
    s = set()
    for index, item in enumerate(A):
        s.add(item)  # حساب مجموعة الأوراق التي لا تتكرر s
        if len(s) == X:  # إذا كان طول مجموعة الأوراق غير المتكررة يساوي مسافة النهر X ، فيتم إرجاع المؤشر.
            return index
    return -1

#Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters
def solution_counter(x, a):
    count = [0] * x
    c = 0
    for item in a:
        if 1 <= item <= x:
            count[item-1] += 1
            c = max(count)
            print("less",count)
        else:
            count = [c]* x
            print("great", count)

    return count


def solution_passing_car(A):
    pairs = 0
    # count the numbers of zero discovered while traversing 'A'
    # for each successive '1' in the list, number of pairs will
    # be incremented by the number of zeros discovered before that '1'
    zero_count = 0
    # traverse through the list 'A'
    for i in range(0, len(A)):
        if A[i] == 0:
            # counting the number of zeros discovered
            zero_count += 1
        elif A[i] == 1:
            # if '1' is discovered, then number of pairs is incremented
            # by the number of '0's discovered before that '1'
            pairs += zero_count
            # if pairs is greater than 1 billion, return -1
        if pairs > 1000000000:
            return -1
    # return number of pairs
    return pairs

def solution_dna(S, P, Q):
    result = []
    for k in range(len(P)):
        p = P[k]
        q = Q[k]
        v = S[p:q + 1]

        if 'A' in v:
            result.append(1)

        elif 'C' in v:
            result.append(2)

        elif 'G' in v:
            result.append(3)

        elif 'T' in v:
            result.append(4)

    return result

#MinAvgTwoSlice Detected time complexity:O(N)

def solution_MinAvgTwoSlice1(A):
    min_avg_value = (A[0] + A[1]) / 2.0  # The mininal average
    min_avg_pos = 0  # The begin position of the first
    # slice with mininal average

    for index in range(0, len(A) - 2):
        # Try the next 2-element slice
        if (A[index] + A[index + 1]) / 2.0 < min_avg_value:
            min_avg_value = (A[index] + A[index + 1]) / 2.0
            min_avg_pos = index

        # Try the next 3-element slice
        if (A[index] + A[index + 1] + A[index + 2]) / 3.0 < min_avg_value:
            min_avg_value = (A[index] + A[index + 1] + A[index + 2]) / 3.0
            min_avg_pos = index

    # Try the last 2-element slice
    if (A[-1] + A[-2]) / 2.0 < min_avg_value:
        min_avg_value = (A[-1] + A[-2]) / 2.0
        min_avg_pos = len(A) - 2
    return min_avg_pos

def solution2_minavgslice2(a):
    total = A[0]
    left_index = 1
    length = 0
    min_average, min_index = float('inf'), float('inf')

    for index, (left, right) in enumerate(zip(A[:-1], A[1:])):
        print(index, left, right)
        total = total + right
        print("t", total)
        length = length + 1
        print("len",length)
        average = total / float(length)
        print("avg", average)
        if (left + right) / 2.0 <= average:
            total = (left + right)
            print("tot2",total)
            length = 2
            average = total / float(length)
            print("avg2",average)
            left_index = index

        if average < min_average:
            min_average = average
            min_index = left_index
    return min_index


def solution_dominator(A):
    from collections import defaultdict
    d = defaultdict(int)
    half = len(A) / 2
    for a in A:
        d[a] += 1
    for k, v in d.items():
        if v > half:
            return A.index(k)
    return -1

def reverse_cha_recurs(s):
    if len(s) == 0:
        return s
    else:

        return reverse(s[1:]) + s[0]


def conseq(A):
    s = set(A)
    ans = 0

    for i in range(len(A)):
        if A[i] - 1 not in s:

            coun = A[i]

            while coun in s:
                coun += 1
                print("coun", coun)
            ans = max(ans, coun - A[i])
    return ans

# the code gave 100% in codility
from collections import defaultdict
def solution_equileade(A):
    # write your code in Python 3.6
    marker_l = defaultdict(lambda: 0)
    marker_r = defaultdict(lambda: 0)

    for i in range(len(A)):
        marker_r[A[i]] += 1

    n_equi_leader = 0
    leader = A[0]
    for i in range(len(A)):
        marker_r[A[i]] -= 1
        marker_l[A[i]] += 1

        if i == 0 or marker_l[leader] < marker_l[A[i]]:
            leader = A[i]

        if (i + 1) // 2 < marker_l[leader] and (len(A) - (i + 1)) // 2 < marker_r[leader]:
            n_equi_leader += 1

    return n_equi_leader


def solution__bracket(S):
    # write your code in Python 3.6

    matches, stack = dict(['()', '[]', '{}']), []

    for i in S:
        if i in matches.values():
            if stack and matches[stack[-1]] == i:

                stack.pop()
            else:
                return 0
        else:
            stack.append(i)

    return int(not stack)



def solution_CountDiv(A, B, K):
    edge = 1 if A % K == 0 else 0
    return ((B - A) // K) + edge


def solution_maxproductofthre(A):
    if len(A) < 3:
        raise Exception("Invalid input")

    A.sort()
    return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])#


def solution_triangle(A):
    A_len = len(A)
    if A_len < 3:
        # N is an integer within the range [0..1,000,000]
        # if the list is too short, it is impossible to
        # find out a triangular.
        return 0

    A.sort()
    for index in range(0, A_len - 2):
        if A[index] + A[index + 1] > A[index + 2]:
            return 1
        # The list is sorted, so A[index+(i>2)] >= A[index+2]          A[P] + A[Q] > A[R],
        #         A[Q] + A[R] > A[P],
        #         A[R] + A[P] > A[Q].    [1, 2, 5, 8, 10, 20]// [1, 5, 10, 50]
        # where i>2. If A[index]+A[index+1] <= A[index+2],
        # then A[index]+A[index+1] <= A[index+i], where
        # i>=2. So there is no element in A[index+2:] that
        # could be combined with A[index] and A[index+1]
        # to be a triangular.
    # No triangular is found
    return 0


def solution_no_fdisc(A):
    upper = sorted([k + v for k, v in enumerate(A)])
    lower = sorted([k - v for k, v in enumerate(A)])

    j = 0
    counter = 0
    for i, v in enumerate(upper):
        while j < len(upper) and v >= lower[j]:
            counter += j - i
            j += 1
        if counter > 10 ** 7: return -1

    return counter


# reverse charc with nested function
def solution_reverschar(A):
    low = 0
    high = len(A) - 1

    def charechter_dh(ch):
        if 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122:
            return True
        else:
            return False

    print(charechter_dh(A[0]))
    while low < high:

        if not charechter_dh(A[low]):
            print('ggg')
            low += low
        if not charechter_dh(A[high]):
            print(A[high])
            high -= 1
        else:
            temp = A[low]
            A[low] = A[high]
            print(A[low])
            A[high] = temp
            print(A[high])
            low += 1
            high -= 1

    return A


# The leader of this array is the value that occurs in more than half of the elements of A.
def solution_eqleader(A):
    A.sort()
    print(A)
    l = len(A)
    mid = l % 2
    print(mid)
    if mid == 0:
        firstmid = (len(A) // 2) - 1
        print(firstmid)

        secmid = len(A) // 2
        print(secmid)
        if (A[secmid] == A[0]) or (A[firstmid] == A[len(A) - 1]):
            return A.index(secmid)
        else:
            return -1

    else:
        if (A[len(A) // 2] == A[0]) or (A[len(A) // 2] == A[len(A) - 1]):
            return A.index(len(A) // 2)
        else:
            return -1


if __name__ == '__main__':
    print(binary_gap(44))
    assert binary_gap(44) == 1, "List is empty."
    print(circu_array(4, [1, 2, 3, 4]))
    print(odd_ocu_in_array([2, 3, 3, 3, 3, 1, 4, 4, 1, 1, 1]))
    print(frog_jump(1, 5, 2))

    print("frogriverone", solution_frogriverone(3, [5, 1, 2, 4, 6]))
    print(solution__bracket("{[()()]}"))
