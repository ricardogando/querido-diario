from gazette.spiders.base.doem import DoemGazetteSpider
from datetime import date

class BaBanzaeSpider(DoemGazetteSpider):
    TERRITORY_ID = "2902658"
    name = "ba_banzae"
    state_city_url_part = "ba/banzae"
    start_date = date(2017, 2, 2)
