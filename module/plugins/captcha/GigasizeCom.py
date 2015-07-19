# -*- coding: utf-8 -*-

from module.plugins.internal.OCR import OCR


class GigasizeCom(OCR):
    __name__    = "GigasizeCom"
    __type__    = "ocr"
    __version__ = "0.14"
    __status__  = "stable"

    __description__ = """Gigasize.com ocr plugin"""
    __license__     = "GPLv3"
    __authors__     = [("pyLoad Team", "admin@pyload.org")]


    def get_captcha(self, image):
        self.load_image(image)
        self.threshold(2.8)
        self.run_tesser(True, False, False, True)
        return self.result_captcha
