import indicoio
import numpy as np
import matplotlib.pyplot as plt

# This is an example of how the batch API works on three different words
indicoio.batch_sentiment(["Happy", "Terrible", "Wonderful"])

text_file = open("call_of_the_wild.txt","r")
chunks = text_file.read().split()
text_file.close()

# We then slice the chunks to send to indico's sentiment API:
def chunker(seq, size):
      return (seq[pos:pos + size] for pos in xrange(0, len(seq), 1))

# Split the data up into 30,000+ chunks of 100 words each
data = [" ".join(group) for group in chunker(chunks, 100)]

# Sending off data for remote processing
sentiment_scores = indicoio.batch_sentiment(data)
 
# Conversion to numpy arrays
x = np.arange(len(data))
y = np.array(sentiment_scores)   

# Plotting and formatting
plt.scatter(x,y)
plt.ylim(ymax = 1.0, ymin = 0.0)
plt.xlim(xmax = 325, xmin = -1.0)
plt.title('Change In Sentiment Through "The Call of The Wild"', weight='bold')
plt.savefig('sentiment_scores.png')
