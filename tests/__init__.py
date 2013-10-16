# coding: utf8
from unittest import TestCase
from toc import table_of_contents
import os
import html5lib
import xpath

class TocTest(TestCase):
    def test_generate(self):

        html = '''
<h1>스타트업 개발 강의</h1>

<p><strong>스타트업 개발 강의</strong>는 소프트웨어 분야에서 스타트업을 하려는 사람들을 위한 강의입니다. 주로 프로그래밍 경험이 없는 초보자를 대상으로 하며, 교육을 받은 후 실제로 <strong>자신의 아이디어를 구현해낼 수 있는 능력</strong>을 함양하는 것을 목표로 합니다.</p>

<p>이미 IT 업계에는 개발을 전혀 모르는 상태에서 스타트업을 하면서 개발을 배워서 훌륭한 제품을 만들어낸 사례가 있습니다. 미국 실리콘 밸리에는 물론 무수한 사례가 있지만, 미국 뿐 아니라 국내에도 개발 경험이 별로 없던 네 명의 창업자가 <a href="http://rubyonrails.org/">루비 온 레일즈</a>를 배워서 <a href="https://www.tumblbug.com/">텀블벅</a>처럼 멋진 소셜펀딩 사이트를 만들어내기도 했습니다.</p>

<p>창업을 하고 싶은데 개발을 할 줄 모른다고 포기할 필요는 없습니다. 최근 수년 간 소프트웨어 개발은 많은 기술의 발전이 있었고, 그 덕분에 비전문가도 쉽게 배워서 할 수 있을 만큼 문턱이 낮아졌습니다. 실제로 성공적인 스타트업 아이디어 중에 그다지 높은 기술력을 필요로 하지 않으며, 초보자들도 해낼 수 있는 경우가 많습니다. <strong>스타트업 개발 강의</strong>에서 스스로 개발자의 길에 들어설 수 있도록 도와드리겠습니다.</p>

<p>초보자 대상이니만큼 깊이 있는 내용을 다루기 어렵고, 예제를 따라하는 방식이 되겠지만, 준비된 튜토리얼을 단순히 따라하는 것이 아니라 그 과정에서 개념 원리를 이해할 수 있도록 예제를 구성했고, 몇몇 예제들은 직접적인 가이드를 주는 것이 아니라 직접 개발 문서를 찾아보고 스스로 해낼 수 있도록 유도합니다. 그리고, 교육이 끝난 후에도 실전에서 활용할 수 있도록 여러 가지 A/S를 제공합니다.</p>

<p>개발자가 하는 분야는 다양하지만 이 강의에서는 그 중에 스타트업에 적합한 기술에만 초점을 맞춥니다. 스타트업은 불확실성이 높기 때문에 천천히 높은 품질로 개발해내기보다는, 여러 가지 문제가 많더라도 빨리 핵심 기능을 만들어서 시장에 출시하는 것이 중요합니다. 그래서 난이도가 높은 고급 기술을 배우느라 시간을 너무 많이 소모하지 않도록 쉬우면서도 빠른 개발이 가능한 기술들을 중심으로 교육과정을 구성했습니다. 따라서, 직접 스타트업을 할 생각이 없고 일반적인 개발자의 커리어를 쌓아나가고 싶은 분들에게는 이 교육과정이 적합하지 않습니다.</p>

<h2>교육과정</h2>

<p>교육과정은 표준교육과정과 맞춤교육으로 나뉩니다. 표준교육과정은 5~10명의 수강생이 함께 수강하는 단체 교육과정이며, 스타트업에서 많이 필요한 웹 개발과 모바일 앱 개발에 중점을 두어서 구성했고, 입문 과정과 심화 과정으로 분리되어 있습니다. 맞춤교육은 실제로 스타트업을 진행해 나가는 상황에서 그 때 그 때 필요한 기술들을 교육하고 실제 문제들에 대한 컨설팅도 진행합니다.</p>

<h3>웹 개발</h3>

<ul>
    <li>
    <p><a href="스타트업을 위한 웹 개발 기초">스타트업을 위한 웹 개발 기초</a> 1일 4시간</p>
    </li>
    <li>
    <p><a href="스타트업 웹 개발자로 거듭나기">스타트업 웹 개발자로 거듭나기</a> 4일 16시간</p>
    </li>
</ul>

<h2>iOS 개발</h2>

<ul>
    <li>
    <p>나의 첫번째 아이폰 앱 만들기</p>
    </li>
    <li>
    <p>iOS 개발 베스트 프랙티스</p>
    </li>
</ul>

<h3>웹 개발</h3>

<ul>
    <li>
    <p><a href="스타트업을 위한 웹 개발 기초">스타트업을 위한 웹 개발 기초</a> 1일 4시간</p>
    </li>
    <li>
    <p><a href="스타트업 웹 개발자로 거듭나기">스타트업 웹 개발자로 거듭나기</a> 4일 16시간</p>
    </li>
</ul>

<h3>iOS 개발</h3>

<ul>
    <li>
    <p>나의 첫번째 아이폰 앱 만들기</p>
    </li>
    <li>
    <p>iOS 개발 베스트 프랙티스</p>
    </li>
</ul>

<h3>안드로이드 개발</h3>

<ul>
    <li>
    <p>하루 만에 만드는 안드로이드 앱</p>
    </li>
    <li>안드로이드로 린 스타트업</li>
</ul>

<h3>맞춤교육</h3>

<ul>
    <li>스타트업 개발 맞춤교육</li>
</ul>
'''        
        toc, body = table_of_contents(html, fragment=True)

        toc_dom = html5lib.parse(toc, treebuilder='dom', namespaceHTMLElements=False)

        self.assertEquals('#header-1', xpath.find('//ol[@class="toc"]/li[1]/a', toc_dom)[0].getAttribute('href'))
        self.assertEquals('안드로이드 개발', xpath.find('//ol[@class="toc"]/ol/ol[2]/li[3]/a', toc_dom)[0].firstChild.nodeValue)
        self.assertEquals('#header-1.2.3', xpath.find('//ol[@class="toc"]/ol/ol[2]/li[3]/a', toc_dom)[0].getAttribute('href'))

        body_dom = html5lib.parse(body, treebuilder='dom', namespaceHTMLElements=False)
        self.assertEquals('안드로이드 개발', xpath.find('//h3[@id="header-1.2.3"]/text()', body_dom)[0].nodeValue)
        self.assertEquals('1.2.3', xpath.find('//h3[@id="header-1.2.3"]/a', body_dom)[0].firstChild.nodeValue)
            
            
            