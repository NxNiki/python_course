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

path = [p for p in path.iterdir() if p.isdir()]
py_files = [p for p in path.glob("*.py")]
# search recursively
py_files = [p for p in path.rglob("*.py")]

# working with files:
path = Path("ecommerce/__init__.py")
path.exist()
path.rename("init.txt")
# delete file:
path.unlink()
path.stat()

from time import ctime
ctime(path.stat().st_ctime)) # st_ctime: creation time

path.read_bytes()
path.read_text()
path.write_text("xxx")

## copy files to a different location:
source = Path("ecommerce/__init__.py")
target = Path() / "__init__.py"

target.write_text(source.read_text())

## a cleaner way:
import shutil
shutile.copy(source, target)

# working with zip files:
from zipfile import ZipFile

# create a zip file object (create a zip file in the current folder):
zip = ZipFile("files.zip", "w")

for path in Path("ecommerce").rglob("*.*"):
  zip.write(path)
zip.close()

## use with statement to avoid zip not closed:
with ZipFile("files.zip", "w") as zip:
  for path in Path("ecommerce").rglob("*.*"):
    zip.write(path)

with ZipFile("files.zip") as zip:
  print(zip.namelist())

  info = zip.getinfo("ecommerce/__init__.py")
  print(info.file_size)
  print(info.compress_size)

  # extract all files in zip to a directory:
  zip.extractall("extract")

# working with csv files:
import csv

file = open("data.csv", "w")
file.close()

with open("data.csv", "w") as file:
  writer = csv.write(file)
  writer.writerow(["transaction_id", "product_id", "price"])
  writer.writerow([1000, 1, 5])
  writer.writerow([1001, 2, 15])


with open("data.csv") as file:
  reader = csv.reader(file)
  # print(list(reader)) # all values are string.

  # we cannot iterate reader twice to comment the above line to run:
  for row in reader:
    print(row)

# working with json file: javascript object notation
import json

movies = [
  {"id": 1, "title": "Terminator", "year": 1989},
  {"id": 2, "title": "Kindergarten Cop", "year": 1993},
]

data = json.dumps(movies)
## write json object to json file:
Path("movies.json").write_text(data)

## read json file:
data = Path("movies.json").read_text()
movies = json.loads(data)


# working with SQLite Database:
import sqlite3

movies = json.loead(Path("movies.json").read_text())

## create a Movies table first: 
## google search db browser for sqlite and find: sqlitebrowser.org

with sqlite3.connect("db.sqlite3") as conn:
  command = "INSERT INTO Movies VALUES(?, ?, ?)"
  for movie in movies:
    conn.execute(command, tuple(movie.values()))
  conn.commit()

## read from data base:
with sqlite3.connect("db.sqlite3") as conn:
  command = "SELECT * FROM Movies"
  cursor = conn.execute(command)
  # for row in cursor:
  #   print(row)
  
  # cursor can only be iterated once:
  movies = cursor.fetchall()


# Timestamps and DateTimes:
import time

time.time() # current datetime as a timestamp

import datetime

dt = datetime.datetime(2018, 1, 1)

from datetime import datetime

dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()
dt = datetime.strptime("2018/01/01", "%Y/%m%d")

## search for python 3 strptime for more

## convert timestamp to datetime object:
dt = datetime.fromtimestamp(time.time())

print(f"{dt.year}/{dt.month}")

print(dt.strftime("%Y/%m%d"))

print(dt2 > dt1)


