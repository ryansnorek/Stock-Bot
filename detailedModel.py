# DETAILED ONE-STAGE MODEL
import math
from variables import eps, dividend, PEatSale, targetRateOfReturn
from variables import volumeGrowthRate, pricingGrowthRate, pmExpansionRate, shareReductionPercentPerYear, dividendPayoutChangeRate
from variables import epsProjections, dividendProjections

# Calculations from input variables
revenueGrowthRate = round((
    (1 + volumeGrowthRate) * (1 + pricingGrowthRate) - 1), 3)

netIncomeGrowthRate = round(
    ((1 + revenueGrowthRate) * (1 + pmExpansionRate) - 1), 3)

epsGrowthRate = round((((1 + netIncomeGrowthRate) /
                        (1 - shareReductionPercentPerYear)) - 1), 3)

dividendGrowthRate = round(
    ((1 + epsGrowthRate) * (1 + dividendPayoutChangeRate) - 1), 3)


def getProjections(object, num, growthRate):
    for year in range(10):
        projection = round(num * (1 + growthRate), 3)
        object[year + 1] = projection
        num = projection


getProjections(epsProjections, eps, epsGrowthRate)
getProjections(dividendProjections, dividend, dividendGrowthRate)


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
salePrice = round((epsProjections[10] * PEatSale), 2)

dividendYieldAtSale = round((dividendProjections[10] / salePrice * 100), 2)

sumOfReinvestedDividends = getSumOfReinvestedDividends()

totalValueAtSale = round(salePrice + sumOfReinvestedDividends, 2)

buyPrice = round(totalValueAtSale / pow((1 + targetRateOfReturn), 10), 2)


print("DETAILED MODEL")
# print("EPS Projections: ", epsProjections)
# print("Dividend Projections: ", dividendProjections)

print("Sale Price In 10 Years: $", salePrice)
print("Dividend Yield at Sale: ", dividendYieldAtSale, "%")
print("Sum of Reinvested Dividends: $", sumOfReinvestedDividends)
print("Total Value at Sale: $", totalValueAtSale)
print("Buy Below: $", buyPrice)
