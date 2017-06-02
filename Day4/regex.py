import re

email_file = "C:\\Users\\gk\\Documents\\myPython\\Day4\\contacts_regex.txt"

pattern = re.compile(r'@\w[\w\.\-]+\w')

with open(email_file,"r",encoding='utf8') as file :
    dict_domain = dict()
    for line in file.readlines() :
        for domain in re.findall(pattern,line) :
            if domain in dict_domain.keys() :
                dict_domain[domain] += 1
            else:
                dict_domain[domain] = 1

print("len:", len(dict_domain))
print(dict_domain)



nameList = list(len(l.split(":")[0]) for l in dict_domain.keys() )
maxString = max(nameList)

shiftMaxStringFormat = '{:' + str(maxString) + '}'

print("\nshiftMaxStringFormat:")
print(shiftMaxStringFormat)

for d in sorted(dict_domain.keys()) :
    print(shiftMaxStringFormat.format(d), "\t:\t", dict_domain[d])
