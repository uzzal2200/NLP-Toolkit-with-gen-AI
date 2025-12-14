"""
AI NLP Toolkit - Command Line Interface (CLI) Application
==========================================================
Author: Your Name
Date: December 2025
Description: Terminal-based NLP toolkit powered by Google Gemini AI.
            Provides 21+ NLP tasks with user registration/login system.

Features:
- Terminal-based user authentication
- 21 different NLP tasks accessible via numbered menu
- Simple and fast - no web browser required
- Session-based user management (in-memory database)

Usage:
    python app.py

Note: This is a CLI alternative to UI_streamlit.py
      User data is stored in memory and lost when app exits.
"""

import google.generativeai as genai
from dotenv import load_dotenv 
import os

# Load environment variables from .env file
# This file should contain: GOOGLE_API_KEY or GEMINI_API_KEY
load_dotenv()

# ============================
# BASE MODEL CLASS
# ============================

class BaseModel:
    """
    Base class that handles Gemini AI model initialization.
    
    This class is inherited by AppFeatures to provide AI capabilities.
    Separating this allows for easy model switching or configuration changes.
    """
    
    def getmodel(self):
        """
        Initialize and return the Gemini AI model.
        
        Returns:
            GenerativeModel: Configured Gemini model instance
            
        Raises:
            Exception: If API key is invalid or model initialization fails
        """
        try:
            # Configure Gemini with API key from environment
            genai.configure(api_key = os.getenv("GEMINI_API_KEY"))
            # Initialize Gemini 2.5 Flash model (fast and cost-effective)
            model = genai.GenerativeModel("gemini-2.5-flash")
            return model
        except Exception as e:
            print(f"Error initializing model: {e}")
            return None
            

# ============================
# APP FEATURES CLASS
# ============================

