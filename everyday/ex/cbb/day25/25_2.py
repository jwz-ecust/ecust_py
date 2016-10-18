from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        print '<%s>' % tag

    def handle_endtag(self, tag):
        print "</%s>" % tag

    def handle_startendtag(self, tag, attrs):
        print '<%s/>' % tag

    def handle_data(self, data):
        print data

    def handle_comment(self, data):
        print '<!-- -->'

    def handle_entityref(self, name):
        print "&%s;" % name

    def handle_charref(self, name):
        print "&#%s;" % name


parser = MyHTMLParser()
parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial.\
    ..<br>END</p></body></html>')
