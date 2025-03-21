Renamerino

Renamerino is a simple automatic file renaming tool built with Python and Tkinter. It allows you to:

Select a folder with the files you want to rename.
Provide a custom prefix.
Optionally include the current date (in YYYYMMDD format) in each filename.
Use separate counters for each file extension (e.g., .txt, .pdf, .jpg each get their own sequence).
Features:

GUI-based interface: no command line needed – just click and rename!
Extension-aware counting: each file type (.txt, .jpg, .pdf, etc.) has its own incrementing sequence.
Conflict detection: if a file with the new name already exists, the tool will skip that file.
Cross-platform source: the Python script runs on Windows/Mac/Linux, as long as Python and Tkinter are installed.
Installation:

Install Python (3.x or higher) with Tkinter support.
Clone or download the repository (for example: git clone https://github.com/kennethbicocchi/Renamerino.git).
Navigate to the project folder (cd Renamerino).
(Optional) Create a virtual environment and activate it. For instance, on Windows: python -m venv venv venv\Scripts\activate and on macOS/Linux: python -m venv venv source venv/bin/activate
(Optional) If you plan to install any extra packages (like pyinstaller), you can do so with pip install <package-name>.
Usage:

Run the Python script by typing: python renamerino.py
The GUI window will appear:
Select Folder: choose the directory containing your files.
Prefix: enter a custom prefix (e.g., ProjectA, Images, etc.).
Include current date: check this if you want a date (YYYYMMDD) in each filename.
Rename Files: click this button to rename the files in place.
Examples:

Without date: if your prefix is MyDocs and you have .txt, .docx, .jpg files, you might get: MyDocs_1.txt MyDocs_2.txt MyDocs_1.docx MyDocs_2.docx MyDocs_1.jpg ...and so on for each extension.
With date: if today is 2025-03-24 and you checked "Include current date," you would get: MyDocs_20250324_1.txt MyDocs_20250324_2.txt MyDocs_20250324_1.docx etc.
Contributing: Feel free to open issues or submit pull requests if you find bugs or have suggestions for improvements. Any contribution is welcome!
