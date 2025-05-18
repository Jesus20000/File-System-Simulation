from file import File
from folder import Folder

def main():
    root = Folder("root")
    root.add(File("README.md", 5))
    root.add(File("setup.py", 2))

    src = Folder("src")
    src.add(File("main.py", 15))
    src.add(File("utils.py", 7))

    assets = Folder("assets")
    assets.add(File("logo.png", 150))
    assets.add(File("bg.jpg", 300))

    root.add(src)
    root.add(assets)

    print("\n🗂 File System Structure:\n")
    root.display()

    print(f"\n📦 Total size of 'root': {root.get_size()} KB\n")

if __name__ == "__main__":
    main()
