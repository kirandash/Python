# Parcing XML Files
import xml.dom.minidom

def main():
    # use the parse() function to load and parse an XML file
    doc = xml.dom.minidom.parse("python_101/05/samplexml.xml")

    # print out the document node and the name of the first child tag
    print(doc.nodeName) # #document is the nodename as per W3 standards
    print(doc.firstChild.tagName)

    # get a list of XML tags from the document and print each name
    skills = doc.getElementsByTagName("skill")
    print("%d skills: " % skills.length)

    for skill in skills:
        print(skill.getAttribute("name"))

    # create a new XML tag and add it to the document
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name", "python")
    doc.firstChild.appendChild(newSkill) # append to end of firstChild

    print("After adding new skill")
    skills = doc.getElementsByTagName("skill")
    print("%d skills: " % skills.length)

    for skill in skills:
        print(skill.getAttribute("name"))

if __name__ == "__main__":
    main()