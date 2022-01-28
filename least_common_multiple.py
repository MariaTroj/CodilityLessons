# lcm(a1, a2, . . . , an) = lcm(a1, lcm(a2, a3, . . . , an))
# a * b = lcm(a, b) * gcd(a, b)
def lcm(numbers):
    a, *rest = numbers
    if len(numbers) == 2:
        return lcm_of_two(a, rest[0])
    else:
        return lcm([a, lcm(rest)])

def lcm_of_two(a, b):
    return a * b / gcd(a, b)

# gcd(a, b) = gcd(b, r)
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(lcm([2, 3, 12, 4, 6, 12]))