import os, re

#first line of concat xml file
header = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
header2 = "<mxfile host=\"app.diagrams.net\">"
footer = "</mxfile>"

#delete the output file if it already exists
if os.path.exists("./Master_diagram.drawio"):
    os.remove("./Master_diagram.drawio")

#concat xml files
retstr = ""
for name in [f for f in sorted(os.listdir("./diagrams")) if f.endswith((".drawio",".xml"))]:
    #read the file
     # file_extension = os.path.splitext(name)[1]
     # if(file_extension == '.drawio' or file_extension == '.xml'):
    print(name + " has been merged!\n")
    with open("./diagrams/" + name, "r") as f:
        content = f.read()
        content = re.sub(".*?xml.*","",content) #strip xml header
        content = re.sub(".*mxfile.*","",content) #remove mxfile start/end tag
        retstr += content
     # else:
        # print(name + " has been skipped :(\n")

# add the header to the top, footer to the bottom
retstr = header + header2 + "\t" + retstr + footer


#write the file
with open("Master_diagram.drawio", "w") as f:
    f.write(retstr)
