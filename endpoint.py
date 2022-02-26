import requests
import json

# URL for the web service, should be similar to:
scoring_uri = "http://365c8544-8e62-4f3e-a25c-a298b2bbee6e.southcentralus.azurecontainer.io/score"

# If the service is authenticated, set the key or token
key = "ToOzAV1TYHdkY5tbGG4ei2QdZhhYtRB9"

# Two sets of data to score, so we get two results back
data = {
    "Inputs": {
        "data": [{
		"age": 17,
		"job": "blue-collar",
		"marital": "married",
		"education": "university.degree",
		"default": "no",
		"housing": "yes",
		"loan": "yes",
		"contact": "cellular",
		"month": "may",
		"day_of_week": "mon",
		"duration": 971,
		"campaign": 1,
		"pdays": 999,
		"previous": 1,
		"poutcome": "failure",
		"emp.var.rate": -2,
		"cons.price.idx": 92,
		"cons.conf.idx": -46,
		"euribor3m": 1,
		"nr.employed": 5099,
	}, {
		"age": 87,
		"job": "blue-collar",
		"marital": "married",
		"education": "university.degree",
		"default": "no",
		"housing": "yes",
		"loan": "yes",
		"contact": "cellular",
		"month": "may",
		"day_of_week": "mon",
		"duration": 471,
		"campaign": 1,
		"pdays": 999,
		"previous": 1,
		"poutcome": "failure",
		"emp.var.rate": -2,
		"cons.price.idx": 92,
		"cons.conf.idx": -46,
		"euribor3m": 1,
		"nr.employed": 5099,
	},],
    },
    "GlobalParameters": {
        'method': "predict",
    }
}

# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {"Content-Type": "application/json"}
# If authentication is enabled, set the authorization header
headers["Authorization"] = f"Bearer {key}"

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())