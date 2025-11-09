steps = int(input())

owner = {
    "fishing": "alice",
    "golf": "bob",
    "hockey": "charlie"
}

for i in range(steps):
    words = input().split()
    borrower = words[0]
    game = words[-1]

    if (owner[game] == borrower):
        print(f"{borrower} already has {game}")
    else:
        print(f"{borrower} borrows {game} from {owner[game]}")
        
        # Perform transfer
        owner[game] = borrower
