# count domain in email list file
import json
import pdb

input_file = 'out_generate_random_email_with_list_of_domains_v2.csv'
output_file = 'count_domains_in_email_list_file.json'

def get_email_from_file(file_path):
    with open(file_path, 'r') as f:
        emails_raw = f.readlines()

    email_clean = [i.strip(',\n') for i in emails_raw]

    return email_clean

def count_domain_option_1(list_of_emails):
    print("doing count option 1")
    email_count = dict()
    for email in list_of_emails:
        domain = email.split('@')[-1]
        if domain not in email_count.keys():
            email_count[domain] = 1
        else:
            email_count[domain] = email_count[domain] + 1

    return email_count

def count_domain_option_2(list_of_emails):
    print("doing count option 2")
    domains_list = []
    for email in list_of_emails:
        domains = email.split('@')[-1]
        domains_list.append(domains)

    unique_domains = set(domains_list)


    email_count = dict()
    for domains in unique_domains:
        email_count[domains] = domains_list.count(domains)

    return email_count

def save_output_in_json_file(counts_dict, json_file_path):
    print(f"saving file: {json_file_path}")
    with open(json_file_path, 'w') as f:
        json_obj = json.dumps(counts_dict)
        f.write(json_obj)

email_list = get_email_from_file(input_file)

# solution 1
counts1 = count_domain_option_1(email_list)
save_output_in_json_file(counts1, output_file)
print(counts1)


# option 2
count2 = count_domain_option_2(email_list)
print(count2)


