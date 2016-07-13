import re
import urllib2
from threading import Thread

from BeautifulSoup import BeautifulSoup


class PageFinder(object):
    def __init__(self):
        self.threads = []
        self.list_of_pages = []
        self.keyword = ""

    def worker(self):
        page = self.list_of_pages[len(self.list_of_pages) - 1]
        print("New connection " + page)
        try:
            req = urllib2.urlopen(page)
        except urllib2.HTTPError:
            pass
        try:
            soup = BeautifulSoup(req)
            for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
                l = link.get('href')
                if l not in self.list_of_pages and self.keyword in l:
                    self.list_of_pages.append(l)
                    fi = open("pages.txt", "a")
                    fi.write(l + "\n")
                    fi.close()
                    worker_thread = Thread(target=self.worker)
                    worker_thread.start()
                    self.threads.append(worker_thread)
        except UnboundLocalError:
            pass
        except urllib2.URLError:
            pass
        return

    def go(self):
        file_name = raw_input("file to write to> ")
        f = open(file_name, "w")
        f.write("")
        f.close()
        thing = raw_input("URL to crawl: ")
        self.keyword = raw_input("Keyword to search for: ")
        self.list_of_pages.append(thing)
        thread = Thread(target=self.worker)
        thread.start()
        self.threads.append(thread)
        for x in self.threads:
            x.join()
        print("Done.")
        return
