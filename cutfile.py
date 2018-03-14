import textwrap
def cutting(text_sample, width):

 if 0<len(text_sample) < 1000 and 0 < width < len(text_sample):
  result = textwrap.fill(text_sample,width)
 else:
  result = "fail"
 return result

print cutting("abcdefghijklmnopqrstuvwxyz",9)
