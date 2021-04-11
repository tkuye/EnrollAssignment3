import unittest
from enrollStudent import StudentNode, EnrollTable, PriorityQueue, PrintColour
from assignment3 import dropStudent, enrollStudentData, lineSplitter



class testStudentNode(unittest.TestCase):
    

    def test_init_student(self):
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
        student = StudentNode("123456", "ART", "Tosin", "Kuye")
        student.setID("654321")
        self.assertEqual(student.getID(), "654321")
    
    def test_setFac(self):
        student = StudentNode("123456", "ART", "Tosin", "Kuye")
        student.setFaculty("SCI")
        self.assertEqual(student.getFac(), "SCI")
    
    def test_setFirstName(self):
        student = StudentNode("123456", "ART", "Tosin", "Kuye")
        student.setFirstName("John")
        self.assertEqual(student.getFirstName(), "John")
    def test_setLastName(self):
        student = StudentNode("123456", "ART", "Tosin", "Kuye")
        student.setLastName("Smith")
        self.assertEqual(student.getLastName(), "Smith")
    
    def test_setAndGet(self):
        student = StudentNode("123456", "ART", "Tosin", "Kuye")
        newStudent = StudentNode("555555", "ART", "Matthew", "Jones")
        student.setNext(newStudent)
        newStudent.setPrev(student)
        self.assertEqual(student.getNext().getID(), "555555")
        self.assertEqual(newStudent.getPrev().getID(), "123456")
        self.assertEqual(newStudent.getNext(), None)


    def test_init_enrollment(self):
        table = EnrollTable(35)
        self.assertEqual(table.tableSize, 0)
        self.assertEqual(table.MAX_CAPACITY, 51)
        self.assertEqual(len(table.enrollTable), 35)
    
    def test_cmputIndex(self):
        student1 = StudentNode("123456", "ART", "Tosin", "Kuye")
        student2 = StudentNode("555555", "ART", "Matthew", "Jones")
        student3 = StudentNode("654321", "ART", "Matthew", "Jones")
        table = EnrollTable(35)
        self.assertEqual(table.cmputIndex(student1.getID()), 32)
        self.assertEqual(table.cmputIndex(student2.getID()), 20)
        self.assertEqual(table.cmputIndex(student3.getID()), 24)

    def test_insert(self):
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
        queue = PriorityQueue()

        self.assertEqual(queue.head, None)
        self.assertEqual(queue.tail, None)
        self.assertEqual(queue.size(), 0)
    
    def test_enqueue(self):
        queue = PriorityQueue()
        student = StudentNode("999670", "ART", "Tosin", "Kuye")
        student1 = StudentNode("999635", "SCI", "Satoshi", "Nakamoto")
        student2 = StudentNode("999600", "EDU", "Levi", "Ackermann")

        queue.enqueue(student)
        queue.enqueue(student1)
        queue.enqueue(student2)

        self.assertEqual(queue.size(), 3)
        self.assertTrue(queue.tail.getFac(), "SCI")
        self.assertTrue(queue.head.getFac(), "EDU")
        
    def test_dequeue(self):
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
        
        self.assertTrue(queue.tail.getFac(), "SCI")
        queue.dequeue()
        queue.dequeue()
        self.assertTrue(queue.tail.getFac(), "ENG")
        self.assertTrue(queue.head.getFac(), "ENG")
        self.assertEqual(queue.size(), 1)
        
        


class testAssignment(unittest.TestCase):
    pc = PrintColour()
    def test_line_split(self):
        with open("input.txt") as f:
            for line in f.readlines():
                studentId, faculty, fname, lname =  lineSplitter(line)
                node = StudentNode(studentId, faculty, fname, lname)
                self.assertEqual(node.getFac(), faculty)
                self.assertEqual(node.getFirstName(), fname)
                self.assertEqual(node.getID(), studentId)
                self.assertEqual(node.getLastName(), lname)
                f.close()

    def test_enroll_student(self):
        queue = PriorityQueue()
        
        table = None
        for i in range(1, 51):
            table = EnrollTable(i)
            with open("input.txt") as f:
                enrollStudentData(f, table, queue)
            f.close()
        self.pc.printout(queue, color="WHITE")
        self.pc.printout(table, color="WHITE")
        self.assertEqual(table.size(), 51)
    def test_drop_student(self):
        queue = PriorityQueue()
        table = EnrollTable(51)
        with open("input.txt") as f:
            enrollStudentData(f, table, queue)
            f.close()
        with open("input.txt") as f:
            dropStudent(f, table, queue)
        
        self.assertEqual(queue.size(), 0)
    

if __name__ == '__main__':
    unittest.main()
