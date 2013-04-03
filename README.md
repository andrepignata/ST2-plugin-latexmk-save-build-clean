ST2-plugin-latexmk-save-build-clean
===================================

This is a Sublime Text 2 plugin designed to run on the OSX operating system Snow Leopard through Mountain Lion.  Provided that MacTex is installed (e.g., TexLive), this plugin will take a *.tex file in the open tab and perform the following operations:  save, build, clean-up.  If the build fails due to an improperly configured *.tex file, then an error message will appear in the status bar (and within the Python console) and the clean-up process is aborted.

In the process of adding shutil copy option, with plans to enable forward/backward sync to / from the *.pdf.
