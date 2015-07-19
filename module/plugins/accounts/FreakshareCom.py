# -*- coding: utf-8 -*-

import re
import time

from module.plugins.internal.Account import Account


class FreakshareCom(Account):
    __name__    = "FreakshareCom"
    __type__    = "account"
    __version__ = "0.15"
    __status__  = "stable"

    __description__ = """Freakshare.com account plugin"""
    __license__     = "GPLv3"
    __authors__     = [("RaNaN", "RaNaN@pyload.org")]


    def load_account_info(self, user, req):
        premium = False
        validuntil  = None
        trafficleft = None

        html = self.load("http://freakshare.com/")

        try:
            m = re.search(r'ltig bis:</td>\s*<td><b>([\d.:-]+)</b></td>', html, re.M)
            validuntil = time.mktime(time.strptime(m.group(1).strip(), "%d.%m.%Y - %H:%M"))

        except Exception:
            pass

        try:
            m = re.search(r'Traffic verbleibend:</td>\s*<td>([^<]+)', html, re.M)
            trafficleft = self.parse_traffic(m.group(1))

        except Exception:
            pass

        return {'premium': premium, 'validuntil': validuntil, 'trafficleft': trafficleft}


    def login(self, user, data, req):
        self.load("http://freakshare.com/index.php?language=EN")

        html = self.load("https://freakshare.com/login.html",
                         post={'submit': "Login",
                               'user'  : user,
                               'pass'  : data['password']})

        if ">Wrong Username or Password" in html:
            self.wrong_password()
