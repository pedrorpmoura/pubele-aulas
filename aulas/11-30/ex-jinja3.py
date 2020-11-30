#!/usr/bin/python2

import jinja2 as j2
t = j2.Template( open("musica.template").read() )


print(t.render({ 
   'name' : "experiencia de música",
   'c' : 'turma de PE',
   'tit' : '3 galinhas',
   'vozs' : 'C C G G A A G2 F F E E D D C2',
   'voza': 'C'
   } ))
