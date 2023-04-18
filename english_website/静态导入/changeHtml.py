import os
from lxml import etree
import lxml
from bs4 import BeautifulSoup as bs
import re

if __name__ == '__main__':
    path = 'F://English//20-1//TE_USA_Edition_January_02_2021.html'
    new_path = 'F://English//20-1//TE_USA_Edition_January_02_2021_new.html'
    special = tuple(',.*?■-_+@:;')
    with open(path, 'r', encoding='utf-8') as fp:
        page = fp.read()
        tree = etree.HTML(page)
        k_index = 1
        sum = 0

        # spanlist = tree.xpath('/html/body/div/div/div/div/span/text()')
        for k in tree.xpath('/html/body/div/div/div/div/span'):
            k_index += 1
            i_index = 0
            span = str(etree.tostring(k, encoding='utf-8', method='html'))
            # print(span)
            prefix = re.findall('<span.*?>', span)[0]
            subfix = '</span>'
            word_list = k.text.split(' ')
            # print(word_list)
            t = 0
            for j in word_list:
                t += 1
                if j.isalpha():
                    word_list[t - 1] = '<a herf="javascript:attackEnemy("' + str(j) + '")">' + str(j) + '</a>'
                else:
                    if len(j) <= 0:
                        continue
                    if j[0] in special:
                        j_content = j.split(j[0])[0]
                        if j_content == '':
                            continue
                        else:
                            word_list[t - 1] = '<a>' + str(j[0]) + '</a>' + '<a herf="javascript:attackEnemy("' + str(
                                j_content) + '")">' + str(j_content) + '</a>'
                    elif j[-1] in special:
                        j_content = j.split(j[-1])[0]
                        if j_content == '':
                            continue
                        else:
                            word_list[t - 1] = '<a herf="javascript:attackEnemy("' + str(
                                j_content) + '")">' + j_content + '</a>' + '<a>' + str(j[-1]) + '</a>'

                    else:
                        if j == ' ':
                            continue
                        word_list[t - 1] = '<a herf="javascript:attackEnemy("' + str(j) + '")">' + str(j) + '</a>'

            # print(''.join(word_list))
            k.text = None
            e = etree.HTML(prefix + ' '.join(word_list) + subfix)
            print(str(etree.tostring(e.xpath('/html/body/span')[0],method='html')))
            # print(etree.tostring(e))
            try:
                e_a_list = e.xpath('/html/body/span')
                for e_a in e_a_list:
                    sum += 1
                    k=e_a
                    # print(etree.tostring(e_a))
            except:
                print(e)

        print(sum)
        print(len(tree.xpath('/html/body/div/div/div/div/span')))

        # for k in tree.xpath('/html/body/div/div/div/div/span'):
        #     print(k.text)
        # print(str(tree))
        with open(new_path, 'wb') as fp:
            fp.write(etree.tostring(tree, encoding='utf-8', method='html'))
