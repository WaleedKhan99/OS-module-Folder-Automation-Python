import os

if (not os.path.exists("data")):
    os.mkdir("data")
for i in range(0, 20):
    os.mkdir(f"data/Waleed{i+1}")
