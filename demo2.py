# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 14:00:33 2018

@author: 15215
"""
import urllib
import urllib2
import requests
import re
          
header = {
    'Host': 'fishlovemeat.site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': 'Hm_lvt_6dc8c593faac02555277212cac149826=1503034809; _ga=GA1.2.2066645986.1492089596; xyQi_2132_sid=rdfJQq; xyQi_2132_saltkey=RGZRR64q; xyQi_2132_lastvisit=1531706724; xyQi_2132_lastact=1531717375%09misc.php%09patch; xyQi_2132_st_p=0%7C1531711421%7C6f0fb9e37abf3d9ca05c42edf1c3a251; xyQi_2132_ulastactivity=9da2PUsyP9gUE6tER8DJQQtT3FemIe7bxIqBy4QvnsOz5yh%2Fs6Hf; xyQi_2132_auth=2addg5jtoyjXO874CrSFLfDfA1q7wgFO76eEfWb6pikwGW6o3PS5bh1VdRxu6QWXu0rlenSWz%2FlF%2B3OGFf%2BnFkH0Tn0; xyQi_2132_lastcheckfeed=191058%7C1531711427; xyQi_2132_lip=112.17.237.160%2C1531711427; xyQi_2132_home_diymode=1; xyQi_2132_nofavfid=1; xyQi_2132_onlineusernum=170; xyQi_2132_sendmail=1; xyQi_2132_checkpm=1; xyQi_2132_st_t=191058%7C1531717372%7C7a8bb48ce1b77d4cc6755466b84407b8; xyQi_2132_atarget=1; xyQi_2132_forum_lastvisit=D_13_1531717372; xyQi_2132_visitedfid=13',
    'DNT': '1'
}
for i in range(1,10):
    x = i+ 29150
    url = "http://fishlovemeat.site/forum.php?mod=viewthread&tid="+ urllib.quote_plus(str(x))
    html = requests.get(url, headers = header)
    #print html.text
    article = html.content
    save_location = 'E:/fish/'
    save_name = url[-3:]
    save_name2= url[-2:]
    with open(save_location + save_name2 + '.txt', 'w') as f:      
        f.write(article)
        #print('完成')
        f.close()    
    title = re.findall('<title>(.*?)</title>',article)
    body = re.findall('<div align="left">(.*?)</div><br />',article)
    
    with open(save_location + save_name + '.txt', 'w') as f:      
        f.write('\n'.join(title))
        f.write('\n'.join(body))
        print('完成')
        f.close()
    