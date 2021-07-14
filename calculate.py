
def calculateAge(currentYear,birthyear):

 age=currentYear-birthyear
 return age

def userInputCurrentYearBirthyear():
     currentYear=int(input("Enter currentYear"))
     birthYear=int(input("Enter birthyear"))
     return calculateAge(currentYear, birthYear)

print (userInputCurrentYearBirthyear())