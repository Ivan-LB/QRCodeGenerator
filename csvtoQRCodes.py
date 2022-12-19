import csv
import qrcode

# Here we store the values of the columns in the csv file
column1 = []  # URLs
column2 = []  # Image Names
CSV_FILE_NAME = 'subfolders.csv'

# Here we open the csv file
with open(CSV_FILE_NAME, 'r') as f:
  reader = csv.reader(f)

  # Here we iterate for each row on the file
  for index, row in enumerate(reader):
    # If it's the first row we skip it
    if index == 0:
      continue
    # Here we append the values to the corresponding array
    column1.append(row[1])
    column2.append(row[0])

# Here we iterate over the values stored in column1
for i in range(len(column1)):
    # Here we create a QR object
    qr = qrcode.QRCode(
        version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(column1[i])
    qr.make(fit=True)

    # An image is created based of the QR object
    img = qr.make_image()

    # The image is saved with the name on the array
    img.save(f'{column2[i]}.png')
