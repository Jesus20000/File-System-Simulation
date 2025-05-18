from filesystem import FileSystemComponent

class Folder(FileSystemComponent):
    def __init__(self, name):
        super().__init__(name)
        self._children = []

    def add(self, component: FileSystemComponent):
        self._children.append(component)

    def remove(self, component: FileSystemComponent):
        self._children.remove(component)

    def get_size(self):
        return sum(child.get_size() for child in self._children)

    def display(self, indent=0):
        print(" " * indent + f"📁 {self.name}/")
        for child in self._children:
            child.display(indent + 2)