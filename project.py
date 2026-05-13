# Smart Village Banking & Offline Transaction System
# Simple Python Demo Project

# Local Offline Storage
offline_transactions = []

# User Balance
users = {
    "Aklesh": 5000,
    "Dharmendra": 3000
}

# Function to show balance
def check_balance(user):
    print(f"{user} Balance = ₹{users[user]}")

# Offline Transaction Function
def offline_transfer(sender, receiver, amount):

    # Check balance
    if users[sender] >= amount:

        # Save transaction locally
        transaction = {
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
            "status": "Pending Sync"
        }

        offline_transactions.append(transaction)

        # Deduct amount locally
        users[sender] -= amount

        print("\nTransaction Saved Offline")
        print("Waiting for Internet Sync...")

    else:
        print("\nInsufficient Balance")

# Sync Function
def sync_transactions():

    print("\nInternet Connected...")
    print("Syncing Transactions...\n")

    for t in offline_transactions:

        receiver = t["receiver"]
        amount = t["amount"]

        # Add money to receiver
        users[receiver] += amount

        # Update status
        t["status"] = "Completed"

        print(f"{t['sender']} sent ₹{amount} to {receiver}")

    # Clear transactions after sync
    offline_transactions.clear()

    print("\nAll Transactions Synced Successfully")

# ---------------- MAIN PROGRAM ----------------

print("SMART VILLAGE BANKING SYSTEM\n")

# Check balance before transfer
check_balance("Aklesh")
check_balance("Dharmendra")

# Offline transfer
offline_transfer("Aklesh", "Dharmendra", 1000)

# Sync when internet available
sync_transactions()

# Final balance
print("\nUpdated Balances:")
check_balance("Aklesh")
check_balance("Dharmendra")