# Variables for importing
from getInputs import financials


# Shared model variables
name = financials['Name']
price = float(financials['Price'])
eps = float(financials['EPS'])
dividend = float(financials['Dividend'])
targetRateOfReturn = float(financials['Target Rate of Return'])
PEatSale = float(financials['PE at Sale'])

# Graham-Lynch model
longTermGrowthRate = float(financials['Long Term Growth Rate'])
corporateAAABondYield = float(financials['Corporate AAA Bond Yield'])

# Simple model
shortTermEPSgrowth = float(financials['Short Term EPS Growth Rate'])
longTermEPSgrowth = float(financials['Long Term EPS Growth Rate'])
shortTermDividendGrowth = float(financials['Short Term Dividend Growth Rate'])
longTermDividendGrowth = float(financials['Long Term Dividend Growth Rate'])

# Detailed model
volumeGrowthRate = float(financials['Volume Growth Rate'])
pricingGrowthRate = float(financials['Pricing Growth Rate'])
pmExpansionRate = float(financials['Profit Margin Expansion Rate'])
shareReductionPercentPerYear = float(financials['Share Reduction % Per Year'])
dividendPayoutChangeRate = float(financials['Dividend Payout Change Rate'])

# Empty objects for storing projections
epsProjections = {}
dividendProjections = {}
