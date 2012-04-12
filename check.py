#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
## 2012 Víctor R. Ruiz <rvr@linotipo.es>
##
## Checks the status of delicious bookmarks using its
## export file format
##

import urllib2
import re

def urlopen(url):
    """ Returns the HTTP status code of the URL """
    try:
        resp = urllib2.urlopen(url)
    except:
        return -1
    return resp.code

def main():
    reBookmark = re.compile('^<DT><A HREF="(.*?)" ADD_DATE="(.*?)" PRIVATE="(.*)" TAGS="(.*?)">(.*?)</A>')
    bookmarks = open('delicious.html') # Bookmark file
    output = open('delicious-status.txt', 'a') # Status file
    found = False
    for bookmark in bookmarks.readlines():
        find = reBookmark.findall(bookmark)
        if (find and len(find) == 1):
            (url, date, private, tags, title) = find[0]
            status = urlopen(url)
            status_line = "%s\t%s\t%s" % (date, url, status)
            print status_line
            output.write(status_line + "\n")
    output.close()
    bookmarks.close()

if __name__ == '__main__':
    main()
