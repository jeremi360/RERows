#!/usr/bin/env python

from gi.repository import Gtk, WebKit
import os

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

try:
    from crowbar.tab import Tab
    print("Eclipse way")
except:
    from tab import Tab
    print("Normal way")

try:
    import grabbo
except:
    print("Please first install Grabbo in your python path or copy to crowbar dir")
    print("Grabbo can be download from https://github.com/jeremi360/Grabbo")
    exit()

home = os.path.expanduser("~")
conf = os.path.join(home,'.crowbar')

UI_Group = os.path.join(r, 'ui', 'Group.xml')

class Tabs_Manager(grabbo.Notebook):
    def __init__(self, mc):
        self.MC = mc
        super(Tabs_Manager, self).__init__(Gtk.Stack())

    def on_add(self, button):
        self.add_tab()

    def add_tab(self, url = None):
        con = Tab(self, url)
        self.add_content(con)

    def add_content(self, content):
        grabbo.Notebook.add_tab(self, content.get(), content.tb)
        content.get().show()
        w = self.get_width() + 210
        self.set_width(w)
        self.sc.show()

    def set_width(self, width):
        w = self.MC.parent.get_screen().get_width()
        if width < w*0.85:
            self.sc.set_min_content_width(width)

    def get_width(self):
        return self.sc.get_min_content_width()


class Main_Controls(grabbo.Builder):
    def __init__(self, parent):
        grabbo.Builder.__init__(self, UI_Group)

        self.parent = parent
        self.menub = self.ui.get_object("MenuButton")
        self.downs = self.ui.get_object("Downs")
        self.full = self.ui.get_object("Full")
        self.StartBox = self.ui.get_object("StartBox")
        self.EndBox = self.ui.get_object("EndBox")

    def set_title(self, title):
        self.parent.hb.set_title("Crowbar: " + title)

class Window(grabbo.Window):
    def __init__(self):
        super(Window, self).__init__()
        self.MC = Main_Controls(self)

        i = os.path.join(r, 'icons', 'icon.png')
        self.set_icon_from_file(i)

        self.tabs = Tabs_Manager(self.MC)

        self.tabs.add_tab("https://github.com/jeremi360/cRoWBaR")


        self.hb = Gtk.HeaderBar()
        self.hb.set_show_close_button(True)
        self.hb.set_title("Crowbar")
        self.hb.set_custom_title(self.tabs.get())
        self.hb.props.border_width = 0
        self.hb.props.margin_end = 0
        self.hb.props.margin_start = 0
        self.hb.props.margin = 0
        self.hb.props.height_request = 1
        self.hb.pack_start(self.MC.StartBox)
        self.hb.pack_end(self.MC.EndBox)
        self.hb.set_has_subtitle(False)
        self.set_titlebar(self.hb)

        self.add(self.tabs.stack)

        self.hb.show()
        self.tabs.stack.show()
        self.show()

    def on_close(self, button):
        grabbo.Window.on_close(self, button)

if __name__ == "__main__":
    app = Window()
    Gtk.main()
