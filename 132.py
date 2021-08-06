prov={"A":"Newfoundland","B":"Nova Scotia","C":"Prince Edward Island",\
      "E":"New Brunswick","G":"Quebec","H":"Quebec","J":"Quebec","K":"Ontario",\
      "L":"Ontario","M":"Ontario","N":"Ontario","P":"Ontario","R":"Manitoba",\
      "S":"Saskatchewan","T":"Alberta","V":"British Columbia",\
      "X":"Nunavut or Northwest Territories","Y":"Yukon"}

postal = input("Postal code:")
if postal[0] not in prov.keys():
    print("Invalid postal code")
else:
    if postal[1]==0:
        print(f'The postal code is for an rural address in {prov[postal[0]]}')
    else:
        print(f'The postal code is for an urban address in {prov[postal[0]]}')
