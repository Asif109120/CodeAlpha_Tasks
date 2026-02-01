import re

input_file = "input.txt"
output_file = "emails.txt"

with open(input_file, "r") as file:
    text = file.read()

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print("✅ Emails extracted and saved to emails.txt")
