import requests

def demo_github_api():
    """
    Demonstrates a simple GET request to the GitHub API.
    """
    print("--- GitHub API Demo ---")
    url = "https://api.github.com/users/octocat"
    
    try:
        # Sending the request
        response = requests.get(url, timeout=5)
        
        # Exploring the response object
        print(f"Status Code: {response.status_code}")
        print(f"Content Type: {response.headers.get('Content-Type')}")
        
        if response.status_code == 200:
            # Parsing JSON data
            data = response.json()
            print(f"Name: {data.get('name')}")
            print(f"Company: {data.get('company')}")
            print(f"Public Repos: {data.get('public_repos')}")
        elif response.status_code == 404:
            print("User not found!")
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    demo_github_api()
