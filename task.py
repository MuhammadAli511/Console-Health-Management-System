def getAllPatientRecord():
    file1 = open("data.txt","r") # File Reading
    for line in file1:
        line = line.replace('\n','') # Replacing end line with empty string
        print(line.replace(',','\t')) # Replacing commas with tabs
    cont = input("Press Enter key to continue : ")
    while (cont != ""):
        cont = input("Press Enter key to continue : ")
    return

def getPatient(patientID):
    file1 = open("data.txt","r") # File Reading
    counter = 0
    heading = ""
    bool1 = False
    for line in file1:
        line = line.replace('\n','')
        line2 = line.split(',') # Splitting string based on comma and putting in List
        if (line2[0] == patientID):
            bool1 = True
            print("\n"+heading)
            print(line.replace(',','\t')+"\n")
        if (counter == 0):
            heading = line.replace(',','\t')
        counter+=1
    if (bool1 == False):
        print("Error: Invalid Patient")
    cont = input("Press Enter key to continue : ")
    while (cont != ""):
        cont = input("Press Enter key to continue : ")
    return


def getWeight(weight):
    bool1 = True
    if (float(weight) < 0):
        bool1 = False
        print("Error: Invalid weight")
    if (bool1 == True):
        file1 = open("data.txt","r") # File Reading
        heading = ""
        counter = 0
        for line in file1:
            line = line.replace('\n','')
            line2 = line.split(',')
            if (counter == 0):
                line3 = line.split(',')
                line3.insert(4,"P(%)")
                for word in line3:
                    heading += str(word) + "\t"
            
            elif (float(line2[2]) <= float(weight)):
                print("\n"+heading)
                percent = (float(line2[2]) - float(line2[3])) / (float(line2[3]))
                percent *= 100
                percent = float("{:.3f}".format(percent))
                line2.insert(4,percent)
                final = ""
                for word in line2:
                    final += str(word) + "\t"
                print(final)
            counter+=1
    cont = input("Press Enter key to continue : ")
    while (cont != ""):
        cont = input("Press Enter key to continue : ")
    return


def update(patientID,weight):
    bool3 = False
    avgWeight = float(input("Enter average weight : "))
    visits = int(input("Enter the patients number of visits : "))
    if int(patientID) <= 0:
        print("Error: Invalid Patient ID ")
        bool3 = True
    if float(weight) <= 0:
        print("Error: Invalid Weight ")
        bool3 = True
    if avgWeight <= 0:
        print("Error: Invalid Average Weight")
        bool3 = True
    if visits <= 0:
        print("Error: Invalid Visits")
        bool3 = True

    if (bool3 == True):
        cont = input("Press Enter key to continue : ")
        while (cont != ""):
            cont = input("Press Enter key to continue : ")
        return


        
    bool1 = False
    file1 = open("data.txt","r") # File Reading
    final = ""
    name = ""
    for line in file1:
        if (patientID not in line):
            final += line
        else:
            bool1 = True
            line2 = line.split(',')
            name = line2[1]

    file1.close()
    if (bool1 == False):
        print("Patient Doesn't Exist")
        cont = input("Press Enter key to continue : ")
        while (cont != ""):
            cont = input("Press Enter key to continue : ")
        return
    else:
        navgWeight = float ( (float(weight) + float(avgWeight) * visits)/(visits+1) )
        nVisits = visits + 1
        final += patientID + "," + name + "," + str(weight) + "," + str(navgWeight) + "," + str(nVisits) + "\n"
        file2 = open("data.txt","w") # File Writting
        file2.write(final)
        file2.close()
        print("Patient's information has been updated")
        cont = input("Press Enter key to continue : ")
        while (cont != ""):
            cont = input("Press Enter key to continue : ")
        return


def addPatient(name,patientID):
    bool1 = True
    file1 = open("data.txt","r") # File Reading
    for line in file1:
        if (patientID in line):
            bool1 = False
    file1.close()
    if (bool1 == False):
        print("Patient Already Exists")
        cont = input("Press Enter key to continue : ")
        while (cont != ""):
            cont = input("Press Enter key to continue : ")
        return
    elif (bool1 == True):
        weight = input("Enter weight : ")
        final = patientID + "," + name + "," + weight + "," + weight + ",1\n"
        file2 = open("data.txt","a") # File Writting with append functionality
        file2.write(final)
        file2.close()
        print("Patient Added .")
        cont = input("Press Enter key to continue : ")
        while (cont != ""):
            cont = input("Press Enter key to continue : ")
        return
        


def deletePatient(patientID):
    file1 = open("data.txt","r") # File Reading
    bool1 = False
    final = ""
    for line in file1:
        if (patientID in line):
            bool1 = True
        else:
            final += line
    file1.close()
    if (bool1 == False):
        print("Patient Doesn't Exist")
        cont = input("Press Enter key to continue : ")
        while (cont != ""):
            cont = input("Press Enter key to continue : ")
        return
    else:
        file2 = open("data.txt","w") # File Writting
        file2.write(final)
        file2.close()
        print("Patient Deleted .")
        cont = input("Press Enter key to continue : ")
        while (cont != ""):
            cont = input("Press Enter key to continue : ")
        return


def main():
    while(1):
        # Menu
        print("1. Display all Patient Record")
        print("2. Display the Record of a particular Patient")
        print("3. Display all Patient Weight")
        print("4. Update Patient")
        print("5. Add New Patient")
        print("6. Delete Patient")
        print("0. Exit")
        # Menu Choice input
        choice = int(input("Please select your choice : "))
        # Conditions for all menu options
        if (choice == 0):
            break
        if (choice == 1):
            getAllPatientRecord()
        if (choice == 2):
            patientId = input("Enter Patient ID : ")
            getPatient(patientId)
        if (choice == 3):
            maxWeight = float(input("Please enter max. weight (Kg): "))
            getWeight(maxWeight)
        if (choice == 4):
            patientId = input("Enter Patient ID : ")
            weight = float(input("Enter weight : "))
            update(patientId,weight)
        if (choice == 5):
            name = input("Enter name : ")
            patientId = input("Enter Patient ID : ")
            addPatient(name,patientId)
        if (choice == 6):
            patientId = input("Enter Patient ID : ")
            deletePatient(patientId)
        else: # Invalid Choice
            print("Invalid Choice . ")
            print("Try Again")



if __name__ == "__main__":
    main()