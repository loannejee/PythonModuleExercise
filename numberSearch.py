import os
import re

# Step 3: Regular Expression to Find the Link
# Test if this works:
# Another format: \d\d\d-\d\d\d-\d\d\d\d
pattern = r'\d{3}-\d{3}-\d{4}'
test_string = "here is a random number 1231231234 , here is phone number formatted 123-123-1234"
print(re.findall(pattern, test_string))


# Step 4: Create a function for regex
def search(file, pattern= r'\d{3}-\d{3}-\d{4}'):
    f = open(file,'r')
    text = f.read()
    
    if re.search(pattern, text):
        # If there is a match, return the phone number
        return re.search(pattern,text)
    else:
        return ''


# Step 5: OS Walk through the Files to Get the Link
results = []
# getcwd() = current working directory
# \\ inserts a backslash
for folder , sub_folders , files in os.walk(os.getcwd()+"\\extracted_content"):
    
    for f in files:
        full_path = folder+'\\'+f
        # A default pattern has already been defined:
        results.append(search(full_path)) 


for r in results:
    if r != '':
        print(r.group())


