import docx
from docx import Document
from docx.shared import Inches
document = Document()


class DocWord:
    # default constructor
    def __init__(self, details):
        document.add_heading(details.name, 0)
        p = document.add_paragraph('Resume demo created by ')
        p.add_run(' Dor').bold = True
        p.add_run(' and ')
        p.add_run('Assaf').italic = True
        document.add_heading('Work Experience', level=1)
        # document.add_paragraph('Intense quote', style='Intense Quote')
        #self.add_bullet_to_resume("aabbcc")
        #document.add_paragraph(
        #    'first item in ordered list', style='List Number'
        #)
        document.save('resume_demo.docx')


    def create_new_word_file(self):
        document.add_heading('Document Title', 0)
        p = document.add_paragraph('A plain paragraph having some ')
        p.add_run('bold').bold = True
        p.add_run(' and some ')
        p.add_run('italic.').italic = True
        document.add_heading('Heading, level 1', level=1)
        #document.add_paragraph('Intense quote', style='Intense Quote')
        self.add_bullet_to_resume("aabbcc")
        document.add_paragraph(
            'first item in ordered list', style='List Number'
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

    def add_bullet_to_resume(self, bullets):
        for bullet in bullets:
            document.add_paragraph(
                bullet[0], style='List Bullet'
            )
        document.save('resume_demo.docx')

    # def word():
    #     mydoc = docx.Document()
    #     mydoc.add_paragraph("This is first paragraph of a MS Word file.")
    #     mydoc = docx.Document("resume.docx")
    #     mydoc.add_paragraph("This is the second paragraph of a MS Word file.")
    #     mydoc = docx.Document("resume.docx")
    #     third_para = mydoc.add_paragraph("This is the third paragraph.")
    #     third_para.add_run(" this is a section at the end of third paragraph")
    #     mydoc.save("resume_template.docx")
    #     mydoc.add_heading("This is level 1 heading", 0)
    #     mydoc.add_heading("This is level 2 heading", 1)
    #     mydoc.add_heading("This is level 3 heading", 2)
    #     mydoc.save("resume_template.docx")
    #     mydoc.add_picture("eiffel-tower.jpg", width=docx.shared.Inches(2), height=docx.shared.Inches(3))
    #     mydoc.save("resume_template.docx")


# if __name__ == '__main__':
#     obj = DocWord()
#     list1 = ["Aaa","bbb","11111"]
#     obj.add_bullet_to_resume(list1)

