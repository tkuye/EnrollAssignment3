


from enrollStudent import PrintColour, EnrollTable, StudentNode, PriorityQueue

def lineSplitter(line) -> tuple:
    
    """Helper fucntion to split the line into the needed data."""
    pc = PrintColour()
    try:
        assert len(line.split(" ")) == 4, "Not a valid Line!"
        lines = line.split(" ")
        studentId = lines[0]
        faculty = lines[1]
        fname = lines[2]
        lname = lines[3].strip()
        return (studentId, faculty, fname, lname)
    except IndexError:
        return (None, None, None, None)
    except AssertionError as e:
        pc.printout(e.args[0], color="RED")
        return (None, None, None, None)

def enrollStudentData(file, enrollTable:EnrollTable, queue:PriorityQueue) -> None:
    

    """Helper method to enroll a student in a class or if it is full then add to queue"""
    pc = PrintColour()
    assert isinstance(enrollTable, EnrollTable), "Not an EnrollTable."
    assert isinstance(queue, PriorityQueue), "Not a PriorityQueue"
    for line in file.readlines():
        studentId, faculty, fname, lname = lineSplitter(line)
        if studentId is None:
            pass
        else:
            node = StudentNode(studentId, faculty, fname, lname)
            try:
                enrollTable.insert(node)
            except AssertionError as e:
                pc.printout(e.args[0], color="RED")
                try:
                    if enrollTable.isFull():
                        queue.enqueue(node)
                except AssertionError:
                    pc.printout(f"Cannot insert student {fname} {lname} (ID:{studentId}) as they are already on the waitlist!", color="RED")


def dropStudent(file, enrollTable:EnrollTable, queue:PriorityQueue) -> None:
    
    """This helper method reads in a file and drops students from the class with a given ID."""
    pc = PrintColour()
    assert isinstance(enrollTable, EnrollTable), "Not an EnrollTable."
    assert isinstance(queue, PriorityQueue), "Not a PriorityQueue"
    for line in file.readlines():
        studentId, faculty, fname, lname = lineSplitter(line)
        if studentId is None:
            pass
        else:
            student = enrollTable.remove(studentId)
            if student is False:
                pc.printout(f"WARNING:There is no student {fname} {lname}, (ID: {studentId}) currently enrolled and cannot be dropped!", color="RED")
            else:
                try:
                    if not queue.isEmpty():
                        item = queue.dequeue()

                        item.setNext(None)
                        item.setPrev(None)
                        enrollTable.insert(item)
                except AssertionError as e:
                    pc.printout(e.args[0], color="RED")
    
def main():
    
    """THE MAIN FUNCTION\n
    Used for the full and total implementation of the classes and code for
    this project.
    """
    enrolled = "enrolled.txt"
    waitlist = "waitlist.txt"
    LOGOTOP = """  
                 ________               ________       ________
                |           |\      |  |        \     /        \    |           |
                |           | \     |  |         |   |    __    |   |           |
                |________   |  \    |  |________/    |   /  \   |   |           |
                |           |   \   |  |        \    |   \__/   |   |           |
                |           |    \  |  |         \   |          |   |           |
                |________   |      \|  |          \   \_______ /    |________   |________"""

    LOGOBOTTOM="""   
                                    .       _________     __________
                                   /|               /    |
                                  / |              /     |
                                 /  |             /      |_________
                                /   |            /                 |
                                    |           /                  |   
                                ____|____      /         __________|
                                
                                """     
    linebreak = "-"*75
    noFile = "There is no file with that name please try again."
    enrollTable = EnrollTable(51)
    queue = PriorityQueue()
    pc = PrintColour()
    
    entries = ["R", "D", "Q"]
    running = True
    pc.printout(LOGOTOP, color="YELLOW")
    pc.printout(LOGOBOTTOM, color="YELLOW")
    pc.printout("Author: Tosin Kuye\n", color="YELLOW")
    inputText = "Hello! Please enter one of the following: "
    cursor = "::> "
    goodbye = "Thank you for joining the program, have a nice day!"
    pc.printout(inputText, color="CYAN")
    try:
        while running:
            pc.printout("R - To register for a course", color="WHITE")
            pc.printout("D - To drop a course", color="WHITE")
            pc.printout("Q - To exit the program", color="WHITE")
            inputs = pc.stdinput(cursor, color="YELLOW")
            if inputs not in entries:
                pc.printout("That is not a valid input! Try again...", color="RED")
            elif inputs == "Q":
                pc.printout(goodbye, color="CYAN")
                running = False
            elif inputs == "R":
                pc.printout("Please enter the file name containing the students you with to register:", color="BLUE")
                fileNameInvalid = True
                while fileNameInvalid:
                    file = pc.stdinput(cursor, color="YELLOW")
                    try:
                        with open(file, "r") as f:
                            try:
                                enrollStudentData(f, enrollTable, queue)
                            except AssertionError as e:
                                pc.printout(e.args[0], color="RED")
                            pc.printout("The file's contents has been successfully added to the enrollment table.\nHere are the contents in the table:", color="GREEN")
                            pc.printout(enrollTable, bold=False, color="MAGENTA")
                            f.close()

                        with open(enrolled, "w") as f:
                            f.write(str(enrollTable))
                            f.close()
                        pc.printout("The waitlist currently contains the following: ", color="GREEN")
                        pc.printout(queue, bold=False, color="MAGENTA")
                        with open(waitlist, "w") as f:
                            f.write(str(queue))
                            f.close()

                        pc.printout("The contents of the enrollment table and the waitlist\nhave been save to files named 'enrolled.txt' and 'waitlist.txt' respectively.", color="WHITE")
                        pc.printout(linebreak, color="WHITE")
                        fileNameInvalid = False
                    except FileNotFoundError:
                        pc.printout(noFile, color="RED")

            elif inputs == "D":
                pc.printout("Please enter the file name for students you wish to drop.", color="BLUE")
                fileNameInvalid = True
                while fileNameInvalid:
                    file = pc.stdinput(cursor, color="YELLOW")
                    try:
                        with open(file, "r") as f:
                            try:
                                dropStudent(f, enrollTable, queue)
                            except AssertionError as e:
                                pc.printout(e.args[0], color="RED")

                            f.close()
                        with open(waitlist, "a") as f:
                            f.write(str(queue))
                            f.close()
                        pc.printout("After updating the contents of the waitlist, here is what it looks like now:", color="GREEN")
                        pc.printout(str(queue), bold=False, color="MAGENTA")
                        pc.printout("The updated waitlist has been appended to file 'waitlist.txt'.", color="WHITE")
                        pc.printout(linebreak)
                        fileNameInvalid = False
                    except FileNotFoundError:
                        pc.printout(noFile, color="RED")
    except KeyboardInterrupt:
        pc.printout('\n' +goodbye, color="CYAN")



if __name__ == '__main__':
    main()

