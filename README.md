# QRCodeGenerator

`QRCodeGenerator` helps you to create QRCode in bulk. It also has the feature to generate a csv file in case you want to get the URL and the name for subfolders in a ***Shared with me*** Google Drive folder. You can follow the following link for the Google Cloud setup until you get the `credentials.json`.

[Python Quickstart](https://developers.google.com/drive/api/quickstart/python)

### Installation
---
#### Python Dependencies
```bash
pip3 install qrcode
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
### Usage
---
#### If you dont have a csv and wants to generate one from a ***Shared with me*** google drive folder:
Once you have the `credentials.json` in the same folder as this project open the **"googleDriveApi.py"** to edit the ***SHARED_WITH_ME_FOLDER_NAME*** variable to your desired folder. Then simply open the cmd inside the folder of the project and run:
```bash
python googleDriveApi.py
```
#### If you already have a csv file:
* Change your csv file to **"subfolders"** or edit the code with your file name. Then simply open the cmd inside the folder of the project and run:
```bash
python csvtoQRCodes.py
```
