import streamlit as st
import pandas as pd

# In-memory database (dictionary) to store clients
clients_database = {}

# Function to add a new client to the database
def add_client(client_id, name, email, phone):
    clients_database[client_id] = {'Name': name, 'Email': email, 'Phone': phone}

# Streamlit App
def main():
    st.title("Client Database Management")

    # Sidebar for adding clients
    st.sidebar.header("Add New Client")

    client_id = st.sidebar.text_input("Client ID", "")
    name = st.sidebar.text_input("Name", "")
    email = st.sidebar.text_input("Email", "")
    phone = st.sidebar.text_input("Phone", "")

    if st.sidebar.button("Add Client"):
        if client_id and name and email and phone:
            add_client(client_id, name, email, phone)
            st.sidebar.success("Client added successfully!")
        else:
            st.sidebar.error("Please fill in all the fields.")

    # Display the current database
    st.header("Current Client Database")
    if clients_database:
        st.table(pd.DataFrame(clients_database).T)
    else:
        st.info("No clients in the database yet.")

if __name__ == "__main__":
    main()
