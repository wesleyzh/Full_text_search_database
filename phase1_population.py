from __future__ import division
import sqlite3

#only used in weili's mac for packages
import sys
#sys.path.append('/Users/naiyuwang/anaconda/lib/python2.7/site-packages')

#import html2text
import nltk, re, pprint
from nltk import word_tokenize, sent_tokenize
from urllib2 import urlopen
from bs4 import BeautifulSoup


#create the SQlite database
conn = sqlite3.connect('albertanus.db', timeout=10)

c = conn.cursor()

# Create table 
c.execute('''CREATE TABLE if not exists albertanus
             (title text, book text, language text, author text, dates text, chapter text, verse interger, passage text, link text)''')


#url = "http://www.thelatinlibrary.com/albertanus/albertanus1.shtml"
#html = urlopen(url).read().decode('utf8', 'replace')
#raw = BeautifulSoup(html).get_text()
#tokens = sent_tokenize(raw)
#tokens = tokens  #get rid of [an error occurred while processing this directive]

title = u'ALBERTANO OF BRESCIA'
books = [u'DE AMORE ET DILECTIONE DEI', u'DE AMORE ET DILECTIONE DEI', u'DE AMORE ET DILECTIONE DEI', u'DE AMORE ET DILECTIONE DEI',
         u'SERMONES', u'SERMONES', u'SERMONES', u'SERMONES',
         u'Sermo Januensis', u'Liber consolationis et consilii', u'Ars loquendi et tacendi']

language = u'Latin'
author = None
dates = None

chapters = [u'Liber I', u'Liber II', u'Liber III', u'Liber IV',
            u'Sermo I', u'Sermo II', u'Sermo III', u'Sermo IV',
            u'Sermo Januensis', u'Liber consolationis et consilii', u'Ars loquendi et tacendi']

links = [u'http://www.thelatinlibrary.com/albertanus/albertanus1.shtml',
         u'http://www.thelatinlibrary.com/albertanus/albertanus2.shtml',
         u'http://www.thelatinlibrary.com/albertanus/albertanus3.shtml',
         u'http://www.thelatinlibrary.com/albertanus/albertanus4.shtml',
         u'http://www.thelatinlibrary.com/albertanus/albertanus.sermo1.shtml',
         u'http://www.thelatinlibrary.com/albertanus/albertanus.sermo2.shtml',
         u'http://www.thelatinlibrary.com/albertanus/albertanus.sermo3.shtml',
         u'http://www.thelatinlibrary.com/albertanus/albertanus.sermo4.shtml',
         u'http://www.thelatinlibrary.com/albertanus/albertanus.sermo.shtml',
         u'http://www.thelatinlibrary.com/albertanus/albertanus.liberconsol.shtml',
         u'http://www.thelatinlibrary.com/albertanus/albertanus.arsloquendi.shtml']

if len(chapters) != len(links):
    print "Length of chapters is not equal to links"
    sys.exit(0)
    
if len(chapters) != len(books):
    print "Length of chapters is not equal to books"
    sys.exit(0)
    

for i in xrange(len(links)):
    url = links[i]
    html = urlopen(url).read().decode('utf8', 'replace')
    raw = BeautifulSoup(html, "html.parser").get_text()
    tokens = sent_tokenize(raw)    
    book = books[i]
    chapter = chapters[i]
    verse = 1
    for j in tokens:
        passage = j
        c.execute("INSERT INTO albertanus VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", [title, book, language, author, dates, chapter, verse, passage, url])                        
        verse += 1


#create FTS search database
c.execute("CREATE VIRTUAL TABLE  if not exists fts_albertanus USING fts4(title, book, language, author, dates, chapter, verse, passage, link)")
c.execute("INSERT INTO fts_albertanus SELECT * from albertanus")

#c.execute('select count(*) from albertanus')
#a = c.fetchall()
#c.execute('select count(*) from fts_albertanus')
#b = c.fetchall()

# Save (commit) the changes
conn.commit()

conn.close()

print "Database: albertanus.db is created successfully "
print "Table albertanus is created successfully"
print "FTS Table fts_albertanus is created successfully"