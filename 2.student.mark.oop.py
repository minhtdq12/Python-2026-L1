class Entity:
    """Lớp cơ sở đại diện cho các đối tượng trong hệ thống (Tính đa hình)"""
    def __init__(self, entity_id, name):
        self._id = entity_id
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def input(self):
        """Phương thức nhập liệu cơ bản (sẽ được override ở lớp con)"""
        pass

    def list(self):
        """Phương thức hiển thị cơ bản (sẽ được override ở lớp con)"""
        pass


class Student(Entity):
    """Lớp Sinh viên (kế thừa từ Entity)"""
    def __init__(self, s_id="", name="", dob=""):
        super().__init__(s_id, name)
        self._dob = dob

    @property
    def dob(self):
        return self._dob

    def input(self):
        self._id = input("Nhap Ma sinh vien (ID): ").strip()
        self._name = input("Nhap Ho ten (Name): ").strip()
        self._dob = input("Nhap Ngay sinh (DoB): ").strip()

    def list(self):
        print(f"ID: {self._id:<10} | Name: {self._name:<20} | DoB: {self._dob}")


class Course(Entity):
    """Lớp Môn học (kế thừa từ Entity)"""
    def __init__(self, c_id="", name=""):
        super().__init__(c_id, name)

    def input(self):
        self._id = input("Nhap Ma mon hoc (Course ID): ").strip()
        self._name = input("Nhap Ten mon hoc (Course Name): ").strip()

    def list(self):
        print(f"ID: {self._id:<10} | Name: {self._name}")


class MarkManager:
    """Lớp quản lý danh sách Sinh viên, Môn học và Bảng điểm"""
    def __init__(self):
        self._students = []
        self._courses = []
        self._marks = {}  # marks[course_id][student_id] = float_score

    def input_students(self):
        try:
            count = int(input("Nhap so luong sinh vien: "))
            for i in range(count):
                print(f"\n--- Nhap thong tin sinh vien #{i + 1} ---")
                s = Student()
                s.input()
                self._students.append(s)
            print(">> Da them danh sach sinh vien thanh cong!")
        except ValueError:
            print(">> Loi: So luong phai la so nguyen!")

    def input_courses(self):
        try:
            count = int(input("Nhap so luong mon hoc: "))
            for i in range(count):
                print(f"\n--- Nhap thong tin mon hoc #{i + 1} ---")
                c = Course()
                c.input()
                self._courses.append(c)
            print(">> Da them danh sach mon hoc thanh cong!")
        except ValueError:
            print(">> Loi: So luong phai la so nguyen!")

    def input_marks(self):
        if not self._courses:
            print(">> Chua co mon hoc nao. Vui long nhap mon hoc truoc!")
            return
        if not self._students:
            print(">> Chua co sinh vien nao. Vui long nhap sinh vien truoc!")
            return

        c_id = input("Nhap Ma mon hoc (Course ID) can vao diem: ").strip()
        course = next((c for c in self._courses if c.id == c_id), None)
        if not course:
            print(f">> Khong tim thay mon hoc voi ma: {c_id}")
            return

        if c_id not in self._marks:
            self._marks[c_id] = {}

        print(f"\n--- Nhap diem cho mon: {course.name} ({c_id}) ---")
        for s in self._students:
            while True:
                try:
                    score = float(input(f"Nhap diem cho {s.name} (ID: {s.id}) [0-20]: "))
                    if 0 <= score <= 20:
                        self._marks[c_id][s.id] = score
                        break
                    print(">> Diem phai nam trong thang tu 0 den 20!")
                except ValueError:
                    print(">> Gia tri diem khong hop le, vui long nhap lai!")

        print(">> Da nhap diem thanh cong!")

    def list_students(self):
        print("\n=== DANH SACH SINH VIEN ===")
        if not self._students:
            print("Chua co sinh vien nao.")
            return
        for s in self._students:
            s.list()

    def list_courses(self):
        print("\n=== DANH SACH MON HOC ===")
        if not self._courses:
            print("Chua co mon hoc nao.")
            return
        for c in self._courses:
            c.list()

    def show_marks(self):
        if not self._courses:
            print(">> Chua co mon hoc nao.")
            return

        c_id = input("Nhap Ma mon hoc (Course ID) can xem bang diem: ").strip()
        course = next((c for c in self._courses if c.id == c_id), None)
        if not course:
            print(f">> Khong tim thay mon hoc voi ma: {c_id}")
            return

        print(f"\n=== BANG DIEM MON: {course.name} ({c_id}) ===")
        for s in self._students:
            score = self._marks.get(c_id, {}).get(s.id, "N/A")
            print(f"ID: {s.id:<10} | Name: {s.name:<20} | Mark: {score}")


def main():
    manager = MarkManager()

    while True:
        print("\n========================================")
        print("STUDENT MARK MANAGEMENT SYSTEM (PW2: OOP)")
        print("========================================")
        print("1. Nhap thong tin sinh vien")
        print("2. Nhap thong tin mon hoc")
        print("3. Nhap diem mon hoc")
        print("4. Xem danh sach sinh vien")
        print("5. Xem danh sach mon hoc")
        print("6. Xem bang diem theo mon hoc")
        print("0. Thoat")

        choice = input("Chon chuc nang (0-6): ").strip()

        if choice == "1":
            manager.input_students()
        elif choice == "2":
            manager.input_courses()
        elif choice == "3":
            manager.input_marks()
        elif choice == "4":
            manager.list_students()
        elif choice == "5":
            manager.list_courses()
        elif choice == "6":
            manager.show_marks()
        elif choice == "0":
            print("Da thoat chuong trinh.")
            break
        else:
            print("Lua chon khong hop le, vui long chon lai!")


if __name__ == "__main__":
    main()