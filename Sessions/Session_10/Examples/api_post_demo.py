import requests

def create_todo():
    """
    Demonstrates a POST request to create a new resource.
    """
    print("--- Creating a New To-Do (POST) ---")
    url = "https://jsonplaceholder.typicode.com/todos"
    
    # Data to be sent in the request body
    new_todo = {
        "title": "Learn APIs with Python",
        "completed": False,
        "userId": 1
    }
    
    try:
        # Use the 'json' parameter to automatically set headers and encode data
        response = requests.post(url, json=new_todo, timeout=5)
        
        print(f"Status Code: {response.status_code} (201 means Created)")
        
        if response.status_code == 201:
            created_item = response.json()
            print("Successfully created item:")
            print(created_item)
            
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_todo()
