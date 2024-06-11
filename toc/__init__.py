"""
Table of contents generator for html
"""
import re
from xml.dom.minidom import getDOMImplementation

import html5lib


__version__ = '0.0.14'


# def traverse_headings(doc):
#     return reduce(operator.add, map(doc.getElementsByTagName, ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']))


def table_of_contents(html, url='', anchor_type='stacked-number', quote_attr_values='spec'):
    index = [0, 0, 0, 0, 0, 0]
    depth = 0

    toc_doc = getDOMImplementation().createDocument(None, 'ol', None)
    toc = ol = toc_doc.documentElement

    doc = html5lib.parse(html, treebuilder='dom', namespaceHTMLElements=False)
    for header in traverse_headings(doc.documentElement):
        nextdepth = int(header.nodeName[1])

        if nextdepth > depth:
            for i in range(nextdepth, 6):
                index[i - 1] = 0
                
            for i in range(depth, nextdepth):
                next_ol = toc_doc.createElement('ol')
                ol.appendChild(next_ol)
                ol = next_ol
        elif nextdepth < depth:
            for i in range(nextdepth, depth): ol = ol.parentNode
            
        depth = nextdepth
            
        index[depth - 1] += 1
        label = '-'.join([str(index[d]) for d in range(0, depth) if index[d]])

        li = toc_doc.createElement('li')
        a = toc_doc.createElement('a')
        a.setAttribute('href', '%s#header-%s' % (url, label))
        a.appendChild(doc.createTextNode(innerText(header)))
        li.appendChild(a)
        ol.appendChild(li)
        
        header.setAttribute('id', 'header-' + label)
        
        if anchor_type == 'following-marker':
            anchor = toc_doc.createElement('a')
            anchor.setAttribute('href', '#header-%s' % label)
            anchor.setAttribute('class', 'toc-anchor')
            anchor.appendChild(doc.createTextNode('#'))
            header.appendChild(anchor)
        else:
            anchor = toc_doc.createElement('a')
            anchor.setAttribute('href', '#header-%s' % label)
            anchor.setAttribute('class', 'toc-anchor')
            anchor.appendChild(doc.createTextNode(label))
            header.insertBefore(anchor, header.firstChild)
        

    ol = toc
    while not list(filter(lambda node: node.nodeName == 'li', ol.childNodes)) and list(filter(lambda node: node.nodeName == 'ol', ol.childNodes)):
        ol = list(filter(lambda node: node.nodeName == 'ol', ol.childNodes))[0]
    ol.setAttribute('class', 'toc')

    return (html5lib.serialize(ol, 'dom', quote_attr_values=quote_attr_values),
            html5lib.serialize(doc, 'dom', quote_attr_values=quote_attr_values))
        

def innerHTML(node):
    return ''.join([child.toxml() for child in node.childNodes])

tag_pattern = re.compile('<[^<]+?>')

def innerText(node):
    return re.sub(tag_pattern, '', innerHTML(node))

heading_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']

def traverse_headings(element):
    headings = []

    for child in element.childNodes:
        if child.nodeName in heading_tags:
            headings.append(child)

        headings.extend(traverse_headings(child))

    return headings