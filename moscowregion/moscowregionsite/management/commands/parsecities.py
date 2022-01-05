from django.core.management.base import BaseCommand
import requests
from lxml import html
from ...models import Locality


class Command(BaseCommand):
    help = 'Парсинг городских населённых пунктов Московской области'

    def handle(self, *args, **options):
        Locality.truncate()

        url = 'https://ru.wikipedia.org/wiki/Городские_населённые_пункты_Московской_области'
        # content = ''
        r = requests.get(url)
        tree = html.fromstring(r.text)

        # content += "==Города==\n"

        trs = tree.xpath("(//h2[.//span[@id='Города']]/following::table)[1]//tr[.//td]")
        for tr in trs:
            tds = tr.xpath('./td')
            Locality(
                subordination="RE" if "bright" in tr.classes else "CL" if "shadow" in tr.classes else "DI",
                name=tds[1].xpath('.//text()')[0],
                url="https://ru.wikipedia.org/" + tds[1].xpath('./a/@href')[0],
                unit=tds[2].xpath('.//text()')[0],
                OKATO=tds[3].xpath('.//text()')[0],
                population=tds[4].xpath('./@data-sort-value')[0],
                founded=tds[5].xpath('.//text()')[0],
                city_status=tds[6].xpath('.//text()')[0],
                category="город"
            ).save()
            # content += ("RE" if "bright" in tr.classes else "CL" if "shadow" in tr.classes else "DI") + '\n'
            # content += tds[1].xpath('.//text()')[0] + '\n'
            # content += "https://ru.wikipedia.org/" + tds[1].xpath('./a/@href')[0] + '\n'
            # content += tds[2].xpath('.//text()')[0] + '\n'
            # content += tds[3].xpath('.//text()')[0] + '\n'
            # content += tds[4].xpath('./@data-sort-value')[0] + '\n'
            # content += tds[5].xpath('.//text()')[0] + '\n'

        # content += "\n==Посёлки_городского_типа==\n"

        trs = tree.xpath("(//h2[.//span[@id='Посёлки_городского_типа']]/following::table)[1]//tr[.//td]")
        for tr in trs:
            tds = tr.xpath('./td')
            Locality(
                subordination="RE" if "bright" in tr.classes else "CL" if "shadow" in tr.classes else "DI",
                name=tds[1].xpath('.//text()')[0],
                url="https://ru.wikipedia.org/" + tds[1].xpath('./a/@href')[0],
                unit=tds[2].xpath('.//text()')[0],
                OKATO=tds[3].xpath('.//text()')[0],
                population=tds[4].xpath('./@data-sort-value')[0],
                category=tds[5].xpath('.//text()')[0]
            ).save()
            # content += ("ОБЛ_ПОДЧ" if "bright" in tr.classes else "ЗАТО" if "shadow" in tr.classes else "АДМ_ПОДЧ") + '\n'
            # content += tds[1].xpath('.//text()')[0] + '\n'
            # content += "https://ru.wikipedia.org/" + tds[1].xpath('./a/@href')[0] + '\n'
            # content += tds[2].xpath('.//text()')[0] + '\n'
            # content += tds[3].xpath('.//text()')[0].replace(' ', ' ') + '\n'
            # content += tds[4].xpath('./@data-sort-value')[0] + '\n'
            # content += tds[5].xpath('.//text()')[0] + '\n'

        # with open('test.html', 'w') as output_file:
        #     output_file.write(content)
