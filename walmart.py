from sys import argv
from PIL import Image
from queue import Queue

colors = [
  (255, 0, 0),
  (255, 0, 0),
  (255, 0, 0),
  (255, 0, 0),
  (255, 0, 0),
  (255, 0, 0),
  (255, 0, 0),
  (255, 0, 0),
  (255, 0, 0),
  (255, 125, 0),
  (255, 125, 0),
  (255, 125, 0),
  (255, 125, 0),
  (255, 125, 0),
  (255, 125, 0),
  (255, 125, 0),
  (255, 125, 0),
  (255, 125, 0),
  (255, 255, 0),
  (255, 255, 0),
  (255, 255, 0),
  (255, 255, 0),
  (255, 255, 0),
  (255, 255, 0),
  (255, 255, 0),
  (255, 255, 0),
  (255, 255, 0),
  (0, 255, 0),
  (0, 255, 0),
  (0, 255, 0),
  (0, 255, 0),
  (0, 255, 0),
  (0, 255, 0),
  (0, 255, 0),
  (0, 255, 0),
  (0, 255, 0),
  (0, 0, 255),
  (0, 0, 255),
  (0, 0, 255),
  (0, 0, 255),
  (0, 0, 255),
  (0, 0, 255),
  (0, 0, 255),
  (0, 0, 255)
]

colors = [
  (0, 162, 232),
  (0, 162, 232),
  (0, 162, 232),
  (0, 162, 232),
  (0, 162, 232),
  (0, 162, 232),
  (0, 162, 232),
  (0, 162, 232),
  (0, 162, 232),
  (0, 162, 232),
  (255, 127, 39),
  (255, 127, 39),
  (255, 127, 39),
  (255, 127, 39),
  (255, 127, 39),
  (255, 127, 39),
  (255, 127, 39),
  (255, 127, 39),
  (255, 127, 39),
  (255, 127, 39)
]

def betweenColors(color, minColor, maxColor):
  return (minColor[0] <= color[0] <= maxColor[0] and minColor[1] <= color[1] <= maxColor[1] and minColor[2] <= color[2] <= maxColor[2])

def iswhite(value):
    return value == (255, 255, 255, 255)

def isgray(value):
  return value == (127, 127, 127, 255)

def getadjacent(n):
    x,y = n
    return [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]

def BFS(start, endings, pixels):

  queue = Queue()
  queue.put([start]) # Wrapping the start tuple in a list

  while not queue.empty():

      path = queue.get()
      pixel = path[-1]
      other = {v: k for k,v in endings.items()}

      if pixel in other:
        print('Found', other[pixel])
        return other[pixel], path
      # for endName, endCoords in endings.items():
      #   # print(endName, endCoords, pixel)
      #   if endCoords == pixel:
      #     print('FOUND END', endCoords)
      #     return endName, path
      for adjacent in getadjacent(pixel):
          x,y = adjacent
          # print(x, y, pixels[x, y])
          if iswhite(pixels[x,y]):
              pixels[x,y] = (127, 127, 127, 255) # see note
              new_path = list(path)
              new_path.append(adjacent)
              queue.put(new_path)

  print("Queue has been exhausted. No answer was found")

def pathfind(args):
  im = Image.open("floorplan.png")
  pixels=im.load()

  loc = {
    "dairy" : (185, 30),
    "bakery" : (400, 35),
    "shoes" : (199, 226),
    "sporting-goods" : (201, 443),
    "toys" : (310, 456),
    "health" : (410, 420),
    "housewares" : (272, 357),
    "boys-wear" : (301, 171),
    "ladies-wear" : (346, 188),
    "intimates" : (255, 280),
    "entry" : (475, 120),
    "registers" : (411, 220)
  }

  paths = []
  endings = {}
  start = loc['entry']

  for category in args:
    endings[category] = loc[category]

  while endings:
    im = Image.open("floorplan.png")
    pixels=im.load()
    print('Endings', endings, 'start', start)
    search = BFS(start, endings, pixels)
    if not search:
      break
    foundEnd, path = search
    del endings[foundEnd]
    start = path[-1]
    paths += path

  endings['registers'] = loc['registers']
  search = BFS(start, endings, pixels)
  if not search:
    print('Unable to locate regisers')
  else:
    foundEnd, path = search
    paths += path

    path_img = Image.open("original.png")
    path_pixels = path_img.load()

    colorIndex = 0

    for position in paths:
      colorIndex += 1
      for x, y in getadjacent(position):
        path_pixels[x,y] = colors[colorIndex % len(colors)]

    path_img.rotate(-90).transpose(Image.FLIP_LEFT_RIGHT).save("path.png")

if __name__ == '__main__':
    pathfind(argv)
  # # Brown between
  # brownMax = (203, 195, 182)
  # brownMin = (142, 131, 116)

  # # Gray between
  # grayMax = (227, 227, 227)
  # grayMin = (180, 180, 180)

  # row,col = im.size
  # blackWhiteMatrix = [[0 for _ in range(col)] for _ in range(row)]
  # for i in range(row):
  #   for j in range(col):
  #     red = pixels[i, j][0]
  #     green = pixels[i, j][1]
  #     blue = pixels[i, j][2]

  #     black = range(90)
  #     # if red in black and green in black and blue in black:
  #     if betweenColors(pixels[i, j], brownMin, brownMax) or betweenColors(pixels[i, j], grayMin, grayMax):
  #       # print('pixel at ', i, j, ' is black')
  #       blackWhiteMatrix[i][j] = 1

  # for r in blackWhiteMatrix:
  #   print(''.join(map(str, r)))

