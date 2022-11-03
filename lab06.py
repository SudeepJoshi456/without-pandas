database = []
with open("input.csv","r") as f:
    f.readline()
    for i in f:
        linelist = i.strip()
        linelist = linelist.split(",")
        prices = []
        prices.append(float(linelist[8]))
        prices.append(float(linelist[9]))
        prices.append(float(linelist[10]))
        people = {"FirstName":linelist[0],
        "MiddleInitial":linelist[1],
        "LastName":linelist[2],
        "StreetAddress":linelist[3],
        "City":linelist[4],
        "State":linelist[5],
        "ZipCode":linelist[6],
        "Box":linelist[7],
        "prices":prices}
        
        database.append(people)

    for j in range(5):
        box = database[j]["Box"]
        if box.lower()=="a":
            database[j]["prices"]=database[j]["prices"][0]
            print(f"""{database[j]["FirstName"]} {database[j]["MiddleInitial"]} {database[j]["LastName"]}\n{database[j]["StreetAddress"]} {database[j]["City"]}, {database[j]["State"]} {database[j]["ZipCode"]}\n${database[j]["prices"]}\n""")
        elif box.lower()=="b":
            database[j]["prices"]=database[j]["prices"][1]
            print(f"""{database[j]["FirstName"]} {database[j]["MiddleInitial"]} {database[j]["LastName"]}\n{database[j]["StreetAddress"]} {database[j]["City"]}, {database[j]["State"]} {database[j]["ZipCode"]}\n${database[j]["prices"]}\n""")
            
        elif box.lower()=="c":
            database[j]["prices"]=database[j]["prices"][2]
            print(f"""{database[j]["FirstName"]} {database[j]["MiddleInitial"]} {database[j]["LastName"]}\n{database[j]["StreetAddress"]} {database[j]["City"]}, {database[j]["State"]} {database[j]["ZipCode"]}\n${database[j]["prices"]}\n""")
            



        



