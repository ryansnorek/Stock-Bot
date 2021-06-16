# GRAHAM AND LYNCH FORMULAS
import math
from variables import eps, dividend, price, longTermGrowthRate, corporateAAABondYield

grahamFairValue = round(
    (eps * (8.5 + 2 * (longTermGrowthRate * 100))), 2)

adjGrahamFairValue = round(
    grahamFairValue * (4.4 / (corporateAAABondYield * 100)), 2)

dividendAdjPEGratio = round((price / eps) /
                            ((longTermGrowthRate * 100) +
                             (dividend * 100)), 2)

print("GRAHAM LYNCH MODEL")
print("Graham Fair Value: $", grahamFairValue)
print("GFV [adjusted for interest rates]: $", adjGrahamFairValue)
print("Dividend Adjusted PEG Ratio: ", dividendAdjPEGratio)
