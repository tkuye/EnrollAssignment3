
##### Author: Tosin Kuye
##### Collaborators:None
##### References: programiz.com, realpython.com, python.org

################# NOTE TO MARKER####################
#### I used the python unit test module but since modules aren't allowed I didn't 
#### include the results here so my tests in this file aren't as robust!!!

class FailError(Exception):
    """Exeption used for the failure of one or more tests."""
    
class TestCase:
    """Test class to emulate the python unit test module\n
    Must start all tests with 'test' to work"""
    
    def __init__(self):
        
        self.pc = PrintColour()
        self.fails = 0
        
        
    def assertEqual(self, arg1, arg2) -> bool:
        """Asserts that arg1 and arg2 are equal."""
        if arg1 != arg2:
           raise FailError(arg1, arg2)
        
    
    def assertTrue(self, args)-> bool:
        """Asserts that arguments as a statement is True"""

        if args is not True:
            raise FailError(args)
    
    def assertFalse(self, args)-> None:
        """Asserts that arguments as a statement is False"""
        if args is not False:
            raise FailError(args)
    
    def __testCases(self):
        """Method to test all the cases present."""
        for item in self.__dir__():
            if item.startswith("test"):
                caller = getattr(self, item)
                if callable(caller):
                    caller()
                   
                        
        
    def main(self):
        """The test class main function"""
        try:
            self.__testCases()
            if self.fails != 0:
                self.pc.printout("FAILS: {}".format(self.fails), color="RED")
            else:
                self.pc.printout("ALL PASSED!", color="GREEN")
        except FailError as f:
            self.pc.printout(f"FAIL: {f.with_traceback(None)}", color="RED")
        except Exception as e:
            
            self.pc.printout(f"FAIL: {e.args[0]}", color="RED")

class PrintColour:

    """Class used to add some color and bold to the boring terminal!"""
    def __init__(self):
        self.RESET="\u001b[0m"
        self.BOLD="\u001b[1m"
        self.colors = {
        "BLACK":"\u001b[30m",
        "RED":"\u001b[31m",
        "GREEN":"\u001b[32m",
        "YELLOW":"\u001b[33m",
        "BLUE":"\u001b[34m",
        "MAGENTA":"\u001b[35m",
        "CYAN":"\u001b[36m",
        "WHITE":"\u001b[37m",
        }
        
    def printout(self, *inputs, color:str="WHITE", bold:bool=True) -> None:
        """Method used to printout text to the terminal with
        with specified colors and bold. Returns None and all colors
        must be in capital letters."""
        assert color in self.colors.keys(), "Not a valid color"
        if bold:
            for i in inputs:
                print(u"{0}{1}{2}{3}".format(self.colors.get(color), self.BOLD, i, self.RESET), end=" ")
            print()
        else:
            for i in inputs:
                print(u"{0}{1}{2}".format(self.colors.get(color), i, self.RESET), end=" ")
            print()

    def stdinput(self, inputs, color:str="WHITE", bold:bool=True) -> str:
        """Method used for the input of the terminal with specified colors
        returns a string from the input result."""
        assert color in self.colors.keys(), "Not a valid color"
        response = ""
        if bold:
            response = input(u"{0}{1}{2}{3}".format(self.colors.get(color), self.BOLD, inputs, self.RESET))
        else:
            response = input(u"{0}{1}{2}".format(self.colors.get(color), inputs, self.RESET))
        return response
    



