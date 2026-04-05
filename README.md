# 💡 Instant Idea Rating System (Firebase + AI Analysis)

A real-time, CLI-based idea rating system built with **Python**, **Firebase Realtime Database**, and **Hugging Face Transformers**. This tool lets you store ideas, get instant AI-powered sentiment analysis, and rate ideas collectively.

---

## 🚀 Features
- **Add Idea**: Submit your innovative ideas with a title and description.
- **AI Analysis**: Automatically analyzes the sentiment (Positive/Negative) of your idea using pretrained Hugging Face models.
- **Idea Summary**: Generates a short summary of your idea using AI.
- **Real-Time Data**: Persists ideas and ratings in Firebase Realtime Database.
- **Dynamic Rating**: Users can rate ideas (1 to 5), and the average rating is recalculated and updated instantly.

---

## 🛠️ Step-by-Step Firebase Setup

### 1. Create a Firebase Project
- Go to [Firebase Console](https://console.firebase.google.com/).
- Click **Add project** and name it (e.g., `InstantIdeaRatingSystem`).
- Disable Google Analytics (optional) and click **Create project**.

### 2. Set Up Realtime Database
- In the left sidebar, click **Build** > **Realtime Database**.
- Click **Create Database**. Choose a location.
- Start in **Test Mode** (This allows you to test the app without setting complex security rules immediately).
- **Copy your Database URL**: It looks like `https://your-project-id.firebaseio.com/`.

### 3. Get Service Account Key
- Go to **Project Settings** (gear icon) > **Service accounts**.
- Ensure **Python** is selected and click **Generate new private key**.
- Download the `.json` file and **Rename it to `serviceAccountKey.json`**.
- Place this file inside your `InstantIdeaRatingSystem` project folder.

---

## 🏃 How to Run

### 1. Install Dependencies
Run the following command in your terminal/command prompt:
```bash
pip install -r requirements.txt
```

### 2. Start the Application
```bash
python main.py
```

> [!IMPORTANT]
> **First Run Note**: On your first run, the application will download about **700MB** of AI models from Hugging Face. This may take **2-5 minutes** depending on your internet speed. Please do not interrupt the process!

### 3. Provide Database URL
When prompted, paste your **Firebase Realtime Database URL**. This will be saved in `db_url.txt` so you only have to do it once.

---

## 🤖 AI Integration Details
- **Sentiment Analysis**: Uses `distilbert-base-uncased-finetuned-sst-2-english` to categorize the tone of your idea.
- **Summarization**: Uses `sshleifer/distilbart-cnn-12-6` to generate a one-sentence summary of long descriptions.

---

## 📁 Project Structure
- `main.py`: Main CLI menu, logic, and database operations.
- `ai_model.py`: Hugging Face pipelines for sentiment and summarization.
- `firebase_config.py`: Firebase Admin SDK initialization and persistence.
- `utils.py`: Text formatting and validation helpers.
- `requirements.txt`: Necessary Python libraries.

---

## 📝 Sample Output
```text
========================================
           INSTANT IDEA RATING          
========================================
1. Add New Idea
2. View Ideas & AI Analysis
3. Rate an Idea
4. Exit

Choose an option (1-4): 2

ID: 27c64d57
Title: FinGenius
Description: AI Powered Finance & Investment Tracker
Average Rating: 4.50
AI Sentiment: POSITIVE (Confidence: 0.99)
AI Summary: AI Powered Finance & Investment Tracker
----------------------------------------
```

---

## 📜 License
This project is for educational purposes. Feel free to use and modify it!
