#!/usr/bin/python3
"""Markdown to HTML converter script."""
from sys import argv
import os.path
from os import path
import sys


def eprint(*args, **kwargs):
    """Standerd error printed."""
    print(*args, file=sys.stderr, **kwargs)


if __name__ == "__main__":
    parameters = sys.argv
    if len(parameters) != 3:
        eprint("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    ParameterFileName = parameters[1]
    if not path.exists(ParameterFileName):
        eprint("Missing {}".format(ParameterFileName))
        exit(1)
    html = []
    uList = ""
    oList = ""
    with open(parameters[1], "r") as src:
        lines = src.readlines()
        lines[-1] = lines[-1].replace("\n", "")
    with open(parameters[2], "w") as destination:
        for line in lines:
            HashCount = line.count("#")
            if HashCount >= 1:
                noHash = line.replace("#" * HashCount + " ", "")
                noHash = noHash.replace("\n", "")
                HTML = "<h{}>{}</h{}>\n".format(HashCount, noHash, HashCount)
                html.append(HTML)
            elif " " in line[1] and "-" in line[0]:
                if "<li>" not in uList:
                    uList = "<ul>\n"
                CurrentLine = line.replace("- ", "")
                CurrentLine = CurrentLine.replace("\n", "")
                uList = uList + "\t<li>{}</li>\n".format(CurrentLine)
                if lines.index(line) + 1 < len(lines):
                    if "- " not in lines[lines.index(line) + 1]:
                        uList += "</ul>\n"
                        html.append(uList)
                        uList = ""
                else:
                    uList += "</ul>\n"
                    html.append(uList)
                    uList = ""
            elif " " in line[1] and "*" in line[0]:
                if "<li>" not in oList:
                    oList = "<ol>\n"
                CurrentLine = line.replace("* ", "")
                CurrentLine = CurrentLine.replace("\n", "")
                oList += "\t<li>{}</li>\n".format(CurrentLine)
                if lines.index(line) + 1 < len(lines):
                    if "* " not in lines[lines.index(line) + 1]:
                        oList += "</ol>\n"
                        html.append(oList)
                        oList = ""
                else:
                    oList += "</ol>\n"
                    html.append(oList)
                    oList = ""
        destination.writelines(html)
    exit(0)
