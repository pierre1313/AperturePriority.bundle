from PMS import *
from PMS.Objects import *
from PMS.Shortcuts import *

PLUGIN_PREFIX = "/photos/aperturePriority"
RSS_FEED = "http://www.theingersolls.com/Will/index.php?x=rss"

####################################################################################################

def Start():
  Plugin.AddPrefixHandler(PLUGIN_PREFIX, MainMenu, L('Aperture Priority'), 'icon-default.png', 'art-default.jpg')
  Plugin.AddViewGroup("Pictures", viewMode="Pictures", mediaType="photos")

####################################################################################################

def MainMenu():
  dir = MediaContainer(art="art-default.jpg", viewGroup="Pictures", title1="Aperture Priority")

  for item in RSS.FeedFromURL(RSS_FEED).entries:
      node = XML.ElementFromString(item.description, True)
      summary = ' '.join(node.xpath("//text()")).replace('\n','').strip()
      thumb = node.xpath("//img")[0].get('src')
      img = thumb.replace('thumbnails/thumb_', 'images/')

      dir.Append(PhotoItem(img, title=item.title, summary=summary, thumb=img))
  return dir
