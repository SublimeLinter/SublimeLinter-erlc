SublimeLinter-erlc
==========================


[![Build Status](https://travis-ci.com/SublimeLinter/SublimeLinter-erlc.svg?branch=master)](https://travis-ci.com/SublimeLinter/SublimeLinter-erlc)


This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [erlc](http://erlang.org/doc/man/erlc.html). It will be used with files that have the `Erlang` syntax.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before using this plugin, ensure that `erlc` is installed on your system, which is part of the `erlang` distribution.
`erlang` may be installed via package managers (`brew` on Mac OS X, `apt-get` on Debian), or via [installers at the erlang site](https://www.erlang-solutions.com/downloads/download-erlang-otp).

Please make sure that the path to `erlc` is available to SublimeLinter.
The docs cover [troubleshooting PATH configuration](http://sublimelinter.com/en/latest/troubleshooting.html#finding-a-linter-executable).


## Settings

Additional settings for erlc:

|Setting|Description|
|:------|:----------|
|I      |A list of directories to be added to the header search paths.
|pa     |A list of directories to be added to the beginning of the code path.
|pz     |A list of directories to be added to the end of the code path.
|o      |The directory where the compiler should place the output file. (Defaults to the working dir.)

You can add arbitrary command line arguments using the setting `args`.

Note:  On previous version sof this plugin the above settings were named `include_dirs`, `pa_dirs`, `pz_dirs`, and `output_dir`.  We now use the default name from the command line.

General documentation about the settings system can be found here:

- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html
