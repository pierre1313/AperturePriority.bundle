PLUGIN_PREFIX = "/photos/aperturePriority"
RSS_FEED = "http://www.aperturepriorityphoto.com/index.php?x=rss"

####################################################################################################

def Start():
  Plugin.AddPrefixHandler(PLUGIN_PREFIX, MainMenu, L('Aperture Priority'), 'icon-default.png', 'art-default.jpg')
  Plugin.AddViewGroup("Pictures", viewMode="Pictures", mediaType="photos")

####################################################################################################

def MainMenu():
  dir = MediaContainer(art=R("art-default.jpg"), viewGroup="Pictures", title1="Aperture Priority")

  for item in RSS.FeedFromURL(RSS_FEED).entries:
      node = HTML.ElementFromString(item.description)
      summary = ' '.join(node.xpath("//text()")).replace('\n','').strip()
      thumb = node.xpath("//img")[0].get('src')
      img = thumb.replace('thumbnails/thumb_', 'images/')

      dir.Append(PhotoItem(img, title=item.title, summary=summary, thumb=img))
  return dir
