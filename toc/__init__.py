from xml.dom.minidom import Element, Text
import xpath
import html5lib
import re

def table_of_contents(label_node, fragment=False):
    index = [0, 0, 0, 0, 0, 0]
    depth = 0
    
    toc = ol = Element('ol')

    doc = html5lib.parse(label_node, treebuilder='dom', namespaceHTMLElements=False)
    for header in xpath.find('//h1|//h2|//h3|//h4|//h5|//h6', doc):
        nextdepth = int(header.nodeName[1])

        if nextdepth > depth:
            for i in range(nextdepth, 6):
                index[i - 1] = 0
            next_ol = Element('ol')
            ol.appendChild(next_ol)
            ol = next_ol
        elif nextdepth < depth:
            ol = ol.parentNode
            
        depth = nextdepth
            
        index[depth - 1] += 1
        label = '.'.join([str(index[d]) for d in range(0, depth) if index[d]])

        li = Element('li')
        a = Element('a')
        a.setAttribute('href', '#header-%s' % label)
        a.appendChild(doc.createTextNode(innerText(header)))
        li.appendChild(a)
        ol.appendChild(li)
        
        header.setAttribute('id', 'header-' + label)
        anchor = Element('a')
        anchor.setAttribute('href', '#header-%s' % label)
        anchor.setAttribute('class', 'toc-anchor')
        anchor.appendChild(doc.createTextNode(label))
        header.insertBefore(anchor, header.firstChild)

    ol = toc
    while not filter(lambda node: node.nodeName == 'li', ol.childNodes) and filter(lambda node: node.nodeName == 'ol', ol.childNodes):
        ol = filter(lambda node: node.nodeName == 'ol', ol.childNodes)[0]
    ol.setAttribute('class', 'toc')
    
    if fragment:
        return ol.toxml(), innerHTML(doc.getElementsByTagName('body')[0])
    else:
        return ol.toxml(), doc.toxml()
        

def innerHTML(node):
    return ''.join([child.toxml() for child in node.childNodes])

tag_pattern = re.compile('<[^<]+?>')

def innerText(node):
    return re.sub(tag_pattern, '', innerHTML(node))
