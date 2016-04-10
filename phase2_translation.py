from __future__ import division
from textblob import TextBlob
import sqlite3
import sys


def tranlate_check():
    text = u'hope'
    assert search.translate(to='la') == 'spem'
    
def search_check():
    global result
    assert result[0][0] == 64
    
conn = sqlite3.connect('albertanus.db')
c = conn.cursor()

#create FTS search database
c.execute("CREATE VIRTUAL TABLE  if not exists fts_albertanus USING fts4(title, book, language, author, dates, chapter, verse, passage, link)")
c.execute("INSERT INTO fts_albertanus SELECT * from albertanus")

search = TextBlob(u'hope')
#language detection
if search.detect_language() == 'en':
    search = search.translate(to='la')
elif search.detect_language() == 'la':
    pass
else:
    print "The search word is neither Enlgish nor Latin"
    sys.exit(0)
    
c.execute("SELECT count(*) FROM fts_albertanus WHERE passage MATCH '{}' ".format(search))
result = c.fetchall()

print "Number of rows match ", str(search), result[0][0]

    
# Save (commit) the changes
conn.commit()

conn.close()