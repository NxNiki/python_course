from pathlib import Path

# create a path object:
Path("C:\\Programs File\\Microsoft")
Path(r"C:\Program Files\Microsoft")
Path("/user/local/")

# create a path object represents the current folder:
Path()

Path("ecommerce/__init__.py")

Path() / Path("ecommerce")
Path() / "ecommerce" / "__init__.py"

Path.home()


# working with paths:

path = Path("ecommerce/__init__.py")

path.exists()
path.is_file()
path.is_dir()
path.mkdir()
path.rmdir()
path.rename("ecommerce2")

print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)

# we are not renaming the file but the path object.
path = path.with_name("file.txt")
path = path.with_suffix("file.txt")

print(path.absolute())

path = path.with_suffix("file.txt")

# working with directories:
path.iterdir()

