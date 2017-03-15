# -*- coding: utf-8 -*-
'''
自动爬去豆瓣轻步不要害羞小组图片
'''
import requests
from bs4 import BeautifulSoup
import time

url = "https://www.douban.com/group/haixiuzu/discussion?start="  # 0, 25, 50, 75...
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36"
header = {"User-Agent": UA}

# f = open("./zjw.txt", "w")
s = 0
for n in range(50):
    url0 = url + str(n * 25)
    req = requests.get(url0, headers=header, verify=False)
    content = req.content
    soup = BeautifulSoup(content, "html.parser")

    tiezi = soup.find_all("td", attrs={"title"})
    for i in tiezi:
        aa = i.a
        href = aa["href"]
        print href
        # title = aa['title'].encode("utf-8")
        # f.write(href + "\n")
        # f.write(title + "\n")
        req2 = requests.get(href, headers=header, verify=False)
        cont2 = req2.content
        soup2 = BeautifulSoup(cont2, "html.parser")
        photo = soup2.find("div", attrs={"topic-figure"})
        try:
            plink = photo.img['src']
            print plink

            #        "https://img1.doubanio.com/view/group_topic/large/public/p70426527.jpg"
            ppath = "./shamephoto/" + plink.split("/")[-1]
            with open(ppath, 'wb') as fuck:
                s += 1
                print "第{}张照片下载中.....................".format(s)
                time.sleep(10)
                image = requests.get(plink, stream=True, verify=False).content
                fuck.write(image)
        except:
            pass

# f.close()

# print i.children.
# print i.text.encode("utf-8")
"""
<td class="title">
<a class="" href="https://www.douban.com/group/topic/97854754/" title="豆瓣女性群">豆瓣女性群</a>
</td>

['HTML_FORMATTERS', 'XML_FORMATTERS', '__call__', '__class__', '__contains__',
'__copy__', '__delattr__', '__delitem__', '__dict__', '__doc__', '__eq__',
'__format__', '__getattr__', '__getattribute__', '__getitem__', '__hash__',
'__init__', '__iter__', '__len__', '__module__', '__ne__', '__new__',
'__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
'__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__unicode__',
'__weakref__', '_all_strings', '_attr_value_as_string', '_attribute_checker',
'_find_all', '_find_one', '_formatter_for_name', '_is_xml', '_lastRecursiveChild',
'_last_descendant', '_select_debug', '_selector_combinators', '_should_pretty_print',
'_tag_name_matches_and', 'append', 'attribselect_re', 'attrs', 'can_be_empty_element',
'childGenerator', 'children', 'clear', 'contents', 'decode', 'decode_contents',
'decompose', 'descendants', 'encode', 'encode_contents', 'extract', 'fetchNextSiblings',
'fetchParents', 'fetchPrevious', 'fetchPreviousSiblings', 'find', 'findAll',
'findAllNext', 'findAllPrevious', 'findChild', 'findChildren', 'findNext',
'findNextSibling', 'findNextSiblings', 'findParent', 'findParents',
'findPrevious', 'findPreviousSibling', 'findPreviousSiblings', 'find_all',
'find_all_next', 'find_all_previous', 'find_next', 'find_next_sibling',
'find_next_siblings', 'find_parent', 'find_parents', 'find_previous',
'find_previous_sibling', 'find_previous_siblings', 'format_string', 'get',
'getText', 'get_text', 'has_attr', 'has_key', 'hidden', 'index', 'insert',
'insert_after', 'insert_before', 'isSelfClosing', 'is_empty_element', 'known_xml',
'name', 'namespace', 'next', 'nextGenerator', 'nextSibling', 'nextSiblingGenerator',
'next_element', 'next_elements', 'next_sibling', 'next_siblings', 'parent',
'parentGenerator', 'parents', 'parserClass', 'parser_class', 'prefix',
'preserve_whitespace_tags', 'prettify', 'previous', 'previousGenerator',
'previousSibling', 'previousSiblingGenerator', 'previous_element', 'previous_elements',
'previous_sibling', 'previous_siblings', 'quoted_colon', 'recursiveChildGenerator',
'renderContents', 'replaceWith', 'replaceWithChildren', 'replace_with', 'replace_with_children',
'select', 'select_one', 'setup', 'string', 'strings', 'stripped_strings', 'tag_name_re', 'text', 'unwrap', 'wrap']
"""
