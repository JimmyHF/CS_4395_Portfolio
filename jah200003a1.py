import sys
import os
import re
import pickle


class Person:
    # Conceptual class for employees
    last = ""
    first = ""
    mi = ""
    pid = ""
    phone = ""

    def __init__(self, last, first, mi, pid, phone):
        # Constructor with all fields assigned
        self.last = last
        self.first = first
        self.mi = mi
        self.pid = pid
        self.phone = phone

    def display(self):
        # Print formatted employee information
        print("Employee ID: " + self.pid)
        print("\t" + self.first + " " + self.mi + ". " + self.last)
        print("\t" + self.phone)


def read_data(file_path):
    # Reads csv file from specified file path, returns file text
    with open(os.path.join(os.getcwd(), file_path), "r") as f:
        text = f.read()
    return text


def process_data(file_text):
    # Processes text data, returns a dictionary of Person objects indexed by pid
    person_dict = {}
    lines = file_text.split("\n")
    lines.remove(lines[0])
    for text in lines:
        person = text.split(",")
        last = person[0].title()
        first = person[1].title()
        if len(person[2]) > 0:
            mi = person[2][0].title()
        else:
            mi = "X"
        pid = person[3]
        while not re.fullmatch("[A-Z]{2}\d{4}", pid):
            print("ID invalid: " + person[3])
            print("ID is two uppercase letters followed by 4 digits")
            pid = input("Please enter a valid ID: ")
        phone = person[4]
        while not re.fullmatch("\d{3}-\d{3}-\d{4}", phone):
            print("Phone " + phone + " is invalid")
            print("Enter phone number in form 123-456-7890")
            phone = input("Enter phone number: ")
        this_person = Person(last, first, mi, pid, phone)
        if person_dict.get(pid):
            print("Error: Duplicate ID")
        else:
            person_dict[pid] = this_person
    return person_dict


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please enter a data file path')
    else:
        filePath = sys.argv[1]
        fileText = read_data(filePath)
        personDict = process_data(fileText)
        pickle.dump(personDict, open("dict.p", "wb"))
        pickleDict = pickle.load(open("dict.p", "rb"))
        print("\nEmployee List: ")
        for entry in pickleDict:
            pickleDict.get(entry).display()
