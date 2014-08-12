from gi.repository import Gtk
from grabbo import Builder
import os

ExtBox_UI = os.path.join('..', 'ui', 'ExtBox.ui')

class ExtBox(Builder):
    def __init__(self, ext):
        super(ExtBox, self).__init__(ExtBox_UI)
        self._label = self.ui.get_object("label")
        self._icon = self.ui.get_object("image")
        self._switch = self.ui.get_object("switch")
        self._des = self.ui.get_object("des")
        self._desEx = self.ui.get_object("desEx")
        self._link = self.ui.get_object("link")
        self._roz = self.ui.get_object("roz")
        self._zwi = self.ui.get_object("zwi")
        self._DesBox = self.ui.get_object("DesBox")

        self._label.set_text(ext.get_name())
        self._des.set_test(ext.get_short_descrption())
        self._desEX.set_text(ext.get_descrption())
        self._icon.set_image(ext.get_icon())
        self._link.set_text("Author's page")
        self._link.set_link(ext.get_url())

        self._zwi.connect("clicked", lambda x: self.on_zwi())
        self._roz.connect("clicked", lambda x:self.on_roz())

        self._zwi.hide()
        self._DesBox.hide()

        self.get().show()

    def on_zwi(self):
        self._roz.show()
        self._zwi.hide()
        self._DesBox.hide()

    def on_roz(self):
        self._roz.hide()
        self._zwi.show()
        self._DesBox.show()

    def get(self):
        return self.ui.get_object("box")

class Extension(object):
    def __init__(self, Name, shortDes, Descrption, Author, url, Icon):
        self._name = Name
        self._des = Descrption
        self._short = shortDes
        self._aur = Author
        self._url = url
        self._icon = Icon
        self._box = ExtBox(self)

    def get_name(self):
        return self._name

    def get_descrption(self):
        return self._des

    def get_short_descrption(self):
        return self._des

    def get_author(self):
        return self._aur

    def get_url(self):
        return self._url

    def get_icon(self):
        return self._icon




