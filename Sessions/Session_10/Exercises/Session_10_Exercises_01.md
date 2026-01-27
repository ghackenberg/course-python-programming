# Exercises 10: Web APIs, Testing & Documentation

Welcome to the exercises for Session 10! This final sheet covers professional software development practices, including interacting with web services, automated testing, and documenting your code.

## 10.1: Introduction to Web APIs (REST)

1.  **The Waiter Analogy:** In the context of the "Waiter Analogy" for APIs, identify who represents the *Client*, the *Server*, and the *API* itself.
2.  **HTTP Verbs:** Match the following actions to their corresponding HTTP methods:
    -   Create a new user: \_\_\_\_\_\_
    -   Retrieve a list of products: \_\_\_\_\_\_
    -   Delete an old log entry: \_\_\_\_\_\_
    -   Update a user's email address: \_\_\_\_\_\_
3.  **Status Codes:** What do the following status code ranges generally indicate?
    -   `2xx`: \_\_\_\_\_\_
    -   `4xx`: \_\_\_\_\_\_
    -   `5xx`: \_\_\_\_\_\_
4.  **URL Anatomy:** Breakdown the following URL into *Domain*, *Path*, and *Query Parameters*:
    `https://api.weather.com/v3/forecast?city=Wels&units=metric`

## 10.2: Consuming APIs with the requests Library

1.  **Basic GET:** Write a Python snippet that uses the `requests` library to fetch data from `https://api.github.com/events` and prints the status code.
2.  **JSON Parsing:** If an API returns a JSON response representing a dictionary, how do you convert it into a Python dictionary?
3.  **Query Params:** Show how to send the parameters `{'page': 2, 'limit': 50}` in a GET request without manually typing them into the URL string.
4.  **Error Handling:** What is the purpose of `response.raise_for_status()`? Wrap a request in a `try...except` block to catch potential network errors.
5.  **POST Request:** Write the code to send a dictionary `{"status": "active"}` as a JSON body to `https://httpbin.org/post` using a POST request.

## 10.3: Automated Testing with pytest

1.  **The "Why":** Give two reasons why automated testing is more cost-effective than manual testing in the long run.
2.  **Test Structure:**
    -   What prefix must your test files and test functions have for `pytest` to find them?
    -   Which keyword is used to verify that a result matches expectations?
3.  **Writing a Test:** Write a test function `test_calculate_bmi` that verifies a `calculate_bmi(weight, height)` function returns `25.0` for `weight=80` and `height=1.78` (approximate is fine, or use `pytest.approx`).
4.  **Edge Cases:** List three edge cases you should test for a function that calculates the average of a list of numbers.

## 10.4: Documentation and Professional Best Practices

1.  **Docstrings:** What is a Docstring, and where is it placed in a Python function?
2.  **Type Hinting:** Rewrite the following function signature using type hints for both parameters and the return value:
    `def calculate_area(width, height):`
3.  **Clean Code:**
    -   Explain the "One Job Rule" for functions.
    -   Why should you avoid variable names like `x`, `temp`, or `data` in professional code?
4.  **Refactoring:** Take the following "messy" code and describe how you would improve it according to clean code principles:
    ```python
    def f(l):
        res = []
        for i in l:
            if i > 18:
                res.append(i)
        return res
    ```
