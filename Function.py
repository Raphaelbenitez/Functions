
def calculateInclPrice(exclPrice, vaTax):
  inclprice = exclPrice + (exclPrice* vaTax)
  return inclprice

def userInputExcelTaxRate():
        excelprice = float(input)("Enter exclPrice"))
        vatTax = float (input)( "Enter tax rate"))
        return calculateInclPrice(exclPrice,vatTax)
  
  
print(userInputExclTaxrate())


