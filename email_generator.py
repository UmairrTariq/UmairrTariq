import pandas as pd
import random
import string

# Number of spam and non-spam emails in the dataset
num_spam_emails = 10000
num_non_spam_emails = 10000

# Generate random spam emails
spam_emails = []
for _ in range(num_spam_emails):
    email_length = random.randint(50, 500)  # Random email length between 50 and 500 characters
    email_text = ''.join(random.choices(string.ascii_lowercase, k=email_length))
    spam_emails.append(email_text)

# Generate random non-spam emails
non_spam_emails = []
for _ in range(num_non_spam_emails):
    email_length = random.randint(50, 500)  # Random email length between 50 and 500 characters
    email_text = ''.join(random.choices(string.ascii_lowercase, k=email_length))
    non_spam_emails.append(email_text)

# Create a DataFrame with the combined dataset
data = {
    'text': spam_emails + non_spam_emails,
    'label': [1] * num_spam_emails + [0] * num_non_spam_emails
}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('spam_data.csv', index=False)