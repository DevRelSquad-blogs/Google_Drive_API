from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/drive']

# Variables to be configured by user 
# ======================================================
SERVICE_ACCOUNT_FILE = '<SERVICE_ACCOUNT_JSON_KEY_FILE_PATH>' 
PARENT_FOLDER_ID = '<PARENT_FOLDER_ID>'
# ======================================================

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def create_folder():
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name' : "TestingMyFolder",
        'parents' : [PARENT_FOLDER_ID],
        'mimeType': 'application/vnd.google-apps.folder' 
    }

    file = service.files().create(
        body=file_metadata,
        fields='id'
    ).execute()

create_folder()
