import os
import urllib2
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf


def quit_event(widget, event):
    os.remove(imgname)
    Gtk.main_quit()

imgname = '1338.jpg'
url = 'http://lolcat.com/images/lolcats/'+imgname
response = urllib2.urlopen(url)
with open(imgname, 'wb') as img:
    img.write(response.read())

image = Gtk.Image()
pb = Pixbuf.new_from_file(imgname)
image.set_from_pixbuf(pb)

window = Gtk.Window()
window.connect('delete-event', quit_event)
window.add(image)
window.show_all()
Gtk.main()
