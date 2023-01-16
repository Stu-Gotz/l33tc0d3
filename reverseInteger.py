def reverse(x: int) -> int:
    if x >= 2 ** 31 - 1 or x <= -2 ** 31: 
        return 0
    else:
        s = str(abs(x))
        rev = s[::-1]
        if x < 0:
            rev = "-" + rev
    if int(rev) >= 2 ** 31 -1 or int(rev) <= -2 ** 31:
        return 0
    else:
        return int(rev)

print(reverse(321))
print(reverse(5673934))