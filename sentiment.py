# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Sentiment Analysis of Jack London's "The Call of The Wild"
# ================================
# 
# Analysis by: Perry Grossman ([perrygrossman2008@gmail.com](mailto:perrygrossman2008@gmail.com)) using the Indico Sentiment API
# 
# Book Source from Project Gutenberg:
# http://www.gutenberg.org/files/215/215-h/215-h.htm

# <markdowncell>

# **Resources:** <br>
# See http://indico.readme.io/v1.0/docs/python for information on the Indico APIs.
# <br>
# Lower scores (< .5) correspond to negative sentiment, while higher scores (> 0.5) correspond to positive sentiment.

# <markdowncell>

# Using the Indico Sentiment API
# ======

# <markdowncell>

# You should have Python Installed. If you don't have it you can get it here:
# https://www.python.org/
# <br>I use Anaconda, which includes a number of extra libraries:
# https://store.continuum.io/cshop/anaconda/

# <markdowncell>

# Install the Indicoio public API, if it is not already installed, with `pip install indicoio`.

# <codecell>

# Import the indicoio module:
import indicoio

# Import other python modules for data analysis and visualization
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# <codecell>

# This is an example of how the batch API works on three different words
indicoio.batch_sentiment(["Happy", "Terrible", "Wonderful"])

# <markdowncell>

# **Opening the file**
# <br>Now we open the text from "The Call of the Wild."<br>
# (in a text editor I already trimmed the header and footer information.)

# <codecell>

text_file = open("call_of_the_wild.txt","r")
chunks = text_file.read().split()
text_file.close()

# <codecell>

s = len(chunks)
print "There are %s words in the file." %s

# <codecell>

# We then slice the chunks to send to indico's sentiment API:
def chunker(seq, size):
      return (seq[pos:pos + size] for pos in xrange(0, len(seq), 1))

# Split the data up into 30,000+ chunks of 100 words each
data = [" ".join(group) for group in chunker(chunks, 100)]

# Sending off data for remote processing
sentiment_scores = indicoio.batch_sentiment(data)

# <headingcell level=3>

# Now we chart the results

# <codecell>

# Chart sentiment scores
 
# Conversion to numpy arrays
x = np.arange(len(data))
y = np.array(sentiment_scores)   

# Plotting and formatting
plt.scatter(x,y)
plt.ylim(ymax = 1.0, ymin = 0.0)
plt.xlim(xmax = 325, xmin = -1.0)
plt.title('Change In Sentiment Through "The Call of The Wild"', weight='bold')
plt.savefig('sentiment_scores.png')

