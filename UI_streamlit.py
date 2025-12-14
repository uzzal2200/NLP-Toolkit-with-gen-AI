"""
AI NLP Toolkit - Streamlit UI Application
==========================================
Author: Your Name
Date: December 2025
Description: A modern web-based NLP toolkit powered by Google Gemini AI.
            Provides 21+ NLP tasks with user authentication and dark theme UI.

Features:
- User registration and login with session management
- 21 different NLP tasks (sentiment analysis, translation, summarization, etc.)
- Dark theme with gradient styling
- Real-time AI-powered text analysis

Usage:
    streamlit run UI_streamlit.py
"""

import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# ============================
# CONFIGURATION & SETUP
# ============================

# Load environment variables from .env file
# This file should contain: GOOGLE_API_KEY or GEMINI_API_KEY
load_dotenv()

# Configure Gemini AI client with API key from environment
# The API key is loaded from .env file for security
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model (gemini-2.5-flash is fast and cost-effective)
model = genai.GenerativeModel("gemini-2.5-flash")

# ============================
# SESSION STATE MANAGEMENT
# ============================
# Streamlit session state persists data across reruns
# This is used for user authentication and app state

# Initialize users dictionary to store registered users
# Format: {email: [name, password]}
if "users" not in st.session_state:
    st.session_state.users = {}

# Track login status - False by default (user not logged in)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ============================
# PAGE CONFIGURATION
# ============================
# Configure the Streamlit page settings
# This must be the first Streamlit command in the script
st.set_page_config(
    page_title="AI NLP Toolkit",        # Browser tab title
    page_icon="🤖",                     # Browser tab icon
    layout="wide",                       # Use full width of the screen
    initial_sidebar_state="expanded"     # Sidebar expanded by default
)

# ============================
# CUSTOM CSS STYLING
# ============================
# Inject custom CSS for dark theme and professional design
# - Dark background for main app
# - Purple gradient header
# - Styled buttons with hover effects
# - Dark cards for displaying results
st.markdown("""
<style>
    body, .stApp {
        background-color: #0e1117;
        color: #e6e6e6;
    }
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton>button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #764ba2 0%, #667eea 100%);
    }
    .task-card {
        background: #1e293b; /* dark card */
        color: #f8fafc;      /* text visible on dark */
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #334155;
        box-shadow: 0 8px 24px rgba(0,0,0,0.35);
    }
    .task-card h1, .task-card h2, .task-card h3, .task-card p, .task-card li {
        color: #f8fafc;
    }
</style>
""", unsafe_allow_html=True)

# Render the main header with gradient background
st.markdown('<div class="main-header"><h1>🤖 AI-Powered NLP Toolkit</h1><p>Advanced Natural Language Processing with Gemini AI</p></div>', unsafe_allow_html=True)

# ============================
# AUTHENTICATION SECTION
# ============================
# Show login/registration forms if user is not logged in
# Session state manages the authentication status
if not st.session_state.logged_in:

    # Radio button to switch between Login and Register
    menu = st.radio("Choose an option", ["Login", "Register"])

    # ========== REGISTRATION FORM ==========
    if menu == "Register":
        st.subheader("📝 Registration")

        # Collect user registration details
        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")  # Hide password input

        # Handle registration button click
        if st.button("Register"):
            # Check if email already exists in the users database
            if email in st.session_state.users:
                st.error("Email already exists!")
            else:
                # Store new user: email -> [name, password]
                st.session_state.users[email] = [name, password]
                st.success("Registration successful! Please login.")

    # ========== LOGIN FORM ==========
    else:
        st.subheader("🔐 Login")

        # Collect login credentials
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        # Handle login button click
        if st.button("Login"):
            # Verify email exists and password matches
            if email in st.session_state.users and st.session_state.users[email][1] == password:
                # Set logged_in flag to True
                st.session_state.logged_in = True
                st.success("Login successful!")
                # Rerun the app to show the main interface
                st.rerun()
            else:
                st.error("Invalid email or password")

