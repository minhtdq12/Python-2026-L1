import curses
import numpy as np


def show_message(stdscr, msg):
    stdscr.clear()
    stdscr.addstr(4, 4, msg, curses.A_STANDOUT)
    stdscr.addstr(6, 4, "Nhan phim bat ky de tiep tuc...")
    stdscr.refresh()
    stdscr.getch()


def list_courses(stdscr, courses):
    stdscr.clear()
    stdscr.addstr(2, 4, "=== DANH SACH MON HOC ===", curses.A_BOLD)
    header = f"{'Course ID':<15} | {'Course Name':<25} | {'Credits':<8}"
    stdscr.addstr(4, 4, header, curses.A_UNDERLINE)

    if not courses:
        stdscr.addstr(6, 4, "Chua co mon hoc nao.")
    else:
        row = 5
        for c in courses:
            line = f"{c.id:<15} | {c.name:<25} | {c.credits:<8}"
            stdscr.addstr(row, 4, line)
            row += 1

    stdscr.addstr(len(courses) + 7, 4, "Nhan phim bat ky de quay lai...")
    stdscr.refresh()
    stdscr.getch()


def list_students(stdscr, students):
    stdscr.clear()
    stdscr.addstr(2, 4, "=== DANH SACH SINH VIEN (SAP XEP THEO GPA GIAM DAN) ===", curses.A_BOLD)
    header = f"{'Student ID':<15} | {'Name':<22} | {'DoB':<13} | {'GPA':<6}"
    stdscr.addstr(4, 4, header, curses.A_UNDERLINE)

    if not students:
        stdscr.addstr(6, 4, "Chua co sinh vien nao.")
    else:
        gpa_array = np.array([s.gpa for s in students])
        sorted_indices = np.argsort(-gpa_array)

        row = 5
        for idx in sorted_indices:
            s = students[idx]
            line = f"{s.id:<15} | {s.name:<22} | {s.dob:<13} | {s.gpa:<6.2f}"
            stdscr.addstr(row, 4, line)
            row += 1

    stdscr.addstr(len(students) + 7, 4, "Nhan phim bat ky de quay lai...")
    stdscr.refresh()
    stdscr.getch()