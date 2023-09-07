import Levenshtein
from fuzzywuzzy import fuzz

# Predefined list of keywords with associated links
keyword_links = {
    "Python": "https://example.com/python_article",
    "programming": "https://example.com/programming_article",
    "data": "https://example.com/data_article",
    "tutorial": "https://example.com/tutorial_article",
    "code": "https://example.com/code_article",
    "examples": "https://example.com/examples_article",
    "escalate": "KB0015747 | An article used to see which teams are required to escalate specific issues to for GCC."
}

# Function to find the closest matching keyword
def find_closest_keyword(query, keywords):
    best_match = max(keywords, key=lambda keyword: fuzz.ratio(query, keyword))
    return best_match

# Function to search for articles based on keywords
def search_articles(query, keyword_links):
    # Find the closest matching keyword
    closest_keyword = find_closest_keyword(query, keyword_links.keys())
    
    matching_articles = []
    
    # Check if the closest keyword is a good match (you can adjust the threshold)
    if fuzz.ratio(query, closest_keyword) >= 50:
        matching_articles.append(f"Okay! Here's what I found for: '{closest_keyword}':\n{keyword_links[closest_keyword]}")
    
    return matching_articles

# Function to ask if the user wants to search again
def search_again():
    response = input(f"\nDo you want to search for another knowledge article? (yes/no) ").lower()
    return response == "yes"
    clear()

# Loop to allow multiple searches
while True:
    # Ask the user for a knowledge article search query
    user_query = input("What Knowledge Article would you like to search for? ")

    # Confirm with the user
    confirmation = input(f'You want to search for "{user_query}". Is this correct? (yes/no) ').lower()

    if confirmation == "yes":
        # Search for articles based on the user's query and keywords
        articles = search_articles(user_query, keyword_links)

        if articles:
            print("Matching Articles:")
            for article in articles:
                print(article)
        else:
            print("No matching articles found.")
    else:
        print("Search canceled.")

    # Ask the user if they want to search again
    if not search_again():
        break