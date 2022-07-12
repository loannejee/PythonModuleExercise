# Step 1: Unzipping the File
# Step 2: Read the instructions file
import zipfile

zipped_obj = zipfile.ZipFile('unzip_me_for_instructions.zip', 'r')
zipped_obj.extractall('extracted_content')
