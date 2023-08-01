from PyPDF2 import PdfReader

filename = '1t23_sker-demonstracoes-financeiras-e-press-release.pdf'
file = open(filename, 'rb')
pdf = PdfReader(file)

pages = pdf.pages

num_of_pages = len(pages)

page1 = pages[0].extract_text()

for page in pages:
    content = page.extract_text()

    if 'Indicadores Econômicos' in content:

        lines = content.split('\n')
        for line in lines:
            if 'Receita líquida (R$ mil)' in line:
                dados = line.split()
                print('Receita líquida no 1T23:', dados[4])
                print('Receita líquida no 1T22:', dados[5])