from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/drive']

# Variables to be configured by user 
# ======================================================
SERVICE_ACCOUNT_FILE = '<SERVICE_ACCOUNT_JSON_KEY_FILE_PATH>' 
FILE_PATH = '<FILE_PATH>'
PARENT_FOLDER_ID = '<PARENT_FOLDER_ID>'
# ======================================================

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def upload_file(file_path):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name' : "TestingFile.txt",
        'parents' : [PARENT_FOLDER_ID]
    }

    file = service.files().create(
        body=file_metadata,
        media_body=file_path
    ).execute()

upload_file(FILE_PATH)