class StudentNode:
    """The node class for a student within a falculty """
    def __init__(self, sid:str, faculty:str, first:str, last:str) -> None:
        """The initialization method for the student node class"""
        assert len(sid) == 6, "Student Id is not valid."
        assert len(faculty) == 3, "Not a valid Faculty."
        assert sid.isnumeric(), "Student ID must be a valid integer."
        
        assert " " not in first, "Not whitespace allowed in names"
        assert " " not in last, "Not whitespace allowed in names"

        self.priority = {"SCI":4, "ENG":3, "BUS":2, "ART":1, "EDU":0}
        assert faculty in self.priority, "Not an available Faculty."
        
        
        self.id = sid
        self.faculty = faculty
        self.first = first
        self.last = last
        # Linked list implementation
        self.next = None
        self.prev = None
    
    def setID(self, sid:str) -> None:
        """Set the student id to a given id"""
        try:
            assert len(sid) == 6, "Student ID must be 6 characters long."
            assert sid.isnumeric(), "Student ID must be a valid integer."
            int(sid)
        except ValueError:
            print("Student ID must be a valid integer in string format")
        except AssertionError as e:
            print(e.args[0]) 
        else:
            self.id = sid
    
    def setFaculty(self, faculty:str) -> None:
        """Sets the faculty abbreviation to the given faculty."""
        assert len(faculty) == 3, "Faculty must be an abbreviation of 3 characters."
        assert type(faculty) == str, "Must be a string type!"
        for c in faculty:
            assert 122 >= ord(c) >= 97 or 90 >= ord(c) >= 65, "Must be a valid alphabet character!" 
        faculty = faculty.upper()
        self.faculty = faculty
    
    def setFirstName(self, first:str) -> None:
        assert " " not in first, "Not whitespace allowed in names"
        
        """Sets the student's first name to the given first name."""
        self.first = first
    
    def setLastName(self, last:str) -> None:
        assert " " not in last, "Not whitespace allowed in names"
        """Sets the student's last name to the given last name."""
        self.last = last
    
    def setNext(self, snext) -> None:
        """Set's the next as the next node."""
        self.next = snext
        

    def setPrev(self, sprev) -> None:
        """Set's previous as the previous node."""
        self.prev = sprev
        
    
    def getID(self) -> str:
        """returns the student's id as a string """
        return self.id
    
    def getFac(self) -> str:
        """returns the student's faculty abbretiation as a string"""
        return self.faculty
    
    def getFirstName(self) -> str:
        """returns a string of the student's first name"""  
        return self.first
    
    def getLastName(self) -> str:
        """ returns a string of the student's last name"""
        return self.last
    
    def getNext(self):
        """ returns the next node"""
        return self.next
    
    def getPrev(self):
        """returns the previous node"""
        return self.prev


