##SecInsecURL

##Sorting function
def checkthistxt (path,path1):
    ##Open text file with urls
    urlFile=open(path,'r')
    opened=urlFile.read()
    print('''This file that contain urls in it looks like this:\n\n'''+opened+'\n')
    ##Regex for http and https
    httporsreg=re.compile(r'''((http://|https://) #in urls there http:// or https://
([a-zA-Z0-9]*\.)? #then there is something.something.something
([a-zA-Z0-9]*\.)? #and mby some more
([a-zA-Z0-9/]{2,})?) #usualy url is ended something like this, 2 or more char
''',re.VERBOSE)
    sites=httporsreg.findall(opened) ##This is a container for all found urls
    ##Counters
    j=1
    k=1
    ##For loop goes through urls container
    for i in range (len(sites)):
        if sites[i][1]=='https://':#Check first group of found urls
            forPrint=sites[i][0]#Container for whole https urls
            Note=open(path1+r'/SecureSites.txt','a')
            Note.write(str(j)+'- '+forPrint+'\n')
            j=j+1
            Note.close()
        ##Same story here
        elif sites[i][1]=='http://':
            forPrint=sites[i][0]
            ##This is just one time variable like the one above, the point is to write in another file
            Note=open(path1+r'/NotSecureSites.txt','a')
            Note.write(str(k)+'- '+forPrint+'\n')
            k=k+1
            Note.close()
    print('It is done...')
    print('Secure web sites are:\n')
    sec=open(path1+r'/SecureSites.txt','r')
    sresult=sec.read()
    print(sresult)
    sec.close()
    print('Not secure web sites are:\n')
    nsec=open(path1+r'/NotSecureSites.txt','r')
    nresult=nsec.read()
    print(nresult)
    nsec.close()
    print('Files with Secure and Not secure web sites are created')

##Function for deleting files
def noLoseEnds(path1):
    os.remove(path1+r'/SecureSites.txt')
    os.remove(path1+r'/NotSecureSites.txt')


##----------SCRIPT----------
import os, re
pathUrl=input('''Insert path to file with all urls
which you want to sort out as secure and not secure
(for example /home/yourname/Desktop)
''')
pathSave=input('''Insert path to file in which
you want to save secure and not secure urls
(for example /home/yourname/Desktop)
''')
checkthistxt(pathUrl,pathSave)
while True:
    answer=input('''Do you want this files with secure and not secure urls to stay on your computer?
Y for Yes, N for No)\n''')
    if answer!='Y' and answer!='N':
        print('Wrong input! (Y for Yes, N for No)')
        continue
    elif answer=='Y':
        break
    elif answer=='N':
        noLoseEnds(pathSave)
    break
