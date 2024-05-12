API_KEY = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJEWkVPVFE0TkRWRE1VVXlNemszUWprME9FSkVNekl4T0VJM09FUXhNRFZFTVRRM1F6QTNSQSJ9.eyJodHRwczovL2hlcm1lc2Nsb3VkLmNvLnVrL3NlY3VyaXR5Ijp7Imhlcm1lc0NsaWVudElkIjoiNjU0OSIsImF1dGhvcml6YXRpb25fdjIiOnsicGVybWlzc2lvbnMiOm51bGwsInJvbGVzIjpbIlZpZXcgcGFyY2VsIGRldGFpbHMiXX0sImF1dGhvcml6YXRpb24iOnsiZ3JvdXBzIjpbXSwicm9sZXMiOltdLCJwZXJtaXNzaW9ucyI6W119fSwiaHR0cHM6Ly9oZXJtZXNjbG91ZC5jby51ay91c2VybmFtZSI6InUwMDAwMDAwMDAyNjMzOSIsImlzcyI6Imh0dHBzOi8vaGVybWVzLWNsb3VkLWNsdC1wcm9kLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NWQ3NTk3NTA0NmJiZTZhOTY4NjRiNWYiLCJhdWQiOlsiY2xpZW50LXBvcnRhbC1hcGkucHJvZC5oZXJtZXNjbG91ZC5jby51ayIsImh0dHBzOi8vaGVybWVzLWNsb3VkLWNsdC1wcm9kLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3MTU1MzczODQsImV4cCI6MTcxNTU0NDU4NCwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsImF6cCI6Im1WQnpxTzU2UDdHYTFSbmhMOVBFTFJVS0xxeXNNSnBhIiwicGVybWlzc2lvbnMiOlsiYWNjZXNzOmNsaWVudC1wb3J0YWwiLCJjcmVhdGU6YmF0Y2gtY29sbGVjdGlvbiIsImNyZWF0ZTpsYWJlbCIsImVkaXQ6Y29sbGVjdGlvbiIsImVkaXQ6ZGVsaXZlcnktYWRkcmVzcyIsImVkaXQ6ZGVsaXZlcnktaW5zdHJ1Y3Rpb25zIiwiZWRpdDpwYXJjZWwiLCJwZXJmb3JtOnN0b3AtYW5kLXJldHVybiIsInVpOnZpZXc6dmlldy1wYXJjZWwtZGV0YWlscyIsInVpOnZpZXc6d2ViZm9ybSIsInZpZXc6YmF0Y2gtY29sbGVjdGlvbi10ZW1wbGF0ZSIsInZpZXc6Y2xpZW50LWNvbmZpZyIsInZpZXc6Y29sbGVjdGlvbiIsInZpZXc6ZGVsaXZlcnktbWV0aG9kcyIsInZpZXc6cGFyY2VsIl19.oYJN6jOoWhU4gts7yaJAooDc81JwWihe-Q6GZNfMVlkX_kI0GVPnBNEoewOQE5k5fS1pNQMZORXBb5yrYajWXwvt_lSiDzCyuwQhNZBSnEjISVFHMo9PSGhiWrmS6bC5GDumXqG6czqFb2pL9kb4o2w312uhLWu7M9rW4Ln1utFTSCOwiCH0T_OIcSgPdmTRCZIJjgc3xK1ZzeLeKgfmOBDacwIo0UJhEUNX9mxEEB4iRIMw6pjlFyjlQDN_BqV5t0NR_T_njR7xHvG-HFto9r2ND6qDLOlpRjPy0O_EwmfeOSeSJR4hm3pkmBM8RKXXgotnzVut2D-pZhX027M1iA"
def index(request):
    return HttpResponse("hello words")

import requests
from django.conf import settings  # Ensure you have your API keys stored in settings or environment variables

def fetch_parcel_details(reference):
    url = f"https://api.hermesworld.co.uk/v2/client-portal-api/parcel-search?customerRef={reference}&fromDate=2023-11-14&toDate=2024-05-12"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Origin": "https://clients.evricloud.co.uk"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
        parcel_id = data['parcelSearchResults'][0]['parcelId'] if data['parcelSearchResults'] else None
        return parcel_id
    else:
        return None

def fetch_tracking_details(parcel_id):
    url = f"https://api.hermesworld.co.uk/v2/client-portal-api/tracking/{parcel_id}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # Assuming the response is a list of tracking points
        description = data[0]['point']['externalDescription'] if data else None
        return description
    else:
        return None
    
x = fetch_parcel_details("EVR42749299")
y= fetch_tracking_details(x)
print(y)