from bs4 import BeautifulSoup
import re

html = """
<ul>
	<li><a href = "hoge.html">hoge</li>
	<li><a href = "https://example.com/fuga">fuga</li>
        <li><a href = "https://example.com/foo">foo</li>
        <li><a href = "https://example.com/aaa">ada</li>
</ul>
"""

soup = BeautifulSoup(html, "html.parser")
href_reg = re.compile(r"https://")
li = soup.find_all(href=href_reg)

for e in li:
	print(e.attrs['href'])
	print(e.string)

