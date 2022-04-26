import random
import string

list_of_domains = ['supersqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']
length_of_email = 10   # each email has 10 characters
letters = string.ascii_lowercase
output_path = 'out_generate_random_email_with_list_of_domains_v1.csv'

# generate random emails and store in a list
all_emails = []
for domain in list_of_domains:
   # print(domain)
    for i in range(20):
        random_string = ''.join(random.choice(letters) for i in range(length_of_email))
       # email = random_string + '@' + domain
        email = f"{random_string}@{domain}"
       # email = "{}@{}".format(random_string, domain)
        all_emails.append(email)

# print(all_emails)
# import pdb; pdb.set_trace()

# take the list and write in a file

with open(output_path, 'w') as f:
    # option 1
    '''for email in all_emails:
        f.write(email)
        f.write(',\n')'''

    # option 2
    all_emails_str = ',\n'.join(all_emails)
    f.write(all_emails_str)