# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class NovelspiderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # bookName = Field()
    # bookTitle = Field()
    # chapterNum = Field()
    # chapterName = Field()
    # chapterURL = Field()
    # text = Field()
    read = Field()
    comment = Field()
    title = Field()
    author = Field()
    date = Field()
    last = Field()
    text = Field()