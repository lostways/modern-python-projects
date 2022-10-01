import tkinter as tk
from urllib import response

from guptimer.helpers import check_url

# Dictionary of colors for statuses
COLORS = {
    2: "green",
    3: "yellow",
    4: "bright_red",
    5: "red",
}


def main():
    """Draw a GUI for checking URLs"""

    def check_urls():
        # Grap text from URLs box and split by new lines
        urls_string = urls_box.get("1.0", tk.END)
        urls = urls_string.rstrip().split("\n")

        # Enable response box for editing
        response_box.configure(state="normal")

        # Remove contents of the response box
        response_box.delete("1.0", tk.END)

        # Add colorized statuses
        for line, url in enumerate(urls, start=1):
            status_code = check_url(url)
            if status_code:
                response_box.insert(tk.END, str(status_code) + "\n")
                fg_color = COLORS.get(status_code // 100, "magenta")
                response_box.tag_add(fg_color, f"{line}.0", f"{line}.9")
            else:
                response_box.insert(tk.END, "Wrong URL !\n")
                response_box.tag_add("magenta", f"{line}.0", f"{line}.9")

        # Disable response box for editing
        response_box.configure(state="disabled")

    # Create window
    window = tk.Tk()
    window.config(bg="#f6f6f6")

    # Add label for URLs box
    tk.Label(window, text="URLs to check (one per line)").grid(row=0)

    # Add URLs box
    urls_box = tk.Text(window, height=20, width=50)
    urls_box.grid(row=1, column=0)

    # Add reponse box
    response_box = tk.Text(window, height=20, width=10, state="disabled", bg="#f6f6f6")
    response_box.grid(row=1, column=1)

    # Add tags to response box for colors
    response_box.tag_config("green", foreground="#9CCC65")
    response_box.tag_config("yellow", foreground="#FF9800")
    response_box.tag_config("bright_red", foreground="#EF5350")
    response_box.tag_config("red", foreground="#C62828")
    response_box.tag_config("magenta", foreground="#9C27B0")

    # Add check URLs button
    check_button = tk.Button(window, text="Check", command=check_urls)
    check_button.grid(row=2)

    # Start main loop
    window.mainloop()


# Test URLs:
# http://httpstat.us/200
# http://httpstat.us/301
# http://httpstat.us/404
# http://httpstat.us/500

if __name__ == "__main__":
    main()
