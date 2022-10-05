###
# Erlang linter plugin for SublimeLinter3
# Uses erlc, make sure it is in your PATH
#
# Copyright (C) 2014  Clement 'cmc' Rey <cr.rey.clement@gmail.com>
#
# MIT License
###

"""This module exports the Erlc plugin class."""

from SublimeLinter.lint import Linter, util


class Erlc(Linter):
    """Provides an interface to erlc."""

    tempfile_suffix = "-"

    # ERROR FORMAT # <file>:<line>: [Warning:|] <message> #
    # ERROR FORMAT # <file>:<line>:<col>: [Warning:|] <message> #
    regex = (
        r"^.+?:(?P<line>\d+):(?:(?P<col>\d+):)?"
        r"(?:(?P<warning>\sWarning:\s)|(?P<error>\s))+"
        r"(?P<message>.+)"
    )

    error_stream = util.STREAM_STDOUT

    defaults = {
        "selector": "source.erlang",
        "-I": [],
        "-pa": [],
        "-pz": [],
        "-o": ".",
    }

    def cmd(self):
        """
        return the command line to execute.

        this func is overridden so we can handle included directories.
        """
        command = ['erlc', '-W', '${args}']

        settings = self.settings
        dirs = settings.get('include_dirs', [])
        pa_dirs = settings.get('pa_dirs', [])
        pz_dirs = settings.get('pz_dirs', [])
        output_dir = settings.get('output_dir', ".")

        if dirs:
            self.logger.warn(
                "Setting 'include_dirs' has been renamed to just 'I'.")
        if pa_dirs:
            self.logger.warn(
                "Setting 'pa_dirs' has been renamed to just 'pa'.")
        if pz_dirs:
            self.logger.warn(
                "Setting 'pz_dirs' has been renamed to just 'pz'.")
        if "output_dir" in settings and output_dir != ".":
            self.logger.warn(
                "Setting 'output_dir' has been renamed to just 'o'.")

        for d in dirs:
            command.extend(["-I", d])

        for d in pa_dirs:
            command.extend(["-pa", d])

        for d in pz_dirs:
            command.extend(["-pz", d])

        command.extend(["-o", output_dir])

        command.extend(["${file_on_disk}"])

        return command
