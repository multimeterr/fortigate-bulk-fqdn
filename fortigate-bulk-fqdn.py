import csv
group_name = input("Gimme grp name:")
list_fqdn = []
names = ""

try:
    with open('urls.csv', newline='') as csvfile:
        list_url = csv.reader(csvfile, delimiter=';')
        for row in list_url:
            for i in row:
    	         list_fqdn.append(i.strip())
    	         names += "\""+i.strip()+"\" "
                 
except Exception as e:
    print("Error occurred: ",e)

  
lines = ['config firewall address']
with open('conf_fqdn.txt', 'w') as f:
    f.write('\n'.join(lines))

for url in list_fqdn:
    edit = '\nedit '+url
    name = 'set fqdn '+url
    lines = [edit,'set type fqdn',name,'next']
    with open('conf_fqdn.txt', 'a') as f:
        f.write('\n'.join(lines))

with open('conf_fqdn.txt', 'a') as f:
    lines = ['\nconfig firewall addrgrp','edit '+group_name,'set member '+names,'next','end']
    f.write('\nend')
    f.write('\n'.join(lines))
    