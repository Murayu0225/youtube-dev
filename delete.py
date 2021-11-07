import datetime, os, send2trash
 
now = datetime.date.today()

# ディレクトリ移動の必要がGitHub Actionsは要らないのかもしれない。
# os.chdir(__file__)

for file in os.listdir():
 mtime = datetime.date.fromtimestamp(int(os.path.getmtime(file)))
 base, ext = os.path.splitext(file)

 if (now - mtime).days >= 30:
  if ext.endswith('.txt'):
   send2trash.send2trash(file)
