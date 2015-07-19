# -*- coding: utf-8 -*-

from module.plugins.internal.MultiHook import MultiHook


class PremiumToHook(MultiHook):
    __name__    = "PremiumToHook"
    __type__    = "hook"
    __version__ = "0.10"
    __status__  = "stable"

    __config__ = [("pluginmode"    , "all;listed;unlisted", "Use for plugins"              , "all"),
                  ("pluginlist"    , "str"                , "Plugin list (comma separated)", ""   ),
                  ("reload"        , "bool"               , "Reload plugin list"           , True ),
                  ("reloadinterval", "int"                , "Reload interval in hours"     , 12   )]

    __description__ = """Premium.to hook plugin"""
    __license__     = "GPLv3"
    __authors__     = [("RaNaN"   , "RaNaN@pyload.org"   ),
                       ("zoidberg", "zoidberg@mujmail.cz"),
                       ("stickell", "l.stickell@yahoo.it")]


    def get_hosters(self):
        user, data = self.account.select_account()
        html = self.load("http://premium.to/api/hosters.php",
                      get={'username': user, 'password': data['password']})
        return [x.strip() for x in html.replace("\"", "").split(";")]
