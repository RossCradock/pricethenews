from config import db

class stocks(db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   display_name = db.Column('display_name', db.String(255))
   url_name = db.Column('url_name', db.String(255))
   symbol = db.Column('symbol', db.String(255))
   specific_tag = db.Column('specific_tag', db.String(255))
   broad_tag = db.Column('broad_tag', db.String(255))
   region = db.Column('region', db.String(255))

def __init__(id, display_name, url_name, symbol, specific_tag, broad_tag, region):
    self.id = id
    self.display_name = display_name
    self.url_name = url_name
    self.symbol = symbol
    self.specific_tag = specific_tag
    self.broad_tag = broad_tag
    self.region = region


class indices(db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   name = db.Column('name', db.String(255))
   country = db.Column('country', db.String(255))
   symbol = db.Column('symbol', db.String(255))
   search_tag = db.Column('search_tag', db.String(255))

def __init__(id, name, country, symbol, search_tag):
    self.id = id
    self.name = name
    self.country = country
    self.symbol = symbol
    self.search_tag = search_tag