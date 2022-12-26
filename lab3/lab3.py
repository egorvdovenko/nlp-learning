import re
import spacy
import xlsxwriter

from spacy import displacy

text = open("text.txt", encoding="utf-8").read()
first_paragraph = re.findall('.*?\n', text)[0]

nlp = spacy.load("ru_core_news_sm")
doc = nlp(first_paragraph)

sentence_spans = list(doc.sents)

for ss in sentence_spans:
  print(ss)
  print('***')

  for token in ss:
    print(token.text, ": ", token.dep_, ": ", spacy.explain(token.dep_))

  print('***')

# Визуализировать граф синтаксического разбора для предложений первого абзаца. Сохранить в файле png.

sentence_spans = list(doc.sents)
html = displacy.render(sentence_spans, style="dep", page=True)
svg = displacy.render(sentence_spans, style="dep")

open("sentence.html", "w", encoding="utf-8").write(html)
open("sentence.svg", "w", encoding="utf-8").write(svg)

# Сформировать список: для каждого предложения рассказа указать подлежащее и сказуемое. Оценить точность работы алгоритма.

workbook = xlsxwriter.Workbook("sentence.xlsx")
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, "N")
worksheet.write(0, 1, "NSUBJS")
worksheet.write(0, 2, "ROOTS")

for ssi, ss in enumerate(sentence_spans):
  nsubjs = list()
  roots = list()

  for token in ss:
    if "nsubj" in token.dep_:
      nsubjs.append(token.text.lower())
    elif "ROOT" in token.dep_:
      roots.append(token.text.lower())
  
  worksheet.write(ssi + 1, 0, ssi + 1)
  worksheet.write(ssi + 1, 1, ",".join(nsubjs))
  worksheet.write(ssi + 1, 2, ",".join(roots))

workbook.close()
