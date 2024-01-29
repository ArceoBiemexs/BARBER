import streamlit as st
import pandas as pd
import hashlib
import time



# Sample data for the barber shop
data = pd.DataFrame({
    'Style': ['Classic Cut', 'Fade', 'Pompadour', 'Buzz Cut', 'Undercut'],
    'Description': [
        'Timeless and clean look suitable for any occasion.',
        'Gradual transition from short to long, modern style.',
        'High volume on top with shorter sides.',
        'Short and uniform length all around.',
        'Longer hair on top with short sides and back.'
    ]
})


#   DATABASE





###


# Sample data for user testimonials
testimonials = pd.DataFrame({
    'Client': ['John', 'Jane', 'Alex'],
    'Testimonial': [
        'Excellent service! I always leave satisfied with my haircut.',
        'The barbers are skilled and friendly. Great atmosphere!',
        'I love the attention to detail. Best barbershop in town!'
    ]
})

# Sample data for barbers
barbers = pd.DataFrame({
    'Name': ['Barber1', 'Barber2', 'Barber3'],
    'Bio': [
        'With over 10 years of experience, Barber1 is dedicated to providing top-notch haircuts.',
        'Barber2 is known for keeping up with the latest trends and delivering exceptional results.',
        'Barber3 is passionate about creating unique styles that suit each client.'
    ]
})

# Sample data for popular styles
popular_styles = pd.DataFrame({
    'Style': ['Classic Cut', 'Fade', 'Pompadour']
})

# Function to authenticate user login
def authenticate(username, password):
    # Add your own logic for authentication (e.g., using a database)
    # For simplicity, using hardcoded credentials in this example
    users = {'user1': 'pass1', 'user2': 'pass2'}
    return users.get(username) == password

# Streamlit App
def main():
    st.title("Barbershop Website")

    # Login section
    st.sidebar.header("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if authenticate(username, password):
            st.success(f"Welcome, {username}!")
            show_homepage()
        else:
            st.error("Invalid credentials. Please try again.")

def show_homepage():
    st.image("barbershop_logo.png", width=200)
    st.subheader("Welcome to Our Barbershop")

    # Navigation
    navigation = st.radio("Navigate", ["Services", "Gallery", "Barbers", "Testimonials", "Contact"])
    
    if navigation == "Services":
        show_services()
    elif navigation == "Gallery":
        show_gallery()
    elif navigation == "Barbers":
        show_barbers()
    elif navigation == "Testimonials":
        show_testimonials()
    elif navigation == "Contact":
        show_contact()

def show_services():
    st.header("Our Services")
    st.table(data)
    st.header("agregar clientes")
    
    

def show_gallery():
    st.header("Gallery")
    st.subheader("Popular Styles")
    st.image("classic_cut.jpg", caption="Classic Cut", width=200)
    st.image("fade.jpg", caption="Fade", width=200)
    st.image("pompadour.jpg", caption="Pompadour", width=200)
    st.write("Explore more styles in our portfolio.")

def show_barbers():
    st.header("Meet Our Barbers")
    st.table(barbers)

def show_testimonials():
    st.header("Client Testimonials")
    st.table(testimonials)

def show_contact():
    st.header("Contact Us")
    st.subheader("Visit Our Barbershop")
    st.write("123 Main Street, Cityville")
    st.subheader("Call Us")
    st.write("+123 456 7890")
    st.subheader("Business Hours")
    st.write("Monday to Saturday: 9:00 AM - 7:00 PM")

if __name__ == "__main__":
    main()
