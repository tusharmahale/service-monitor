import threading, time, os
from flask import Flask, render_template, g
import urllib.request, urllib.error

app = Flask(__name__)

def performCheck(name,url):
    while True:
        status, url = getStatus(url)
        if name not in url_stats:
            url_stats[name] = {}
        url_stats[name].setdefault(url, []).insert(0,status)
        url_stats[name][url] = url_stats[name][url][:7]
        time.sleep(600)

def getStatus(ourl):
    try:
        conn = urllib.request.urlopen(ourl)
        return '200', ourl
    except urllib.error.HTTPError as e:
        return e.code, ourl
    except urllib.error.URLError as e:
        return "DOWN", ourl
    except:
        return 'error', ourl
try:
  if os.path.getsize('input.csv') > 0:
    try:
      url_stats={}
      threads = [threading.Thread(target=performCheck, args=(line.split(",")[0],line.split(",")[1].strip(),)) for line in open('input.csv')]
      for thread in threads:
        thread.daemon = True
        thread.start()
    except:
      pass
except:
  print("File input.csv is empty or does not exists")
  
@app.route("/")
@app.route("/stats")
def stats_html():
  try:
    g.url_stats = url_stats
    return render_template('stats.html')
  except:
    return "Please correct inputfile input.csv"

@app.route("/api")
def stats():
  try:
    return url_stats
  except:
    return "Please correct inputfile input.csv"

@app.route("/health")
def stats_health():
  return "OK"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port='8000')
