# importing csv module
import csv
import pandas as pd
  
# initializing the titles and rows list
fields = []
rows = []
  
col_list = ["Link", "GoogleScholar"]
df = pd.read_csv("a.csv", usecols=col_list)

import csv
with open('a.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)

 for row in data:
   print("<tr>"+"<td>"+row['Name']+"</td>"),
   print('\n'),
   print("<td>"+row['College']+"</td>"),
   print('\n'),
   print("<td>"+row['Branch']+"</td>"),
   print('\n'),
   print("<td>"+row['Interest']+"</td>"),
   print('\n'),
   print("<td>"+"<div class=\"dropdown\">"+"<button class=\"dropbtn\">Details</button>"+"<div class=\"dropdown-content\">"+"<a href="+"\""+row['Link']+"\""+" "+"target=\"_blank\">Profile</a>")
   print('\n'),
   print("<a href="+"\""+row['GoogleScholar']+"\""+" "+"target=\"_blank\">Publications</a>"+"<p></p></div></td></tr>")