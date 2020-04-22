def solve(b):
    years = 0
    while b[0] <= b[1]:
        b[0] *= 3
        b[1] *= 2        
        years += 1
    return years


def main(b):
    b = b.split(" ")
    b = [int(b_str) for b_str in b]
    print(solve(b))

if __name__ == "__main__":
     b = input()
     main(b)
