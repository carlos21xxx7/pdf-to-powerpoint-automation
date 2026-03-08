# PDF to PowerPoint Automation
#### Video Demo: https://youtu.be/AaaM9Z8w-E8
#### Description:

In many technical and engineering environments, presentations often need to be updated when new plans, diagrams, or drawings are released in PDF format. Updating PowerPoint slides manually can be repetitive and time-consuming, especially when many slides must be replaced. This project solves that problem by automating the process.

This Python program updates PowerPoint slides using pages from a PDF file. The user specifies which PDF page should be inserted into which PowerPoint slide, and the program performs the update automatically.

The program is organized into several parts:

First, the program collects the necessary inputs. The user is asked for the name of the PDF file and the PowerPoint presentation that will be updated. The program also asks whether a mapping file already exists. The mapping file defines which PDF page corresponds to each PowerPoint slide.
If the mapping file already exists, the program loads it from a CSV file called "mapping.csv". Each row in the file contains two numbers: the PDF page and the PowerPoint slide number. This allows the program to know exactly which content should replace each slide.
If the mapping file does not exist, the program allows the user to create it interactively. The user enters pairs in the format "PDFpage-PPTslide", such as "4-15". These pairs are stored in a list and then saved into "mapping.csv" so they can be reused in future executions.

After the inputs and mapping are prepared, the program begins the update process. It opens the PDF file using the PyMuPDF library and opens the PowerPoint presentation using the python-pptx library. For each pair in the mapping, the program loads the corresponding page of the PDF and converts it into an image. This step is necessary because PowerPoint slides insert images rather than PDF pages directly.

Next, the program locates the corresponding slide in the PowerPoint presentation. Any previous images on that slide are removed to ensure that the old content does not remain.
The newly generated image is then inserted into the slide, covering the entire slide area. This effectively replaces the old content with the new plan or diagram from the PDF.
Once all mappings have been processed, the program saves the updated presentation as a new file. The new file uses the original PowerPoint name with "_updated" added at the end of the filename.

During the process, temporary image files are created to store the converted PDF pages. At the end of the program, these temporary files are deleted automatically to keep the project folder clean.

Overall, this tool automates a task that would otherwise require manually copying and pasting content between documents. It helps reduce repetitive work and makes it easier to keep presentations synchronized with updated technical documents.
