import curses
import math
from output import show_message


def get_input(stdscr, prompt):
    curses.echo()
    stdscr.clear()
    stdscr.addstr(2, 4, prompt, curses.A_BOLD)
    stdscr.refresh()
    val = stdscr.getstr(3, 4, 60).decode("utf-8").strip()
    curses.noecho()
    return val


def get_int_input(stdscr, prompt):
    while True:
        val = get_input(stdscr, prompt)
        try:
            n = int(val)
            if n > 0:
                return n
            show_message(stdscr, "Gia tri phai lon hon 0!")
        except ValueError:
            show_message(stdscr, "Vui long nhap so nguyen hop le!")


def save_students_to_file(students):
    with open("students.txt", "w", encoding="utf-8") as f:
        for s in students:
            f.write(f"{s.id},{s.name},{s.dob}\n")


def save_courses_to_file(courses):
    with open("courses.txt", "w", encoding="utf-8") as f:
        for c in courses:
            f.write(f"{c.id},{c.name},{c.credits}\n")


def save_marks_to_file(marks):
    with open("marks.txt", "w", encoding="utf-8") as f:
        for c_id, s_marks in marks.items():
            for s_id, score in s_marks.items():
                f.write(f"{c_id},{s_id},{score}\n")


def input_students(stdscr, students, StudentClass):
    num = get_int_input(stdscr, "Nhap so luong sinh vien: ")
    for i in range(num):
        stdscr.clear()
        stdscr.addstr(2, 4, f"--- Sinh vien #{i + 1} ---", curses.A_BOLD)
        s_id = get_input(stdscr, f"Sinh vien #{i + 1} - Nhap ID: ")
        s_name = get_input(stdscr, f"Sinh vien #{i + 1} - Nhap Ho ten: ")
        s_dob = get_input(stdscr, f"Sinh vien #{i + 1} - Nhap Ngay sinh: ")

        students.append(StudentClass(s_id, s_name, s_dob))

    save_students_to_file(students)
    show_message(stdscr, "Da luu thong tin sinh vien vao students.txt!")


def input_courses(stdscr, courses, CourseClass):
    num = get_int_input(stdscr, "Nhap so luong mon hoc: ")
    for i in range(num):
        stdscr.clear()
        c_id = get_input(stdscr, f"Mon #{i + 1} - Nhap Course ID: ")
        c_name = get_input(stdscr, f"Mon #{i + 1} - Nhap Ten mon hoc: ")
        c_credits = get_int_input(stdscr, f"Mon #{i + 1} - Nhap So tin chi: ")

        courses.append(CourseClass(c_id, c_name, c_credits))

    save_courses_to_file(courses)
    show_message(stdscr, "Da luu thong tin mon hoc vao courses.txt!")


def input_marks(stdscr, students, courses, marks, calculate_all_gpa_func):
    if not courses:
        show_message(stdscr, "Chua co mon hoc. Vui long nhap mon hoc truoc!")
        return
    if not students:
        show_message(stdscr, "Chua co sinh vien. Vui long nhap sinh vien truoc!")
        return

    c_id = get_input(stdscr, "Nhap Course ID can nhap diem: ")
    course = next((c for c in courses if c.id == c_id), None)
    if not course:
        show_message(stdscr, f"Khong tim thay mon hoc ID: {c_id}")
        return

    if c_id not in marks:
        marks[c_id] = {}

    for s in students:
        s_id = s.id
        while True:
            val = get_input(stdscr, f"Nhap diem cho {s.name} (ID: {s_id}) [0 - 20]: ")
            try:
                raw_score = float(val)
                if 0 <= raw_score <= 20:
                    rounded_score = math.floor(raw_score * 10) / 10
                    marks[c_id][s_id] = rounded_score
                    break
                show_message(stdscr, "Diem phai tu 0 den 20!")
            except ValueError:
                show_message(stdscr, "Vui long nhap so thuc hop le!")

    save_marks_to_file(marks)
    calculate_all_gpa_func(students, courses, marks)
    show_message(stdscr, "Da luu diem vao marks.txt va cap nhat GPA!")