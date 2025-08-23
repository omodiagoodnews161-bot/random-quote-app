import streamlit as st
import requests
import random
import urllib.parse

st.set_page_config(page_title="Random Quote Generator", page_icon="✨", layout="centered")

st.title("✨ Random Quote Generator")
st.write("Click below to get inspired!")

# Function to fetch a random quote
def get_quote():
    try:
        response = requests.get("https://api.quotable.io/random")
        if response.status_code == 200:
            data = response.json()
            return f"“{data['content']}” — {data['author']}"
        else:
            return None
    except:
        return None

quote = None

if st.button("💡 Inspire Me"):
    quote = get_quote()
    
    if not quote:  # fallback if API fails
        quote = random.choice([
            "Keep going, you’re doing great!",
            "Every step counts, no matter how small.",
            "Your future self will thank you for today."
        ])
    
    # Show the quote inside a styled box (soft blue background 💙)
    st.markdown(
        f"""
        <div style='
            background-color:#e6f3ff;
            border-radius:15px;
            padding:20px;
            margin-top:20px;
            box-shadow:2px 2px 10px rgba(0,0,0,0.1);
            font-size:20px;
            font-style:italic;
            text-align:center;
        '>
            {quote}
        </div>
        """,
        unsafe_allow_html=True
    )

    # Copy to clipboard
    st.code(quote, language="")

    # Share to Twitter link
    tweet_url = "https://twitter.com/intent/tweet?text=" + urllib.parse.quote(quote)
    st.markdown(f"[🐦 Share this quote on Twitter]({tweet_url})")

custom_st_style = """
    <style>
    #MainMenu {visibility: hidden;}     /* Hides the hamburger menu */
    header {visibility: hidden;}       /* Hides the header */
    footer {visibility: hidden;}       /* Hides the default footer */
    
    /* Add custom footer */
    .custom-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0e1117; /* dark background */
        color: #fafafa;            
        text-align: center;
        padding: 10px;
        font-size: 14px;
        border-top: 1px solid #444;
        z-index: 100;
    }

    .custom-footer a {
        color: #61dafb; /* link color (light blue) */
        text-decoration: none;
        margin: 0 8px;
    }

    .custom-footer a:hover {
        text-decoration: underline;
    }

    /* Responsive design */
    @media (max-width: 768px) {
        .custom-footer {
            font-size: 12px;
            padding: 8px;
        }
    }

    @media (max-width: 480px) {
        .custom-footer {
            font-size: 11px;
            padding: 6px;
        }
    }
    </style>

    <div class="custom-footer">
        Built by <b>Goodnews</b> © 2025 | Powered with ❤️ by Streamlit <br>
        <a href="https://github.com/yourusername" target="_blank">GitHub</a> |
        
    </div>
"""
st.markdown(custom_st_style, unsafe_allow_html=True)
