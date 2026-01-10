import json
from typing import Optional, List
from datetime import datetime


class StudentNode:
    """Node for Linked List implementation"""
    def __init__(self, student_id: str, name: str, grade: float, department: str):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.department = department
        self.next = None
        self.prev = None

class BSTNode:
    """Node for Binary Search Tree implementation (sorted by grade)"""
    def __init__(self, student: StudentNode):
        self.student = student
        self.left = None
        self.right = None


class DoublyLinkedList:
    """Doubly Linked List for storing students"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def insert_at_end(self, student_id: str, name: str, grade: float, department: str):
        """Insert student at the end - O(1)"""
        new_node = StudentNode(student_id, name, grade, department)
        
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.size += 1
        return new_node
    
    def delete_by_id(self, student_id: str) -> bool:
        """Delete student by ID - O(n)"""
        current = self.head
        
        while current:
            if current.student_id == student_id:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def search_by_id(self, student_id: str) -> Optional[StudentNode]:
        """Linear search by student ID - O(n)"""
        current = self.head
        while current:
            if current.student_id == student_id:
                return current
            current = current.next
        return None
    
    def display_all(self):
        """Display all students"""
        if not self.head:
            print("No students in the system.")
            return
        
        current = self.head
        print(f"\n{'ID':<10} {'Name':<20} {'Grade':<8} {'Department':<15}")
        print("-" * 60)
        while current:
            print(f"{current.student_id:<10} {current.name:<20} {current.grade:<8.2f} {current.department:<15}")
            current = current.next
        print(f"\nTotal Students: {self.size}")

# ==================== BINARY SEARCH TREE ====================

class BinarySearchTree:
    """BST for efficient searching by grade"""
    def __init__(self):
        self.root = None
    
    def insert(self, student: StudentNode):
        """Insert student into BST - O(log n) average"""
        if not self.root:
            self.root = BSTNode(student)
        else:
            self._insert_recursive(self.root, student)
    
    def _insert_recursive(self, node: BSTNode, student: StudentNode):
        if student.grade < node.student.grade:
            if node.left is None:
                node.left = BSTNode(student)
            else:
                self._insert_recursive(node.left, student)
        else:
            if node.right is None:
                node.right = BSTNode(student)
            else:
                self._insert_recursive(node.right, student)
    
    def inorder_traversal(self) -> List[StudentNode]:
        """Inorder traversal (sorted by grade) - O(n)"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node: BSTNode, result: List[StudentNode]):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.student)
            self._inorder_recursive(node.right, result)
    
    def find_students_above_grade(self, min_grade: float) -> List[StudentNode]:
        """Find all students with grade >= min_grade"""
        result = []
        self._find_above_grade(self.root, min_grade, result)
        return result
    
    def _find_above_grade(self, node: BSTNode, min_grade: float, result: List[StudentNode]):
        if node:
            if node.student.grade >= min_grade:
                self._find_above_grade(node.left, min_grade, result)
                result.append(node.student)
                self._find_above_grade(node.right, min_grade, result)
            else:
                self._find_above_grade(node.right, min_grade, result)

# ==================== HASH TABLE ====================

class HashTable:
    """Hash Table for O(1) average lookup by student ID"""
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key: str) -> int:
        """Hash function using polynomial rolling hash"""
        hash_value = 0
        for char in key:
            hash_value = (hash_value * 31 + ord(char)) % self.size
        return hash_value
    
    def insert(self, student: StudentNode):
        """Insert student - O(1) average"""
        index = self._hash(student.student_id)
        # Check for duplicates
        for item in self.table[index]:
            if item.student_id == student.student_id:
                return False
        self.table[index].append(student)
        return True
    
    def search(self, student_id: str) -> Optional[StudentNode]:
        """Search student - O(1) average"""
        index = self._hash(student_id)
        for student in self.table[index]:
            if student.student_id == student_id:
                return student
        return None
    
    def delete(self, student_id: str) -> bool:
        """Delete student - O(1) average"""
        index = self._hash(student_id)
        for i, student in enumerate(self.table[index]):
            if student.student_id == student_id:
                self.table[index].pop(i)
                return True
        return False

