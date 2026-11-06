import curses
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


def main_screen(stdscr):
    curses.curs_set(0)
    menu_items = [
        "1. Nhap danh sach sinh vien",
        "2. Nhap danh sach mon hoc (co credits)",
        "3. Nhap diem mon hoc (math.floor 1 decimal)",
        "4. Xem danh sach mon hoc",
        "5. Xem danh sach sinh vien theo GPA giam dan (numpy)",
        "0. Thoat"
    ]

    while True:
        stdscr.clear()
        stdscr.addstr(2, 4, "STUDENT MARK MANAGEMENT (PW4: MODULARIZATION)", curses.A_BOLD)
        stdscr.addstr(3, 4, "--------------------------------------------")

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
            break


def main():
    curses.wrapper(main_screen)


if __name__ == "__main__":
    main()