class EnrollTable:
    """class implemenation of the table of the classes for the students"""
    
    def __init__(self, capacity:int) -> None:
        """The initialization method for the table class."""
        self.MAX_CAPACITY = 51
        self.capacity = capacity
        assert isinstance(capacity, int), "Not a valid capacity!"
        assert capacity <= self.MAX_CAPACITY, "Capacity greater than maximum allowed capacity."
        self.enrollTable = [None for i in range(capacity)]
        self.tableSize = 0


    def cmputIndex(self, studentID:str) -> int:
        """This method will take a student id as a string parameter and
        returns an integer as to where the student node is inserted."""
        assert len(studentID) == 6, "ID must be 6 characters long"
        # type conversions to integers
        firstNum = int(studentID[:2])
        secondNum = int(studentID[2:4])
        thirdNum = int(studentID[4:])
        thirdNum = thirdNum*thirdNum

        IndexNum = (firstNum + secondNum + thirdNum) % self.capacity

        return IndexNum

    def __insertBegin(self, item:StudentNode, temp:StudentNode) -> StudentNode:
        """Helper method to insert at the beginning of the node returns the first node item."""
        item.setNext(temp)
        temp.setPrev(item)
        return item


    
    def __getEnd(self, temp:StudentNode) -> StudentNode:
        """Helper method that travserses  a linked list and returns the last student node item"""
        while temp.getNext() is not None:
            temp = temp.getNext()
        return temp

        
    def insert(self, item:StudentNode) -> None:
        pc = PrintColour()
        """Inserts a given item, a student node object into the enrollment table. """
        assert self.tableSize < self.capacity, "Table is full cannot insert."
        assert isinstance(item, StudentNode), "Not a student node, cannot insert."
        assert self.isEnrolled(item.getID()) is False, "Already enrolled cannot enroll again!"
        index = self.cmputIndex(item.getID())
        

        end = None
        if self.enrollTable[index] is not None:
            # If its not none get the item at the end 
            end = self.__getEnd(self.enrollTable[index])

        if self.enrollTable[index] is None:
            self.enrollTable[index] = item
            self.incTable()
        
        elif int(self.enrollTable[index].getID()) > int(item.getID()):
            # Must go at the front
            self.enrollTable[index] = self.__insertBegin(item, self.enrollTable[index])
            self.incTable()
        
        elif int(end.getID()) < int(item.getID()):
            # Must go at the end
            end.setNext(item)
            item.setPrev(end)
            self.incTable()
        else:
            # Traversal time
            indexList = self.enrollTable[index]
            temp = indexList.getNext()
            prev = indexList
            itemId = int(item.getID())
            found = False

            while temp is not None and not found:
                # Must be in between if we get to this point
                if itemId < int(temp.getID()) and itemId > int(prev.getID()):
                    item.setNext(temp)
                    temp.setPrev(item)
                    prev.setNext(item)
                    item.setPrev(prev)
                    found = True
                    self.incTable()
                else:
                    temp = temp.getNext()
                    prev = prev.getNext()
        
        
    def isFull(self):
        return self.capacity == self.tableSize
       
        
    def incTable(self) -> None:
        """Increments the table size by one."""
        self.tableSize += 1

    def decTable(self) -> None:
        """Decrements table size by one"""
        self.tableSize -= 1

    def remove(self, studentID:str) -> bool:
        pc = PrintColour()
        """Removes student from the enrollment table"""
        assert len(studentID) == 6, "Not a valid student ID"
        assert studentID.isnumeric(), "Student ID must be numeric"
        index = self.cmputIndex(studentID)
        temp = self.enrollTable[index]

        removed = False

        if temp is None:
            return removed
        # check for 1 element
        elif temp.getNext() is None:
            self.enrollTable[index] = None
            self.decTable()
            removed = True
        else:
            
            while temp is not None and not removed:
                
                if temp.getID() == studentID:
                # must be at location if this is true
                # first element
                    if temp.getPrev() is None:
                        
                        self.enrollTable[index] = temp.getNext()
                        self.enrollTable[index].setPrev(None)
                        removed = True
                        self.decTable()
                # last element
                    elif temp.getNext() is None:
                        
                        prev = temp.getPrev()
                        
                        prev.setNext(None)
                        temp = None
                        self.decTable()
                        removed = True
                # In the middle somewhere
                    else:
                        
                        prev = temp.getPrev()
                        tnext = temp.getNext()
                        prev.setNext(tnext)

                        tnext.setPrev(prev)
                        temp = None
                        self.decTable()

                        removed = True

                else:
                    temp = temp.getNext()

        return removed


    def isEnrolled(self, studentID:str) -> bool:
        """This method determines if a student with the given id is enrolled."""
        assert len(studentID) == 6, "Not a valid student ID"
        assert studentID.isnumeric(), "Student ID must be numeric"
        index = self.cmputIndex(studentID)
        table = self.enrollTable[index]

        temp = table
        found = False
        while temp is not None and not found:
            if temp.getID() == studentID:
                found = True
            else:
                temp = temp.getNext()
        return found

    def size(self) -> int:
        
        """returns the size of the enrollment table."""
        return self.tableSize

    def isEmpty(self) -> bool:
        
        """Returns a bool to determine if the table is empty or not"""
        return self.tableSize == 0

    def __str__(self):
        """Returns a string implementation of the enrollment table. """
        printout = "["
        i = 0
        
        for i in range(len(self.enrollTable)):
            enrolledStudents = ""
            first = False
            table = self.enrollTable[i]
            while table is not None:
                if not first:
                    enrolledStudent = f"{i} : {table.getID()} {table.getFac()} {table.getFirstName()} {table.getLastName()}, "
                    first = True
                else:
                    enrolledStudent = f"{table.getID()} {table.getFac()} {table.getFirstName()} {table.getLastName()}, "
                table = table.getNext()
                enrolledStudents += enrolledStudent

            i += 1
            if enrolledStudents != "" and printout != "[":
                printout += "\n"

            printout += enrolledStudents
        
        printout = printout[:-2]
        printout += "]"

        if printout == "]": printout = "[]"
        return printout

