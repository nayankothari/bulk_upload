# bulk_upload
for testing purpose only


# Run using command prompt
curl -X POST -F "file=@data_sheet.xlsx" http://127.0.0.1/api/v1/upload-files

# With python 
import requests

url = 'http://127.0.0.1/api/v1/upload-files/'
files = {'file': open('data_sheet.xlsx', 'rb')}
response = requests.post(url, files=files)
print(response.json())


# Bulk Upload API - Django REST Framework

This test project is django rest API to bulk upload employee and company data from an Excel file. 
It uses pandas for reading excel data and django ORM for saving it efficiently to the database withour
using sql/ORM in loop.

## Features
- Upload .xlsx file with employee and company data.
- Automatically creates unique companies if they don’t exist.
- Validate employee data using serializers.
- bulk insert for better performance.

## API Endpoint

### `POST /api/v1/upload-files/`

Uploads an Excel file with employee and company data.

## Requirements.txt for python dependencies
pip install -r requirement.txt


