import requests

def search_repositories(language="python", sort="stars"):
    """
    Demonstrates using query parameters to filter API results.
    """
    print(f"--- Searching for {language} repos sorted by {sort} ---")
    url = "https://api.github.com/search/repositories"
    
    # Defining query parameters as a dictionary
    query_params = {
        "q": f"language:{language}",
        "sort": sort,
        "order": "desc"
    }
    
    try:
        response = requests.get(url, params=query_params, timeout=10)
        
        # Print the final URL to show how parameters were encoded
        print(f"Final URL: {response.url}")
        
        if response.status_code == 200:
            data = response.json()
            items = data.get("items", [])[:5]  # Get top 5
            
            for repo in items:
                print(f"- {repo['full_name']} ({repo['stargazers_count']} stars)")
        else:
            print(f"Search failed with status: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    search_repositories()
