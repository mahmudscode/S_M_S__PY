# Student Management System - DSA Project

A comprehensive Python-based Student Management System implementing fundamental Data Structures and Algorithms concepts for academic demonstration.
## 🎯 Overview

This Student Management System demonstrates the practical implementation of core data structures and algorithms in a real-world scenario. The system manages student records efficiently using multiple data structures, each optimized for specific operations.

**Purpose**: Academic project showcasing DSA concepts including linked lists, trees, hash tables, and sorting algorithms.

**Language**: Python 3.x

**Type**: Command-line application

## ✨ Features

- **Add Students**: Register new students with ID, name, grade, and department
- **Delete Students**: Remove student records by ID
- **Search Students**: Fast lookup using hash table implementation
- **Display All Students**: View complete student list
- **Sort by Grade**: Display students ordered by academic performance
- **Sort by Name**: Alphabetically sorted student list
- **Top Performers**: Filter students by minimum grade threshold
- **Sample Data**: Quick population with test data

## 🏗️ Data Structures Implemented

### 1. Doubly Linked List
- **Purpose**: Primary storage for sequential access
- **Operations**: Insert at end, delete by ID, traverse
- **Advantages**: Dynamic size, efficient insertion/deletion
- **Implementation**: Custom `DoublyLinkedList` class with head and tail pointers

### 2. Binary Search Tree (BST)
- **Purpose**: Efficient grade-based queries and sorting
- **Operations**: Insert, inorder traversal, range queries
- **Advantages**: O(log n) average insertion, sorted traversal
- **Implementation**: Custom `BinarySearchTree` class with recursive methods

### 3. Hash Table
- **Purpose**: Fast student lookup by ID
- **Hash Function**: Polynomial rolling hash (base 31)
- **Collision Handling**: Chaining with linked lists
- **Advantages**: O(1) average time for search/insert/delete
- **Implementation**: Custom `HashTable` class with configurable size

## 🔧 Algorithms Implemented

### Sorting Algorithms

#### Quick Sort
- **Time Complexity**: O(n log n) average, O(n²) worst case
- **Space Complexity**: O(log n)
- **Used For**: Sorting by grade (descending/ascending)
- **Method**: Divide and conquer with pivot selection

#### Merge Sort
- **Time Complexity**: O(n log n) all cases
- **Space Complexity**: O(n)
- **Used For**: Sorting by name (alphabetical)
- **Method**: Divide and conquer with merging

### Searching Algorithms

#### Hash-based Search
- **Time Complexity**: O(1) average
- **Used For**: Student ID lookup

#### Linear Search
- **Time Complexity**: O(n)
- **Used For**: Linked list traversal

#### BST Range Search
- **Time Complexity**: O(log n + k) where k is number of results
- **Used For**: Finding students above grade threshold

## 📥 Installation

### Prerequisites
- Python 3.6 or higher
### Steps

1. Clone or download the project:
```bash
git clone <repository-url>
cd student-management-system
```

2. Run the program:
```bash
python student_management.py
```

## 🚀 Usage

### Starting the Application

Run the main script:
```bash
python student_management.py
```

### Menu Options

```
1. Add Student          - Register a new student
2. Delete Student       - Remove student by ID
3. Search Student       - Find student by ID
4. Display All Students - Show all records
5. Display Students Sorted by Grade - BST inorder traversal
6. Display Students Sorted by Name - Merge sort
7. Display Top Performers - Filter by grade threshold
8. Add Sample Data      - Load test data
9. Exit                 - Close application
```

### Adding a Student

```
Enter your choice: 1
Enter Student ID: S001
Enter Name: John Doe
Enter Grade (0-100): 85.5
Enter Department: Computer Science
```

### Searching for a Student

```
Enter your choice: 3
Enter Student ID to search: S001

Student Found:
ID: S001
Name: John Doe
Grade: 85.5
Department: Computer Science
```

## 🏛️ System Architecture

```
StudentManagementSystem
│
├── DoublyLinkedList
│   ├── StudentNode (data storage)
│   ├── insert_at_end()
│   ├── delete_by_id()
│   └── search_by_id()
│
├── BinarySearchTree
│   ├── BSTNode (grade-based indexing)
│   ├── insert()
│   ├── inorder_traversal()
│   └── find_students_above_grade()
│
├── HashTable
│   ├── hash() - Polynomial rolling hash
│   ├── insert()
│   ├── search()
│   └── delete()
│
└── SortingAlgorithms
    ├── quick_sort()
    └── merge_sort()
```

## ⏱️ Time Complexity Analysis

| Operation | Data Structure | Time Complexity | Space Complexity |
|-----------|---------------|-----------------|------------------|
| Add Student | Linked List | O(1) | O(1) |
| Add Student | Hash Table | O(1) average | O(1) |
| Add Student | BST | O(log n) average | O(1) |
| Delete Student | Linked List | O(n) | O(1) |
| Delete Student | Hash Table | O(1) average | O(1) |
| Search by ID | Hash Table | O(1) average | O(1) |
| Search by ID | Linked List | O(n) | O(1) |
| Display All | Linked List | O(n) | O(1) |
| Sort by Grade | BST Traversal | O(n) | O(n) |
| Sort by Name | Merge Sort | O(n log n) | O(n) |
| Top Performers | BST Range Query | O(log n + k) | O(k) |

**Note**: n = number of students, k = number of results

## 📁 Project Structure

```
student-management-system/
│
├── student_management.py    # Main application file
├── README.md               # This file
└── requirements.txt        # Dependencies (none required)
```

### Code Organization

- **Node Classes**: `StudentNode`, `BSTNode`
- **Data Structure Classes**: `DoublyLinkedList`, `BinarySearchTree`, `HashTable`
- **Algorithm Classes**: `SortingAlgorithms`
- **Main System**: `StudentManagementSystem`
- **User Interface**: `main()`, `display_menu()`

## 💻 Example Operations

### Sample Output - Display All Students

```
ID         Name                 Grade    Department     
------------------------------------------------------------
S001       Alice Johnson        92.50    Computer Science
S002       Bob Smith            78.30    Mathematics    
S003       Charlie Brown        85.70    Physics        
S004       Diana Prince         95.20    Computer Science

Total Students: 4
```

### Sample Output - Top Performers

```
Students with grade >= 80:
ID         Name                 Grade    Department     
------------------------------------------------------------
S003       Charlie Brown        85.70    Physics        
S001       Alice Johnson        92.50    Computer Science
S004       Diana Prince         95.20    Computer Science
```

## 🔮 Future Enhancements

### Potential Improvements

1. **Persistent Storage**: Save data to file/database
2. **Advanced Search**: Search by name, department, grade range
3. **Update Student**: Modify existing student records
4. **Grade Statistics**: Calculate mean, median, mode
5. **Department Analytics**: Students per department, department averages
6. **Export Functionality**: Export to CSV, JSON
7. **GUI Interface**: Tkinter or web-based interface
8. **AVL Tree**: Self-balancing BST for guaranteed O(log n)
9. **Bloom Filter**: Fast existence checking
10. **Graph Representation**: Student relationships/prerequisites

### Advanced Features

- **Authentication System**: User login with password hashing
- **Course Management**: Link students to courses
- **Attendance Tracking**: Mark and analyze attendance
- **Report Generation**: PDF reports with statistics
- **Batch Operations**: Import/export multiple students
