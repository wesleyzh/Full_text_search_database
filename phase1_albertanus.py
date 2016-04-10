import urllib2
import sys

def download_html(target_url, id):
    
    url=target_url

    w = open("albertanus{}.txt".format(id), "w")
    for line in urllib2.urlopen(url):
        w.write(line)
    
    w.close()


def get_bytes(s):
    return sys.getsizeof(s)



def test_download():
    global urls
    x = ['http://www.thelatinlibrary.com/albertanus.html', 'http://www.thelatinlibrary.com/albertanus/albertanus1.shtml', 'http://www.thelatinlibrary.com/albertanus/albertanus2.shtml', 'http://www.thelatinlibrary.com/albertanus/albertanus3.shtml', 'http://www.thelatinlibrary.com/albertanus/albertanus4.shtml', 'http://www.thelatinlibrary.com/albertanus/albertanus.sermo1.shtml', 'http://www.thelatinlibrary.com/albertanus/albertanus.sermo2.shtml', 'http://www.thelatinlibrary.com/albertanus/albertanus.sermo3.shtml', 'http://www.thelatinlibrary.com/albertanus/albertanus.sermo4.shtml', 'http://www.thelatinlibrary.com/albertanus/albertanus.sermo.shtml', 'http://www.thelatinlibrary.com/albertanus/albertanus.liberconsol.shtml', 'http://www.thelatinlibrary.com/albertanus/albertanus.arsloquendi.shtml']
    assert x == urls  #too see if all files are downloaded
    


    
urls = []
#download html files from the website
target_url =  "http://www.thelatinlibrary.com/albertanus.html"
urls.append(target_url)
download_html(target_url, 0)
target_url =  "http://www.thelatinlibrary.com/albertanus/albertanus1.shtml"
urls.append(target_url)
download_html(target_url, 1)
target_url =  "http://www.thelatinlibrary.com/albertanus/albertanus2.shtml"
urls.append(target_url)
download_html(target_url, 2)
target_url =  "http://www.thelatinlibrary.com/albertanus/albertanus3.shtml"
urls.append(target_url)
download_html(target_url, 3)
target_url =  "http://www.thelatinlibrary.com/albertanus/albertanus4.shtml"
urls.append(target_url)
download_html(target_url, 4)
target_url =  "http://www.thelatinlibrary.com/albertanus/albertanus.sermo1.shtml"
urls.append(target_url)
download_html(target_url, 5)
target_url =  "http://www.thelatinlibrary.com/albertanus/albertanus.sermo2.shtml"
urls.append(target_url)
download_html(target_url, 6)
target_url =  "http://www.thelatinlibrary.com/albertanus/albertanus.sermo3.shtml"
urls.append(target_url)
download_html(target_url, 7)
target_url =  "http://www.thelatinlibrary.com/albertanus/albertanus.sermo4.shtml"
urls.append(target_url)
download_html(target_url, 8)    
target_url =  "http://www.thelatinlibrary.com/albertanus/albertanus.sermo.shtml"
urls.append(target_url)
download_html(target_url, 9)
target_url =  "http://www.thelatinlibrary.com/albertanus/albertanus.liberconsol.shtml"
urls.append(target_url)
download_html(target_url, 10)
target_url =  "http://www.thelatinlibrary.com/albertanus/albertanus.arsloquendi.shtml"
urls.append(target_url)
download_html(target_url, 11)    

#get the size of all files

size = 0
for id in xrange(0, 12):
    
    file = open("albertanus{}.txt".format(id), "r")
    content = file.read()

    size += get_bytes(content)

pass

