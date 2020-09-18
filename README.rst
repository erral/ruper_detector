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
    20131108
    Ondo!!! Gaur Ruper 2 aldiz entzungo dugu!! Hauek dira orduak:
    10:43:31 EGIN KONTU
    18:10:58 I-SIGARRILLOS AMARILLOS B

Beste aukera bat, programa hau zure garapen baten integratzea da. Horretarako instalatu
programa lehen esandako moduan (pip install ruper_detector) edo zure garapenaren
dependentziak instalatzeko erabiltzen duzun sisteman (gure kasuan `zc.buildout`_
darabilgun horretarako), eta ondoren inportatu Ruper detektorea zure garapenean::

    >>> from ruper_detector import detektorea
    >>> kantak = detektorea('20131108')
    >>> ruperren_kantak
    [{'artista': u'ORDORIKA RUPER', 'kanta': u'EGIN KONTU', 'ordua': u'10:43:31'},
     {'artista': u'I-ORDORIKA RUPER B',
      'kanta': u'I-SIGARRILLOS AMARILLOS B',
      'ordua': u'18:10:58'}]

Adibide bat
--------------

Ruper detektorearen adibide bat, helbide honetan duzue: `http://www.codesyntax.com/eu/labs/ruper_detector`_

.. _`EITB Musika`: https://www.eitb.eus/eu/irratia/eitb-musika/
.. _`http://www.codesyntax.com/eu/labs/ruper_detector`: http://www.codesyntax.com/eu/labs/ruper_detector
.. _Python: http://python.org
.. _`zc.buildout`: http://buildout.org
.. _pip: http://www.pip-installer.org
.. _`EITB Euskal Kantak`: https://www.eitb.eus/eu/irratia/eitb-euskal-kantak/
