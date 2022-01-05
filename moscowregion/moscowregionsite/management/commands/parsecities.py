from django.core.management.base import BaseCommand
import requests
from lxml import html
from moscowregionsite.models import Locality


class Command(BaseCommand):
    help = 'Парсинг городских населённых пунктов Московской области'

    def handle(self, *args, **options):

        url = 'https://ru.wikipedia.org/wiki/Городские_населённые_пункты_Московской_области'
        r = requests.get(url)
        tree = html.fromstring(r.text)

        trs = tree.xpath("(//h2[.//span[@id='Города']]/following::table)[1]//tr[.//td]")
        for tr in trs:
            tds = tr.xpath('./td')
            city_name = tds[1].xpath('.//text()')[0]
            if Locality.objects.filter(name=city_name).count():
                record = Locality.objects.get(name=city_name)
                record.subordination = "RE" if "bright" in tr.classes else "CL" if "shadow" in tr.classes else "DI"
                record.url = "https://ru.wikipedia.org/" + tds[1].xpath('./a/@href')[0]
                record.unit = tds[2].xpath('.//text()')[0]
                record.OKATO = tds[3].xpath('.//text()')[0]
                record.population = tds[4].xpath('./@data-sort-value')[0]
                record.founded = tds[5].xpath('.//text()')[0]
                record.city_status = tds[6].xpath('.//text()')[0]
                record.category = "город"
                record.save()
            else:
                Locality(
                    subordination="RE" if "bright" in tr.classes else "CL" if "shadow" in tr.classes else "DI",
                    name=city_name,
                    url="https://ru.wikipedia.org/" + tds[1].xpath('./a/@href')[0],
                    unit=tds[2].xpath('.//text()')[0],
                    OKATO=tds[3].xpath('.//text()')[0],
                    population=tds[4].xpath('./@data-sort-value')[0],
                    founded=tds[5].xpath('.//text()')[0],
                    city_status=tds[6].xpath('.//text()')[0],
                    category="город"
                ).save()

        trs = tree.xpath("(//h2[.//span[@id='Посёлки_городского_типа']]/following::table)[1]//tr[.//td]")
        for tr in trs:
            tds = tr.xpath('./td')
            village_name = tds[1].xpath('.//text()')[0]
            if Locality.objects.filter(name=village_name).count():
                record = Locality.objects.get(name=village_name)
                record.subordination = "RE" if "bright" in tr.classes else "CL" if "shadow" in tr.classes else "DI"
                record.url = "https://ru.wikipedia.org/" + tds[1].xpath('./a/@href')[0]
                record.unit = tds[2].xpath('.//text()')[0]
                record.OKATO = tds[3].xpath('.//text()')[0]
                record.population = tds[4].xpath('./@data-sort-value')[0]
                record.category = tds[5].xpath('.//text()')[0]
                record.save()
            else:
                Locality(
                    subordination="RE" if "bright" in tr.classes else "CL" if "shadow" in tr.classes else "DI",
                    name=village_name,
                    url="https://ru.wikipedia.org/" + tds[1].xpath('./a/@href')[0],
                    unit=tds[2].xpath('.//text()')[0],
                    OKATO=tds[3].xpath('.//text()')[0],
                    population=tds[4].xpath('./@data-sort-value')[0],
                    category=tds[5].xpath('.//text()')[0]
                ).save()
