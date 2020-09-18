from bs4 import BeautifulSoup

import argparse
import urllib.request


EITB_MUSIKA_URL = "http://www.eitb.eus/es/modulo/radio/eitbmusika_2col_ajax/?station=1&date={0}&hour={1}"

EITB_EUSKAL_MUSIKA_URL = "http://www.eitb.eus/es/modulo/radio/euskalkantak_2col_ajax/?station=1&date={0}&hour={1}"

RUPER = u"RUPER"

IRRATIAK = [
    {"title": "EITB Musika", "url": EITB_MUSIKA_URL},
    {"title": "EITB Euskal Kantak", "url": EITB_EUSKAL_MUSIKA_URL},
]


def detektorea(eguna):
    """ Detektatu Ruper! """
    ruperren_kantak = []
    for int_ordua in range(24):
        ordua = "{0:02}".format(int_ordua)
        for irratia in IRRATIAK:
            irratia_url = irratia["url"]
            irratia_title = irratia["title"]

            url = irratia_url.format(eguna, ordua)
            sock = urllib.request.urlopen(url)
            soup = BeautifulSoup(sock.read(), "html.parser")
            sock.close()
            for kanta in soup.find_all("tr"):
                zutabeak = kanta.find_all("td")
                if len(zutabeak) == 3:
                    if RUPER in zutabeak[1].text:
                        ruperren_kantak.append(
                            dict(
                                ordua=zutabeak[0].text,
                                artista=zutabeak[1].text,
                                kanta=zutabeak[2].text,
                                irratia=irratia_title,
                            )
                        )

            print(ordua, "done")

    return ruperren_kantak


def inprimatu(eguna):
    print("Ruper detektatzen...")
    ruperren_kantak = detektorea(eguna)
    print(eguna)
    if len(ruperren_kantak) == 1:
        print("Gaur Ruper behin bakarrik entzungo dugu. Apuntatu agendan!")
    elif len(ruperren_kantak) == 0:
        print("Ohhh! Gaur ez dute Ruper jarriko!!!")
    else:
        print(
            "Ondo!!! Gaur Ruper {0} aldiz entzungo dugu!! Hauek dira orduak:".format(
                len(ruperren_kantak)
            )
        )

    for kanta in ruperren_kantak:
        print(kanta["irratia"], kanta["ordua"], kanta["kanta"])


def main():
    parser = argparse.ArgumentParser(description="EITB Irratiko Ruper detektorea")

    parser.add_argument(
        "eguna",
        type=str,
        help="Idatzi eguna honako formatu honetan: UUUUHHEE. Adibidez 20131107",
    )

    arguments = parser.parse_args()

    inprimatu(arguments.eguna)
