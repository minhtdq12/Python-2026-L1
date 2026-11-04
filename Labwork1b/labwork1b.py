students = []
courses = []
marks = {} 

def input_number_of_students():
    """Nhap so luong sinh vien"""
    while True:
        try:
            n = int(input("Enter the number of students in the class: "))
            if n > 0:
                return n
            print("Number of students must be greater than 0")
        except ValueError:
            print("Please enter a valid integer")

def input_student_info():
    """Nhap thong tin sinh vien: id, name, dob"""
    num_students = input_number_of_students()
    for i in range(num_students):
        print(f"\n- Enter details for student #{i + 1} -")
        s_id = input("Student ID: ").strip()
        s_name = input("Student name: ").strip()
        s_dob = input("Date of Birth (DoB - e.g., DD/MM/YYYY): ").strip()

        students.append({
            "id": s_id,
            "name": s_name,
            "dob": s_dob
        })

def input_number_of_courses():
    """Nhap so luong mon hoc"""
    while True:
        try:
            n = int(input("\nEnter the number of courses: "))
            if n > 0:
                return n
            print("Number of courses must be greaeter than 0")
        except ValueError:
            print("Please enter a valid integer")

def input_course_info():
    """Nhap thong tin mon hoc: id, name"""
    num_courses = input_number_of_courses()
    for i in range(num_courses):
        print(f"\n- Enter details for course #{i + 1} -")
        c_id = input("Course ID: ").strip()
        c_name = input("Course name: ").strip()

        courses.append({
            "id": c_id,
            "name": c_name
        })

def input_marks_for_course():
    """Chon mon hoc va nhap diem sinh vien theo mon do"""
    if not courses:
        print("\n[!] No courses available. Please input courses first.")
        return
    if not students:
        print("\n[!] No students available. Please input students first.")
        return

    print("\n--- Available Courses ---")
    list_courses()
    c_id = input("\nSelect Course ID to enter marks: ").strip()

    # Kiểm tra xem mã môn học có tồn tại hay không
    course_found = any(course["id"] == c_id for course in courses)
    if not course_found:
        print(f"[!] Course with ID '{c_id}' not found.")
        return

    if c_id not in marks:
        marks[c_id] = {}

    print(f"\n--- Entering marks for course {c_id} ---")
    for student in students:
        s_id = student["id"]
        while True:
            try:
                score = float(input(f"Enter mark for {student['name']} (ID: {s_id}) [0 - 20]: "))
                if 0 <= score <= 20:
                    marks[c_id][s_id] = score
                    break
                else:
                    print("Score must be between 0 and 20.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

# ==================== LISTING FUNCTIONS ====================

def list_courses():
    """Liệt kê danh sách các môn học"""
    if not courses:
        print("No courses in the system.")
        return
    print("\n+---------------+--------------------------------+")
    print("| Course ID     | Course Name                    |")
    print("+---------------+--------------------------------+")
    for c in courses:
        print(f"| {c['id']:<13} | {c['name']:<30} |")
    print("+---------------+--------------------------------+")

def list_students():
    """Liệt kê danh sách sinh viên"""
    if not students:
        print("No students in the system.")
        return
    print("\n+---------------+----------------------+---------------+")
    print("| Student ID    | Name                 | Date of Birth |")
    print("+---------------+----------------------+---------------+")
    for s in students:
        print(f"| {s['id']:<13} | {s['name']:<20} | {s['dob']:<13} |")
    print("+---------------+----------------------+---------------+")

def show_student_marks():
    """Hiển thị điểm của sinh viên trong một môn học chỉ định"""
    if not courses:
        print("No courses available.")
        return

    list_courses()
    c_id = input("\nEnter Course ID to view marks: ").strip()

    if c_id not in marks or not marks[c_id]:
        print(f"No marks recorded yet for course '{c_id}'.")
        return

    # Lấy tên môn học
    course_name = next((c["name"] for c in courses if c["id"] == c_id), c_id)
    print(f"\n--- Mark Report for: {course_name} ({c_id}) ---")
    print("+---------------+----------------------+-------+")
    print("| Student ID    | Student Name         | Mark  |")
    print("+---------------+----------------------+-------+")
    for student in students:
        s_id = student["id"]
        score = marks[c_id].get(s_id, "N/A")
        if isinstance(score, float):
            score_str = f"{score:.2f}"
        else:
            score_str = str(score)
        print(f"| {s_id:<13} | {student['name']:<20} | {score_str:<5} |")
    print("+---------------+----------------------+-------+")

# ==================== MAIN PROGRAM ====================

def main():
    while True:
        print("\n" + "="*40)
        print(" STUDENT MARK MANAGEMENT SYSTEM ")
        print("="*40)
        print("1. Input Student Information")
        print("2. Input Course Information")
        print("3. Enter Marks for a Course")
        print("4. List Courses")
        print("5. List Students")
        print("6. Show Marks for a Course")
        print("0. Exit")
        print("="*40)
        choice = input("Enter your choice (0-6): ").strip()

        if choice == "1":
            input_student_info()
        elif choice == "2":
            input_course_info()
        elif choice == "3":
            input_marks_for_course()
        elif choice == "4":
            list_courses()
        elif choice == "5":
            list_students()
        elif choice == "6":
            show_student_marks()
        elif choice == "0":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid selection! Please enter a number between 0 and 6.")

if __name__ == "__main__":
    main()
