# Sticky To-Do Desktop Application

A production-ready **Windows desktop productivity application** built using **Python and PyQt5**.  
The application functions as a persistent desktop widget that launches automatically on system startup and maintains task state across device restarts until tasks are explicitly completed.

---

## Project Overview

Sticky To-Do is a lightweight, distraction-free task management application designed to solve a common productivity issue: losing important reminders after closing applications or restarting the system.

The application remains fixed on the desktop, avoids overlapping active applications, and provides a clean, visually clear interface for managing daily tasks efficiently.

This project demonstrates strong fundamentals in **desktop application development**, **UI/UX design**, **persistent data handling**, and **Windows OS integration**.

---

## Key Features

- Persistent task storage across system restarts
- Automatic application launch on Windows startup
- Desktop-only widget behavior (non-intrusive to active applications)
- Tasks remain visible until marked completed
- One-click task completion with permanent deletion
- Fixed placement on the right side of the desktop
- Frameless, minimal UI with vibrant, eye-friendly colors
- Standalone Windows executable support

---

## Engineering Highlights

- Implemented **file-system-safe persistence** using Windows AppData to ensure task reliability across startup executions
- Designed **event-driven UI interactions** using PyQt5 signals and slots
- Applied **custom window flags** to restrict rendering to desktop layers only
- Packaged the application into a **standalone executable** using PyInstaller
- Focused on readability, accessibility, and minimal visual clutter

---

## Technology Stack

- **Programming Language:** Python 3  
- **GUI Framework:** PyQt5  
- **Data Storage:** JSON (local persistent storage)  
- **Build Tool:** PyInstaller  
- **Operating System:** Windows  

---

## Application Workflow

1. Application launches automatically on system startup
2. Tasks are loaded from persistent local storage
3. User adds tasks via the input field
4. Tasks remain visible across laptop restarts
5. Clicking a task marks it as completed and removes it permanently

---

## Persistent Storage

Tasks are stored locally at:

C:\Users<username>\AppData\Roaming\StickyTodo\tasks.json


This ensures consistent behavior regardless of how the application is launched.

---

## Project Structure

StickyTodo/

├── sticky_todo.py # Core application logic
├── README.md # Project documentation
├── .gitignore # Git ignore rules






## Installation & Execution

### Development Mode

**Prerequisites**
- Python 3.8+
- pip package manager

```bash
pip install PyQt5

python sticky_todo.py

Build Windows Executable
pyinstaller --onefile --noconsole sticky_todo.py

The executable will be generated in the dist/ directory.

Enable Auto-Start on Windows
Press Win + R

Enter:

shell:startup
Create a shortcut to sticky_todo.exe in the Startup folder

The application will now launch automatically on system startup.

###Use Cases
Daily task reminders
Lightweight personal productivity tool
Desktop widget reference implementation
Python GUI application showcase


###Skills Demonstrated
Desktop application development
GUI design with PyQt5
Persistent state management
Windows OS integration
Software packaging and deployment
Clean, maintainable code structure

###Author
Tanuja Prasad

###License
This project is released under the MIT License.
