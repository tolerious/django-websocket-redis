from fabric.api import *

def p(b):
    with settings(warn_only=True):
        local("git commit -am 'translation update.'&&git push origin %s" % b)