# ============================
# MAIN APPLICATION (After Login)
# ============================
# This section is displayed only when user is logged in
else:
    # Create a two-column layout: main content (2/3) and stats sidebar (1/3)
    col1, col2 = st.columns([2, 1])
    
    # ========== RIGHT COLUMN: Quick Stats ==========
    # Display app statistics in the right sidebar
    with col2:
        st.markdown("### 📊 Quick Stats")
        st.metric("Total Tasks", "21")          # Number of available NLP tasks
        st.metric("AI Model", "Gemini 2.5")    # AI model being used
        st.metric("Status", "🟢 Online")       # App status indicator
    
    # ========== LEFT COLUMN: Main Interaction Area ==========
    with col1:
        st.markdown("### 🚀 Welcome to AI NLP Toolkit")

        # ========== TASK SELECTION DROPDOWN ==========
        # User selects one of 21 available NLP tasks
        # Each task has an emoji icon for better UX
        task = st.selectbox(
            "🎯 Select NLP Task",
            [
                "💭 Sentiment Analysis",
                "🌐 Language Translation (English → Bangla)",
                "🔍 Language Detection",
                "📝 Text Summarization",
                "🔑 Keyword Extraction",
                "👤 Named Entity Recognition",
                "📚 Part-of-Speech Tagging",
                "🏷️ Topic Modeling",
                "📊 Text Classification",
                "❓ Question Answering",
                "✍️ Text Generation",
                "😊 Emotion Detection",
                "🎯 Intent Detection",
                "🔄 Paraphrase Detection",
                "✏️ Text Paraphrasing",
                "✅ Grammar Correction",
                "⚠️ Hate Speech Detection",
                "🚫 Spam Detection",
                "📰 Fake News Detection",
                "📖 Text Simplification",
                "💡 Opinion Mining"
            ]
        )

        # ========== TEXT INPUT AREA ==========
        # Paraphrase Detection needs two separate inputs, handled differently
        if task == "🔄 Paraphrase Detection":
            user_text = None  # Will use separate inputs later
        else:
            # Standard single text area for most tasks
            user_text = st.text_area("📄 Enter your text", height=150, placeholder="Type or paste your text here...")

        # ========== RUN ANALYSIS BUTTON ==========
        # When clicked, generates appropriate prompt and calls Gemini API
        if st.button("🚀 Run Analysis", use_container_width=True):
            # Show loading spinner while processing
            with st.spinner("🔄 Processing..."):

                # ========== PROMPT ENGINEERING ==========
                # Each task has a specific prompt template optimized for Gemini
                # The prompts are designed to get structured, useful responses

                if task == "💭 Sentiment Analysis":
                    prompt = f"Analyze the sentiment of this text and classify it as Positive, Negative, or Neutral with confidence score: {user_text}"

                elif task == "🌐 Language Translation (English → Bangla)":
                    prompt = f"Translate this English text to Bangla (Bengali): {user_text}"

                elif task == "🔍 Language Detection":
                    prompt = f"Detect the language of this text and provide the language name: {user_text}"

                elif task == "📝 Text Summarization":
                    prompt = f"Provide a concise summary of this text: {user_text}"

                elif task == "🔑 Keyword Extraction":
                    prompt = f"Extract the most important keywords and key phrases from this text: {user_text}"

                elif task == "👤 Named Entity Recognition":
                    prompt = f"Identify and categorize named entities (Person, Organization, Location, Date, etc.) in this text: {user_text}"

                elif task == "📚 Part-of-Speech Tagging":
                    prompt = f"Tag each word in this sentence with its part of speech (noun, verb, adjective, etc.): {user_text}"

                elif task == "🏷️ Topic Modeling":
                    prompt = f"Identify the main topic and sub-topics of this text: {user_text}"

                elif task == "📊 Text Classification":
                    prompt = f"Classify this text into appropriate categories (e.g., Technology, Sports, Politics, Entertainment, Business, Health, Science): {user_text}"

                elif task == "❓ Question Answering":
                    prompt = f"Provide a detailed and accurate answer to this question: {user_text}"

                elif task == "✍️ Text Generation":
                    prompt = f"Generate creative and engaging text based on this prompt: {user_text}"

                elif task == "😊 Emotion Detection":
                    prompt = f"Detect and identify the specific emotions (joy, sadness, anger, fear, surprise, disgust, etc.) expressed in this text: {user_text}"

                elif task == "🎯 Intent Detection":
                    prompt = f"Detect the user's intent in this text (e.g., question, request, complaint, feedback, greeting, booking): {user_text}"

                elif task == "🔄 Paraphrase Detection":
                    text1 = st.text_input("📄 First sentence")
                    text2 = st.text_input("📄 Second sentence")
                    prompt = f"Analyze if these two sentences are paraphrases (convey the same meaning):\n1. {text1}\n2. {text2}\nProvide a Yes/No answer with explanation."

                elif task == "✏️ Text Paraphrasing":
                    prompt = f"Paraphrase this text while maintaining its original meaning: {user_text}"

                elif task == "✅ Grammar Correction":
                    prompt = f"Correct all grammar, spelling, and punctuation errors in this text and explain the corrections: {user_text}"

                elif task == "⚠️ Hate Speech Detection":
                    prompt = f"Analyze if this text contains hate speech, offensive language, or harmful content. Classify as: Safe, Warning, or Harmful: {user_text}"

                elif task == "🚫 Spam Detection":
                    prompt = f"Analyze if this text is spam/promotional content or legitimate. Classify as Spam or Not Spam with confidence score: {user_text}"

                elif task == "📰 Fake News Detection":
                    prompt = f"Analyze this text for potential misinformation, fake news, or unreliable claims. Provide credibility assessment: {user_text}"

                elif task == "📖 Text Simplification":
                    prompt = f"Simplify this text to make it easier to understand for a general audience: {user_text}"

                elif task == "💡 Opinion Mining":
                    prompt = f"Extract and analyze opinions, attitudes, and subjective information from this text: {user_text}"

                response = model.generate_content(prompt)
                
                st.markdown("---")
                st.markdown("### ✅ Analysis Result")
                st.markdown(f'<div class="task-card">{response.text}</div>', unsafe_allow_html=True)

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()