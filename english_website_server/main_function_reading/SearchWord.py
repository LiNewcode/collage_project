"""
    SearchWord：搜索单词的总入口
"""
import re

import requests
from lxml import etree
import json

# from end_of_term_work.Tool.link_db import db_obj
from end_of_term_work.Tool.link_db import db_obj


class SearchWordClass:
    word = "",
    explain = [],
    explain_exist = 0,
    mp3_usa = "",
    mp3_bt = "",
    # 音 标
    phsUsa = "",
    phsUsa_exist = 0,
    phsBt = "",
    phsBt_exist = 0,
    phrase = {},
    phrase_exist = 0,
    sentence = {},
    sentence_exist = 0,
    # 近义词
    simWor = [],
    simWor_exist = 0,
    # 同根词
    Homonym = {},
    Homonym_exist = 0,
    wordDiscrimination = {},
    wordDiscrimination_exist = 0,
    isPee = 0,
    html = ''

    def __init__(self, word):
        self.word = word
        # str(word)
        self.transUrl = 'https://dict.youdao.com/w/' + str(word) + '/'
        self.mp3_usa = 'https://dict.youdao.com/dictvoice?audio=' + str(word) + '&type=2'
        self.mp3_bt = 'https://dict.youdao.com/dictvoice?audio=' + str(word) + '&type=1'
        try:
            self.html = self.get_Html()
        except:
            # print('无法获取HTML')

            return None
        self.tree = etree.HTML(self.html)
        # t = self.tree.xpath('//div[@id=\'synonyms\']')
        # if type(t) is type([]):
        #     #print('tttt')
        #     for i in t:
        #         #print('[ 查看 ]:', etree.tostring(i, method='html'))
        # else:
        #     print('[ 查看 ]:', etree.tostring(t, method='html'))
        # print('kkkkk')

    def run(self):
        try:
            self.get_sentence()
        except:
            # print('无法获取句子')
            pass
        try:
            self.get_phrase()
        except:
            pass
            # print('无法获取词组')
        try:
            self.get_explain()
            if self.explain == [] or self.explain == ([],):
                try:
                    self.get_explain_re()
                except:
                    pass
                    # print("无法获取解释")
        except:
            try:
                self.get_explain_re()
            except:
                pass
                # print("无法获取解释")
        try:
            self.get_phsBt()
        except:
            pass
            # print("无法获取英 音标")
        try:
            self.get_phsUsa()
        except:
            pass
            # print('无法获取美 音标')
        try:
            self.get_simWor(str(5))
        except:
            pass
            # try:
            #     self.get_simWor(str(5))
            # except:
            # print('无法获取近义词')
        try:
            self.get_homonym(str(4))
        except:
            try:
                self.get_homonym(str(5))
            except:
                pass
                # print('无法获取同根词')
        try:
            self.get_wordDiscrimination()
        except:
            pass
            # print('无法获取辨析')
        isExist = self.check()
        if isExist:

            wordData = {'_id': self.word, 'explain': self.explain, 'mp3_usa': self.mp3_usa, 'mp3_bt': self.mp3_bt,
                        'phs': [self.phsUsa, self.phsBt], 'phrase': self.phrase, 'sentence': self.sentence,
                        'simWor': self.simWor, 'Homonym': self.Homonym, 'wordDiscrimination': self.wordDiscrimination,
                        'explain_exist': self.explain_exist, 'phsUsa_exist': self.phsUsa_exist,
                        'phsBt_exist': self.phsBt_exist, 'phrase_exist': self.phrase_exist,
                        'sentence_exist': self.sentence_exist, 'simWor_exist': self.simWor_exist,
                        'Homonym_exist': self.Homonym_exist, 'wordDiscrimination_exist': self.wordDiscrimination_exist,
                        'isPee': self.isPee}

        else:
            return False
        return wordData

    def get_Html(self):
        headers = {
            'Host': 'dict.youdao.com',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.41',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://dict.youdao.com/',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        }

        response = requests.get(url=self.transUrl, headers=headers, timeout=2)
        return response.text

    def get_img(self):
        Xpath = '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/a/img/@src'
        self.img = ''

    def get_phsUsa(self):
        Xpath = '//div[@id=\'phrsListTab\']/h2[@class=\'wordbook-js\']/div[@class=\'baav\']/span[1]/span/text()'
        if type(self.tree.xpath(Xpath)) is type([]):

            self.phsUsa = self.tree.xpath(Xpath)[0]
        else:

            self.phsUsa = self.tree.xpath(Xpath)
        if len(self.phsUsa) < 1:
            self.phsUsa = ''

    def get_phsBt(self):
        Xpath = '//div[@id=\'phrsListTab\']/h2[@class=\'wordbook-js\']/div[@class=\'baav\']/span[2]/span/text()'
        if type(self.tree.xpath(Xpath)) is type([]):

            self.phsBt = self.tree.xpath(Xpath)[0]
        else:

            self.phsBt = self.tree.xpath(Xpath)
        if len(self.phsBt) < 1:
            self.phsBt = ''

    def get_explain(self):
        Xpath = '//div[@id=\'phrsListTab\']/div[@class=\'trans-container\']/ul/li/text()'
        self.explain = self.tree.xpath(Xpath)

    def get_explain_re(self, ):
        res = self.tree.xpath('//div[@id=\'tWebTrans\']/div/div/span/text()')

        self.explain=[]
        for i in res:
            self.explain.append(i.strip())

    def get_phrase(self):

        wordXpath = '//div[@id=\'wordGroup2\']/p/span/a/text()'
        explainXpath = '//div[@id=\'wordGroup2\']/p/text()'


        key = self.tree.xpath(wordXpath)
        val = []
        for i in self.tree.xpath(explainXpath):
            if i.strip() == '':
                continue
            val.append(i.strip())
        index = 0
        content = []
        for i in key:
            content.append({'en': i, 'ch': val[index]})
            index += 1
        self.phrase = {'phrase': content}

    def get_sentence(self):
        # '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[4]/div/div/div/div/div[@class=\'collinsToggle trans-container\']/div/ul/li[1]/div[2]/div/p[1]/text()'
        # '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[4]/div/div/div/div/div[@class=\'collinsToggle trans-container\']'
        # '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[4]/div/div/div/div/div[@class=\'collinsToggle trans-container\']/div/ul/li[1]/div[2]/div/p[2]'

        en = self.tree.xpath(
            '//div[@class=\'collinsToggle trans-container\']/div/ul/li/div[2]/div/p[1]/text()')

        ch = self.tree.xpath(
            '//div[@class=\'collinsToggle trans-container\']/div/ul/li/div[2]/div/p[2]/text()')

        index = 0
        dic = []
        for i in en:
            dic.append({'en': i, 'ch': ch[index]})
            index += 1
        self.sentence = {'word': i, 'example': dic}

    def get_simWor(self, sign):

        synonyms_index = 1
        self.simWor = []
        for i in self.tree.xpath('//div[@id=\'synonyms\']/ul/li/text()'):
            description = i
            word = self.tree.xpath('//div[@id=\'synonyms\']/ul/p[' + str(
                synonyms_index) + ']/span/a/text()')

            #  print(word)
            dic = {'description': description, 'word': word}

            self.simWor.append(dic)

            synonyms_index += 1
            word = []

        # self.simWor[key] = (j.xpath('/p/span/a/text()'))

    def get_homonym(self, sign):

        # 先获得词根
        fix_title = \
            self.tree.xpath(
                '//div[@id=\'relWordTab\']/p[1]/text()')[
                0].strip()
        fix_content = self.tree.xpath(
            '//div[@id=\'relWordTab\']/p[1]/span/a/text()')
        fix = {'ft': fix_title, 'fc': fix_content}
        a = self.tree.xpath('//div/div[@id=\'relWordTab\']')[0]
        allcontent = etree.tostring(a,
                                    method='html')
        result = ''.join(str(allcontent).split('\\n'))
        index = 1
        content = re.split('(n\.|v\.|vt\.|adj\.|adv\.|a\.|num\.|pron\.|art\.|prep\.)', result)
        result = []
        for i in content:

            try:
                if index % 2 == 0:
                    nature = i
                    list = re.findall('<p.*?/p>', content[index])

                    example = []
                    for j in list:

                        en = re.findall('<a .*?>(.*?)</a>', j)[0]

                        ch_index = 1
                        for k in self.tree.xpath(
                                '//div[@id=\'relWordTab\']/p/span/a/text()'):

                            if str(k) == en:
                                ch = self.tree.xpath(
                                    '//div[@id=\'relWordTab\']/p[' + str(
                                        ch_index) + ']/text()')[1].strip()

                            ch_index += 1
                            if ch_index == len(self.tree.xpath(
                                    '//div[@id=\'relWordTab\']/p')):
                                break
                        ex = {'en': en, 'ch': ch}
                        example.append(ex)
                    result.append({'nature': nature, 'example': example})
            except:

                index += 1
                continue
            index += 1
        col = []
        for i in result:
            col.append(i)
        self.Homonym = {'fix': fix, 'col': col}

    def get_wordDiscrimination(self):
        # '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[5]/div/div[4]/div/div[1]/span/text()'
        word = \
            self.tree.xpath(
                '//div[@id=\'discriminate\']/div/div[1]/span/text()')
        # print('word:', word)
        # '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[4]/div/div[4]/div/div[1]/span/text()'
        des = \
            self.tree.xpath(
                '//div[@id=\'discriminate\']/div/div[2]/p[1]/text()')

        wordList = self.tree.xpath(
            '//div[@id=\'discriminate\']/div/div[2]/div/p/span/a/text()')

        desList = self.tree.xpath(
            '//div[@id=\'discriminate\']/div/div[2]/div/p/text()')

        content = []
        index = 1
        for i in wordList:
            try:

                ch = (desList[index]).strip()
                content.append({'en': i, 'ch': ch})
                index += 2
            except:
                continue
        self.wordDiscrimination = {'word': word, 'des': des, 'content': content}

    def pack2json(self):
        wordData = {'_id': self.word, 'explain': self.explain, 'mp3_usa': self.mp3_usa, 'mp3_bt': self.mp3_bt,
                    'phs': [self.phsUsa, self.phsBt], 'phrase': self.phrase, 'sentence': self.sentence,
                    'simWor': self.simWor, 'Homonym': self.Homonym, 'wordDiscrimination': self.wordDiscrimination,
                    'explain_exist': self.explain_exist, 'phsUsa_exist': self.phsUsa_exist,
                    'phsBt_exist': self.phsBt_exist, 'phrase_exist': self.phrase_exist,
                    'sentence_exist': self.sentence_exist, 'simWor_exist': self.simWor_exist,
                    'Homonym_exist': self.Homonym_exist, 'wordDiscrimination_exist': self.wordDiscrimination_exist,
                    'isPee': self.isPee}

        word_json = json.dumps(wordData, ensure_ascii=True)
        return word_json

    def check(self):
        try:
            if len(self.explain) == 0:
                explain_exist = 0
            elif self.explain[0] == '':
                explain_exist = 0
            else:
                explain_exist = 1
            self.explain_exist = explain_exist
        except:
            pass
        try:
            if self.phsUsa == '':
                phsUsa_exist = 0
            elif len(self.phsUsa) == 0:
                phsUsa_exist = 0
            else:
                phsUsa_exist = 1
            self.phsUsa_exist = phsUsa_exist
        except:
            pass
        try:
            if self.phsBt == '':
                phsBt_exist = 0
            elif len(self.phsBt) == 0:
                phsBt_exist = 0
            else:
                phsBt_exist = 1
            self.phsBt_exist = phsBt_exist
        except:
            pass
        try:

            if self.phrase == {}:
                phrase_exist = 0
            elif len(self.phrase['phrase']) == 0:
                phrase_exist = 0
            elif list(self.phrase['phrase'])[0] == '':
                phrase_exist = 0
            else:
                phrase_exist = 1

            self.phrase_exist = phrase_exist
        except:
            pass
        try:
            if self.sentence == {}:
                sentence_exist = 0
            elif len(self.sentence['example']) == 0:
                sentence_exist = 0
            elif len(self.sentence['example'][0]['en']) == 0:
                sentence_exist = 0
            else:
                sentence_exist = 1
            self.sentence_exist = sentence_exist
        except:
            pass
        try:
            if self.simWor == '':
                simWor_exist = 0
            elif len(self.simWor) == 0:
                simWor_exist = 0
            elif self.simWor[0]['description'] == '':
                simWor_exist = 0
            elif len(self.simWor[0]['description']) == 0:
                simWor_exist = 0
            else:
                simWor_exist = 1

            self.simWor_exist = simWor_exist
        except:
            pass
        try:
            if self.Homonym == {}:
                Homonym_exist = 0
            elif self.Homonym['fix'] == {}:
                Homonym_exist = 0
            elif self.Homonym['fix']['ft'] == '':
                Homonym_exist = 0
            elif len(self.Homonym['fix']['ft']) == 0:
                Homonym_exist = 0
            else:
                Homonym_exist = 1

            self.Homonym_exist = Homonym_exist
        except:
            pass
        try:
            if self.wordDiscrimination == {}:
                wordDiscrimination_exist = 0
            elif self.wordDiscrimination['word'] == '':
                wordDiscrimination_exist = 0
            elif len(self.wordDiscrimination['word']) == 0:
                wordDiscrimination_exist = 0
            else:
                wordDiscrimination_exist = 1
            self.wordDiscrimination_exist = wordDiscrimination_exist
        except:
            pass
        pee_db = db_obj(col='pee_word')
        if pee_db.search(content={'word': self.word}) is not None:
            self.isPee = 1
        else:
            self.isPee = 0
        pee_db.close()
        return True

    def __str__(self):
        return str(json.loads(self.pack2json()))
    # return (f'self.word = {self.word}\n  self.explain = {self.explain}\n  self.img = {self.img}\n   self.mp3 = {self.mp3}\n  self.phsUsa = {self.phsUsa}\n  self.phsBt = {self.phsBt}\n   self.phrase = {self.phrase}\n  self.sentence = {self.sentence}\n  self.simWor = {self.simWor}\n  self.Homonym = {self.Homonym}\n  self.wordDiscrimination ={self.wordDiscrimination}\n  ')
