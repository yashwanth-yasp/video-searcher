# window.py
#
# Copyright 2023 Yashwanth A Doddegowda
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk


@Gtk.Template(resource_path='/com/example/video_searacher/window.ui')
class VideoSearcherWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'VideoSearcherWindow'

    label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class AboutDialog(Gtk.AboutDialog):

    def __init__(self, parent):
        Gtk.AboutDialog.__init__(self)
        self.props.program_name = 'video_searcher'
        self.props.version = "0.1.0"
        self.props.authors = ['Yashwanth A Doddegowda']
        self.props.copyright = '2022 Yashwanth A Doddegowda'
        self.props.logo_icon_name = 'com.example.video_searacher'
        self.props.modal = True
        self.set_transient_for(parent)
