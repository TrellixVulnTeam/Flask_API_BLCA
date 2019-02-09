import requests, json

api_endpoint1 = 'http://localhost:54199/api/test/testHitGet'
api_endpoint2 = 'http://localhost:54199/api/test/testHitPost'

post_call_input = {
      "id": "003", 
      "name": "vidushi"
    }

response = requests.get(api_endpoint1)
response_post = requests.post(api_endpoint2, data=post_call_input)

print("\nGET Call Results")
if(response.status_code == 200):
	print("Request Successful !", response.status_code)
	print(response.text)
else:
	print("Request Unsuccessful! status code:", response.status_code)
	print(response.text)

print("\nPOST Call Results")
if(response_post.status_code == 200):
	print("Request Successful !", response_post.status_code)
	print(response_post.text)
else:
	print("Request Unsuccessful! status code:", response_post.status_code)
	print(response_post.text)


