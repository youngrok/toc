# toc
**toc** is HTML table of contents generator. It parses html, generate table of contents, and put anchors into original html.

## usage
	toc, body = table_of_contents(html, fragment=True)

* `toc`: table of contents 
* `body`: modified html

## install
	pip install toc

## notes
* **toc** use [html5lib](https://github.com/html5lib/html5lib-python) for html parser. It's much slower than the popular xml library for python, [lxml](https://github.com/lxml/lxml), but parses more precisely, especially for html5.
* I don't think [ElementTree](http://docs.python.org/2/library/xml.etree.elementtree.html) is more pythonic than [DOM](http://docs.python.org/2/library/xml.dom). So I used `minidom` for treebuilder and `py-dom-xpath` for xpath.
