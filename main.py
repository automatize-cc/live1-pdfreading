from PyPDF2 import PdfReader
import re

filename = '1t23_sker-demonstracoes-financeiras-e-press-release.pdf'
file = open(filename, 'rb')
pdf = PdfReader(file)

pages = pdf.pages

num_of_pages = len(pages)

page1 = pages[0].extract_text()

regex1 = 'Indicadores Econômicos'
regex2 = 'Receita líquida \(R\$ mil\)(.*)'
regex3 = 'Principais Indicadores(.*)'
regex4 = 'EBITDA ICVM 527\(R\$ mil\)(.*)'
regex5 = 'Margem EBITDA \(%\)(.*)'
regex6 = 'Lucro líquido \(R\$ mil\)(.*)'
regex7 = 'Dívida Líquida \(R\$ milhões\)(.*)'
regex8 = 'Preço bruto \(R\$/MWh\)(.*)'
regex9 = 'Energia gerada \(GWh\)(.*)'
regex10 = 'Disponibilidade \(%\)(.*)'
regex11 = 'EBITDA Recorrente\(R\$ mil\)(.*)'
regex12 = 'Margem EBITDA Recorrente\(%\)(.*)'

regex13 = '6 – Perfil do Endividamento'
regex14 = 'Dívida Líquida \(R\$ mil\)(.*)'
regex15 = 'Endividamento(.*)'
regex16 = 'EBITDA \(últimos 12 meses\)(.*)'

for page in pages:
    text = page.extract_text()

    match1 = re.search(regex1, text) 
    match2 = re.search(regex2, text)
    match3 = re.search(regex3, text)
    match4 = re.search(regex4, text)
    match5 = re.search(regex5, text)
    match6 = re.search(regex6, text)
    match7 = re.search(regex7, text)
    match8 = re.search(regex8, text)
    match9 = re.search(regex9, text)
    match10 = re.search(regex10, text)
    match11 = re.search(regex11, text)
    match12 = re.search(regex12, text)
    match13 = re.search(regex13, text)
    match14 = re.search(regex14, text)
    match15 = re.search(regex15, text)
    match16 = re.search(regex16, text)
            
    receita_liquida = {}

    if match1 and match2 and match3 and match4 and match5 and match6 and \
       match7 and match8 and match9 and match10 and match11 and match12:
        
        receita = match2[1].split()
        indicadores = match3[1].split()

        receita_liquida[indicadores[0]] = receita[0]
        receita_liquida[indicadores[1]] = receita[1]
        
        print(receita_liquida)
        
    
    endividamento = {}
    if match13 and match14:

        titulos = match14[1]
        divida = match15[1].split()
        
        regex_data = '\d+ de \D+?\sde \d{4}'
        
        titulos = re.findall(' *\d+ de \D+?\sde \d{4} *| *Diferença nominal *|Var. %', titulos)
        for i, titulo in enumerate(titulos):
            endividamento[titulo.strip()] = divida[i]
            
        print(endividamento)