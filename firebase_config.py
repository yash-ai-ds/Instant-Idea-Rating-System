import firebase_admin
from firebase_admin import credentials, db
import os

def initialize_firebase():
    """
    Initializes Firebase Admin SDK using serviceAccountKey.json.
    """
    # Look for serviceAccountKey.json in the current directory
    cred_path = os.path.join(os.path.dirname(__file__), 'serviceAccountKey.json')
    
    if not os.path.exists(cred_path):
        print("\n[ERROR] 'serviceAccountKey.json' not found!")
        print("Please follow the instructions in README.md to download your Firebase key.")
        return False

    try:
        # Re-initialize only if no apps are registered
        if not firebase_admin._apps:
            cred = credentials.Certificate(cred_path)
            # DATABASE_URL should be your FIREBASE RTDB URL
            # Note: The user should provide this URL via environment variable or prompt
            # For simplicity, we'll try to get it from a potential config file or prompt later
            # In a real app, use a secret manager or .env
            
            # Example database URL (user must change this):
            # https://your-project-id.firebaseio.com/
            
            # Use absolute path for the config file
            url_config_path = os.path.join(os.path.dirname(__file__), 'db_url.txt')
            
            # Let's check for a config file for the URL
            database_url = "REPLACE_WITH_YOUR_FIREBASE_DATABASE_URL" # Placeholder
            
            # If the user hasn't replaced it, it won't work, so it's a prompt
            if "REPLACE" in database_url:
                if os.path.exists(url_config_path):
                    with open(url_config_path, 'r') as f:
                        database_url = f.read().strip()
                else:
                    database_url = None
                    
            if not database_url:
                database_url = input("\nEnter your Firebase Realtime Database URL: ").strip()
                with open(url_config_path, 'w') as f:
                    f.write(database_url)

            firebase_admin.initialize_app(cred, {
                'databaseURL': database_url
            })
        return True
    except Exception as e:
        print(f"\n[ERROR] Firebase Initialization Failed: {e}")
        return False
