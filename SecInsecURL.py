###sorting function
def checkthistxt (path,path1):
    ##open text file with urls
    urlFile=open(path,'r')
    opened=urlFile.read()
    print('''The file that contain urls in it looks like this:\n\n'''+opened+'\n')
    ##regex for http and https
    httporsreg=re.compile(r'''((http://|https://) #in urls there http:// or https://
([a-zA-Z0-9]*\.)? #then there is something.something.something
([a-zA-Z0-9]*\.)? #and mby some more
([a-zA-Z0-9/]{2,})?) #usualy url is ended something like this, 2 or more char
''',re.VERBOSE)
    sites=httporsreg.findall(opened) ##this is a container for all found urls
    ##counters
    j=1
    k=1
    ##for loop goes through urls container
    for i in range (len(sites)):
        if sites[i][1]=='https://':#check first group of found urls
            forPrint=sites[i][0]#container for https urls
            Note=open(path1+r'/secure_sites.txt','a')
            Note.write(str(j)+'- '+forPrint+'\n')
            j=j+1
            Note.close()
        ##same story here
        elif sites[i][1]=='http://':
            forPrint=sites[i][0]
            ##this is just one time variable like the one above, the point is to write in another file
            Note=open(path1+r'/not_secure_sites.txt','a')
            Note.write(str(k)+'- '+forPrint+'\n')
            k=k+1
            Note.close()
    print('It is done...')
    print('Secure web sites are:\n')
    sec=open(path1+r'/secure_sites.txt','r')
    sresult=sec.read()
    print(sresult)
    sec.close()
    print('Not secure web sites are:\n')
    nsec=open(path1+r'/not_secure_sites.txt','r')
    nresult=nsec.read()
    print(nresult)
    nsec.close()
    print('Files with Secure and Not secure web sites are created')

##function for deleting files
def no_lose_ends(path1):
    os.remove(path1+r'/secure_sites.txt')
    os.remove(path1+r'/not_secure_sites.txt')

###MAIN
import os, re
path_url=input('''Insert path to text file (file included) with all urls
which you want to sort out as secure and not secure
(for example /home/yourname/Desktop/url.txt)
''')
path_save=input('''Insert path to file in which
you want to save secure and not secure urls
(for example /home/yourname/Desktop)
''')
checkthistxt(path_url,path_save)
while True:
    answer=input('''Do you want this files with secure and not secure urls to stay on your computer?
Y for Yes, N for No)\n''')
    if answer!='Y' and answer!='N':
        print('Wrong input! (Y for Yes, N for No)')
        continue
    elif answer=='Y':
        break
    elif answer=='N':
        no_lose_ends(path_save)
    break
