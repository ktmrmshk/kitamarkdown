import md
import os.path
import sys
import glob

def usage():
    print 'usage: python pagen.py your_dir'

if len(sys.argv) != 2:
    usage()
    exit()

mdlist = glob.glob('%s/*.md' % sys.argv[1])
#print mdlist

for mdfile in mdlist:
    prefix = os.path.splitext(mdfile)[0]
    htmlfile= '%s.html' % prefix
    if os.path.exists(htmlfile):
        print prefix, 'html file exists'
    else:
        print 'generating html:', htmlfile
        md.makehtml(mdfile, htmlfile)

