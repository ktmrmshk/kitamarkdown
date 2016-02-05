# coding:utf-8
import markdown
import sys

CSSFILE="<link rel='stylesheet' href='markdown4.css'/>"
HTMLHEAD='''
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<!-- Always force latest IE rendering engine (even in intranet) & Chrome Frame
		Remove this if you use the .htaccess -->
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">

		<title>###TITLE###</title>
		<meta name="description" content="">
		<meta name="author" content="kitamura">

		<meta name="viewport" content="width=device-width; initial-scale=1.0">

		<!-- Replace favicon.ico & apple-touch-icon.png in the root of your domain and delete these references -->
		<link rel="shortcut icon" href="/favicon.ico">
		<link rel="apple-touch-icon" href="/apple-touch-icon.png">
	</head>
'''

CSS1='''
<style>
body {
font-family: Helvetica, Arial, Freesans, clean, sans-serif;
padding:1em;
margin:auto;
max-width:42em;
background:#fefefe;
}

h1, h2, h3, h4, h5, h6 {
    font-weight: bold;
}

h1 {
    color: #000000;
    font-size: 28px;
}

h2 {
    border-bottom: 1px solid #CCCCCC;
    color: #000000;
    font-size: 24px;
}

h3 {
    font-size: 18px;
}

h4 {
    font-size: 16px;
}

h5 {
    font-size: 14px;
}

h6 {
    color: #777777;
    background-color: inherit;
    font-size: 14px;
}

hr {
    height: 0.2em;
    border: 0;
    color: #CCCCCC;
    background-color: #CCCCCC;
}

p, blockquote, ul, ol, dl, li, table, pre {
    margin: 15px 0;
}

code, pre {
    border-radius: 3px;
    background-color: #F8F8F8;
    color: inherit;
}

code {
    border: 1px solid #EAEAEA;
    margin: 0 2px;
    padding: 0 5px;
}

pre {
    border: 1px solid #CCCCCC;
    line-height: 1.25em;
    overflow: auto;
    padding: 6px 10px;
}

pre > code {
    border: 0;
    margin: 0;
    padding: 0;
}

a, a:visited {
    color: #4183C4;
    background-color: inherit;
    text-decoration: none;
}
</style>
'''

