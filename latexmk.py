import sublime, sublime_plugin
import os, os.path
import subprocess

class LatexmkBuildClean(sublime_plugin.TextCommand):

    def run(self, edit):

        path, filename = os.path.split(self.view.file_name())

        latexmkrc = '/Users/HOME/Library/Application Support/Sublime Text 2/Packages/0.LaTeX/.latexmkrc'

        script = '/usr/local/texlive/2012/texmf-dist/scripts/latexmk/latexmk.pl'

        try:

            print "\n" * 100

            print "----------------------------------------------------------------------------------\n"

            print "/Users/HOME/Library/Application Support/Sublime Text 2/Packages/0.LaTeX/latexmk.py\n"

            print "latexmk (build):  beginning process.\n"

            sublime.status_message("latexmk: saving: %s" % filename)

            print "latexmk (build):  saving file.\n"

            view = self.view

            if view.file_name() is None:

                view.run_command('prompt_save_as')

            else:

                view.run_command('save')

            print " "

            subprocess.check_call([script, "-r", latexmkrc, "-output-directory=" + path, path + "/" + filename])

            # BEGIN -- print the terminal output to the python console.
            proc=subprocess.Popen([script, "-r", latexmkrc, "-output-directory=" + path, path + "/" + filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output=proc.communicate()[0]
            print output
            # END -- print the terminal output to the python console.

            sublime.set_timeout(lambda: sublime.status_message("latexmk: build successfully completed: %s" % filename), 2000)

            print "latexmk (build):  process complete.\n"

        except subprocess.CalledProcessError:

            sublime.status_message("latexmk: ERROR: %s" % filename)

            print "latexmk:  Ooops!  Please check your *.tex for errors and try again.\n"

        else:

            print "----------------------------------------------------------------------------------\n"

            print "latexmk (cleanup):  beginning process.\n"

            subprocess.call([script, "-c", "-r", latexmkrc, "-output-directory=" + path, path + "/" + filename])

            # BEGIN -- print the terminal output to the python console.
            proc=subprocess.Popen([script, "-c", "-r", latexmkrc, "-output-directory=" + path, path + "/" + filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output=proc.communicate()[0]
            print output
            # END -- print the terminal output to the python console.

            sublime.set_timeout(lambda: sublime.status_message("latexmk: cleanup successfully completed: %s" % filename), 4000)

            print "latexmk (cleanup):  process complete."