#code from http://svn.effbot.org/public/tags/pil-1.1.7/Scripts/gifmaker.py

from PIL import Image, ImageChops
import string

from PIL.GifImagePlugin import getheader, getdata


class image_sequence:
    def __init__(self, im):
        self.im = im

    def __getitem__(self, ix):
        try:
            if ix:
                self.im.seek(ix)
            return self.im
        except EOFError:
            raise IndexError


def makedelta(fp, sequence):
    """Convert list of image frames to a GIF animation file"""

    frames = 0

    previous = None

    for im in sequence:

        # FIXME: write graphics control block before each frame

        if not previous:

            # global header
            for s in getheader(im) + getdata(im):
                fp.write(s)

        else:

            delta = ImageChops.subtract_modulo(im, previous)

            bbox = delta.getbbox()

            if bbox:

                for s in getdata(im.crop(bbox), offset=bbox[:2]):
                    fp.write(s)

            else:
                # FIXME: what should we do in this case?
                pass

        previous = im.copy()

        frames = frames + 1

    fp.write(";")

    return frames

def compress(infile, outfile):

    im = Image.open(infile)
    im.load()

    # open output file
    fp = open(outfile, "wb")

    seq = image_sequence(im)

    makedelta(fp, seq)

    fp.close()


if __name__ == "__main__":

    import sys

    if len(sys.argv) < 3:
        sys.exit(1)

    compress(sys.argv[1], sys.argv[2])