CSS2='''
<style>
body {
   font-family: Helvetica, arial, sans-serif;
   font-size: 14px;
   line-height: 1.6;
   padding-top: 10px;
   padding-bottom: 10px;
   background-color: white;
   padding: 30px; }

body > *:first-child {
   margin-top: 0 !important; }
body > *:last-child {
   margin-bottom: 0 !important; }

a {
   color: #4183C4; }
a.absent {
   color: #cc0000; }
a.anchor {
   display: block;
   padding-left: 30px;
   margin-left: -30px;
   cursor: pointer;
   position: absolute;
   top: 0;
   left: 0;
   bottom: 0; }

h1, h2, h3, h4, h5, h6 {
   margin: 20px 0 10px;
   padding: 0;
   font-weight: bold;
   -webkit-font-smoothing: antialiased;
   cursor: text;
   position: relative; }

h1:hover a.anchor, h2:hover a.anchor, h3:hover a.anchor, h4:hover a.anchor, h5:hover a.anchor, h6:hover a.anchor {
   text-decoration: none; }

h1 tt, h1 code {
   font-size: inherit; }

h2 tt, h2 code {
   font-size: inherit; }

h3 tt, h3 code {
   font-size: inherit; }

h4 tt, h4 code {
   font-size: inherit; }

h5 tt, h5 code {
   font-size: inherit; }

h6 tt, h6 code {
   font-size: inherit; }

h1 {
   font-size: 28px;
   color: black; }

h2 {
   font-size: 24px;
   border-bottom: 1px solid #cccccc;
   color: black; }

h3 {
   font-size: 18px; }

h4 {
   font-size: 16px; }

h5 {
   font-size: 14px; }

h6 {
   color: #777777;
   font-size: 14px; }

p, blockquote, ul, ol, dl, li, table, pre {
   margin: 15px 0; }

hr {
   border: 0 none;
   color: #cccccc;
   height: 4px;
   padding: 0;
}

body > h2:first-child {
   margin-top: 0;
   padding-top: 0; }
body > h1:first-child {
   margin-top: 0;
   padding-top: 0; }
body > h1:first-child + h2 {
   margin-top: 0;
   padding-top: 0; }
body > h3:first-child, body > h4:first-child, body > h5:first-child, body > h6:first-child {
   margin-top: 0;
   padding-top: 0; }

a:first-child h1, a:first-child h2, a:first-child h3, a:first-child h4, a:first-child h5, a:first-child h6 {
   margin-top: 0;
   padding-top: 0; }

h1 p, h2 p, h3 p, h4 p, h5 p, h6 p {
   margin-top: 0; }

li p.first {
   display: inline-block; }
li {
   margin: 0; }
ul, ol {
   padding-left: 30px; }

ul :first-child, ol :first-child {
   margin-top: 0; }

dl {
   padding: 0; }
dl dt {
   font-size: 14px;
   font-weight: bold;
   font-style: italic;
   padding: 0;
   margin: 15px 0 5px; }
dl dt:first-child {
   padding: 0; }
dl dt > :first-child {
   margin-top: 0; }
dl dt > :last-child {
   margin-bottom: 0; }
dl dd {
   margin: 0 0 15px;
   padding: 0 15px; }
dl dd > :first-child {
   margin-top: 0; }
dl dd > :last-child {
   margin-bottom: 0; }

blockquote {
   border-left: 4px solid #dddddd;
   padding: 0 15px;
   color: #777777; }
blockquote > :first-child {
   margin-top: 0; }
blockquote > :last-child {
   margin-bottom: 0; }

table {
   padding: 0;border-collapse: collapse; }
table tr {
   border-top: 1px solid #cccccc;
   background-color: white;
   margin: 0;
   padding: 0; }
table tr:nth-child(2n) {
   background-color: #f8f8f8; }
table tr th {
   font-weight: bold;
   border: 1px solid #cccccc;
   margin: 0;
   padding: 6px 13px; }
table tr td {
   border: 1px solid #cccccc;
   margin: 0;
   padding: 6px 13px; }
table tr th :first-child, table tr td :first-child {
   margin-top: 0; }
table tr th :last-child, table tr td :last-child {
   margin-bottom: 0; }

img {
   max-width: 100%; }

span.frame {
   display: block;
   overflow: hidden; }
span.frame > span {
   border: 1px solid #dddddd;
   display: block;
   float: left;
   overflow: hidden;
   margin: 13px 0 0;
   padding: 7px;
   width: auto; }
span.frame span img {
   display: block;
   float: left; }
span.frame span span {
   clear: both;
   color: #333333;
   display: block;
   padding: 5px 0 0; }
span.align-center {
   display: block;
   overflow: hidden;
   clear: both; }
span.align-center > span {
   display: block;
   overflow: hidden;
   margin: 13px auto 0;
   text-align: center; }
span.align-center span img {
   margin: 0 auto;
   text-align: center; }
span.align-right {
   display: block;
   overflow: hidden;
   clear: both; }
span.align-right > span {
   display: block;
   overflow: hidden;
   margin: 13px 0 0;
   text-align: right; }
span.align-right span img {
   margin: 0;
   text-align: right; }
span.float-left {
   display: block;
   margin-right: 13px;
   overflow: hidden;
   float: left; }
span.float-left span {
   margin: 13px 0 0; }
span.float-right {
   display: block;
   margin-left: 13px;
   overflow: hidden;
   float: right; }
span.float-right > span {
   display: block;
   overflow: hidden;
   margin: 13px auto 0;
   text-align: right; }

code, tt {
   margin: 0 2px;
   padding: 0 5px;
   white-space: nowrap;
   border: 1px solid #eaeaea;
   background-color: #f8f8f8;
   border-radius: 3px; }

pre code {
   margin: 0;
   padding: 0;
   white-space: pre;
   border: none;
   background: transparent; }

.highlight pre {
   background-color: #f8f8f8;
   border: 1px solid #cccccc;
   font-size: 13px;
   line-height: 19px;
   overflow: auto;
   padding: 6px 10px;
   border-radius: 3px; }

pre {
   background-color: #f8f8f8;
   border: 1px solid #cccccc;
   font-size: 13px;
   line-height: 19px;
   overflow: auto;
   padding: 6px 10px;
   border-radius: 3px; }
pre code, pre tt {
   background-color: transparent;
   border: none; }

sup {
   font-size: 0.83em;
   vertical-align: super;
   line-height: 0;
}
* {
	 -webkit-print-color-adjust: exact;
}
@media screen and (min-width: 914px) {
   body {
      width: 854px;
      margin:0 auto;
   }
}
@media print {
	 table, pre {
		  page-break-inside: avoid;
	 }
	 pre {
		  word-wrap: break-word;
	 }
}
</style>
'''

BODYHEAD='<body>'
BODYTAIL='</html></body>'


def usage():
    print 'usage: python md.py hoge.md foo.html'

def makehtml(in_md_file, out_html_file):
    f=open(in_md_file, 'r')
    mdsrc=f.read()
    f.close()
    
    first_line=""
    with open(in_md_file, 'r') as f:
        first_line = f.readline()

    #print first_line
    md = markdown.Markdown(extensions=['extra', 'toc', 'admonition',])
    html = md.convert(unicode(mdsrc, 'utf-8'))

    print type(html)
    f=open(out_html_file, 'w')
    #f.write(html)

    f.write(HTMLHEAD.replace('###TITLE###', first_line[:-1]))
    f.write(CSS2)
    f.write(BODYHEAD)
    f.write(html.encode('utf-8'))
    f.write(BODYTAIL)
    f.close()



if __name__ == '__main__':

    if(len(sys.argv) != 3):
        usage()
        exit()
    else:
        makehtml(sys.argv[1], sys.argv[2])

