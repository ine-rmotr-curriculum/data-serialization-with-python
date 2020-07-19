import re
from IPython.core.display import HTML
from pprint import pprint

def show(pat, s, flags=re.M):
    if isinstance(pat, str):
        pat = re.compile(pat, flags)
    new = pat.sub(r'·<font color="##AA0000"><b>\g<0></b></font>·', s)
    new = new.replace('\n', '<br/>')
    return HTML(new)

rhyme = '''
Mary had a little lamb
Its fleece as white as snow
And everywhere that Mary
went, the lamb was sure
to go
'''.strip()

couplet = '''
Mary had a little lamb
Its fleece as white as snow
'''.strip()


рифма = '[*] у Мэри был маленький ягненок!'

parts = '''
FORD-2008-xyz37
FORD-1998-ef445
TOYO-1999-wxy66
TOYO-2005-qrst3
FORD-2010-ab614
MAZD-1995-pqr33
TOYO-2013-fg185
TOYO-1997-abc23
FORD-2012-lm034
'''.strip()