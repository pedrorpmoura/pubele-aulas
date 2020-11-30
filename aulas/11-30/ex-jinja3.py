#!/usr/bin/python2

import jinja2 as j2
t = j2.Template( open("musica.template").read() )


print(t.render({ 
   'name' : "Experiência com Jinja2 + música",
   'c' : 'Turma de PE (versão reduzida)',
   'tit' : '3 galinhas a cantar',
   'vozs' : 'C C G G A A G2 | F F E E D D C2 |]',
   'voza': 'C'
   } ))
