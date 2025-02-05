import streamlit as st
import random
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

# Define motivational quotes for different categories
quotes = {
    "Money": [
        "The best investment you can make is in yourself.",
        "Money is only a tool. It will take you wherever you wish, but it will not replace you as the driver.",
        "It's not how much money you make, but how much money you keep, how hard it works for you, and how many generations you keep it for.",
        "Financial freedom is available to those who learn about it and work for it."
    ],
    "Family": [
        "Family is not an important thing. It's everything.",
        "The love of a family is life's greatest blessing.",
        "In family life, love is the oil that eases friction, the cement that binds closer together, and the music that brings harmony.",
        "Family means no one gets left behind or forgotten."
    ],
    "Education": [
        "Education is the most powerful weapon which you can use to change the world.",
        "The roots of education are bitter, but the fruit is sweet.",
        "Education is not preparation for life; education is life itself.",
        "An investment in knowledge pays the best interest."
    ],
    "Success": [
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Success usually comes to those who are too busy to be looking for it.",
        "The only place where success comes before work is in the dictionary.",
        "Success is walking from failure to failure with no loss of enthusiasm."
    ]
}

# Streamlit app
def main():
    st.set_page_config(page_title="Motivational Quotes Generator", page_icon="📚", layout="wide")

    # Header Section
    st.title("Motivational Quotes Generator 📖")
    st.markdown("""
    A professional platform for discovering, sharing, and enjoying motivational quotes to inspire your journey.
    """)

    # Sidebar for Navigation and Category Selection
    st.sidebar.header("Navigation")
    sidebar_option = st.sidebar.radio("Choose an Option", ["Quote of the Day", "Browse Quotes", "Submit a Quote"])

    # Quote of the Day
    if sidebar_option == "Quote of the Day":
        display_quote_of_the_day()

    # Browse Quotes
    elif sidebar_option == "Browse Quotes":
        category = st.selectbox("Select a category:", list(quotes.keys()))
        display_quote_by_category(category)

    # Submit a Quote
    elif sidebar_option == "Submit a Quote":
        submit_quote_form()

def display_quote_of_the_day():
    # Display random quote of the day with professional styling
    random_quote = random.choice(random.choice(list(quotes.values())))
    st.markdown(f"### Quote of the Day: 🏆")
    st.markdown(f"<p style='font-size: 24px; color: #2C3E50; font-weight: bold;'>{random_quote}</p>", unsafe_allow_html=True)
    st.markdown("---")
    st.write("Start your day with this inspiring quote!")

def display_quote_by_category(category):
    # Display random quote from selected category
    st.header(f"Quotes on {category}")
    if category in quotes:
        random_quote = random.choice(quotes[category])
        st.markdown(f"<p style='font-size: 20px; color: #2980B9;'>{random_quote}</p>", unsafe_allow_html=True)
        st.markdown("---")
        
        # Add sharing options
        st.markdown(f"**Share this quote**: ")
        whatsapp_url = f"https://wa.me/?text={random_quote}"
        st.markdown(f"[Share on WhatsApp]( {whatsapp_url} )")

        twitter_url = f"https://twitter.com/intent/tweet?text={random_quote}"
        st.markdown(f"[Share on Twitter]( {twitter_url} )")

        linkedin_url = f"https://www.linkedin.com/sharing/share-offsite/?url={random_quote}"
        st.markdown(f"[Share on LinkedIn]( {linkedin_url} )")

def submit_quote_form():
    st.header("Submit a Motivational Quote ✍️")
    st.write("Submit your favorite quote below, and it will be reviewed and added to the collection!")
    
    user_quote = st.text_area("Enter your quote here:")
    user_name = st.text_input("Your name (optional):")
    submit_button = st.button("Submit Quote")

    if submit_button:
        if user_quote:
            st.success("Thank you for submitting your quote! It will be reviewed.")
            # Optionally save to a database or file
            # Add to the quotes dictionary or store in a CSV file
            quotes["User Submissions"].append(user_quote)
        else:
            st.error("Please enter a quote before submitting.")

def generate_image_with_quote(quote):
    # Create an image with PIL
    img = Image.new('RGB', (600, 250), color='#F0F4F8')
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    # Add the quote text to the image
    draw.text((20, 80), quote, font=font, fill='#2C3E50')
    
    return img

if __name__ == "__main__":
    main()
