'''my_lang = ['python', 'Js', 'PHP', 'Java', 'Ruby']
with open('./my_fav_lang.csv', 'w') as f:
    for i in my_lang:
        f.writelines(i)
        f.writelines('\n')'''


my_lang = ['python', 'Js', 'PHP', 'Java', 'Ruby']
with open('my_fav_lang.csv', 'w') as f:
    str_my_lang = '\n'.join(my_lang)
    f.write(str_my_lang)