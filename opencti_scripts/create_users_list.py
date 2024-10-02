import requests

# Define the OpenCTI API URL and your API token
API_URL = "https://my-octi.io/graphql"
API_TOKEN = "CHANGE_ME"
USER_CONFIDENCE_LEVEL = 75
PASSWORD = "password123"
GROUP_ID = "CHANGE_ME"

# Define the headers for the request
headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# Define a list of predefined users
users = [
    {
        "name": "yass_John Doe",
        "user_email": "john.doe@example.com",
        "firstname": "John",
        "lastname": "Doe",
        "user_confidence_level": {"max_confidence": USER_CONFIDENCE_LEVEL, "overrides": []},
        "password": PASSWORD,
        "account_status": "active",
        "groups": [GROUP_ID]
    },
    {
        "name": "yass_Jane Smith",
        "user_email": "jane.smith@example.com",
        "firstname": "Jane",
        "lastname": "Smith",
        "user_confidence_level": {"max_confidence": USER_CONFIDENCE_LEVEL, "overrides": []},
        "password": PASSWORD,
        "account_status": "inactive",
        "groups": [GROUP_ID]
    }
    # Add more users as needed
]

# Define the GraphQL mutation
mutation = """
mutation UserCreationMutation($input: UserAddInput!) {
  userAdd(input: $input) {
    id
    name
    user_email
    firstname
    external
    lastname
    effective_confidence_level {
      max_confidence
    }
    otp_activated
    created_at
  }
}
"""

# Function to create a user
def create_user(user):
    variables = {
        "input": user
    }
    response = requests.post(API_URL, headers=headers, json={"query": mutation, "variables": variables})
    return response.json()

# Loop through the list of users and create each one
for user in users:
    result = create_user(user)
    print(result)

