#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf=8 :
import urllib2
import bs4
import os


class Book(object):
    """Classe que conté tots els mètodes per tal d'obtenir les dades del llibre
    diari gratuït.
    """
    def to_string(self, title, desc):
        """Retorna un string amb la informació del llibre"""
        return "Title: " + title + "\n" + "Book description: " + desc

    def get_web(self, url):
        """Obté el codi html de la pàgina web en qüestió"""
        fd = urllib2.urlopen(url)
        html = fd.read()
        fd.close()
        return html

    def send_notify(self, msg):
        """Envia una notificació al sistema de notificacions de linux"""
        os.execlp('notify-send', '-i gtk-dialog-info', 'New Book Available',
                  msg)

    def book_info(self):
        """Obté la informació del llibre desitjada i retorna el seu títol i
        descripció
        """
        url = "https://www.packtpub.com/packt/offers/free-learning/"
        html = self.get_web(url)
        soup = bs4.BeautifulSoup(html, "lxml")
        book_info = soup.find("div", "dotd-main-book-summary float-left")
        title = book_info.find("h2")
        title = " ".join(title.text.split())
        description = book_info.find_all("div")
        description = " ".join(description[2].text.split())
        return title, description

    def main(self):
        """Funció principal de la classe"""
        title, description = self.book_info()
        print self.to_string(title, description)
        # self.send_notify(self.to_string(title, description))


if __name__ == '__main__':
    book = Book()
    book.main()
