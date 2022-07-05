from assertpy import assert_that

from src.anchor_transformations import turn_links_into_footnotes


class TestAnchorTransformations:
    def test_turn_link_into_footnote(self):
        expected_text = (
            "text [^text1]"
            "\n\n"
            "[^text1]: #"
        )

        result = turn_links_into_footnotes("[text](#)")

        assert_that(result).is_equal_to(expected_text)

    def test_turn_paragraph_into_footnote(self):
        input_text = (
            "[this book](https://codigosostenible.com) and some other text\n"
            "and some other text line."
        )
        expected_text = (
            "this book [^this book1] and some other text\n"
            "and some other text line."
            "\n\n"
            "[^this book1]: https://codigosostenible.com"
        )

        result = turn_links_into_footnotes(input_text)

        assert_that(result).is_equal_to(expected_text)
