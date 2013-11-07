from bs4 import BeautifulSoup

import argparse
import urllib2


EITB_MUSIKA_URL = 'http://www.eitb.com/es/modulo/radio/eitbmusika_2col_ajax/?station=1&date={0}&hour={1}'

RUPER = u'RUPER ORDORIKA'


def detektorea(eguna):
    """ Detektatu Ruper! """
    ruperren_kantak = []
    for int_ordua in range(24):
        ordua = '{0:02}'.format(1)
        url = EITB_MUSIKA_URL.format(eguna, ordua)
        sock = urllib2.urlopen(url)
        soup = BeautifulSoup(sock.read())
        for kanta in soup.find_all('tr'):
            for zutabe in kanta.find_all('td'):
                if RUPER in zutabe[1].text:
                    ruperren_kantak.append(dict(
                        ordua=zutabe[0].text,
                        artista=zutabe[1].text,
                        kanta=zutabe[2].text,
                        ))

    for kanta in ruperren_kantak:
        print kanta['ordua'], kanta['kanta']


def main():
    parser = argparse.ArgumentParser(
        description='EITB Irratiko Ruper detektorea')

    parser.add_argument('eguna',
                        type=str,
                        help='Idatzi eguna, honako formatu honetan: UUUUHHEE. Adibidez 20131107',
        )

    arguments = parser.parse_args()

    detektorea(arguments.eguna)
