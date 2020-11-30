#!/usr/bin/python2

import jinja2 as j2
t = j2.Template( open("template-xdxf").read() )

dic = { 
  "gato":"cat",
  "cão": "dog",
  "formiga": "ant",
  "pássaro": "bird",
  "abelha": "bee",
  "vaca": "cow",
} 

print(t.render({ 
   'tit' : 'Dicionário Pt-En',
   'fultit' : 'Grande Dicionário Pt-En',
   'l1'  : 'POR',
   'l2'  : 'ENG',
   'date' : 2020,
   'lexi': dic,
   } ))
