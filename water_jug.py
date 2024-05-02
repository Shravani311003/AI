def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def min_steps(n, m, d):
    if m > n:
        n, m = m, n

    if d % gcd(n, m) != 0:
        return -1
    
    return min(Pour(n, m, d), Pour(m, n, d))

def Pour(toJugCap, fromJugCap, d):
    fromJug = fromJugCap
    toJug = 0
    step = 1

    while fromJug != d and toJug != d:
        temp = min(fromJug, toJugCap - toJug)
        toJug += temp
        fromJug -= temp
        step += 1
        

        if fromJug == d or toJug == d:
            break

        if fromJug == 0:
            fromJug = fromJugCap
            step += 1
        
        if toJug == toJugCap:
            toJug = 0
            step += 1

    return step

if __name__ == "__main__":
    n = 3
    m = 5
    d = 4

    print("Minimum number of steps required is", min_steps(n, m, d))
