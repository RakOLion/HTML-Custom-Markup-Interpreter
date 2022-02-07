import re
import sys

if len(sys.argv) != 3:
    print("Invalid argument:\nUse >> python main.py [infile.txt] [outfile.html]")
    sys.exit()
path_in = sys.argv[1]
path_out =  sys.argv[2]

f = open(path_in, "r")

pre = '''<!DOCTYPE html> 
<html>
  <head>  
    <title>%s</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="/styles.css">
    <link href="/prism/prism.css" rel="stylesheet" />
  </head>
<body>
<article>
'''

suf = '''</article>
<footer><p>Made by Rally Lin</p></footer>
<script src="/prism/prism.js"></script>
</body>
</html>
'''

code_block = False

def inline_bold(s):
    return re.sub(r"(?=\*\*).+?(\*\*)", lambda match: f"<strong>{match.group()[2:-2]}</strong>",s) #re.sub works with a string replacement, but it can also take in a function, which we define with lambda here

def inline_italics(s):
    return re.sub(r"(?=__).+?(__)", lambda match: f"<em>{match.group()[2:-2]}</em>",s)

def inline_code(s): 
    find = s.find("`")
    while(find!=-1):
      lang = re.search(r"(?<=\[).+?(?=\])", s[find:]).group()
      s = s[:find]+re.sub(r"(?=`).+?(`)", lambda match: f"<code class='language-{lang}'>{match.group()[3+len(lang):-1]}</code>", s[find:], 1) #substitutes only the first match
      find = s.find("`")
    return s
  
def inline_links(s): 
    find = s.find("~")
    while(find!=-1):
      link = re.search(r"(?<=\[).+?(?=\])", s[find:]).group()
      s = s[:find]+re.sub(r"(?=~).+?(~)", lambda match: f"<a href='{link}'>{match.group()[3+len(link):-1]}</a>", s[find:], 1) #substitutes only the first match
      find = s.find("~")
    return s

def clean_code(s):
  return s.replace("<", "&lt;")

def inline_formatting(s):
    s = inline_bold(s)
    s = inline_italics(s)
    s = inline_code(s)
    s = inline_links(s)
    return s

out = ""
for line in f:
    line = line.rstrip()
    if(line.endswith("```")):
        line = clean_code(line[:-3])
        out+=f"{line}</code></pre>\n\n"
        code_block = False
    elif(code_block):
        line = clean_code(line)
        out+=f"{line}\n"
    elif(line.startswith("@")):
      out= pre % (line[1:])
    elif(line.startswith("##")):
        out+=f"<h2>{line[2:]}</h2>\n\n"
    elif(line.startswith("#")):
        out+=f"<h1>{line[1:]}</h1>\n\n"
    elif(line.startswith("```[")):
        lang = re.search(r"(?<=\[).+?(?=\])", line).group()
        out+=f"<pre><code class='language-{lang}'>"
        code_block = True
    elif(line.startswith("[i]")):
      src = line[3:]
      out+=f"<div class = 'image-container'>\n\t<img src = '{src}' style='width:75%;height:75%;'></img>\n</div>\n\n"
    elif(line!=""):
      line = inline_formatting(line)
      out+=f"<p>{line}</p>\n\n"
out+=suf


f = open(path_out, "w")
f.write(out) 
f.close()
