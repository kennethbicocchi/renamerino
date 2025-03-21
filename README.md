## Renamerino
The renaming experience

## Experience the beautiful minimal design

oh boy....
![images/renamerino_screenshot.png](https://github.com/kennethbicocchi/renamerino/blob/main/renamerino1.png)

## How it works

1. **User opens the app**: Launch Renamerino, which displays a simple Tkinter GUI.
2. **Select Folder**: Browse to the directory containing the files you want to rename.
3. **Enter a Prefix**: (e.g., "MyDocs") for your new file names.
4. **Check "Include current date"** if desired.
5. **Click "Rename Files"**:
   - The application scans each file in the selected folder.
   - It counts files by extension (.txt, .jpg, etc.) and applies a separate numeric sequence.
   - It renames the files to `<prefix>_YYYYMMDD_#` or `<prefix>_#`, depending on user choices.
6. **Done**: A confirmation message pops up, and the files have new names!

## This seems cool! But.... how do I get it?!

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
