# Get Financials from CSV file
import csv


def getCompanyFinancials():
    companyFinancials = {}

    with open('company_financials.csv', newline='') as csvfile:
        readFile = csv.reader(csvfile)
        for row in readFile:
            companyFinancials[row[0]] = row[1]

    return companyFinancials


financials = getCompanyFinancials()
