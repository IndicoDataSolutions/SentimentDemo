# SentimentDemo
Tracking how sentiment changes throughout a novel.

Installing dependencies
------------
You'll need `indicoio`, `numpy`, `ipython` and `matplotlib` to run this demo.

```
pip install numpy matplotlib indicoio
```

For help installing numpy, visit http://docs.scipy.org/doc/numpy/user/install.html

Usage
------

Start the ipython notebook:
```
ipython notebook sentiment.ipynb
```

Or run the standalone python file:
```
python sentiment.py
```

Configuration
--------------

In order to use indico's batch API, you'll need to store your credentials in your `~/.indicorc` file.

```
[auth]
username = example@example.com
password = *************
```
