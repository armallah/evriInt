from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse
from manager.forms import UploadFileForm
import csv

B_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJEWkVPVFE0TkRWRE1VVXlNemszUWprME9FSkVNekl4T0VJM09FUXhNRFZFTVRRM1F6QTNSQSJ9.eyJodHRwczovL2hlcm1lc2Nsb3VkLmNvLnVrL3NlY3VyaXR5Ijp7Imhlcm1lc0NsaWVudElkIjoiNjU0OSIsImF1dGhvcml6YXRpb25fdjIiOnsicGVybWlzc2lvbnMiOm51bGwsInJvbGVzIjpbIlZpZXcgcGFyY2VsIGRldGFpbHMiXX0sImF1dGhvcml6YXRpb24iOnsiZ3JvdXBzIjpbXSwicm9sZXMiOltdLCJwZXJtaXNzaW9ucyI6W119fSwiaHR0cHM6Ly9oZXJtZXNjbG91ZC5jby51ay91c2VybmFtZSI6InUwMDAwMDAwMDAyNjMzOSIsImlzcyI6Imh0dHBzOi8vaGVybWVzLWNsb3VkLWNsdC1wcm9kLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NWQ3NTk3NTA0NmJiZTZhOTY4NjRiNWYiLCJhdWQiOlsiY2xpZW50LXBvcnRhbC1hcGkucHJvZC5oZXJtZXNjbG91ZC5jby51ayIsImh0dHBzOi8vaGVybWVzLWNsb3VkLWNsdC1wcm9kLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3MjQ3NjY5MDYsImV4cCI6MTcyNDc3NDEwNiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsImF6cCI6Im1WQnpxTzU2UDdHYTFSbmhMOVBFTFJVS0xxeXNNSnBhIiwicGVybWlzc2lvbnMiOlsiYWNjZXNzOmNsaWVudC1wb3J0YWwiLCJjcmVhdGU6YmF0Y2gtY29sbGVjdGlvbiIsImNyZWF0ZTpsYWJlbCIsImVkaXQ6Y29sbGVjdGlvbiIsImVkaXQ6ZGVsaXZlcnktYWRkcmVzcyIsImVkaXQ6ZGVsaXZlcnktaW5zdHJ1Y3Rpb25zIiwiZWRpdDpwYXJjZWwiLCJwZXJmb3JtOnN0b3AtYW5kLXJldHVybiIsInVpOnZpZXc6dmlldy1wYXJjZWwtZGV0YWlscyIsInVpOnZpZXc6d2ViZm9ybSIsInZpZXc6YmF0Y2gtY29sbGVjdGlvbi10ZW1wbGF0ZSIsInZpZXc6Y2xpZW50LWNvbmZpZyIsInZpZXc6Y29sbGVjdGlvbiIsInZpZXc6ZGVsaXZlcnktbWV0aG9kcyIsInZpZXc6cGFyY2VsIl19.TJwKz7Jxs27ng9e9PT5-5OVbPHmS9F_BsyUGyAXoT3JSgM7TyDPY0gCgRvuoLXduKYhf9o1fx1Plw9GglPEZA-vXawEl9ewsVA9yS-LTkJeekPIbv-plOK06xEihkX5QLEbjOuOYeFbmxle5-Q3rMiyMuaP08PyG3Ty5OeBXCUkC_wdIcgrJ5SOOOoJXgMSZFtiUpHqbSK0U-c0i4sZ7exv2cO4UQSTfirW1AieXUyuqK3__6A2mbKRUIsWbvpvy7lGVgTfTrJjBmIO5rPoUzVcDqfqus3WBOEMG-VWJ3kyFYgCpt3hPoV19t1R0npiF61ACp85QuPTykEuXRL6jdQ"
def index(request):
    return HttpResponse("hello words")

import requests
from django.conf import settings  


def get_add_details(reference):
    API_KEY = B_TOKEN
    url = f"https://api.hermesworld.co.uk/v2/client-portal-api/v1/parcels/search?barcode={reference}&fromDate=2024-03-01&toDate=2025-01-01"
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
        return data
    else:
        return None


def fetch_parcel_details(reference):
    API_KEY = B_TOKEN
    url = f"https://api.hermesworld.co.uk/v2/client-portal-api/parcel-search?customerRef={reference}&fromDate=2023-11-14&toDate=2025-01-01"
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
        return data
    else:
        return None

def fetch_tracking_details(parcel_id):    
    API_KEY = B_TOKEN
    url = f"https://api.hermesworld.co.uk/v2/client-portal-api/tracking/{parcel_id}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en;q=0.7",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/4.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Origin": "https://clients.evricloud.co.uk"
    }
    response = requests.get(url, headers=headers)
    # print("featchtracking", response)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


