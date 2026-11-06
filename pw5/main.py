import curses
import os
import zipfile
import numpy as np

from domains.student import Student
from domains.course import Course
import input as in_mod
import output as out_mod

students = []
courses = []
marks = {}


def calculate_all_gpa(students_list, courses_list, marks_dict):
    for s in students_list:
        s_id = s.id
        credits_list = []
        marks_list = []

        for c in courses_list:
            c_id = c.id
            if c_id in marks_dict and s_id in marks_dict[c_id]:
                credits_list.append(c.credits)
                marks_list.append(marks_dict[c_id][s_id])

        if credits_list:
            np_credits = np.array(credits_list)
            np_marks = np.array(marks_list)
            total_credits = np.sum(np_credits)

            if total_credits > 0:
                weighted_sum = np.sum(np_credits * np_marks)
                s.gpa = float(weighted_sum / total_credits)
            else:
                s.gpa = 0.0
        else:
            s.gpa = 0.0


def load_initial_data():
    """Giải nén students.dat nếu tồn tại và nạp lại dữ liệu từ các file txt"""
    if os.path.exists("students.dat"):
        with zipfile.ZipFile("students.dat", "r") as zip_ref:
            zip_ref.extractall()

    if os.path.exists("students.txt"):
        with open("students.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    students.append(Student(parts[0], parts[1], parts[2]))

    if os.path.exists("courses.txt"):
        with open("courses.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    courses.append(Course(parts[0], parts[1], int(parts[2])))

    if os.path.exists("marks.txt"):
        with open("marks.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    c_id, s_id, score = parts[0], parts[1], float(parts[2])
                    if c_id not in marks:
                        marks[c_id] = {}
                    marks[c_id][s_id] = score

    calculate_all_gpa(students, courses, marks)


def compress_files_on_exit():
    """Nén các tệp dữ liệu txt thành students.dat trước khi thoát"""
    txt_files = ["students.txt", "courses.txt", "marks.txt"]
    with zipfile.ZipFile("students.dat", "w", zipfile.ZIP_DEFLATED) as zip_file:
        for file in txt_files:
            if os.path.exists(file):
                zip_file.write(file)


def main_screen(stdscr):
    curses.curs_set(0)
    menu_items = [
        "1. Nhap danh sach sinh vien",
        "2. Nhap danh sach mon hoc (co credits)",
        "3. Nhap diem mon hoc (math.floor 1 decimal)",
        "4. Xem danh sach mon hoc",
        "5. Xem danh sach sinh vien theo GPA giam dan (numpy)",
        "0. Thoat (Tu dong nen du lieu vao students.dat)"
    ]

    while True:
        stdscr.clear()
        stdscr.addstr(2, 4, "STUDENT MARK MANAGEMENT (PW5: PERSISTENT INFO)", curses.A_BOLD)
        stdscr.addstr(3, 4, "---------------------------------------------")

        for i, item in enumerate(menu_items):
            stdscr.addstr(5 + i, 6, item)

        stdscr.addstr(13, 4, "Chon chuc nang (0 - 5): ")
        stdscr.refresh()

        key = stdscr.getkey()

        if key == "1":
            in_mod.input_students(stdscr, students, Student)
        elif key == "2":
            in_mod.input_courses(stdscr, courses, Course)
        elif key == "3":
            in_mod.input_marks(stdscr, students, courses, marks, calculate_all_gpa)
        elif key == "4":
            out_mod.list_courses(stdscr, courses)
        elif key == "5":
            out_mod.list_students(stdscr, students)
        elif key == "0":
            compress_files_on_exit()
            break


def main():
    load_initial_data()
    curses.wrapper(main_screen)


if __name__ == "__main__":
    main()