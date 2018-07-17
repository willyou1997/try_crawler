# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 09:58:03 2018

@author: 15215
"""
import urllib
import urllib2
import requests
 
values = {"username":"willyou","password":"8sexiaohuangwen"}
 
            
header = {
    'Host':
    'fishlovemeat.site',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Cookie':
    '_ga	GA1.2.2066645986.1492089596;Hm_lvt_6dc8c593faac02555277212cac149826	1503034809;xyQi_2132_atarget	1;xyQi_2132_auth	2addg5jtoyjXO874CrSFLfDfA1q7wgFO76eEfWb6pikwGW6o3PS5bh1VdRxu6QWXu0rlenSWz/lF+3OGFf+nFkH0Tn0;xyQi_2132_checkpm	1;xyQi_2132_forum_lastvisit	D_13_1531717372;xyQi_2132_home_diymode	1;xyQi_2132_lastact	1531717375 misc.php patch;xyQi_2132_lastcheckfeed	191058|1531711427;xyQi_2132_lastvisit	1531706724;xyQi_2132_lip	112.17.237.160,1531711427;xyQi_2132_nofavfid	1;xyQi_2132_onlineusernum	170;xyQi_2132_saltkey	RGZRR64q;xyQi_2132_sendmail	1;xyQi_2132_sid	rdfJQq;xyQi_2132_st_p	0|1531711421|6f0fb9e37abf3d9ca05c42edf1c3a251;xyQi_2132_st_t	191058|1531717372|7a8bb48ce1b77d4cc6755466b84407b8;xyQi_2132_ulastactivity	9da2PUsyP9gUE6tER8DJQQtT3FemIe7bxIqBy4QvnsOz5yh/s6Hf;xyQi_2132_visitedfid	13'
}
data = urllib.urlencode(values)
url = "http://fishlovemeat.site/forum.php?mod=viewthread&tid=29229&extra=page%3D1%26filter%3Dsortid%26sortid%3D8"
html = requests.get(url, headers = header)
print html.text