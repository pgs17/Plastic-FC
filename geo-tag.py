import PIL.Image
from pathlib import Path
path=Path('C:/Users/Lenovo/DJI_0023.jpg')
img=PIL.Image.open(path)

import PIL.ExifTags
exif={PIL.ExifTags.TAGS[k]:v
      for k,v in img._getexif().items()
      if k in PIL.ExifTags.TAGS
      
      }
n=exif['GPSInfo'][2]
e=exif['GPSInfo'][4]
ltd=(float)((((n[0]*60)+n[1])*60)+n[2])/60/60
lng=(float)((((e[0]*60)+e[1])*60)+e[2])/60/60
print(ltd,lng)
from gmplot import gmplot
gmap=gmplot.GoogleMapPlotter(ltd,lng,12)
gmap.marker(ltd,lng,'blue')
gmap.draw('location.html')