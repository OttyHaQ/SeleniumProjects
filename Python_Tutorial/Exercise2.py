import random
import string

'''list_of_domains = ['supersqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']
length_of_email = 10   # each email has 10 characters
letters = string.ascii_lowercase
output_path = 'out_generate_random_email_with_list_of_domains_v2.csv'
total_number_of_email = 100

# OPTION 1 generate random emails and store in a list

all_emails = []
for i in range(100):
    rand_domain = random.choice(list_of_domains)
    random_string = ''.join(random.choice(letters) for i in range(length_of_email))
    rand_email = f"{random_string}@{rand_domain}"
    all_emails.append(rand_email)

print(all_emails)
print(len(all_emails))

# take the list and write in a file

with open(output_path, 'w') as f:
    # option 1
    # for email in all_emails:
        # f.write(email)
       # f.write(',\n')

    # option 2
    all_emails_str = ',\n'.join(all_emails)
    f.write(all_emails_str)'''

# OPTION 2

with open(output_path, 'w') as f:
    for i in range(100):
        rand_domain = random.choice(list_of_domains)
        random_string = ''.join(random.choice(letters) for i in range(length_of_email))
        rand_email = f"{random_string}@{rand_domain}"
        #all_emails.append(rand_email)
        # all_emails_str = ',\n'.join(all_emails)
        f.write(rand_email + ',\n')