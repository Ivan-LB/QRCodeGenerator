from __future__ import print_function
import csv

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Delete the file subfolders.csv each time you want to get the names and urls of a 'Shared with me' subfolders
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']
SHARED_WITH_ME_FOLDER_NAME = 'CLAMPS'
CREDENTIALS = 'credentials.json'

def get_folder_id(service, folder_name):
    query = f"mimeType='application/vnd.google-apps.folder' and trashed = false and name='{folder_name}'"
    results = service.files().list(
        q=query, fields="nextPageToken, files(id, name)").execute()
    items = results.get("files", [])
    if not items:
        print(f"No folder found with name {folder_name}.")
        return None
    return items[0]['id']

def get_subfolder_urls(service, folder_id):
    query = f"mimeType='application/vnd.google-apps.folder' and trashed = false and parents in '{folder_id}'"
    results = service.files().list(
        q=query, fields="nextPageToken, files(id, name, webViewLink)").execute()
    items = results.get("files", [])
    subfolders = {}
    for item in items:
        subfolders[item['name']] = item['webViewLink']
    with open('subfolders.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for name, url in subfolders.items():
            writer.writerow({'Name': name, 'URL': url})


def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)

        # Retrieve the shared folder's ID
        folder_id = get_folder_id(service, SHARED_WITH_ME_FOLDER_NAME)
        # Retrieve the URLs of the subfolders within the shared folder
        # subfolder_urls = get_subfolder_urls(service, folder_id)
        subfolders = get_subfolder_urls(service, folder_id)
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()