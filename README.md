File System Simulation - Composite Design Pattern

Overview:
This project demonstrates the Composite Design Pattern by modeling a file system with folders and files. 
Folders can contain both files and other folders, allowing recursive operations like calculating total size and displaying structure.

Structure:
- filesystem.py: Abstract base class (FileSystemComponent) for all file system components.
- file.py: File class that represents a leaf node (individual file).
- folder.py: Folder class that represents a composite node (can contain other components).
- main.py: Demo script that builds a sample structure and displays it.
- README.md: Project description and usage guide.

How to Run:
1. Save all files in the same folder.
2. Open terminal and navigate to that folder.
3. Run:

   python main.py

Expected Output:
- Shows a tree-like file system structure.
- Calculates and prints the total size of all files recursively.

Example:
🗂 File System Structure:

📁 root/
  📄 README.md (5 KB)
  📄 setup.py (2 KB)
  📁 src/
    📄 main.py (15 KB)
    📄 utils.py (7 KB)
  📁 assets/
    📄 logo.png (150 KB)
    📄 bg.jpg (300 KB)

📦 Total size of 'root': 479 KB
