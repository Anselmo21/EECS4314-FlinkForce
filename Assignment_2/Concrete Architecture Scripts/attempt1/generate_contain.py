import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

f_ta = open(os.path.join(__location__, "flink_UnderstandFileDependency.raw.ta"), "r")
lines = f_ta.readlines()
f_ta.close()

instance_lines = []
cLink_lines = []

for line in lines:
    if line.__contains__("$INSTANCE"):
        instance_lines.append(line)
    if line.__contains__("cLinks"):
        cLink_lines.append(line)

# print(len(instance_lines))
# print(len(cLink_lines))

def find_links(file_dir):
    links = []
    for line in cLink_lines:
        split_line = line.split(" ")
        if split_line[1].__contains__(file_dir):
            links.append(split_line[2])
    return links

f_contain = open(os.path.join(__location__, "flink_UnderstandFileDependency.contain"), "w")

for line in instance_lines:
    file_dir = line.split(" ")[1]
    links = find_links(file_dir)
    #print(len(links))

    for link in links:
        f_contain.write(f"contain {file_dir} {link}")
        
f_contain.close()