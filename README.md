# WireWorld
This repository contains information the wiring of all the electrical systems in the car.

## Generator script
This script allows us to combine various xml or .drawio files into one single .drawio file.
To export your sheets go into the Master_diagram.drawio file and do File -> Export As -> Uncheck 'All pages' -> Export this will export the sheet you're currently on as a .xml file. Make sure to save it into the 'diagrams' folder.
The script works by deleting the old Master_diagram.drawio file, going through the diagrams folder and merging every file that ends in .drawio or .xml, and exports that as Master_diagram.drawio. This means that any xml sheet not in the diagrams folder will not be represented in the new Master_diagram.drawio and your old changes will be gone.
To use the generator script, simply call `python diagram_generator.py`. This will combine the various xml files representing sub-diagrams into one large XML file which can be opened as a draw.io notebook. Ensure that you have Python installed.
