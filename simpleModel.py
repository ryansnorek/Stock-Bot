# SIMPLE TWO-STAGE MODEL
import math
from functools import reduce
from variables import eps, dividend, shortTermEPSgrowth, longTermEPSgrowth, shortTermDividendGrowth, longTermDividendGrowth, targetRateOfReturn, PEatSale
from variables import epsProjections, dividendProjections


def getProjections(object, num, shortTermGrowthRate, longTermGrowthRate):
    # Function takes in 4 arguements
    # 1. One of the empty objects to store everything in
    # 2. Starts with current input and then updates every iteration with the next years projection
    # 3. Growth rate multiplier of num for short term (1-5 years)
    # 4. Growth rate multiplier of num for long term (6-10 years)
    growthRate = shortTermGrowthRate

    for year in range(10):
        if (year >= 5):
            growthRate = longTermGrowthRate
        projection = round(num * (1 + growthRate), 2)
        object[year + 1] = projection
        num = projection


getProjections(epsProjections, eps,
               shortTermEPSgrowth, longTermEPSgrowth)
getProjections(dividendProjections, dividend,
               shortTermDividendGrowth, longTermDividendGrowth)


def getSumOfReinvestedDividends():
    reinvestedDividends = []
    power = len(dividendProjections) - 1
    for dividend in dividendProjections:

        if (power > 0):
            calc = dividendProjections[dividend] * \
                pow((1 + targetRateOfReturn), power)
            power -= 1
            reinvestedDividends.append(calc)

    reinvestedDividends.append(dividendProjections[10])

    return round(sum(reinvestedDividends), 2)


# Calculations
salePrice = round(epsProjections[10] * PEatSale, 2)

dividendYieldAtSale = round((dividendProjections[10] / salePrice * 100), 2)

sumOfReinvestedDividends = getSumOfReinvestedDividends()

totalValueAtSale = round(salePrice + sumOfReinvestedDividends, 2)

buyPrice = round(totalValueAtSale / pow((1 + targetRateOfReturn), 10), 2)

print("SIMPLE MODEL")
# print("EPS Projections:", epsProjections)
# print("Dividend Projections:", dividendProjections)
# print()
print("Sale Price in 10 Years: $", salePrice)
print("Dividend Yield at Sale: ", dividendYieldAtSale, "%")
print("Sum of Reinvested Dividends: $", sumOfReinvestedDividends)
print("Total Value at Sale: $", totalValueAtSale)
print("Buy Below: $", buyPrice)
