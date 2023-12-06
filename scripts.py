import requests

# Define the necessary parameters
env_name = "env-7592161"
session = "8ce6e9e8510646d6bb2aeb1d566351fe544bed94"
node_id = 15725
image_name = ""  # Replace with the actual image name
image_version = "latest"  # Replace with the desired image version

# Construct the payload for the API request
payload = {
    "envName": env_name,
    "session": session,
    "nodeId": node_id,
    "tag": f"{image_name}:{image_version}"
}

# API endpoint URL (replace with your actual API endpoint)
api_endpoint = "https://your-api-endpoint.com/update-container"

# Make the API request
response = requests.post(api_endpoint, json=payload)

# Check the response status
if response.status_code == 200:
    print("Container updated successfully!")
else:
    print(f"Failed to update container. Status code: {response.status_code}")
    print(f"Error message: {response.text}")
