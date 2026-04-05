from firebase_admin import db
from firebase_config import initialize_firebase
from ai_model import analyze_idea, summarize_idea
from utils import (
    print_header, print_success, print_error, print_info, 
    print_idea, get_input, get_rating, Fore, Style
)
import sys
import uuid

def add_idea():
    """
    Inputs a new idea, generates AI analysis, and saves to Firebase.
    """
    print_header("ADD NEW IDEA")
    title = get_input("Idea Title")
    description = get_input("Description", required=True)
    
    print_info("Analyzing idea description with AI...")
    analysis = analyze_idea(description)
    summary = summarize_idea(description)
    
    # Generate unique idea ID
    idea_id = str(uuid.uuid4())[:8]
    
    new_idea_data = {
        "idea_id": idea_id,
        "title": title,
        "description": description,
        "ratings": [],
        "average_rating": 0.0,
        "ai_analysis": analysis,
        "summary": summary
    }
    
    try:
        # Ref for ideas in Realtime DB
        ref = db.reference('ideas')
        # We'll use idea_id as key for easy lookup
        ref.child(idea_id).set(new_idea_data)
        print_success(f"Idea '{title}' added successfully!")
        print_info(f"AI Tone: {analysis['sentiment']} (Confidence: {analysis['score']:.2f})")
    except Exception as e:
        print_error(f"Failed to add idea: {e}")

def view_ideas():
    """
    Fetches and displays all ideas from Firebase in real-time.
    """
    print_header("VIEW ALL IDEAS")
    try:
        ref = db.reference('ideas')
        ideas = ref.get()
        
        if not ideas:
            print_info("No ideas found yet. Be the first to add one!")
            return
            
        for idea_id, idea_content in ideas.items():
            print_idea(idea_id, idea_content)
    except Exception as e:
        print_error(f"Error fetching ideas: {e}")

def rate_idea():
    """
    Allows user to rate an existing idea.
    Calculates and updates average_rating in real-time.
    """
    print_header("RATE AN IDEA")
    idea_id = get_input("Enter Idea ID to rate")
    
    try:
        ref = db.reference(f'ideas/{idea_id}')
        idea = ref.get()
        
        if not idea:
            print_error(f"No idea found with ID: {idea_id}")
            return
            
        print_idea(idea_id, idea)
        rating = get_rating()
        
        # In Firebase, we can't easily append to lists with `.set()`
        # We retrieve current ratings, add new, and re-avg
        current_ratings = idea.get('ratings', [])
        if isinstance(current_ratings, dict):
            # If Firebase stored it as a dict (it happens with auto-keys)
            current_ratings = list(current_ratings.values())
        
        current_ratings.append(rating)
        new_avg = sum(current_ratings) / len(current_ratings)
        
        # Update Firebase
        ref.update({
            'ratings': current_ratings,
            'average_rating': round(new_avg, 2)
        })
        print_success("Rating recorded! Average updated dynamically.")
    except Exception as e:
        print_error(f"Error rating idea: {e}")

def main_menu():
    """
    Main loop for CLI menu.
    """
    # Initialize Firebase at start
    if not initialize_firebase():
        print_error("Exiting due to Firebase initialization error.")
        sys.exit(1)
        
    while True:
        print_header("INSTANT IDEA RATING")
        print(f"1. {Fore.GREEN}Add New Idea")
        print(f"2. {Fore.CYAN}View Ideas & AI Analysis")
        print(f"3. {Fore.YELLOW}Rate an Idea")
        print(f"4. {Fore.RED}Exit")
        
        choice = input(f"\n{Fore.WHITE}Choose an option (1-4): ")
        
        if choice == '1':
            add_idea()
        elif choice == '2':
            view_ideas()
        elif choice == '3':
            rate_idea()
        elif choice == '4':
            print_info("Goodbye! Keep innovating.")
            break
        else:
            print_error("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
