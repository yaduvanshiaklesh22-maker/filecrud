import streamlit as st
import qrcode

# -----------------------------------
# SESSION STATE
# -----------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "offline_transactions" not in st.session_state:
    st.session_state.offline_transactions = []

# USER DATABASE SAVE IN SESSION
if "users" not in st.session_state:

    st.session_state.users = {
        "Aklesh": 5000,
        "Ravi": 3000
    }

# -----------------------------------
# LOGIN DATA
# -----------------------------------

login_data = {
    "Aklesh": "1234"
}

# -----------------------------------
# TITLE
# -----------------------------------

st.title("Smart Village Banking & Offline Transaction System")

# -----------------------------------
# LOGIN PAGE
# -----------------------------------

if not st.session_state.logged_in:

    username = st.text_input("Enter Username")

    password = st.text_input(
        "Enter Password",
        type="password"
    )

    if st.button("Login"):

        if username in login_data and login_data[username] == password:

            st.session_state.logged_in = True

            st.success("Login Successful")

        else:

            st.error("Invalid Username or Password")

# -----------------------------------
# DASHBOARD
# -----------------------------------

if st.session_state.logged_in:

    st.header("Banking Dashboard")

    # SELECT SENDER
    sender = st.selectbox(
        "Select Sender",
        list(st.session_state.users.keys())
    )

    # SELECT RECEIVER
    receiver = st.selectbox(
        "Select Receiver",
        list(st.session_state.users.keys())
    )

    # ENTER AMOUNT
    amount = st.number_input(
        "Enter Amount",
        min_value=1
    )

    # INTERNET CHECK
    internet = st.checkbox("Internet Available")

    # -----------------------------------
    # SEND MONEY
    # -----------------------------------

    if st.button("Send Money"):

        if sender == receiver:

            st.error(
                "Sender and Receiver cannot be same"
            )

        elif st.session_state.users[sender] >= amount:

            # ONLINE TRANSACTION
            if internet:

                st.session_state.users[sender] -= amount

                st.session_state.users[receiver] += amount

                st.success(
                    "Transaction Successful"
                )

            # OFFLINE TRANSACTION
            else:

                st.session_state.users[sender] -= amount

                transaction = {
                    "sender": sender,
                    "receiver": receiver,
                    "amount": amount,
                    "status": "Pending"
                }

                st.session_state.offline_transactions.append(
                    transaction
                )

                st.warning(
                    "Internet Not Available\nTransaction Saved Offline"
                )

        else:

            st.error("Insufficient Balance")

    # -----------------------------------
    # SYNC TRANSACTIONS
    # -----------------------------------

    if st.button("Sync Transactions"):

        for t in st.session_state.offline_transactions:

            st.session_state.users[t["receiver"]] += t["amount"]

            t["status"] = "Completed"

        st.success(
            "All Offline Transactions Synced"
        )

        st.session_state.offline_transactions.clear()

    # -----------------------------------
    # USER BALANCES
    # -----------------------------------

    st.subheader("User Balances")

    for user, balance in st.session_state.users.items():

        st.write(user, ":", balance)

    # -----------------------------------
    # OFFLINE HISTORY
    # -----------------------------------

    st.subheader("Offline Transaction History")

    if st.session_state.offline_transactions:

        for t in st.session_state.offline_transactions:

            st.write(t)

    else:

        st.info(
            "No Pending Offline Transactions"
        )

    # -----------------------------------
    # QR CODE
    # -----------------------------------

    st.subheader("QR Code Payment")

    if st.button("Generate QR Code"):

        img = qrcode.make(
            "Pay To Smart Village Banking"
        )

        img.save("qr.png")

        st.image("qr.png")

    # -----------------------------------
    # FINGERPRINT
    # -----------------------------------

    st.subheader("Fingerprint Verification")

    if st.button("Verify Fingerprint"):

        st.success(
            "Fingerprint Verified Successfully"
        )