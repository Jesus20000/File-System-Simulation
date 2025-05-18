# 🗂️ File System Simulation

This project demonstrates the **Composite Design Pattern** in Python by simulating a hierarchical file system. It supports recursive folder structures containing files and subfolders, and allows unified operations such as calculating total size and displaying structure.

---

## 🛠️ Technologies Used

- Python 3.x  
- Object-Oriented Programming  
- Composite Design Pattern

---

## 🧠 Design Pattern: Composite

The **Composite Pattern** allows treating individual objects (files) and compositions of objects (folders) uniformly. It is ideal for representing tree structures like file systems where each folder can contain both files and subfolders.

---

## 📁 Project Structure

- `filesystem.py` – Abstract base class for File and Folder  
- `file.py` – Implements the File leaf node  
- `folder.py` – Implements the Folder composite node  
- `main.py` – Demonstrates file/folder hierarchy and operations  
- `README.md` – Project documentation

---

## 🚀 Features

- Create folders that contain files and subfolders  
- Display full directory tree with indentation  
- Recursively calculate total size of any folder  
- Clean and extendable structure for real-world simulations

---

## 📌 Sample Output

```

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

````

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/file-system-simulation.git
cd file-system-simulation
````

2. Run the main script:

```bash
python main.py
```

