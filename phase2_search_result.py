from __future__ import division
from textblob import TextBlob
import sqlite3
import sys
import matplotlib.pyplot as plt
import numpy as np

conn = sqlite3.connect('albertanus.db')
c = conn.cursor()

#create FTS search database
c.execute("CREATE VIRTUAL TABLE  if not exists fts_albertanus USING fts4(title, book, language, author, dates, chapter, verse, passage, link)")
c.execute("INSERT INTO fts_albertanus SELECT * from albertanus")

search = raw_input("Please enter search term: ")
search = TextBlob(search)
#language detection
if search.detect_language() == 'en':
    search = search.translate(to='la')
    print "Your search is English and is trasfered to Latin as: ", search
    print "start search ..."
    
elif search.detect_language() == 'la':
    print "Your search is Latin: ", search
    print "start search ..."
else:
    print "The search word is neither Enlgish nor Latin"
    sys.exit(0)

search = str(search)
search = unicode(search, "utf-8")

#c.execute("SELECT count(*) FROM fts_albertanus WHERE passage MATCH '{}' ".format(search))
#result = c.fetchall()

c.execute("SELECT chapter, passage, link FROM fts_albertanus WHERE passage MATCH '{}' ".format(search))
#c.execute("SELECT chapter, passage, link FROM albertanus WHERE passage like '%{}%' ".format(search))
result = c.fetchall()

print "Total number of matched passages:", len(result)

print "chapter", "snippet, ", "link"
for i in xrange(0, len(result)):
    print 'record ',i+1, result[i][0].encode('utf-8'), result[i][1].encode('utf-8'), result[i][2].encode('utf-8')


#plot g bar chart: counts over chapters
c.execute("SELECT chapter, count(*) FROM fts_albertanus WHERE passage MATCH '{}' GROUP BY chapter ".format(search))
result = c.fetchall()
sorted_by_height = sorted(result, key=lambda tup: tup[1], reverse=True)  #sort by counts
chapters = []
counts = []
for i in xrange(len(result)):
    chapters.append(sorted_by_height[i][0])
    counts.append(sorted_by_height[i][1])

bar_width = 0.6
opacity = 0.4
index = np.arange(len(chapters))
rects1 = plt.bar(index, counts, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Counts')

plt.xlabel('Chapter')
plt.ylabel('Counts')
plt.title('Counts by chapter')
plt.xticks(index + 0.5*bar_width, chapters)
plt.legend()

plt.tight_layout()
plt.show()

# Save (commit) the changes
conn.commit()

conn.close()