# ==================== SORTING ALGORITHMS ====================

class SortingAlgorithms:
    """Various sorting algorithms for demonstration"""
    
    @staticmethod
    def quick_sort(students: List[StudentNode], key='grade', reverse=False) -> List[StudentNode]:
        """Quick Sort - O(n log n) average"""
        if len(students) <= 1:
            return students
        
        pivot = students[len(students) // 2]
        pivot_value = getattr(pivot, key)
        
        if reverse:
            left = [s for s in students if getattr(s, key) > pivot_value]
            middle = [s for s in students if getattr(s, key) == pivot_value]
            right = [s for s in students if getattr(s, key) < pivot_value]
        else:
            left = [s for s in students if getattr(s, key) < pivot_value]
            middle = [s for s in students if getattr(s, key) == pivot_value]
            right = [s for s in students if getattr(s, key) > pivot_value]
        
        return SortingAlgorithms.quick_sort(left, key, reverse) + middle + SortingAlgorithms.quick_sort(right, key, reverse)
    
    @staticmethod
    def merge_sort(students: List[StudentNode], key='name') -> List[StudentNode]:
        """Merge Sort - O(n log n)"""
        if len(students) <= 1:
            return students
        
        mid = len(students) // 2
        left = SortingAlgorithms.merge_sort(students[:mid], key)
        right = SortingAlgorithms.merge_sort(students[mid:], key)
        
        return SortingAlgorithms._merge(left, right, key)
    
    @staticmethod
    def _merge(left: List[StudentNode], right: List[StudentNode], key: str) -> List[StudentNode]:
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if getattr(left[i], key) <= getattr(right[j], key):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result

# ==================== MAIN SYSTEM ====================

class StudentManagementSystem:
    """Main system integrating all data structures"""
    def __init__(self):
        self.linked_list = DoublyLinkedList()
        self.bst = BinarySearchTree()
        self.hash_table = HashTable()
    
    def add_student(self, student_id: str, name: str, grade: float, department: str):
        """Add a new student"""
        # Check if student already exists
        if self.hash_table.search(student_id):
            print(f"Error: Student with ID {student_id} already exists!")
            return False
        
        # Add to linked list
        student = self.linked_list.insert_at_end(student_id, name, grade, department)
        
        # Add to BST
        self.bst.insert(student)
        
        # Add to hash table
        self.hash_table.insert(student)
        
        print(f"Successfully added student: {name} (ID: {student_id})")
        return True
    
    def delete_student(self, student_id: str):
        """Delete a student by ID"""
        if self.linked_list.delete_by_id(student_id):
            self.hash_table.delete(student_id)
            # Note: BST deletion is complex, so we rebuild it
            self._rebuild_bst()
            print(f"Successfully deleted student with ID: {student_id}")
            return True
        else:
            print(f"Error: Student with ID {student_id} not found!")
            return False
    
    def _rebuild_bst(self):
        """Rebuild BST after deletion"""
        self.bst = BinarySearchTree()
        current = self.linked_list.head
        while current:
            self.bst.insert(current)
            current = current.next
    
    def search_student(self, student_id: str):
        """Search for a student using hash table"""
        student = self.hash_table.search(student_id)
        if student:
            print(f"\nStudent Found:")
            print(f"ID: {student.student_id}")
            print(f"Name: {student.name}")
            print(f"Grade: {student.grade}")
            print(f"Department: {student.department}")
            return student
        else:
            print(f"Student with ID {student_id} not found!")
            return None
    
    def display_all_students(self):
        """Display all students"""
        self.linked_list.display_all()
    
    def display_sorted_by_grade(self):
        """Display students sorted by grade using BST"""
        students = self.bst.inorder_traversal()
        if not students:
            print("No students in the system.")
            return
        
        print(f"\n{'ID':<10} {'Name':<20} {'Grade':<8} {'Department':<15}")
        print("-" * 60)
        for student in students:
            print(f"{student.student_id:<10} {student.name:<20} {student.grade:<8.2f} {student.department:<15}")
    
    def display_top_performers(self, min_grade: float = 80.0):
        """Display students with grade above threshold"""
        students = self.bst.find_students_above_grade(min_grade)
        if not students:
            print(f"No students found with grade >= {min_grade}")
            return
        
        print(f"\nStudents with grade >= {min_grade}:")
        print(f"{'ID':<10} {'Name':<20} {'Grade':<8} {'Department':<15}")
        print("-" * 60)
        for student in students:
            print(f"{student.student_id:<10} {student.name:<20} {student.grade:<8.2f} {student.department:<15}")
    
    def get_all_students_list(self) -> List[StudentNode]:
        """Get all students as a list"""
        result = []
        current = self.linked_list.head
        while current:
            result.append(current)
            current = current.next
        return result
    
    def display_sorted_by_name(self):
        """Display students sorted by name using merge sort"""
        students = self.get_all_students_list()
        sorted_students = SortingAlgorithms.merge_sort(students, key='name')
        
        print(f"\n{'ID':<10} {'Name':<20} {'Grade':<8} {'Department':<15}")
        print("-" * 60)
        for student in sorted_students:
            print(f"{student.student_id:<10} {student.name:<20} {student.grade:<8.2f} {student.department:<15}")

# ==================== MENU INTERFACE ====================

def display_menu():
    print("\n" + "="*60)
    print("STUDENT MANAGEMENT SYSTEM - DSA PROJECT")
    print("="*60)
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Display Students Sorted by Grade")
    print("6. Display Students Sorted by Name")
    print("7. Display Top Performers (Grade >= 80)")
    print("8. Add Sample Data")
    print("9. Exit")
    print("="*60)

def main():
    system = StudentManagementSystem()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-9): ").strip()
        
        if choice == '1':
            student_id = input("Enter Student ID: ").strip()
            name = input("Enter Name: ").strip()
            try:
                grade = float(input("Enter Grade (0-100): ").strip())
                if not (0 <= grade <= 100):
                    print("Grade must be between 0 and 100!")
                    continue
            except ValueError:
                print("Invalid grade! Please enter a number.")
                continue
            department = input("Enter Department: ").strip()
            system.add_student(student_id, name, grade, department)
        
        elif choice == '2':
            student_id = input("Enter Student ID to delete: ").strip()
            system.delete_student(student_id)
        
        elif choice == '3':
            student_id = input("Enter Student ID to search: ").strip()
            system.search_student(student_id)
        
        elif choice == '4':
            system.display_all_students()
        
        elif choice == '5':
            system.display_sorted_by_grade()
        
        elif choice == '6':
            system.display_sorted_by_name()
        
        elif choice == '7':
            try:
                min_grade = float(input("Enter minimum grade (default 80): ").strip() or "80")
                system.display_top_performers(min_grade)
            except ValueError:
                print("Invalid input! Using default grade of 80.")
                system.display_top_performers(80.0)
        
        elif choice == '8':
            # Add sample data
            sample_students = [
                ("S001", "Alice Johnson", 92.5, "Computer Science"),
                ("S002", "Bob Smith", 78.3, "Mathematics"),
                ("S003", "Charlie Brown", 85.7, "Physics"),
                ("S004", "Diana Prince", 95.2, "Computer Science"),
                ("S005", "Eve Wilson", 72.8, "Chemistry"),
                ("S006", "Frank Miller", 88.4, "Mathematics"),
                ("S007", "Grace Lee", 91.0, "Computer Science"),
                ("S008", "Henry Davis", 76.5, "Physics"),
            ]
            for sid, name, grade, dept in sample_students:
                system.add_student(sid, name, grade, dept)
            print("\nSample data added successfully!")
        
        elif choice == '9':
            print("\nThank you for using the Student Management System!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()