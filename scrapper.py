import scrapy

class LegoScrapper(scrapy.Spider):
  name = 'lego_scrapper'
  domain = 'https://bulbapedia.bulbagarden.net'

  start_urls = ["https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"]

  def parse(self, response):
    pokemons = response.css('tr')
    for pokemon in pokemons:
      #yield {'pokemon_name': pokemon.css('td>a::text').get()}

      pokemon_url = pokemon.css('td>a::attr(href)').get()
      if pokemon_url is not None:
        yield response.follow(self.domain + pokemon_url, self.parse_pokemon)

  def parse_pokemon(self, response):
    yield {'pokemon_name': response.css('td big big b::text').get()}