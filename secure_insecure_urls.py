#!/usr/bin/env python3

import os
import re

def check_this_txt(path, path1):
    # Open text file with URLs
    with open(path, 'r') as url_file:
        opened = url_file.read()
        print('The file that contains URLs looks like this:\n\n' + opened + '\n')

    # Regex for http and https
    http_https_regex = re.compile(r'''((http://|https://)
                            ([a-zA-Z0-9]*\.)?
                            ([a-zA-Z0-9]*\.)?
                            ([a-zA-Z0-9/]{2,})?)''', re.VERBOSE)
    
    # Container for all found URLs
    sites = http_https_regex.findall(opened)

    # Counters
    j = 1
    k = 1

    # For loop goes through URLs container
    for i in range(len(sites)):
        if sites[i][1] == 'https://':
            # Check the first group of found URLs
            for_print = sites[i][0]
            note = open(os.path.join(path1, 'secure_sites.txt'), 'a')
            note.write(str(j) + '- ' + for_print + '\n')
            j += 1
            note.close()
        elif sites[i][1] == 'http://':
            # Same story here
            for_print = sites[i][0]
            note = open(os.path.join(path1, 'not_secure_sites.txt'), 'a')
            note.write(str(k) + '- ' + for_print + '\n')
            k += 1
            note.close()

    print('It is done...')
    print('Secure web sites are:\n')
    with open(os.path.join(path1, 'secure_sites.txt'), 'r') as sec:
        secure_results = sec.read()
        print(secure_results)

    print('Not secure web sites are:\n')
    with open(os.path.join(path1, 'not_secure_sites.txt'), 'r') as nsec:
        not_secure_results = nsec.read()
        print(not_secure_results)

    print('Files with Secure and Not secure web sites are created')

def no_lose_ends(path1):
    os.remove(os.path.join(path1, 'secure_sites.txt'))
    os.remove(os.path.join(path1, 'not_secure_sites.txt'))

# MAIN
path_url = input('''Insert the path to a text file with all URLs that you want to sort out as secure and not secure
(for example /home/username/Desktop/url.txt)\n''')
path_save = input('''Insert the path to a directory in which you want to save sorted, secure and not secure URLs
(for example /home/username/Desktop)\n''')

check_this_txt(path_url, path_save)

while True:
    answer = input('''Do you want these files with secure and not secure URLs to stay on your computer?
Y for Yes, N for No\n''')
    if answer not in ('Y', 'N'):
        print('Wrong input! (Y for Yes, N for No)')
        continue
    elif answer == 'Y':
        break
    elif answer == 'N':
        no_lose_ends(path_save)
        break
