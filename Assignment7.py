import re

# Sample text
text = """
Contact us at student@gmail.com for more information.
You can also email admin@college.edu or support123@yahoo.com.
"""

# Regular expression pattern for email addresses
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Find all email addresses
emails = re.findall(pattern, text)

# Display email addresses
print("Email addresses found:")

for email in emails:
    print(email)



#User Input
import re

text = input("Enter text: ")

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(pattern, text)

if emails:
    print("Email addresses found:")
    for email in emails:
        print(email)
else:
    print("No email address found.")
