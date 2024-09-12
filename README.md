# Geoloc Utility

## Overview
This utility fetches geographical coordinates (latitude and longitude) for US cities, states, or zip codes using the OpenWeather Geocoding API.

## Prerequisites
- Python 3.x installed.
- An OpenWeather Geocoding API Key.

## Setup Instructions

1. Clone the repository
2. Set up a Python virtual environment (Optional)

•	For Linux/MacOS
```shell
python3 -m venv venv
source venv/bin/activate
```

•	For Windows:
```shell
python -m venv venv
venv\Scripts\activate
```
3. Install project dependencies

Once your virtual environment is active, install the required dependencies from the requirements.txt file. Run the below command:
`pip install -r requirements.txt`

4. Copy the content of the `.env.example` file to the `.env` file in the root of the project (the same directory as `geoloc_util.py`) via:
`cp .env.example .env`

4. Set up the OpenWeather API Key

You need to set up the OpenWeather API key as an environment variable so that the utility can make authenticated API calls.

Use the Key obtained here [https://fetch-hiring.s3.amazonaws.com/SDET/Fetch_Coding_Exercise_SDET_v2.pdf]

5. Run the utility

`python geoloc_util.py "Madison, WI" "90210" "New York, NY"`

6. Running Tests

In the /geoloc-util directory run:
`pytest tests/test_geoloc_util.py`