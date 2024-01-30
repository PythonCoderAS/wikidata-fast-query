from . import sandbox_item
from wikidata_fast_query import ItemContainer


def test_simple():
    item = sandbox_item
    container = ItemContainer(item)
    en_label = container.labels("en")
    assert en_label is not None
    assert en_label == "Wikidata Sandbox"


def test_label_language():
    item = sandbox_item
    container = ItemContainer(item)
    fr_label = container.labels("fr")
    assert fr_label == "bac à sable Wikidata"


def test_label_no_language():
    item = sandbox_item
    container = ItemContainer(item)
    labels = container.labels()
    assert "en" in labels
    assert labels.get("en", None) is not None
    assert "fr" in labels
    assert labels.get("fr", None) is not None
    assert "fake" not in labels


def test_label_fake_language():
    item = sandbox_item
    container = ItemContainer(item)
    fake_label = container.labels("fake")
    assert fake_label is None


def test_label_languages():
    item = sandbox_item
    container = ItemContainer(item)
    languages = container.label_languages()
    assert "en" in languages
    assert "fr" in languages
    assert "fake" not in languages


def test_description_language():
    item = sandbox_item
    container = ItemContainer(item)
    en_description = container.descriptions("en")
    assert en_description
    assert "sandbox" in en_description


def test_description_no_language():
    item = sandbox_item
    container = ItemContainer(item)
    descriptions = container.descriptions()
    assert "en" in descriptions
    assert descriptions.get("en", None) is not None
    assert "fr" in descriptions
    assert descriptions.get("fr", None) is not None
    assert "fake" not in descriptions


def test_description_fake_language():
    item = sandbox_item
    container = ItemContainer(item)
    fake_description = container.descriptions("fake")
    assert fake_description is None


def test_description_languages():
    item = sandbox_item
    container = ItemContainer(item)
    languages = container.description_languages()
    assert "en" in languages
    assert "fr" in languages
    assert "fake" not in languages


def test_aliases_language():
    item = sandbox_item
    container = ItemContainer(item)
    en_aliases = container.aliases("en")
    assert en_aliases
    assert "sandbox" in en_aliases


def test_aliases_fake_language():
    item = sandbox_item
    container = ItemContainer(item)
    fake_aliases = container.aliases("fake")
    assert not fake_aliases


def test_aliases_no_language():
    item = sandbox_item
    container = ItemContainer(item)
    aliases = container.aliases()
    assert "en" in aliases
    assert aliases.get("en", None) is not None
    assert "es" in aliases
    assert aliases.get("es", None) is not None
    assert "fake" not in aliases


def test_aliases_languages():
    item = sandbox_item
    container = ItemContainer(item)
    languages = container.alias_languages()
    assert "en" in languages
    assert "es" in languages
    assert "fake" not in languages


def test_aliases_language_count():
    item = sandbox_item
    container = ItemContainer(item)
    aliases = container.alias_counts_by_language()
    assert "en" in aliases
    assert aliases.get("en", None) is not None
    assert aliases["en"] >= 1
    assert "fake" not in aliases
