import requests

# Replace with the URL where your Flask app is running
api_url = 'http://127.0.0.1:5000'

# Path to the image file you want to predict
image_path = 'Dataset/prediction/0037_png.rf.6231d8fc3fe6083092067e96ac3cd715.jpg'

# Send a POST request with the image file
response = requests.post(api_url, files={'file': open(image_path, 'rb')})

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response to get the prediction result
    result = response.json()
    predicted_class_index = result.get('prediction', 'Unknown')
    print(f'Predicted Class Index: {predicted_class_index}')
else:
    print('Error:', response.status_code)