class PriorityQueue:
    """A class implentation of a queue to put students on base on their priority."""
    def __init__(self):
        self.head = None
        self.tail = None
        self.priority = {"SCI":4, "ENG":3, "BUS":2, "ART":1, "EDU":0}
        self.qsize = 0
    
    def enqueue(self, item:StudentNode) -> None:
        # First check size
        assert self.__inQueue(item.getID()) is False, "Student is already in the queue cannot add."
        """Enqueues a new student node item to a postion in the queue based on its priority of faculty."""
        assert isinstance(item, StudentNode), "Not an instance of a StudentNode"
        assert item.getFac() in self.priority.keys(), "Not a valid faculty"
        if self.qsize == 0:

            self.head = item
            self.tail = item
            self.__incSize()
        else:
            # Must determine location position and priority number
            priority = self.priority.get(item.getFac())
            temp = self.head
            
            ### Keep moving forward until we reach the tail or we find a node with teh same priority
            while self.priority.get(temp.getFac()) < priority and temp != self.tail:
                temp = temp.getNext()

            if temp == self.head and temp == self.tail:
                # one element check
                if self.priority.get(temp.getFac()) < priority:
                    self.__setTail(item)
                else:
                    self.__setHead(item)

            elif temp == self.tail:
                # At the end so add to the end
                self.__setTail(item)
            elif temp == self.head:
                self.__setHead(item)
            else:
                tempPrev = temp.getPrev()
                item.setNext(temp)
                temp.setPrev(item)
                tempPrev.setNext(item)
                item.setPrev(tempPrev)
                self.__incSize()
        
    def __inQueue(self, studentID:str):
        """Helper method to determine if student is in the queue."""
        assert studentID.isnumeric(), "Student ID must be numeric"
        assert len(studentID) == 6, "Student ID must be 6 characters long"
        temp = self.head
        found = False
        while temp is not None and not found:
            if temp.getID() == studentID:
                found = True
            temp = temp.getNext()

        return found


    def __setHead(self, item:StudentNode) -> None:
        """Helper method to set the head of the queue to the new node"""
        assert isinstance(item,StudentNode), "item must be a StudentNode"
        temp = self.head
        item.setNext(temp)
        temp.setPrev(item)
        self.head = item
        self.__incSize()

    def __setTail(self, item:StudentNode) -> None:
        """Helper method to set the tail of the queue to the new node"""
        assert isinstance(item,StudentNode), "item must be a StudentNode"
        self.tail.setNext(item)
        item.setPrev(self.tail)
        self.tail = item
        self.__incSize()

    def dequeue(self) -> StudentNode:
        """Dequeue method for removing the last item at the tail."""
        assert self.qsize > 0, "Cannot dequeue an empty queue."
        if self.size() == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.__decSize()
            return temp
        curr = self.tail
        self.tail = curr.getPrev()
        self.tail.setNext(None)
        self.__decSize()
        return curr
    
    def size(self) -> int:
        """Returns the number of students on the queue."""
        return self.qsize

    def isEmpty(self) -> bool:
        return self.qsize == 0

    def __incSize(self) -> None:
        """Helper method used to increment size of the Queue"""
        self.qsize += 1

    def __decSize(self) -> None:
        """Helper method used to decrement size of the Queue"""
        self.qsize -= 1

    def __str__(self) -> str:
        """A string representation of the PriorityQueue class"""
        string = "["

        temp = self.tail
        # Returns empty if temp is none 
        if temp is None:
            return "[]"
        while temp is not None: 
            student = f"{temp.getID()} {temp.getFac()} {temp.getFirstName()} {temp.getLastName()},\n"
            string += student
            temp = temp.getPrev()
        string = string[:-2]

        string += "]"

        return string



