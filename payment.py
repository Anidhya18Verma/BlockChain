import streamlit as st
import hashlib

# Page configuration
st.set_page_config(page_title="Blockchain Payment Simulator", layout="wide")

# Initialize session state for transactions
if "transactions" not in st.session_state:
    st.session_state.transactions = []

# Sidebar input form
st.sidebar.header("Send Transaction")

sender = st.sidebar.text_input("Sender")
receiver = st.sidebar.text_input("Receiver")
amount = st.sidebar.text_input("Amount")

if st.sidebar.button("Send Transaction"):
    if not sender or not receiver or not amount:
        st.sidebar.error("Please fill in all fields.")
    else:
        tx_data = f"Sender: {sender} | Receiver: {receiver} | Amount: {amount}"
        tx_hash = hashlib.sha256(tx_data.encode()).hexdigest()
        st.session_state.transactions.append({
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
            "hash": tx_hash
        })
        st.sidebar.success("Transaction added!")

# Display transactions
st.title("Blockchain Payment Simulator")
st.subheader("Transaction History")

if st.session_state.transactions:
    for i, tx in enumerate(reversed(st.session_state.transactions), 1):
        color = "#dcebff" if i % 2 == 0 else "#c8ffc8"
        with st.container():
            st.markdown(
                f"""
                <div style="background-color:{color}; padding:10px; border-radius:5px; margin-bottom:10px;">
                    <strong>Sender:</strong> {tx['sender']}<br>
                    <strong>Receiver:</strong> {tx['receiver']}<br>
                    <strong>Amount:</strong> {tx['amount']}<br>
                    <strong>Hash:</strong> {tx['hash']}
                </div>
                """, unsafe_allow_html=True
            )
else:
    st.info("No transactions yet.")
