import curses
import math
import numpy as np

students = []
courses = []
marks = {}


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


def show_message(stdscr, msg):
    stdscr.clear()
    stdscr.addstr(4, 4, msg, curses.A_STANDOUT)
    stdscr.addstr(6, 4, "Nhan phim bat ky de tiep tuc...")
    stdscr.refresh()
    stdscr.getch()


def input_students(stdscr):
    num = get_int_input(stdscr, "Nhap so luong sinh vien: ")
    for i in range(num):
        stdscr.clear()
        stdscr.addstr(2, 4, f"--- Sinh vien #{i + 1} ---", curses.A_BOLD)
        s_id = get_input(stdscr, f"Sinh vien #{i + 1} - Nhap ID: ")
        s_name = get_input(stdscr, f"Sinh vien #{i + 1} - Nhap Ho ten: ")
        s_dob = get_input(stdscr, f"Sinh vien #{i + 1} - Nhap Ngay sinh: ")

        students.append({
            "id": s_id,
            "name": s_name,
            "dob": s_dob,
            "gpa": 0.0
        })
    show_message(stdscr, "Da them danh sach sinh vien thanh cong!")


def input_courses(stdscr):
    num = get_int_input(stdscr, "Nhap so luong mon hoc: ")
    for i in range(num):
        stdscr.clear()
        c_id = get_input(stdscr, f"Mon #{i + 1} - Nhap Course ID: ")
        c_name = get_input(stdscr, f"Mon #{i + 1} - Nhap Ten mon hoc: ")
        c_credits = get_int_input(stdscr, f"Mon #{i + 1} - Nhap So tin chi: ")

        courses.append({
            "id": c_id,
            "name": c_name,
            "credits": c_credits
        })
    show_message(stdscr, "Da them danh sach mon hoc thanh cong!")


def input_marks(stdscr):
    if not courses:
        show_message(stdscr, "Chua co mon hoc. Vui long nhap mon hoc truoc!")
        return
    if not students:
        show_message(stdscr, "Chua co sinh vien. Vui long nhap sinh vien truoc!")
        return

    c_id = get_input(stdscr, "Nhap Course ID can nhap diem: ")
    course = next((c for c in courses if c["id"] == c_id), None)
    if not course:
        show_message(stdscr, f"Khong tim thay mon hoc ID: {c_id}")
        return

    if c_id not in marks:
        marks[c_id] = {}

    for s in students:
        s_id = s["id"]
        while True:
            val = get_input(stdscr, f"Nhap diem cho {s['name']} (ID: {s_id}) [0 - 20]: ")
            try:
                raw_score = float(val)
                if 0 <= raw_score <= 20:
                    rounded_score = math.floor(raw_score * 10) / 10
                    marks[c_id][s_id] = rounded_score
                    break
                show_message(stdscr, "Diem phai tu 0 den 20!")
            except ValueError:
                show_message(stdscr, "Vui long nhap so thực hop le!")

    calculate_all_gpa()
    show_message(stdscr, "Da luu diem va cap nhat GPA thanh cong!")


def calculate_all_gpa():
    for s in students:
        s_id = s["id"]
        credits_list = []
        marks_list = []

        for c in courses:
            c_id = c["id"]
            if c_id in marks and s_id in marks[c_id]:
                credits_list.append(c["credits"])
                marks_list.append(marks[c_id][s_id])

        if credits_list:
            np_credits = np.array(credits_list)
            np_marks = np.array(marks_list)
            total_credits = np.sum(np_credits)

            if total_credits > 0:
                weighted_sum = np.sum(np_credits * np_marks)
                s["gpa"] = float(weighted_sum / total_credits)
            else:
                s["gpa"] = 0.0
        else:
            s["gpa"] = 0.0


def list_courses(stdscr):
    stdscr.clear()
    stdscr.addstr(2, 4, "=== DANH SACH MON HOC ===", curses.A_BOLD)
    header = f"{'Course ID':<15} | {'Course Name':<25} | {'Credits':<8}"
    stdscr.addstr(4, 4, header, curses.A_UNDERLINE)

    if not courses:
        stdscr.addstr(6, 4, "Chua co mon hoc nao.")
    else:
        row = 5
        for c in courses:
            line = f"{c['id']:<15} | {c['name']:<25} | {c['credits']:<8}"
            stdscr.addstr(row, 4, line)
            row += 1

    stdscr.addstr(len(courses) + 7, 4, "Nhan phim bat ky de quay lai...")
    stdscr.refresh()
    stdscr.getch()


def list_students(stdscr):
    stdscr.clear()
    stdscr.addstr(2, 4, "=== DANH SACH SINH VIEN (SAP XEP THEO GPA GIAM DAN) ===", curses.A_BOLD)
    header = f"{'Student ID':<15} | {'Name':<22} | {'DoB':<13} | {'GPA':<6}"
    stdscr.addstr(4, 4, header, curses.A_UNDERLINE)

    if not students:
        stdscr.addstr(6, 4, "Chua co sinh vien nao.")
    else:
        gpa_array = np.array([s["gpa"] for s in students])
        sorted_indices = np.argsort(-gpa_array)

        row = 5
        for idx in sorted_indices:
            s = students[idx]
            line = f"{s['id']:<15} | {s['name']:<22} | {s['dob']:<13} | {s['gpa']:<6.2f}"
            stdscr.addstr(row, 4, line)
            row += 1

    stdscr.addstr(len(students) + 7, 4, "Nhan phim bat ky de quay lai...")
    stdscr.refresh()
    stdscr.getch()


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
        stdscr.addstr(2, 4, "STUDENT MARK MANAGEMENT (PRACTICAL WORK 3)", curses.A_BOLD)
        stdscr.addstr(3, 4, "------------------------------------------")

        for i, item in enumerate(menu_items):
            stdscr.addstr(5 + i, 6, item)

        stdscr.addstr(13, 4, "Chon chuc nang (0 - 5): ")
        stdscr.refresh()

        key = stdscr.getkey()

        if key == "1":
            input_students(stdscr)
        elif key == "2":
            input_courses(stdscr)
        elif key == "3":
            input_marks(stdscr)
        elif key == "4":
            list_courses(stdscr)
        elif key == "5":
            list_students(stdscr)
        elif key == "0":
            break


def main():
    curses.wrapper(main_screen)


if __name__ == "__main__":
    main()