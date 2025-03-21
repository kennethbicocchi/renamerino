buy me a coffee:
https://buymeacoffee.com/kennethbicocchi

## Renamerino
The renaming experience

Introducing Renamerino – the ultimate file renaming powerhouse! With just one click, transform your clutter into organized perfection. Select your folder, add your custom prefix, and watch Renamerino blast each file into order with its auto-numbering magic. Get ready to rock your file system

## Experience the beautiful minimal design

oh boy...

![images/renamerino_screenshot.png](https://github.com/kennethbicocchi/renamerino/blob/main/renamerino1.png)

experience its power!

![images/renamerino_screenshot.png](https://github.com/kennethbicocchi/renamerino/blob/main/renamerino2.png)

## How it works

1. **User opens the app**: Launch Renamerino, which displays a simple Tkinter GUI.
2. **Select Folder**: Browse to the directory containing the files you want to rename.
3. **Enter a Prefix**: (e.g., "MyDocs") for your new file names.
4. **Check "Include current date"** if desired.
5. **Click "Rename Files"**:
   - The application scans each file in the selected folder.
   - It counts files by extension (.txt, .jpg, etc.) and applies a separate numeric sequence.
   - It renames the files to `<prefix>_YYYYMMDD_#` or `<prefix>_#`, depending on user choices.
   - You don't want dates? So Rnamerino doesn't want dates. Renamerino cares about what YOU care.
   - You want dates? Suddenly Renamerino thinks dates are the best thing in the world. Because you care. 
6. **Done**: A confirmation message pops up, and the files have new names!

## This seems cool! But.... how do I get it?!

First of all, watch your mouth: Renamerino IS the coolest thing ever invented by nature. 

It doesn't "Seem" cool. 
It is. 

Install Python (3.x or higher) with Tkinter support.
Clone or download the repository (for example: git clone https://github.com/kennethbicocchi/Renamerino.git).
Navigate to the project folder (cd Renamerino).
(Optional) Create a virtual environment and activate it. For instance, on Windows: python -m venv venv venv\Scripts\activate and on macOS/Linux: python -m venv venv source venv/bin/activate
(Optional) If you plan to install any extra packages (like pyinstaller), you can do so with pip install <package-name>.
Usage:

1. Run the Python script by typing: python renamerino.py
2. The GUI window will appear:
3. Select Folder: choose the directory containing your files.
4. Prefix: enter a custom prefix (e.g., ProjectA, Images, etc.).
5. Include current date: check this if you want a date (YYYYMMDD) in each filename.
6. Rename Files: click this button to rename the files in place.

##  Are you happy now? You Should. 
Now buy me this coffee:
https://buymeacoffee.com/kennethbicocchi

![bmc_qr (2)](https://github.com/user-attachments/assets/5daed42c-f5d5-4838-97bb-bc052b5a8e6c)

I LOVE not being poor! It's my favourite thing after Renamerino!

## Examples:

Without date: if your prefix is MyDocs and you have .txt, .docx, .jpg files, you might get: MyDocs_1.txt MyDocs_2.txt MyDocs_1.docx MyDocs_2.docx MyDocs_1.jpg ...and so on for each extension.
With date: if today is 2025-03-24 and you checked "Include current date," you would get: MyDocs_20250324_1.txt MyDocs_20250324_2.txt MyDocs_20250324_1.docx etc.
Contributing: Feel free to open issues or submit pull requests if you find bugs or have suggestions for improvements. Any contribution is welcome!
