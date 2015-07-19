# -*- coding: utf-8 -*-

from module.plugins.internal.Account import Account
from module.common.json_layer import json_loads


class FastixRu(Account):
    __name__    = "FastixRu"
    __type__    = "account"
    __version__ = "0.05"
    __status__  = "stable"

    __description__ = """Fastix account plugin"""
    __license__     = "GPLv3"
    __authors__     = [("Massimo Rosamilia", "max@spiritix.eu")]


    def load_account_info(self, user, req):
        data = self.get_account_data(user)
        html = json_loads(self.load("http://fastix.ru/api_v2/",
                                    get={'apikey': data['api'],
                                         'sub'   : "getaccountdetails"}))

        points = html['points']
        kb     = float(points) * 1024 ** 2 / 1000

        if points > 0:
            account_info = {'validuntil': -1, 'trafficleft': kb}
        else:
            account_info = {'validuntil': None, 'trafficleft': None, 'premium': False}
        return account_info


    def login(self, user, data, req):
        html = self.load("https://fastix.ru/api_v2/",
                         get={'sub'     : "get_apikey",
                              'email'   : user,
                              'password': data['password']})

        api = json_loads(html)
        api = api['apikey']

        data['api'] = api

        if "error_code" in html:
            self.wrong_password()
