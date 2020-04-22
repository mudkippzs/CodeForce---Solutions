def solve(n):
    if n == 1:
        f = "I hate it"
    else:
        fs = "I hate"
        sl = " that I love "
        sh = " that I hate "
        cnt = 0
        while cnt < n - 1:      
            if cnt %2 == 0:
                fs += sl
            else:
                fs += sh
            cnt += 1
        f = fs + "it"
    print(f)

if __name__ == "__main__":
    i = input()
    solve(i)
