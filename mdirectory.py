import csv
from prettytable import PrettyTable



# Import Pretty tabel, import csv

# Class of directory,load function to modify in it

# 1. Show Directory
# 2. Load csv
# 3. Add entry
# 4. Remove entry based on PK(Roll number, Course Name, Semester, Exam Type)
# 5. Remove entry based on index
# 6. Update entry based on PK(Roll number, Course Name, Semester, Exam Type)
# 7. Update entry based on index
# 8. Search entry
# 9. Store directory
# 10. Exit


class MarksDirectory:
    file_path=" "
    def __init__(self): #for each object created of class
        self.entries = []

    def show_directory(self):#printing done
        # Create a PrettyTable
        table = PrettyTable(self.entries[0].keys())

        # Add rows to the table
        for row in self.entries:
            table.add_row(row.values())

        # Print the table
        print(table)
        # for entry in self.entries:
        #     print(entry)

    def load_csv(self, filepath):#done
        # Input CSV file
        self.file_path=filepath
        input_file = filepath

        # Read data from CSV
        data = []
        with open(input_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)

        self.entries=data
        # with open(file_path, mode='r') as file:
        #     reader = csv.DictReader(file)
        #     self.entries = [dict(row) for row in reader]
    
    def make_entry(self): #done
        roll_number = str(int(input("Enter Roll Number: ")))
        flag=0
        for entry in self.entries:
            if entry["Roll Number"] == str(roll_number):
                flag=1
                break  ##duplicate rollnum
        
        if(flag):
            print("Please enter unique roll number  :(")
            return {} #emplty




        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        course_name = input("Enter Course Name: ")
        semester = input("Enter Semester: ")
        exam_type = input("Enter Exam Type: ")
        total_marks = str(int(input("Enter Total Marks: ")))
       
        scored_marks =str(int(input("Enter Scored Marks: ")))
        
        currentry = {
            "First Name": first_name,
            "Last Name": last_name,
            "Roll Number": roll_number,
            "Course Name": course_name,
            "Semester": semester,
            "Exam Type": exam_type,
            "Total Marks": total_marks,
            "Scored Marks": scored_marks
        }
        print("Entry created.")
        return currentry
        # self.entries.append(currentry)      

   
    def add_entry(self): #done
        temp=self.make_entry()
        if(len(temp)!=0):        #returns empty if repeated roll num
            self.entries.append(temp)

    def remove_enty_byroll(self): #done
        roll= int(input("Enter entry's roll num to delete:   "))
        flag=1
        for entry in self.entries:
            if entry["Roll Number"] == str(roll):
                
                self.entries.remove(entry)
                flag=0
                #break  ##as there is one entry
        
        if(flag):
            print(f"Roll {roll} not found")
        

    def remove_entry_by_index(self):  #done
        index=int(input("Enter 0 based index:   "))
        if 0 <= index < len(self.entries):
            del self.entries[index]
        else:
            print("Incorrect index")

    def update_marksby_roll(self): #done
        roll= int(input("Enter entry's roll num to Update marks:  "))
        for entry in self.entries:
            if entry["Roll Number"] == str(roll):
                
                entry["Total Marks"]= str(int(input("Enter updated Total marks:  ")))
                entry["Scored Marks"]=str(int(input("Enter updated Scored marks:  ")))
                break  ##as there is one entry
        
    def update_entry_by_index(self ): #done #takes index and new_entry
        index=int(input("Enter 0 based index:     "))
        if 0 <= index < len(self.entries):
            
            temp=self.make_entry()
            if(len(temp)!=0):        #returns empty if repeated roll num
                self.entries[index] = temp

    def search_entry(self): ##students enrolled in same course
        course=(input("Enter course name:  "))
        table = PrettyTable(self.entries[0].keys())
        for entry in self.entries:
            if entry["Course Name"] == course:
                    
                table.add_row(entry.values())

        # Print the table
        print(table)

    def update_csv(self): #done update file csv
        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.entries[0].keys())
            writer.writeheader() #write header
            writer.writerows(self.entries) #write data
    
    def store_directory(self,diff_path): #done to different file save csv
        with open(diff_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.entries[0].keys())
            writer.writeheader() #write header
            writer.writerows(self.entries) #write data
    

# Example usage:
marks_directory = MarksDirectory()
import_path=input("Enter Path of CSV file_name.csv:  ")#"employee_data.csv"
marks_directory.load_csv(import_path) ## later take from input file name



common="""
1. Show Directory
2. Update csv with current data
3. Add entry
4. Remove entry based on Roll number
5. Remove entry based on index
6. Update marks based on roll
7. Update entry based on index
8. Search entry based on same Course name
9. Store directory in other file
10. Exit"""

flag =True
while(flag==True):
    print(common)
    op= int(input("Enter option:   "))
    if(op==1):

        marks_directory.show_directory()

    if(op==2):

        marks_directory.update_csv()  #stores current data in main csv file        
        marks_directory.load_csv(import_path)    #take refreshed contents from csv file

    if(op==3):
        
        marks_directory.add_entry()

    if(op==4):

        marks_directory.remove_enty_byroll()

    if(op==5):

        marks_directory.remove_entry_by_index()

        print(5)
    if(op==6):

        marks_directory.update_marksby_roll()


    if(op==7):

        marks_directory.update_entry_by_index()


    if(op==8):
        
        marks_directory.search_entry()

        print(8)
    if(op==9):
        tostore=input("File name, to copy data:   ")
        marks_directory.store_directory(tostore)
    

    if(op==10):
        marks_directory.update_csv() #before exiting store latest data in ongoing file
        print("Exiting: stored latest data in csv file :)")
        exit()
        