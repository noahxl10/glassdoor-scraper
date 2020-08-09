cons = open('/Users/noahalex/Documents/Personal Dox/School Docs/State of Utah/Scraper/cons.txt','r')


with open(r'/Users/noahalex/Documents/Personal Dox/School Docs/State of Utah/Scraper/cons.txt', 'r') as infile, \
     open(r'/Users/noahalex/Documents/Personal Dox/School Docs/State of Utah/Scraper/consfinal.txt', 'w') as outfile:
    data = infile.read()
    j = [',', '.', '!', '?']
    k = [' and ', ' with ', ' job ', 'Job ', ' State ', ' Utah ', ' will ', ' get ', ' of ', ' great ', 'Great ', ' good ', 'Good ', ' I ', ' you ', ' them ', ' a ', ' to ', 'It ', ' have ', ' in ', ' for ', ' that ', ' on ',' it ', ' the ', 'The ', ' are ', ' is ', ' - ', ]
    for i in j:
        data = data.replace(i, '')
        
    for i in k:
        data = data.replace(i, ' ')
    
    data = data.replace('B', 'b')
    outfile.write(data)



 