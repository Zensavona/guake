#!/usr/bin/env python

import gi
import logging
import os

from gi.repository import GLib
from gi.repository import Gtk
from gi.repository import Vte


logger = logging.getLogger(__name__)


def test():
    gi.require_version('Gtk', '3.0')
    # before VTE 0.38
    # vte_terminal_fork_command_full ()
    # after
    # vte_terminal_spawn_sync ()
    terminal = Vte.Terminal()
    print("terminal: %s", dir(terminal))

    terminal.spawn_sync(
        Vte.PtyFlags.DEFAULT,
        os.environ['HOME'],
        ["/bin/bash"],
        [],
        GLib.SpawnFlags.DO_NOT_REAP_CHILD,
        None,
        None,
    )

    win = Gtk.Window()
    win.connect('delete-event', Gtk.main_quit)
    win.add(terminal)
    win.show_all()

    Gtk.main()
