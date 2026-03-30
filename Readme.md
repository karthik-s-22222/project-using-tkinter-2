📝 Project Overview
This application serves as a central hub for productivity:
Think Pad: A classic text editor inspired by Notepad, featuring font zooming, printing, and automatic timestamps.
Task Manager: A modern GUI version of a "To-Do List" that replaces traditional CLI (command line) inputs with interactive buttons and a visual list.
✨ Key Features
1. Think Pad (Editor)
File Control: Create, Open, and Save .txt files easily.
Dynamic Zoom: Change font size instantly using the Zoom menu (Fixes the global font_size error).
Time Stamp: Insert current real-world date and time into your notes with one click.
Print Support: Send your current notes directly to the system's default printer.
2. Task Manager (List View)
Visual Tracking: See all your pending tasks in a structured list.
Auto-Persistence: Tasks are saved to tasks.txt automatically—your data is never lost.
Easy Management: Use simple pop-up dialogs to add or remove tasks.
3. Central Dashboard
A clean "Home Screen" that acts as the entry point for both applications.

🛠️ Technical Explanation (Line-by-Line Logic)
tr.Tk() & tr.Toplevel(): Used to create the main Dashboard and the independent secondary windows.
global font_size: Implemented to bridge the scope between the UI and the scaling logic, preventing UnboundLocalError.
os.startfile(..., "print"): Utilises Windows shell commands to communicate with hardware printers.
simpledialog.askstring: Replaces standard Python input() to provide a better user experience in a windowed environment.


