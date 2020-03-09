# Working with HTML data
from html.parser import HTMLParser

metacount = 0; # global var for handle_startendtag

class MyHTMLParser(HTMLParser):
    # subclass MyHTMLParser is to overwrite default fns from HTMLParser
    def handle_comment(self, data):
        print("Encountered comment: ", data)
        pos = self.getpos() # get position where the comment is (line number and char position is returned)
        print("\tAt line: ", pos[0], "position ", pos[1])

    def handle_starttag(self, tag, attrs):
        # called when closing bracket of start tag is called ex: <div here it is called>
        global metacount # get the global variable
        if tag == "meta":
            metacount += 1 # count meta data
        print("Encountered tag: ", tag)
        pos = self.getpos() # get position
        print("\tAt line: ", pos[0], "position ", pos[1])

        if attrs.__len__():
            print("\tAttributes:")
            for a in attrs:
                print("\t", a[0], "=", a[1])

    def handle_endtag(self, tag):
        print("Encountered tag: ", tag)
        pos = self.getpos() # get position
        print("\tAt line: ", pos[0], "position ", pos[1])

    def handle_data(self, data):
        if data.isspace():
            return # ignore white spaces
        print("Encountered data: ", data)
        pos = self.getpos() # get position
        print("\tAt line: ", pos[0], "position ", pos[1])
        
def main():
    # instantiate parser and feed it some HTML
    parser = MyHTMLParser()
    f = open("python_101/05/samplehtml.html")
    if f.mode == 'r':
        contents = f.read()
        parser.feed(contents)

    print("Meta tags found: " + str(metacount))

if __name__ == "__main__":
    main()