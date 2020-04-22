import random 

def solve(n, k_range):
    """Subtract 1 from n if n%10=0, else n=n/10."""
    for _ in k_range:
        if n%10 == 0:
            n /= 10
        else:
            n -= 1
    return int(n)

def main(n, k):    
    k_range = range(0, k)
    print(solve(n, k_range))

if __name__ == "__main__":
    inp = input().split(" ")
    n, k = int(inp[0]), int(inp[1])
    main(n, k)