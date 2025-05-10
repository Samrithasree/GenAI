import cohere

# Initialize Cohere with your API key
co = cohere.Client('DsRmc5CjA70ZOo1BVBXHRjRwOL9rjCNV9uQgSkxV')  # Replace with your Cohere API key

# Define the user query
user_query = """
I am looking for running shoes with the following preferences:
- Color: Black
- Purpose: Comfortable for long-distance running
- Budget: Under Rs. 10,000
Recommend me some options from trusted sites like Amazon, Flipkart, Myntra, Meesho, and Nike.
Clearly mention the key attributes (e.g., price, brand, features).
"""

# Send the query to Cohere's chat model
response = co.chat(
    message=user_query,
    chat_history=[]  # Empty chat history for a new session
)

# Corrected way to get the response text
print("\n=== Product Recommendations ===\n")
print(response.text)  # Use .text instead of .reply
