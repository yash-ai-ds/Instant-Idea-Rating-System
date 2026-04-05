from transformers import pipeline
import logging

# Disable transformers logs for cleaner output
logging.getLogger("transformers").setLevel(logging.ERROR)

def analyze_idea(description):
    """
    Analyzes the sentiment of an idea description using Hugging Face.
    """
    try:
        # Load sentiment analysis pipeline (distilbert is fast and lightweight)
        print("[INFO] Loading AI Sentiment Model (on first run, this may download ~200MB)...")
        sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", device=-1)
        result = sentiment_analyzer(description)[0]
        return {
            "sentiment": result["label"],
            "score": round(result["score"], 4)
        }
    except Exception as e:
        print(f"AI Analysis Error: {e}")
        return {"sentiment": "Unknown", "score": 0.0}

def summarize_idea(description):
    """
    Optional bonus: Summarizes the idea description using a Hugging Face model.
    Short ideas (~50 words) are best for basic models.
    """
    try:
        # Load summarization pipeline (sshleifer/distilbart-cnn-12-6 is common but can be large, 
        # t5-small is faster for quick CLI tasks)
        print("[INFO] Loading AI Summarization Model (on first run, this may download ~500MB)...")
        summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device=-1)
        
        # Adjust lengths for short CLI inputs
        summary = summarizer(description, max_length=30, min_length=5, do_sample=False)[0]['summary_text']
        return summary
    except Exception as e:
        # If it fails (e.g., input too short), return original
        return description