class testStudentNode(TestCase):
    

    def test_init_student(self):
        """Test initalize studentNode"""
        student = StudentNode("123456", "ART", "Tosin", "Kuye")
        self.assertEqual(
            student.getFac(), "ART")
        self.assertEqual(
            student.getFirstName(), "Tosin")
        self.assertEqual(
            student.getLastName(), "Kuye")
        self.assertEqual(
            student.getID(), "123456")
    
    def test_setID(self):
        """Test set ID"""
        student = StudentNode("123456", "ART", "Tosin", "Kuye")
        student.setID("654321")
        self.assertEqual(student.getID(), "654321")
    
    def test_setFac(self):
        """Test set Faculty"""
        student = StudentNode("123456", "ART", "Tosin", "Kuye")
        student.setFaculty("SCI")
        self.assertEqual(student.getFac(), "SCI")
    
    def test_setFirstName(self):
        """Test set first name"""
        student = StudentNode("123456", "ART", "Tosin", "Kuye")
        student.setFirstName("John")
        self.assertEqual(student.getFirstName(), "John")
    def test_setLastName(self):
        """Test set last name"""
        student = StudentNode("123456", "ART", "Tosin", "Kuye")
        student.setLastName("Smith")
        self.assertEqual(student.getLastName(), "Smith")
    
    def test_setAndGet(self):
        """Test setters and getters for student node"""
        student = StudentNode("123456", "ART", "Tosin", "Kuye")
        newStudent = StudentNode("555555", "ART", "Matthew", "Jones")
        student.setNext(newStudent)
        newStudent.setPrev(student)
        self.assertEqual(student.getNext().getID(), "555555")
        self.assertEqual(newStudent.getPrev().getID(), "123456")
        self.assertEqual(newStudent.getNext(), None)


    def test_init_enrollment(self):
        """Test enrollement init"""
        table = EnrollTable(35)
        self.assertEqual(table.tableSize, 0)
        self.assertEqual(table.MAX_CAPACITY, 51)
        self.assertEqual(len(table.enrollTable), 35)
    
    def test_cmputIndex(self):
        """Test cmputindex method"""
        student1 = StudentNode("123456", "ART", "Tosin", "Kuye")
        student2 = StudentNode("555555", "ART", "Matthew", "Jones")
        student3 = StudentNode("654321", "ART", "Matthew", "Jones")
        table = EnrollTable(35)
        self.assertEqual(table.cmputIndex(student1.getID()), 32)
        self.assertEqual(table.cmputIndex(student2.getID()), 20)
        self.assertEqual(table.cmputIndex(student3.getID()), 24)

    def test_insert(self):
        """Test insert enroll method"""
        student = StudentNode("123456", "ART", "Tosin", "Kuye")
        student1 = StudentNode("555555", "SCI", "Satoshi", "Nakamoto")
        student2 = StudentNode("654321", "ART", "Levi", "Ackermann")
        table = EnrollTable(35)

        table.insert(student)
        table.insert(student1)
        table.insert(student2)
        
        self.assertEqual(table.tableSize, 3)

        self.assertEqual(table.enrollTable[32].getID(), "123456")
        self.assertEqual(table.enrollTable[20].getID(), "555555")
        self.assertEqual(table.enrollTable[24].getID(), "654321")
        
    def test_insert_row(self):
        """test insert via a single row"""
        table = EnrollTable(35)
        student = StudentNode("999670", "ART", "Tosin", "Kuye")
        student1 = StudentNode("999635", "SCI", "Satoshi", "Nakamoto")
        student2 = StudentNode("999600", "ART", "Levi", "Ackermann")
        student3 = StudentNode("999599", "ART", "Tosin", "Kuye")
        student4 = StudentNode("555555", "SCI", "Satoshi", "Nakamoto")
        student5 = StudentNode("534125", "SCI", "Satoshi", "Monkery")
        student6 = StudentNode("211122", "SCI", "Satoshi", "Masaaas")
        table.insert(student)
        table.insert(student1)
        table.insert(student2)
        table.insert(student3)
        table.insert(student4)
        table.insert(student5)
        table.insert(student6)
        temp = table.enrollTable[20]
        
        count = 0 
        while temp is not None:
            temp = temp.getNext()
            count += 1

        self.assertEqual(count, 5)

    def test_remove_table(self):
        """Test removing from the table"""
        table = EnrollTable(35)
        student = StudentNode("999670", "ART", "Tosin", "Kuye")
        student1 = StudentNode("999635", "SCI", "Satoshi", "Nakamoto")
        student2 = StudentNode("999600", "ART", "Levi", "Ackermann")
        student3 = StudentNode("999599", "ART", "Tosin", "Kuye")
        student4 = StudentNode("555555", "SCI", "Satoshi", "Nakamoto")
        student5 = StudentNode("534125", "SCI", "Satoshi", "Monkery")
        student6 = StudentNode("211122", "SCI", "Satoshi", "Masaaas")
        table.insert(student)
        table.insert(student1)
        table.insert(student2)
        table.insert(student3)
        table.insert(student4)
        table.insert(student5)
        table.insert(student6)

        t = table.remove(student1.getID())
        self.assertEqual(table.tableSize, 6)
        self.assertTrue(t)
        table.remove("233433")
        table.remove(student6.getID())
        self.assertEqual(table.tableSize, 5)

    def test_is_enrolled(self):
        """Test isEnrolled method"""
        table = EnrollTable(35)
        student = StudentNode("999670", "ART", "Tosin", "Kuye")
        student1 = StudentNode("999635", "SCI", "Satoshi", "Nakamoto")
        student2 = StudentNode("999600", "ART", "Levi", "Ackermann")
        student3 = StudentNode("999599", "ART", "Tosin", "Kuye")
        student4 = StudentNode("555555", "SCI", "Satoshi", "Nakamoto")
        student5 = StudentNode("534125", "SCI", "Satoshi", "Monkery")
        student6 = StudentNode("211122", "SCI", "Satoshi", "Masaaas")
        table.insert(student)
        table.insert(student1)
        table.insert(student2)
        table.insert(student3)
        table.insert(student4)
        table.insert(student5)
        table.insert(student6)

        self.assertTrue(table.isEnrolled(student.getID()))
        self.assertTrue(table.isEnrolled(student1.getID()))
        self.assertTrue(table.isEnrolled(student2.getID()))
        self.assertTrue(table.isEnrolled(student3.getID()))
        self.assertTrue(table.isEnrolled(student4.getID()))
        self.assertTrue(table.isEnrolled(student5.getID()))
        table.remove(student.getID())
        table.remove(student1.getID())
        self.assertFalse(table.isEnrolled(student.getID()))
        self.assertFalse(table.isEnrolled(student1.getID()))

        self.assertEqual(table.size(), 5)

    def test_assert_empty(self):
        """Test if enroll is empty"""
        table = EnrollTable(35)
        student = StudentNode("999670", "ART", "Tosin", "Kuye")
        student1 = StudentNode("999635", "SCI", "Satoshi", "Nakamoto")
        student2 = StudentNode("999600", "ART", "Levi", "Ackermann")
        student3 = StudentNode("999599", "ART", "Tosin", "Kuye")

        table.insert(student)
        table.insert(student1)
        table.insert(student2)
        table.insert(student3)
        self.assertFalse(table.isEmpty())
        table.remove(student.getID())
        table.remove(student1.getID())
        table.remove(student2.getID())
        table.remove(student3.getID())

        self.assertTrue(table.isEmpty())

    def test_assert_queue(self):
        """Test assertions for priority Queue class"""
        queue = PriorityQueue()

        self.assertEqual(queue.head, None)
        self.assertEqual(queue.tail, None)
        self.assertEqual(queue.size(), 0)
    
    def test_enqueue(self):
        """Test Enqueue methods"""
        queue = PriorityQueue()
        student = StudentNode("999670", "ART", "Tosin", "Kuye")
        student1 = StudentNode("999635", "SCI", "Satoshi", "Nakamoto")
        student2 = StudentNode("999600", "EDU", "Levi", "Ackermann")

        queue.enqueue(student)
        queue.enqueue(student1)
        queue.enqueue(student2)

        self.assertEqual(queue.size(), 3)
        self.assertEqual(queue.tail.getFac(), "SCI")
        self.assertEqual(queue.head.getFac(), "EDU")
        
    def test_dequeue(self):
        """test dequeue methods"""
        queue = PriorityQueue()
        student = StudentNode("999670", "SCI", "Tosin", "Kuye")
        student1 = StudentNode("999635", "SCI", "Satoshi", "Nakamoto")
        student2 = StudentNode("999600", "SCI", "Levi", "Ackermann")
        student3 = StudentNode("999620", "ENG", "Eren", "Jeager")
        
        queue.enqueue(student)
        queue.enqueue(student1)
        queue.enqueue(student2)
        queue.enqueue(student3)
        print(queue)
        queue.dequeue()
        print(queue)
        self.assertEqual(queue.size(), 3)
        
        self.assertEqual(queue.tail.getFac(), "SCI")
        queue.dequeue()
        queue.dequeue()
        self.assertEqual(queue.tail.getFac(), "ENG")
        self.assertEqual(queue.head.getFac(), "ENG")
        self.assertEqual(queue.size(), 1)
        
        


if __name__ == "__main__":
    testStudentNode().main()
    