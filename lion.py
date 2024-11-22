import docx
import matplotlib.pyplot as plt
from collections import Counter

lion = docx.Document('lion.docx')
text = []
for paragraph in lion.paragraphs:
    text.append(paragraph.text)
text = '/n'.join(text)
text_slova = text.lower()
text_slova = text_slova.split()

filter.slova = text.strip(" .,!?()[]{}/';#%:^*--")
for slova in text.slova:
    



