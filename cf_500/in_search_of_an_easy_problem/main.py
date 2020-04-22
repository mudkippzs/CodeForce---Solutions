def solve(np, votes):
    """Check if 1 is in votes and if np is the same as the number of votes."""
    if "1" in votes and len(votes) == int(np):
        return "HARD"
    else:
        return "EASY"

def main(np, votes):
    """Main loop."""    
    print(solve(np, votes))

if __name__ == "__main__":
    np = input()
    votes = input().replace(" ","")
    main(np, votes)