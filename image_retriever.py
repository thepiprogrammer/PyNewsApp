#derived from https://gist.github.com/cdiener/10567484

import sys; from PIL import Image; import numpy as np; from urllib.request import *

def return_image(f, SC, GCF):
	chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))

	#if len(sys.argv) != 4: print( 'Usage: ./asciinator.py image scale factor' ); sys.exit()
	SC, GCF, WCF = float(SC), float(GCF), 7/4

	urlretrieve(f, "image.jpg")

	f = "image.jpg"

	img = Image.open(f)
	S = ( round(img.size[0]*SC*WCF), round(img.size[1]*SC) )
	img = np.sum( np.asarray( img.resize(S) ), axis=2)
	img -= img.min()
	img = (1.0 - img/img.max())**GCF*(chars.size-1)

	return "\n".join( ("".join(r) for r in chars[img.astype(int)]) )
	