class AppFeatures(BaseModel):
    """
    Main application class that handles user interaction and NLP tasks.
    
    Inherits from BaseModel to access Gemini AI capabilities.
    Manages user authentication and provides menu-driven access to 21 NLP tasks.
    
    Attributes:
        __database (dict): In-memory user database {email: [name, password]}
    """
    
    def __init__(self):
        """
        Initialize the application.
        
        Creates empty user database and shows the first menu (login/register).
        """
        self.__database = {}  # Private: stores registered users
        self.first_menu()     # Start the application flow
    
    def first_menu(self):
        """
        Display the initial menu for user authentication.
        
        Allows users to:
        1. Register a new account
        2. Login to existing account
        3. Exit the application
        """
        first_input = input(
            """
            Hi! how would you like to proceed
               
               1. press 1 for Registration 
               2. Press 2 for login
               3. press 3 for exit
               
            """
        )
        
        # Handle user choice
        if first_input =="1":
            # Navigate to registration
            self.__register()
            
        elif first_input =="2":
            # Navigate to login
            self.__login()
        else:
            # Exit the application
            exit()
        
        
    def second_menu(self):
        """
        Display the main NLP tasks menu (shown after login).
        
        Presents 21 different NLP tasks and routes to appropriate handler.
        Each task calls Gemini AI with a specific prompt template.
        """
        second_input = input(
        """
        ========================================
        🤖 AI NLP Toolkit - Select Task
        ========================================
        1.  💭 Sentiment Analysis
        2.  🌐 Language Translation (Bangla)
        3.  🔍 Language Detection
        4.  📝 Text Summarization
        5.  🔑 Keyword Extraction
        6.  👤 Named Entity Recognition
        7.  📚 Part-of-Speech Tagging
        8.  🏷️ Topic Modeling
        9.  📊 Text Classification
        10. ❓ Question Answering
        11. ✍️ Text Generation
        12. 😊 Emotion Detection
        13. 🎯 Intent Detection
        14. 🔄 Paraphrase Detection
        15. ✏️ Text Paraphrasing
        16. ✅ Grammar Correction
        17. ⚠️ Hate Speech Detection
        18. 🚫 Spam Detection
        19. 📰 Fake News Detection
        20. 📖 Text Simplification
        21. 💡 Opinion Mining
        0.  🚪 Exit
        ========================================
        Enter your choice: 
        """
    )
        if second_input == "1":
            self.__sentiment_analysis()
        elif second_input == "2":
            self.__language_translation()
        elif second_input == "3":
            self.__language_detection()
        elif second_input == "4":
            self.__text_summarization()
        elif second_input == "5":
            self.__keyword_extraction()
        elif second_input == "6":
            self.__named_entity_recognition()
        elif second_input == "7":
            self.__part_of_speech_tagging()
        elif second_input == "8":
            self.__topic_modeling()
        elif second_input == "9":
            self.__text_classification()
        elif second_input == "10":
            self.__question_answering()
        elif second_input == "11":
            self.__text_generation()
        elif second_input == "12":
            self.__emotion_detection()
        elif second_input == "13":
            self.__intent_detection()
        elif second_input == "14":
            self.__paraphrase_detection()
        elif second_input == "15":
            self.__text_paraphrasing()
        elif second_input == "16":
            self.__grammar_correction()
        elif second_input == "17":
            self.__hate_speech_detection()
        elif second_input == "18":
            self.__spam_detection()
        elif second_input == "19":
            self.__fake_news_detection()
        elif second_input == "20":
            self.__text_simplification()
        elif second_input == "21":
            self.__opinion_mining()
        elif second_input == "0":
            print("Thank you for using AI NLP Toolkit! Goodbye! 👋")
            exit()
        else:
            print("❌ Invalid choice! Please try again.")
            self.second_menu()
    
    
    def __register(self):
        """
        Handle user registration process.
        
        Collects name, email, and password.
        Checks for duplicate emails before creating account.
        Stores user in in-memory database.
        
        Flow: Register → Return to first_menu → Login
        """
        # Collect registration details from terminal input
        name = input("Enter your Name: ")
        email = input("Enter your Email: ")
        password = input("Enter your Password: ")
        
        # Check if email already exists
        if email in self.__database:
            print("Email already exists ")
        else:
            # Store new user: email -> [name, password]
            self.__database[email] = [name, password]
            
            print("Registration successful. Now you can login!")
        # Return to first menu for login
        self.first_menu()
        
        
    def __login(self):
        """
        Handle user login process.
        
        Verifies email and password against database.
        On success: Navigate to second_menu (NLP tasks)
        On failure: Retry login or redirect to registration
        """
        # Collect login credentials
        email = input("Enter your Email: ")
        password = input("Enter you Password")
        
        # Verify credentials
        if email in self.__database:
            # Email exists, check password
            if self.__database[email][1] == password:
                print("Login Sucessfull!")
                
                # Navigate to main app (NLP tasks menu)
                self.second_menu()
            else:
                # Wrong password, retry login
                print("Your password is incorrect! please try again")
                self.__login()
                
        else:
            # Email not found, redirect to registration
            print("Email not found! Please register firest")
            self.first_menu()
    
    # ============================
    # NLP TASK METHODS
    # ============================
    # Each method below handles a specific NLP task:
    # 1. Get user input
    # 2. Initialize Gemini model
    # 3. Generate prompt and call AI
    # 4. Display result
    # 5. Return to second_menu
    
    def __sentiment_analysis(self):
        """
        Analyze sentiment of text (Positive/Negative/Neutral).
        
        Example input: "This movie is amazing!"
        Expected output: Positive sentiment with confidence score
        """
        user_text = input("Enter your text: ")
        
        model = self.getmodel()
        # Send prompt to Gemini AI
        response = model.generate_content(f"Give me the sentiment fo this sentence: {user_text}")
        results = response.text
        print(results)
        # Return to task menu
        self.second_menu()
    
    def __language_translation(self):
        """
        Translate English text to Bangla (Bengali).
        
        Example: "I love programming" → "আমি প্রোগ্রামিং ভালোবাসি"
        """
        user_text = input("Enter your text: ")
        model = self.getmodel()
        response = model.generate_content(f"Give me Bangla transilation of this sentence: {user_text}")
        results = response.text
        print(results)
        self.second_menu()
    
    def __language_detection(self):
        """
        Detect the language of input text.
        
        Supports multiple languages: English, Bangla, Hindi, French, etc.
        """
        user_text = input("Enter your text: ")
        model = self.getmodel()
        response = model.generate_content(f"Detect the language of this sentence: {user_text}")
        results = response.text
        print(results)
        self.second_menu()

    def __text_summarization(self):
        user_text = input("Enter your text: ")
        model = self.getmodel()
        response = model.generate_content(f"Summarize of this sentence: {user_text}")
        results = response.text
        print(results)
        self.second_menu()

    def __keyword_extraction(self):
        user_text = input("Enter your text: ")
        model = self.getmodel()
        response = model.generate_content(f"Extract the important keywords from this sentence: {user_text}")
        results = response.text
        print(results)
        self.second_menu()

    def __named_entity_recognition(self):
        user_text = input("Enter your text: ")
        model = self.getmodel()
        response = model.generate_content(f"Identify named entities (like person, place, organization) in this sentence: {user_text}")
        results = response.text
        print(results)
        self.second_menu()

    def __part_of_speech_tagging(self):
        user_text = input("Enter your text: ")
        model = self.getmodel()
        response = model.generate_content(f"Tag each word in this sentence with its part of speech: {user_text}")
        results = response.text
        print(results)
        self.second_menu()

    def __topic_modeling(self):
        user_text = input("Enter your text: ")
        model = self.getmodel()
        response = model.generate_content(f"Identify the main topic of this sentence: {user_text}")
        results = response.text
        print(results)
        self.second_menu()

    def __text_classification(self):
        user_text = input("Enter your text: ")
        model = self.getmodel()
        response = model.generate_content(f"Classify this sentence into a category (e.g. sports, politics, technology): {user_text}")
        results = response.text
        print(results)
        self.second_menu()

    def __question_answering(self):
        user_text = input("Enter your question: ")
        model = self.getmodel()
        response = model.generate_content(f"Answer the question based on the user question: {user_text}")
        results = response.text
        print(results)
        self.second_menu()

    def __text_generation(self):
        user_text = input("Enter a prompt: ")
        model = self.getmodel()
        response = model.generate_content(f"Generate a short text based on this prompt: {user_text}")
        results = response.text
        print(results)
        self.second_menu()

    def __emotion_detection(self):
        user_text = input("Enter your text: ")
        model = self.getmodel()
        response = model.generate_content(f"Detect the emotion expressed in this sentence (happy, sad, angry, etc.): {user_text}")
        results = response.text
        print(results)
        self.second_menu()

    def __intent_detection(self):
        user_text = input("Enter your text: ")
        model = self.getmodel()
        response = model.generate_content(f"Detect the intent of this sentence (e.g. booking, inquiry, complaint): {user_text}")
        results = response.text
        print(results)
        self.second_menu()

    def __paraphrase_detection(self):
        text1 = input("Enter first sentence: ")
        text2 = input("Enter second sentence: ")
        model = self.getmodel()
        response = model.generate_content(f"Check if these two sentences mean the same thing:\n1. {text1}\n2. {text2}")
        results = response.text
        print(results)
        self.second_menu()

    def __text_paraphrasing(self):
        user_text = input("Enter text to paraphrase (e.g., 'The weather is very hot today'): ")
        model = self.getmodel()
        response = model.generate_content(f"Paraphrase this text while maintaining its original meaning: {user_text}")
        results = response.text
        print(f"\n\u2705 Paraphrased Text:\n{results}\n")
        self.second_menu()

    def __grammar_correction(self):
        user_text = input("Enter text with grammar errors (e.g., 'She don't like going to school everyday'): ")
        model = self.getmodel()
        response = model.generate_content(f"Correct all grammar, spelling, and punctuation errors in this text and explain the corrections: {user_text}")
        results = response.text
        print(f"\n\u2705 Corrected Text:\n{results}\n")
        self.second_menu()

    def __hate_speech_detection(self):
        user_text = input("Enter text to analyze (e.g., 'You should try harder next time'): ")
        model = self.getmodel()
        response = model.generate_content(f"Analyze if this text contains hate speech, offensive language, or harmful content. Classify as: Safe, Warning, or Harmful: {user_text}")
        results = response.text
        print(f"\n\u26a0\ufe0f Analysis Result:\n{results}\n")
        self.second_menu()

    def __spam_detection(self):
        user_text = input("Enter text to check (e.g., 'Congratulations! You won $1000. Click here now!'): ")
        model = self.getmodel()
        response = model.generate_content(f"Analyze if this text is spam/promotional content or legitimate. Classify as Spam or Not Spam with confidence score: {user_text}")
        results = response.text
        print(f"\n\ud83d\udeab Analysis Result:\n{results}\n")
        self.second_menu()

    def __fake_news_detection(self):
        user_text = input("Enter news text to verify (e.g., 'Scientists discover cure for all diseases'): ")
        model = self.getmodel()
        response = model.generate_content(f"Analyze this text for potential misinformation, fake news, or unreliable claims. Provide credibility assessment: {user_text}")
        results = response.text
        print(f"\n\ud83d\udcf0 Credibility Assessment:\n{results}\n")
        self.second_menu()

    def __text_simplification(self):
        user_text = input("Enter complex text to simplify (e.g., 'The implementation of advanced algorithms...'): ")
        model = self.getmodel()
        response = model.generate_content(f"Simplify this text to make it easier to understand for a general audience: {user_text}")
        results = response.text
        print(f"\n\ud83d\udcd6 Simplified Text:\n{results}\n")
        self.second_menu()

    def __opinion_mining(self):
        user_text = input("Enter text for opinion analysis (e.g., 'I think this product is great but expensive'): ")
        model = self.getmodel()
        response = model.generate_content(f"Extract and analyze opinions, attitudes, and subjective information from this text: {user_text}")
        results = response.text
        print(f"\n\ud83d\udca1 Opinion Analysis:\n{results}\n")
        self.second_menu()
# ============================
# APPLICATION ENTRY POINT
# ============================
# Create an instance of AppFeatures to start the application
# This triggers __init__() which shows the first menuapp = AppFeatures() 
                

        