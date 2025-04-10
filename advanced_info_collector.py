import re
import requests
import curses
import socket

def collect_info(url):
    try:
        response = requests.get(url)
        emails = set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', response.text))
        phone_numbers = set(re.findall(r'\+?\d[\d -]{8,}\d', response.text))
        return emails, phone_numbers
    except Exception as e:
        return f"Error: {e}", []

def get_ip_info(ip_address):
    try:
        ip_info = socket.gethostbyname(ip_address)
        return f"IP Address: {ip_info}"
    except Exception as e:
        return f"Error: {e}"

def draw_banner(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "==============================", curses.A_BOLD)
    stdscr.addstr(1, 0, "      Info Collector Tool      ", curses.A_BOLD | curses.color_pair(1))
    stdscr.addstr(2, 0, "==============================", curses.A_BOLD)
    stdscr.addstr(3, 0, "Collect emails, phone numbers, and IP info.", curses.A_BOLD)
    stdscr.addstr(5, 0, "Press any key to continue...", curses.A_BOLD)
    stdscr.refresh()
    stdscr.getch()

def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

    draw_banner(stdscr)

    stdscr.clear()
    stdscr.addstr(0, 0, "Enter Website URL: ", curses.A_BOLD)
    url = stdscr.getstr(1, 0).decode('utf-8')

    emails, phone_numbers = collect_info(url)

    stdscr.clear()
    stdscr.addstr(0, 0, "Emails: " + str(emails), curses.A_BOLD | curses.color_pair(1))
    stdscr.addstr(1, 0, "Phone Numbers: " + str(phone_numbers), curses.A_BOLD | curses.color_pair(1))

    stdscr.addstr(3, 0, "Enter IP Address: ", curses.A_BOLD)
    ip_address = stdscr.getstr(4, 0).decode('utf-8')

    ip_info = get_ip_info(ip_address)

    stdscr.addstr(6, 0, ip_info, curses.A_BOLD | curses.color_pair(1))
    stdscr.refresh()
    stdscr.addstr(8, 0, "Press any key to exit...", curses.A_BOLD)
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
