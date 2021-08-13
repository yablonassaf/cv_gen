import docx
from docx import Document
from docx.shared import Inches, Pt

document = Document()


def add_bullet_to_resume(bullets):
    for bullet in bullets:
        document.add_paragraph(
            bullet[0], style='List Bullet'
        )
    document.save('resume_demo.docx')


def add_phone_and_email(phone_num, email):
    if phone_num.__len__() == 10:
        phone_num = phone_num[: 0] + "(" + phone_num[0:]
        phone_num = phone_num[: 4] + ")" + phone_num[4:]
        phone_num = phone_num[: 8] + "-" + phone_num[8:]
    phone_and_email = phone_num + " | " + email
    paragraph = document.add_paragraph(phone_and_email)
    paragraph.style.font.bold = 0
    paragraph.alignment = 1
    paragraph.paragraph_format.space_before = Pt(0)
    paragraph.paragraph_format.space_after = Pt(1)
    document.save('resume_demo.docx')


def create_new_word_file():
    # document.add_heading('Document Title', 0)
    p = document.add_paragraph('A plain paragraph having some ')
    p.add_run('bold').bold = True
    p.add_run(' and some ')
    p.add_run('italic.').italic = True
    document.add_heading('Heading, level 1', level=1)
    # document.add_paragraph('Intense quote', style='Intense Quote')
    add_bullet_to_resume("aabbcc")
    document.add_paragraph(
        'first item in ordered list', style='List Number'
    )
    document.add_paragraph(
        'first 2 in ordered list', style='List Number'
    )
    document.add_picture("eiffel-tower.jpg", width=Inches(1.25))
    records = (
        (3, '101', 'Spam'),
        (7, '422', 'Eggs'),
        (4, '631', 'Spam, spam, eggs, and spam')
    )
    table = document.add_table(rows=1, cols=3)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Qty'
    hdr_cells[1].text = 'Id'
    hdr_cells[2].text = 'Desc'
    for qty, id, desc in records:
        row_cells = table.add_row().cells
        row_cells[0].text = str(qty)
        row_cells[1].text = id
        row_cells[2].text = desc
    document.add_page_break()
    document.save('demo.docx')
    return document


def add_name(name):
    paragraph_name = document.add_paragraph(name)
    document.save('resume_demo.docx')

    style = document.styles['Normal']
    font = style.font
    font.name = 'Times new roman'
    font.size = Pt(11)
    paragraph_name.style = document.styles['Normal']
    paragraph_name.style.font.bold = 1
    paragraph_name.alignment = 1
    paragraph_name.paragraph_format.space_before = Pt(0)
    paragraph_name.paragraph_format.space_after = Pt(0)
    document.save('resume_demo.docx')


class DocWord:
    # default constructor
    def __init__(self, details):
        add_name(details.name)
        add_phone_and_email(details.phone_num, details.email)
        paragraph = document.add_paragraph('EDUCATION')

        document.add_heading('Work Experience', level=1)
        document.save('resume_demo.docx')


class details_test:
    name = "ANTHONY (TONY) STARK"
    phone_num = "8572851027"
    email = "assafy@mit.edu"


if __name__ == '__main__':
    #create_new_word_file()
    obj = DocWord(details_test)
    list1 = ["Aaa", "bbb", "11111"]
    add_bullet_to_resume(list1)
