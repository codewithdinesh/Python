import html

myhtml = '<!DOCTYPE html> <html> <head> <title>This is demo site </title></head><body><h1 style="text-align:center;">Progamming Funda is best place to learn programming </h1></body></html>'

result = html.escape(myhtml)
print(result)