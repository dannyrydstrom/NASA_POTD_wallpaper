import xml.etree.ElementTree
import urllib2
import ctypes
import os

"""Load the RSS feed from the website."""
rss_response = urllib2.urlopen('http://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss')
rss = rss_response.read()

"""Load the RSS feed into python's built-in xml library."""
rss_xml = xml.etree.ElementTree.fromstring(rss)

"""Iterate through the xml looking for the URL."""
channel = rss_xml.find('channel')
item = channel.find('item')
enclosure = item.find('enclosure')
img_url = enclosure.attrib['url']

"""Download the image into the local storage."""
filename = img_url.split('/')[-1]
filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
img_response = urllib2.urlopen(img_url)
img = open(filename, 'wb')
img.write(img_response.read())
img.close()

""" Set the windows background to the image. """
ctypes.windll.user32.SystemParametersInfoA(20, 0, filepath, 0)
