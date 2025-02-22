number_of_id = int(input())
ids = []
for i in range(number_of_id) :
    id = input().strip()
    ids.append(id)

numeric = []
upper =[]
for id in ids :
    if len(id) != 10 or len(set(id)) != 10 or id.isalnum() == False :
      print("Invalid")
      continue

    else :
        
      for i in id :
          if i.isupper() :
              upper.append(i)
          elif i.isnumeric() :
              numeric.append(i)

    if len(upper) >= 2 and len(numeric) >= 3 :
      print("Valid")
    else :
      print ("Invalid")
