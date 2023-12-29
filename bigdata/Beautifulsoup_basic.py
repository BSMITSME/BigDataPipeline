from bs4 import BeautifulSoup

html = """
<html><body>
<div id = 'project'>
	<h1 id = 'title'>BIG DATA PROGRAMING</h1>
	<p id = 'body'>DATA ANLYSIS AND SCIENCE</p>
	<p>DATA ACQUISITION PART1</p>
	</ul>
	<ul class='items'>
		<li>CRAWLING</li>
		<li>SCRAPPING</li>
		<li>HYBRID WAY</li>
</div>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling
print(h1.string)
print(p1.string)
print(p2.string)