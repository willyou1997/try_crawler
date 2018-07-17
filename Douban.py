import lxml
import time
import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup

header = {
    'User-Agent':
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Cookie':
    'bid=UuGhEUsLRq8; __utmz=30149280.1522072774.1.1.utmcsr=m.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search/; ap=1; ll="118146"; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1522510351%2C%22https%3A%2F%2Fm.douban.com%2Fsearch%2F%3Fquery%3D%25E5%25AE%25B3%25E7%25BE%259E%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1694527024.1522072774.1522072774.1522510354.2; __utmc=30149280; __utmt=1; dbcl2="132016160:VbXUR6IUUt0"; ck=xoVM; push_noty_num=0; push_doumail_num=0; __utmv=30149280.13201; _pk_id.100001.8cb4=2b7bad2852fa36ea.1522072773.2.1522510451.1522077732.; __utmb=30149280.19.5.1522510451338'
}


def get_article_url(num):
    data = {
        'start': num
    }
    article_list = []
    group_url = 'https://www.douban.com/group/634017/'  #输入豆瓣小组链接
    url = group_url + 'discussion?' + urlencode(data)
    html = requests.get(url, headers=header)
    html.encoding = html.apparent_encoding
    soup = BeautifulSoup(html.text, 'lxml')
    for link in soup.find_all('a'):
        test_link = link.get('href')
        if test_link and len(test_link) >= 35:
            if (test_link.split('/'))[-3] == 'topic':
                article_list.append(test_link)
    for i in range(len(article_list)):
        time.sleep(1)
        img_list = get_img_url(article_list[i], num, group_url)
        for j in range(len(img_list)):
            download(img_list[j])


def get_img_url(url, n, group_url):
    header2 = {
        'Cookie':
        'bid=UuGhEUsLRq8; __utmz=30149280.1522072774.1.1.utmcsr=m.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search/; ap=1; ll="118146"; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1522510351%2C%22https%3A%2F%2Fm.douban.com%2Fsearch%2F%3Fquery%3D%25E5%25AE%25B3%25E7%25BE%259E%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1694527024.1522072774.1522072774.1522510354.2; __utmc=30149280; __utmt=1; dbcl2="132016160:VbXUR6IUUt0"; ck=xoVM; push_noty_num=0; push_doumail_num=0; __utmv=30149280.13201; _pk_id.100001.8cb4=2b7bad2852fa36ea.1522072773.2.1522510481.1522077732.; __utmb=30149280.26.5.1522510481289',
        'Host':
        'www.douban.com',
        'Referer':
        group_url + 'discussion?start=' + str(n),
        'Upgrade-Insecure-Requests':
        '1',
        'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    html = requests.get(url, headers=header2)
    html.encoding = html.apparent_encoding
    img_url = []
    soup = BeautifulSoup(html.text, 'lxml')
    for link in soup.find_all('img'):
        test_link = link.get('src')
        if test_link:
            if test_link.split('/')[-4] == 'group_topic' and test_link.split(
                    '/')[-5] == 'view':
                img_url.append(test_link)
    return img_url


def download(url):
    save_location = 'D:/豆瓣/'  # 输入保存路径
    save_name = url.split('/')[-1]
    html_img = requests.get(url, headers=header)
    with open(save_location + save_name, 'wb') as f:
        f.write(html_img.content)
        print(save_name + '下载完成')
        f.close()


if __name__ == '__main__':
    num = int(input('请输入要下载的页数：'))
    GROUP_START = 0
    GROUP_END = num
    group = [x * 25 for x in range(GROUP_START, GROUP_END)]
    from multiprocessing import Pool
    pool = Pool()
    pool.map(get_article_url, group)
