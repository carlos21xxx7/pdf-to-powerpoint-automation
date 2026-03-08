# This project is a Python tool that automates updating PowerPoint slides using pages from a PDF. The user provides a mapping between PDF pages
# and PowerPoint slides, and the program automatically converts each PDF page into an image, deletes the old one and inserts it into the corresponding slide. This helps
# save time and reduce manual work when presentations need to be updated with new plans, diagrams, or drawings.


from pptx import Presentation
import fitz
import os
import sys
import csv


def main():
    pdf_file, ppt_file, mapping = get_inputs()
    update_ppt(pdf_file, ppt_file, mapping)
    delete_temp()


def get_inputs():
    print("============================================================")
    print("Program to copy pages from a PDF into slides in a PowerPoint")

    answer = input("Do you already have mapping.csv? yes/no: ").lower()

    if answer == "yes":
        mapping = load_mapping()
    elif answer == "no":
        mapping = make_mapping()
    else:
        sys.exit("Invalid answer")

    pdf_file = input("PDF name: ")
    ppt_file = input("PPT name: ")

    if not pdf_file.endswith(".pdf"):
        pdf_file = pdf_file + ".pdf"
    if not ppt_file.endswith(".pptx"):
        ppt_file = ppt_file + ".pptx"

    return pdf_file, ppt_file, mapping

def load_mapping():

    mapping = []

    try:
        file = open("mapping.csv")
    except FileNotFoundError:
        sys.exit("mapping.csv not found")

    reader = csv.reader(file)

    for row in reader:
        pdf_page = int(row[0])
        ppt_slide = int(row[1])
        mapping.append((pdf_page, ppt_slide))

    file.close()

    return mapping


def make_mapping():

    print("Write mapping like this: PDFpage-PPTslide")
    print("Example: 4-15")
    print("Write 'done' when finished")

    mapping = []

    while True:

        text = input("Mapping: ")

        if text == "done":
            break

        parts = text.split("-")

        if len(parts) != 2:
            print("Wrong format")
            continue

        try:
            pdf_page = int(parts[0])
            ppt_slide = int(parts[1])
        except:
            print("Numbers only")
            continue

        mapping.append((pdf_page, ppt_slide))

    file = open("mapping.csv", "w", newline="")
    writer = csv.writer(file)

    for item in mapping:
        writer.writerow(item)

    file.close()

    return mapping


def update_ppt(pdf_file, ppt_file, mapping):

    pdf = fitz.open(pdf_file)
    prs = Presentation(ppt_file)

    width = prs.slide_width
    height = prs.slide_height

    for item in mapping:

        pdf_page = item[0]
        ppt_slide = item[1]

        pdf_index = pdf_page - 1
        ppt_index = ppt_slide - 1

        if pdf_index < 0 or pdf_index >= pdf.page_count:
            print("Skipping pdf page", pdf_page)
            continue

        if ppt_index < 0 or ppt_index >= len(prs.slides):
            print("Skipping slide", ppt_slide)
            continue

        page = pdf.load_page(pdf_index)

        image = page.get_pixmap(dpi=100)

        filename = "_temp_page_" + str(pdf_page) + ".jpg"

        image.save(filename)

        slide = prs.slides[ppt_index]

        # remove old images
        remove_list = []

        for shape in slide.shapes:
            if shape.shape_type == 13:
                remove_list.append(shape)

        for shape in remove_list:
            slide.shapes._spTree.remove(shape._element)

        picture = slide.shapes.add_picture(
            filename,
            0,
            0,
            width=width,
            height=height
        )

        slide.shapes._spTree.remove(picture._element)
        slide.shapes._spTree.insert(1, picture._element)

        print("Copied page", pdf_page, "to slide", ppt_slide)

    base = os.path.splitext(ppt_file)[0]

    output = base + "_updated.pptx"

    prs.save(output)

    print("Saved as", output)


def delete_temp():

    files = os.listdir()
    for name in files:
        if name.startswith("_temp_page_"):
            os.remove(name)


if __name__ == "__main__":
    main()
