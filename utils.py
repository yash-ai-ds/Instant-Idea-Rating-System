from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def print_header(title):
    banner = f"{Fore.CYAN}{'='*40}\n{title.center(40)}\n{'='*40}"
    print(banner)

def print_success(message):
    print(f"{Fore.GREEN}[SUCCESS] {message}")

def print_error(message):
    print(f"{Fore.RED}[ERROR] {message}")

def print_info(message):
    print(f"{Fore.WHITE}[INFO] {Style.DIM}{message}")

def print_idea(idea_id, idea):
    """
    Formatted display for a single idea.
    """
    print(f"\n{Fore.YELLOW}ID: {idea_id}")
    print(f"{Fore.MAGENTA}Title: {Style.BRIGHT}{idea.get('title', 'N/A')}")
    print(f"{Fore.WHITE}Description: {idea.get('description', 'N/A') or 'N/A'}")
    print(f"{Fore.CYAN}Average Rating: {Style.BRIGHT}{idea.get('average_rating', 0.0):.2f}")
    
    # AI analysis if present
    analysis = idea.get("ai_analysis")
    if analysis:
        sentiment = analysis["sentiment"]
        score = analysis["score"]
        color = Fore.GREEN if sentiment == "POSITIVE" else Fore.RED
        print(f"AI Sentiment: {color}{sentiment} {Fore.WHITE}(Confidence: {score})")
        
    summary = idea.get("summary")
    if summary:
        print(f"{Fore.YELLOW}AI Summary: {Style.DIM}{summary}")
    print("-" * 40)

def get_input(prompt, required=True):
    while True:
        value = input(f"{Fore.CYAN}{prompt}: ").strip()
        if required and not value:
            print_error("This field is required!")
            continue
        return value

def get_rating():
    while True:
        try:
            rating = int(input(f"{Fore.YELLOW}Rate this idea (1-5): "))
            if 1 <= rating <= 5:
                return rating
            else:
                print_error("Rating must be between 1 and 5.")
        except ValueError:
            print_error("Please enter a valid number.")
