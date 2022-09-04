# Problem statement:
# Design Unix File Search API to search file with different arguments as "extension", "name", "size" ...
# The design should be maintainable to add new contraints.

# Which pattern you should use?
# Answer: Specification pattern, create for each criteria a specification class

# Follow up: How would you handle if some contraints should support AND, OR conditionals.
# I did not provided it yet. Even though below solution took 30 minutes. Solution: use Specification pattern.


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.children = []
        self.isDirectory = False if "." in name else True
        self.children = []
        self.extension = name.split(".")[1] if "." in name else ""

    def __repr__(self):
        return "{" + self.name + "}"


class filter:
    def __init__(self):
        pass

    def apply(self, file):
        pass


class minSizeFilter(filter):
    def __init__(self, size):
        self.size = size

    def apply(self, file):
        return file.size > self.size


class extensionFilter(filter):
    def __init__(self, extension):
        self.extension = extension

    def apply(self, file):
        return file.extension == self.extension


class fileSystem:
    def __init__(self):
        self.filters = []

    def addFilter(self, givenFilter):
        if isinstance(givenFilter, filter):
            self.filters.append(givenFilter)

    def applyORFiltering(self, root):
        def dfs(root, result):
            if root.isDirectory:
                for child in root.children:
                    dfs(child, result)
            else:
                for filter in self.filters:
                    if filter.apply(root):
                        result.append(root)
                        print(result)
                        return

        result = []
        dfs(root, result)
        return result

    def applyANDFiltering(self, root):
        def dfs(root, result):
            if root.isDirectory:
                for child in root.children:
                    dfs(child, result)
            else:
                for filter in self.filters:
                    if not filter.apply(root):
                        return
                result.append(root)
                print(result)

        result = []
        dfs(root, result)
        return result


f1 = File("root_300", 300)

f2 = File("fiction_100", 100)
f3 = File("action_100", 100)
f4 = File("comedy_100", 100)
f1.children = [f2, f3, f4]

f5 = File("StarTrek_4.txt", 4)
f6 = File("StarWars_10.xml", 10)
f7 = File("JusticeLeague_15.txt", 15)
f8 = File("Spock_1.jpg", 1)
f2.children = [f5, f6, f7, f8]

f9 = File("IronMan_9.txt", 9)
f10 = File("MissionImpossible_10.rar", 10)
f11 = File("TheLordOfRings_3.zip", 3)
f3.children = [f9, f10, f11]

f11 = File("BigBangTheory_4.txt", 4)
f12 = File("AmericanPie_6.mp3", 6)
f4.children = [f11, f12]


greater5 = minSizeFilter(5)
txtFilter = extensionFilter("txt")

myFileSystem = fileSystem()
myFileSystem.addFilter(greater5)
myFileSystem.addFilter(txtFilter)

print(myFileSystem.applyORFiltering(f1))

print(myFileSystem.applyANDFiltering(f1))
