# -*- coding: utf-8 -*-

from module.plugins.internal.Hoster import Hoster, create_getInfo


class DeadHoster(Hoster):
    __name__    = "DeadHoster"
    __type__    = "hoster"
    __version__ = "0.18"
    __status__  = "stable"

    __pattern__ = r'^unmatchable$'

    __description__ = """Hoster is no longer available"""
    __license__     = "GPLv3"
    __authors__     = [("zoidberg", "zoidberg@mujmail.cz")]


    @classmethod
    def get_info(cls, *args, **kwargs):
        info = super(DeadHoster, cls).get_info(*args, **kwargs)
        info['status'] = 1
        return info


    def setup(self):
        self.pyfile.error = "Hoster is no longer available"
        self.offline()  #@TODO: self.offline("Hoster is no longer available")


getInfo = create_getInfo(DeadHoster)
