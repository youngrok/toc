# toc
**toc** is HTML table of contents generator. It parses html, generate table of contents, and put anchors into original html.

## usage
	toc_html, body = table_of_contents(html)
	toc_html, body = table_of_contents(html, url='http://somedomain.com/somepath')
	toc_html, body = table_of_contents(html, anchor_type='following-marker')

* anchor_type
  * following-marker : Add anchor tag to the end of heading tags. Anchor text is `#`
  * stacked-number : Add anchor tag to the begining of heading tags. Anchor text is like `1.2.3`.
* `toc_html`: table of contents 
* `body`: modified html

## install
	pip install toc

## notes
* **toc** use [html5lib](https://github.com/html5lib/html5lib-python) for html parser. It's much slower than the popular xml library for python, [lxml](https://github.com/lxml/lxml), but parses more precisely, especially for html5.
* I don't think [ElementTree](http://docs.python.org/2/library/xml.etree.elementtree.html) is more pythonic than [DOM](http://docs.python.org/2/library/xml.dom). So I used `minidom` for treebuilder and `py-dom-xpath` for xpath.
