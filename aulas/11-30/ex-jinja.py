#!/usr/bin/python2

import jinja2 as j2
## t = t2.Template( open("template-xfdf").read() )
t = j2.Template( """<?xml version="1.0" encoding="UTF-8" ?>
<xdxf lang_from="{{l1}}" lang_to="{{l2}}" format="logical" revision="033">
    <meta_info>
        <title>{{tit}}</title>
        <full_title>{{fultit}}</full_title>
        <file_ver>001</file_ver>
        <creation_date>{{date}}</creation_date>

    </meta_info>
    <lexicon>

 {% for x,v in lexi.items() %}
<ar>
  <k>{{x}}</k>
  <def>{{l2}}: {{v}}</def>
</ar>
 {% endfor %}

    </lexicon>
</xdxf>
""")

dic = { 
  "gato":"cat",
  "cão": "dog",
  "formiga": "ant",
  "pássaro": "bird",
  "abelha": "bee",
} 

print(t.render({ 
   'tit' : 'Dicionário Pt-En',
   'fultit' : 'Grande Dicionário Pt-En',
   'l1'  : 'POR',
   'l2'  : 'ENG',
   'date' : 2020,
   'lexi': dic,
   } ))
