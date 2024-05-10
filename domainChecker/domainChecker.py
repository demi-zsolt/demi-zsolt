import whois
from datetime import datetime
from readExcelFile import readExcelFile

WARNING_LIMIT_IN_DAYS = 10
ERROR_LIMIT_IN_DAYS = 5


# Function to get the number of days until a domain expires
def getDaysToExpire(domain):
    domainInfo = whois.whois(domain)
    now = datetime.now()

    if domainInfo.expiration_date is None:
        expirationDate = now
    elif type(domainInfo.expiration_date) is list:
        expirationDate = domainInfo.expiration_date[0]
    else:
        expirationDate = domainInfo.expiration_date

    return (expirationDate - now).days


def domainNameCallback(cellValue):
    daysToExpire = getDaysToExpire(cellValue)

    if daysToExpire < ERROR_LIMIT_IN_DAYS:
        print("")
    elif daysToExpire < WARNING_LIMIT_IN_DAYS:
        print(cellValue + ' expires in ' + str(daysToExpire) + ' days')


readExcelFile = readExcelFile('domains.xlsx', 'domains')
readExcelFile.getColumnCells('domain', lambda cellValue: domainNameCallback(cellValue))

## pip install pandas openpyxl
## pip install python-whois
## pip install twilio