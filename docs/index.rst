wikidata-fast-query: Simple interface for querying data from an item
====================================================================

.. image:: https://img.shields.io/pypi/v/wikidata-fast-query.svg
   :target: https://pypi.python.org/pypi/wikidata-fast-query

.. image:: https://img.shields.io/pypi/pyversions/wikidata-fast-query.svg
   :target: https://pypi.python.org/pypi/wikidata-fast-query

.. image:: https://img.shields.io/pypi/l/wikidata-fast-query.svg
   :target: https://pypi.python.org/pypi/wikidata-fast-query

Quickstart
##########

.. doctest::

   >>> import pywikibot
   >>> from wikidata_fast_query import ItemContainer

   >>> site = pywikibot.Site("wikidata", "wikidata")
   >>> item = ItemContainer("Q42", site)

   >>> container = ItemContainer(item)
   >>> container.labels("en")
   'Douglas Adams'
   >>> container.descriptions("en")
   'English writer and humorist (1952–2001)'
   >>> container.aliases("en")
   ["Douglas Noël Adams", "DNA"]
   >>> container.claims("P31").first().getTarget()
   "Q5"

API
###

.. automodule:: wikidata_fast_query
   :members:
   :undoc-members:
   :show-inheritance:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
