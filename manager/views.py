from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse
from manager.forms import UploadFileForm
import csv
API_KEY = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJEWkVPVFE0TkRWRE1VVXlNemszUWprME9FSkVNekl4T0VJM09FUXhNRFZFTVRRM1F6QTNSQSJ9.eyJodHRwczovL2hlcm1lc2Nsb3VkLmNvLnVrL3NlY3VyaXR5Ijp7Imhlcm1lc0NsaWVudElkIjoiNjU0OSIsImF1dGhvcml6YXRpb25fdjIiOnsicGVybWlzc2lvbnMiOm51bGwsInJvbGVzIjpbIlZpZXcgcGFyY2VsIGRldGFpbHMiXX0sImF1dGhvcml6YXRpb24iOnsiZ3JvdXBzIjpbXSwicm9sZXMiOltdLCJwZXJtaXNzaW9ucyI6W119fSwiaHR0cHM6Ly9oZXJtZXNjbG91ZC5jby51ay91c2VybmFtZSI6InUwMDAwMDAwMDAyNjMzOSIsImlzcyI6Imh0dHBzOi8vaGVybWVzLWNsb3VkLWNsdC1wcm9kLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NWQ3NTk3NTA0NmJiZTZhOTY4NjRiNWYiLCJhdWQiOlsiY2xpZW50LXBvcnRhbC1hcGkucHJvZC5oZXJtZXNjbG91ZC5jby51ayIsImh0dHBzOi8vaGVybWVzLWNsb3VkLWNsdC1wcm9kLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3MTU1NTI2NDgsImV4cCI6MTcxNTU1OTg0OCwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsImF6cCI6Im1WQnpxTzU2UDdHYTFSbmhMOVBFTFJVS0xxeXNNSnBhIiwicGVybWlzc2lvbnMiOlsiYWNjZXNzOmNsaWVudC1wb3J0YWwiLCJjcmVhdGU6YmF0Y2gtY29sbGVjdGlvbiIsImNyZWF0ZTpsYWJlbCIsImVkaXQ6Y29sbGVjdGlvbiIsImVkaXQ6ZGVsaXZlcnktYWRkcmVzcyIsImVkaXQ6ZGVsaXZlcnktaW5zdHJ1Y3Rpb25zIiwiZWRpdDpwYXJjZWwiLCJwZXJmb3JtOnN0b3AtYW5kLXJldHVybiIsInVpOnZpZXc6dmlldy1wYXJjZWwtZGV0YWlscyIsInVpOnZpZXc6d2ViZm9ybSIsInZpZXc6YmF0Y2gtY29sbGVjdGlvbi10ZW1wbGF0ZSIsInZpZXc6Y2xpZW50LWNvbmZpZyIsInZpZXc6Y29sbGVjdGlvbiIsInZpZXc6ZGVsaXZlcnktbWV0aG9kcyIsInZpZXc6cGFyY2VsIl19.elpZIMv_F3Dr34Nn2cIqlCwIdx11_CnHuRsHT7QZWiLh9TYcUJQ9x32WdxvZb7QxnOlDostXORweZG6-Zdj3RaytdFv3G2_mLIzjdk2vKqN4umlTch-NSjhZOO3CVp_PZ5C_JKMUiTH0Q5l9ksgxIyBOwQ1IPfWTIhZt1YDgcD4kY2PfNLE1QZNfrD-nbhx3TIgGZ7GxwLaL6VcOqzCnQn8JaBH-Y5QwMfLCPqlCIu7xpjQx2ZMWBJlJuPmVp1I2-T40PoyW3HmVDkt17i1cI3a_M0T8WW8L6WKEURKUMQcSX9GXERs979d4D_4pIN_ymsgHP4WVGyNr1ebQbIeYtw"
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

def upload_csv(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            reader = csv.reader(file.read().decode('utf-8').splitlines())
            headers = next(reader, None)  # Get the first row (headers)

            # Identify the indices for the required columns
            required_columns = ['Reference', 'MarketplaceStatus', 'Created', 'Source', 'Service', 'TrackingStatus', 'CustomerReference']
            indices = {headers.index(col): col for col in required_columns if col in headers}
            tracking_status_idx = headers.index('TrackingStatus')  # Get index for trackingstatus
            created_idx = headers.index('Created') 
            service_idx = headers.index('Service')
            
            # Extend headers to include the new "Delayed" column and "ID" as the first column
            headers = ['ID'] + headers + ['Delayed', 'Desc']  # Insert "ID" at the start of headers
            required_columns = ['ID'] + required_columns  + ['Delayed', 'Desc'] # Insert "ID" at the start of required columns
            indices = {col: headers.index(col) for col in required_columns}

            # Collect data only for the required columns and exclude rows with "delivered"
            data = []
            entry_id = 1  # Initialize the ID counter
            for row in reader:
                if row[tracking_status_idx].lower() != "delivered":  # Check tracking status
                    row[created_idx] = reformat_date(row[created_idx])  # Reformat date
                    delayed_info = calculate_delay(row[created_idx], row[service_idx])  # Calculate delay info
                    # row += [delayed_info, ""]  # Append new "Delayed" column information 
                            
                    description = ""
                    if "Delayed by" in delayed_info or "Expected" in delayed_info:
                        reference = row[indices['ID']]
                        parcel_id = fetch_parcel_details(reference)
                        print(parcel_id)
                        if parcel_id:
                            description = fetch_tracking_details(parcel_id)
                            print(description)
                    else:
                        description = "No description"   
                                                
                    row = [str(entry_id)] + row + [delayed_info , description] # Prepend ID to the row
                    filtered_row = [row[i] for i, col in enumerate(headers) if col in required_columns]
                    data.append(filtered_row)
                    entry_id += 1  # Increment ID for each processed row
                
            return render(request, 'display_csv.html', {'data': data, 'headers': required_columns})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

import datetime
def reformat_date(date_str):
    if not date_str.strip():  # Check if the date string is empty or only contains whitespace
        return ""  # Return an empty string or some default date as necessary
    
    # Parse the date-time string and reformat it
    try:
        date_format = "%m/%d/%Y %H:%M"  # Corrected format for hours and minutes
        target_format = "%d/%m/%Y"  # Desired format, keeping time part
        parsed_date = datetime.datetime.strptime(date_str, date_format)
        return parsed_date.strftime(target_format)
    except ValueError:
        return "Invalid date format"  # Return an error message or handle it as per your requirement

def calculate_delay(created_date, service_type):
    # Parse the European formatted date
    date_format = "%d/%m/%Y"
    delivery_date = datetime.datetime.strptime(created_date, date_format)

    # Determine the additional days based on service type
    if service_type == "Standard Parcel":
        add_days = 3
    elif service_type == "Next Day Parcel":
        add_days = 1
    elif service_type == "International":
        add_days = 7
    else:
        add_days = 0  # Default case if no matching service type

    # Calculate the expected delivery date
    expected_delivery = delivery_date + datetime.timedelta(days=add_days)

    # Compare with current system date
    current_date = datetime.datetime.now()
    if expected_delivery < current_date:
        delay_days = (current_date - expected_delivery).days
        if delay_days == 0:
            return f"Expected arival today"
        return f"Delayed by {delay_days} days"
    else:
        return "No noted delay"  # No delay