def fetch_customer_details(parcel_id):
    API_KEY = B_TOKEN
    url = f"https://api.hermesworld.co.uk/v2/client-portal-api/v1/parcels/{parcel_id}"
    print(url)
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/4.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "connection":"keep-alive",
        "host": "api.hermesworld.co.uk",
        "location_id": "12",
        "location_type": "OTHER",
        "origin": "https://clients.evricloud.co.uk",
        "referer": "https://clients.evricloud.co.uk/",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform":"Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "sec-gpc": "1"
    }
    response = requests.get(url, headers=headers)
    # print("CUSS", response)
    if response.status_code == 200:
        data = response.json()
        return data
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
            headers = ['ID'] + headers + ['Delayed', 'Desc', 'Status' ,'Barcode', 'Customer Name','Item Desc', 'Parcel Type', 'Phone No']  # Insert "ID" at the start of headers
            required_columns = ['ID'] + required_columns  + ['Delayed', 'Desc', 'Status' ,'Barcode', 'Customer Name', 'Item Desc', 'Parcel Type', 'Phone No'] # Insert "ID" at the start of required columns
            indices = {col: headers.index(col) for col in required_columns}

            # Collect data only for the required columns and exclude rows with "delivered"
            data = []
            
            entry_id = 1  # Initialize the ID counter
            for row in reader:
                if row[tracking_status_idx].lower().replace(" ", "") == "delivered":
                    continue
                
                if row[tracking_status_idx].lower().replace(" ", "") == "new":
                    continue
                if row[tracking_status_idx].lower().strip() != "delivered" or row[tracking_status_idx].lower() != "new":  # Check tracking status
                    
                    row[created_idx] = reformat_date(row[created_idx])  # Reformat date
                    delayed_info = calculate_delay(row[created_idx], row[service_idx])  # Calculate delay info
                    if delayed_info[0] == "0" or delayed_info[0] == "N":
                        continue
                    # row += [delayed_info, ""]  # Append new "Delayed" column information 
                    reference = row[indices['ID']]
                    parcelData = fetch_parcel_details(reference)
                    description = ""
                    try:
                        parcel_id = parcelData['parcelSearchResults'][0]['parcelId'] if parcelData['parcelSearchResults'] else None
                        print("parcelid ", parcel_id)
                        if parcel_id:
                            trackingdata = fetch_tracking_details(parcel_id)
                            # print("trackingdata" , trackingdata )
                            description = trackingdata[0]['point']['externalDescription'] if trackingdata else None
                            # print("desc ",description)
                            status = getStatus(trackingdata)
                            # print("sgsdfsgsg" , status)
                    except:
                        description = "No description"
                        status = "None"
                                                                          
                    barcode = parcelData['parcelSearchResults'][0]['barcode'] if parcelData['parcelSearchResults'] else None
                
                    addDetails  = get_add_details(barcode)
                    if addDetails != None:  
                        customer_name = addDetails[0].get("customerName")
                        item_description = addDetails[0].get("description")
                        parcelType = addDetails[0].get("parcelTypeDesc")
                        customerData = fetch_customer_details(parcel_id)
                        # print("CUS DATA \t\t", customerData)
                        try: 
                            phonenumber = customerData.get("customerMblPhoneNumber")
                        except:
                            phonenumber = "None"
                        print(customer_name, item_description, parcelType)
                    else:
                        customer_name = "None"
                        parcelType = "None"
                        item_description = "None"
                    
                    row = [str(entry_id)] + row + [delayed_info , description, status, barcode, customer_name, item_description, parcelType, phonenumber] # Prepend ID to the row
                    filtered_row = [row[i] for i, col in enumerate(headers) if col in required_columns]
                    data.append(filtered_row)
                    entry_id += 1  # Increment ID for each processed row
            
            request.session['csv_data'] = data  # Save data to session for export
            request.session['csv_headers'] = ["ID", "Reference", "Marketplace Status" ,"Created", "Source", "Service" , "Tracking Status", "Customer Reference", "Delayed", "Desc","Status", "Barcode Ref", "Customer Name","Item Desc", "Parcel Type", "Phone No"]
                
            return render(request, 'display_csv.html', {'data': data, 'headers': required_columns})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def getStatus(d, p=0): 
    dd  = d[p]['point']['externalDescription'] 
    if "Receipt" not in dd:
        if "Reprint" not in dd:
            if "Parcel processed" not in dd:
                return dd
    
    return getStatus(d,p+1)
                

def export_csv(request):
    data = request.session.get('csv_data', [])
    headers = request.session.get('csv_headers', [])

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'

    writer = csv.writer(response)
    writer.writerow(headers)
    writer.writerows(data)

    return response

import datetime
def reformat_date(date_str):
    if not date_str.strip():  # Check if the date string is empty or only contains whitespace
        return ""  # Return an empty string or some default date as necessary
    
    # Parse the date-time string and reformat it
    try:
        date_format = "%m/%d/%Y %I:%M:%S %p"  # Corrected format for hours and minutes
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
        add_days = 2
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
            return f"0 days"
        return f"{delay_days} days"
    else:
        return "No noted delay"  # No delay
