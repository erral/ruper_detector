ruper_detector
===============

Gure bulegoan askotan edukitzen dugu `EITB Musika`_ jarrita. Eta askotan
esan ohi dugu Ruper Ordorikarenganako lerratze bat duela irrati horrek.

Orain gainera `EITB Euskal Kantak`_ irratia ere sortu du EITBk, eta hor
ere Ruper asko entzungo den susmoa dugu.

Gainera gure bulegoa Ruperren fanez beteta dago, eta beste batzuri logurea
besterik ez digu ematen.

Programatxo honek, egunaren zein ordutan lo hartuko dugun abisatzen digu
Ruper noiz jarriko duten esanez.

Broma bat da, hartu umorez!

Instalazioa eta erabilera
--------------------------

Ruper detektorea Python_ programazio lengoaiarako egindako programa da. Adi, pythonen 3.
bertsioarekin bakarrik funtzionatzen du-eta. Instalatzeko
beste edozein Python_ liburutegi bezala instalatu behar da. Gaur egun
pip_ tresna erabiliz egin dezakezu hori::

  $ pip install ruper_detector

Hori eginda, zure sisteman script bat instalatuko da, *ruper_detector*. Bere erabilera
oso erraza da: pasatu parametro bezala zein datan detektatu nahi duzun Ruper baina
UUUUHHEE formatua erabiliz, adibidez 20131108, horrela::

  $ ruper_detector 20131108

Pantailan bertan inprimatuko ditu emaitzak::

  $ ruper_detector 20131108
    Ruper detektatzen...
    20200918
    Ondo!!! Gaur Ruper 7 aldiz entzungo dugu!! Hauek dira orduak:
    EITB Musika 02:37:58 ETXE ALDERA
    EITB Musika 05:07:55 GALTZETAN GORDETZEKO KOBLAK
    EITB Euskal Kantak 05:42:12 EGIN KONTU
    EITB Musika 12:19:12 ZALDIAK NEGARREZ (LIVE)
    EITB Euskal Kantak 14:51:49 EZ DA POSIBLE (LIVE)
    EITB Musika 19:53:45 NOR DA (LIVE)
    EITB Euskal Kantak 21:25:31 NERE FURGOI BELTZA

Beste aukera bat, programa hau zure garapen baten integratzea da. Horretarako instalatu
programa lehen esandako moduan (pip install ruper_detector) edo zure garapenaren
dependentziak instalatzeko erabiltzen duzun sisteman (gure kasuan `zc.buildout`_
darabilgun horretarako), eta ondoren inportatu Ruper detektorea zure garapenean::

    >>> from ruper_detector import detektorea
    >>> kantak = detektorea('20201118')
    >>> from pprint import pprint
    >>> pprint(kantak)
    [{'artista': 'ORDORIKA RUPER',
      'irratia': 'EITB Musika',
      'kanta': 'ETXE ALDERA',
      'ordua': '02:37:58'},
    {'artista': 'ORDORIKA RUPER',
      'irratia': 'EITB Musika',
      'kanta': 'GALTZETAN GORDETZEKO KOBLAK',
      'ordua': '05:07:55'},
    {'artista': 'ORDORIKA RUPER',
      'irratia': 'EITB Euskal Kantak',
      'kanta': 'EGIN KONTU',
      'ordua': '05:42:12'},
    {'artista': 'ORDORIKA RUPER',
      'irratia': 'EITB Musika',
      'kanta': 'ZALDIAK NEGARREZ (LIVE)',
      'ordua': '12:19:12'},
    {'artista': 'ORDORIKA RUPER',
      'irratia': 'EITB Euskal Kantak',
      'kanta': 'EZ DA POSIBLE (LIVE)',
      'ordua': '14:51:49'},
    {'artista': 'ORDORIKA RUPER',
      'irratia': 'EITB Musika',
      'kanta': 'NOR DA (LIVE)',
      'ordua': '19:53:45'},
    {'artista': 'ORDORIKA RUPER',
      'irratia': 'EITB Euskal Kantak',
      'kanta': 'NERE FURGOI BELTZA',
      'ordua': '21:25:31'}]



Adibide bat
--------------

Ruper detektorearen adibide bat, helbide honetan duzue: `http://www.codesyntax.com/eu/labs/ruper_detector`_

.. _`EITB Musika`: https://www.eitb.eus/eu/irratia/eitb-musika/
.. _`http://www.codesyntax.com/eu/labs/ruper_detector`: http://www.codesyntax.com/eu/labs/ruper_detector
.. _Python: http://python.org
.. _`zc.buildout`: http://buildout.org
.. _pip: http://www.pip-installer.org
.. _`EITB Euskal Kantak`: https://www.eitb.eus/eu/irratia/eitb-euskal-kantak/
