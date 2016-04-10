- Part A: Data Extraction

To download and test if the all the contents of albertanus are downloaded
  urllib2 is used to extract html pages and save them into txt files
  test compares whether or not all html links are included in the main function
  

run the program as following:
  
python phase1_albertanus.py
  
py.test phase1_albertanus.py




- Part B: Database Population

I use a different way to create the database without downloading the html files. 
Step 1, use BeautifulSoup to get text from url
Step 2, use sent_tokenize to do sentence tokenize and insert each into database iteratively
Step 3, FTS search system is built over the passage attribute

The code is phase1_population.py and the SQLite database is albertanus.db.

I have checked the contents, it should be correct according to the project requirements.

A FTS table has been created by FTS4.


run the program as following:
python phase1_population.py

Since the database is too large 347MB, I can not upload it on jaunx.ou.edu. However, the program should build a database on your local machine and print the results. It runs correctly on my windows machine, if you have any problems, please send me an email.

It is not required to run download html files to build the database. That is to say, we do not need to run python phase1_albertanus.py



- Part C: Translation code
I use another python package named textblob as the translation API
to run the code you need to install it on your machine.

1. The code can detect the language, if it is Englishs, it will be translated to Latin; if it is Latin, just pass; otherwise, it will print the error: "The search word is neither English nor Latin"
2. The program will search the term in FTS table and return the number of matched rows.

Run:
python phase2_translation.py


Part D: Search results and visualization

1. connect with albertans.db
2. create FTS table fts_albertanus
3. read the user input
4. detect the type of language, if it is Englishs, it will be translated to Latin; if it is Latin, just pass; otherwise, it will print the error: "The search word is neither English nor Latin"
5. search the matched passages
6. print the record id, chapter, passage, link
7. produce the bar chart 

Example of code running:
open command prompt:
run python phase2_search_result.py
It will ask you to enter the search term
“Please enter search term: hope (my input)”
It will print all the records (too many to be pasted here) and the graph (compressed in the zip fold).

Tests I have done: 
- search hope
- search death

no errors reported for these two search


Files in the .zip

- Readme.txt
- phase1_albertanus.py
- phase1_population.py
- pre-populated files
- albertanus.db (too large, removed)
- phase2_translation.py
- phase2_search_result.py
- hope_barchart.png

