class MoonStringClear:
    @staticmethod
    def clear(txt):
        txt = txt.replace("&lt;b&gt;", "")
        txt = txt.replace("&lt;/b&gt;", "")
        txt = txt.replace("<b>", "")
        txt = txt.replace("</b>", "")
        txt = txt.replace("&amp;", "")
        txt = txt.replace("&apos;", "")
        txt = txt.replace("&quot;", "")
        return txt