import math
from variables import *


def getSumOfReinvestedDividends():
    # Sum of dividends are added to the simple and detailed models
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


def simpleModel():

    def getProjections(object, num, shortTermGrowthRate, longTermGrowthRate):
        # Short term is 1-5 yrs, Long term is 6-10 yrs
        growthRate = shortTermGrowthRate

        for year in range(10):
            if (year >= 5):
                growthRate = longTermGrowthRate
            projection = round(num * (1 + growthRate), 2)
            object[year + 1] = projection
            num = projection

    # Load the EPS and Dividned projection objects
    getProjections(epsProjections, eps,
                   shortTermEPSgrowth, longTermEPSgrowth)
    getProjections(dividendProjections, dividend,
                   shortTermDividendGrowth, longTermDividendGrowth)

    # Calculations from company financials
    salePrice = round(epsProjections[10] * PEatSale, 2)
    dividendYieldAtSale = round((dividendProjections[10] / salePrice * 100), 2)
    sumOfReinvestedDividends = getSumOfReinvestedDividends()
    totalValueAtSale = round(salePrice + sumOfReinvestedDividends, 2)
    buyPrice = round(totalValueAtSale / pow((1 + targetRateOfReturn), 10), 2)

    print("SIMPLE MODEL")
    print(name)
    print("Sale Price in 10 Years: $", salePrice)
    print("Dividend Yield at Sale: ", dividendYieldAtSale, "%")
    print("Sum of Reinvested Dividends: $", sumOfReinvestedDividends)
    print("Total Value at Sale: $", totalValueAtSale)
    print("Buy Below: $", buyPrice)
    print()

    epsProjections.clear()
    dividendProjections.clear()


def detailedModel():

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

    # Load the EPS and Dividend projection objects
    getProjections(epsProjections, eps, epsGrowthRate)
    getProjections(dividendProjections, dividend, dividendGrowthRate)

    # Calculations
    salePrice = round((epsProjections[10] * PEatSale), 2)

    dividendYieldAtSale = round((dividendProjections[10] / salePrice * 100), 2)

    sumOfReinvestedDividends = getSumOfReinvestedDividends()

    totalValueAtSale = round(salePrice + sumOfReinvestedDividends, 2)

    buyPrice = round(totalValueAtSale / pow((1 + targetRateOfReturn), 10), 2)

    print("DETAILED MODEL")
    print(name)
    print("Sale Price In 10 Years: $", salePrice)
    print("Dividend Yield at Sale: ", dividendYieldAtSale, "%")
    print("Sum of Reinvested Dividends: $", sumOfReinvestedDividends)
    print("Total Value at Sale: $", totalValueAtSale)
    print("Buy Below: $", buyPrice)
    print()

    epsProjections.clear()
    dividendProjections.clear()


def grahamLynchModel():
    grahamFairValue = round(
        (eps * (8.5 + 2 * (longTermGrowthRate * 100))), 2)

    adjGrahamFairValue = round(
        grahamFairValue * (4.4 / (corporateAAABondYield * 100)), 2)

    dividendAdjPEGratio = round((price / eps) /
                                ((longTermGrowthRate * 100) +
                                 (dividend * 100)), 2)

    print("GRAHAM LYNCH MODEL")
    print(name)
    print("Graham Fair Value: $", grahamFairValue)
    print("GFV adjusted: $", adjGrahamFairValue)
    print("Dividend Adjusted PEG Ratio: ", dividendAdjPEGratio)
    print()


grahamLynchModel()
detailedModel()
simpleModel()
