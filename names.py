import sys

names =["Bill", "Charlie", "Fred", "George", "Ginny", "Percy", "Ron"]

if "Robert" in names:
    print("Found")
    sys.exit(0)

print("Not Found")
sys.exit(1)