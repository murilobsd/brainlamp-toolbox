"""Test Essay."""

from unittest import TestCase

from brainlamp_toolbox.essay.model import Paragraph, Essay


class TestParagraph(TestCase):
    """Test Paragraph class."""

    def setUp(self):
        """Setup."""
        self.sample_text = """This family was a victim of a problem they could have avoided-a problem that, according to Florida park rangers, hundreds of visitors suffer each year." Several times a month," ranger Rod Torres of O'Leno State Park said, "people get scared and leave the park in the middle of the night." Those people picked the wrong kind of park to visit. Not that there was anything wrong with the park: The hikers camped next to them loved the wild isolation of it. But it just wasn't the kind of place the couple from New Jersey had in mind when they decided to camp out on this trip through Florida."""

        self.p1 = Paragraph(self.sample_text)

    def test_words(self):
        """Test to see words."""
        self.assertEqual("victim" in self.p1.words, True)

    def test_no_word(self):
        """Test no word."""
        self.assertEqual("sdasdsd" in self.p1.words, False)

    def test_words_count(self):
        """Test word count."""
        self.assertEqual(self.p1.words_count, 123)

    def test_size(self):
        """Test size."""
        self.assertEqual(self.p1.size, 589)

    def test_sentences(self):
        """Test sentences."""
        expected = "This family was a victim of a problem they could have avoided-a problem that, according to Florida park rangers, hundreds of visitors suffer each year.\""
        self.assertEqual(expected in self.p1.sentences, True)

    def test_str__(self):
        """Test paragraph string."""
        self.assertEqual(str(self.p1), str(self.sample_text))

    def test_repr__(self):
        """Test paragraph string."""
        self.assertEqual(repr(self.p1), 'Paragraph({!r})'.
                         format(self.sample_text))


class TestEssay(TestCase):
    """Test Paragraph class."""

    def setUp(self):
        """Setup."""
        essay_text = """What are the application differences of a Polyurethane dispersion coating compared to a solvent based polyurethane and what are the advantages upon each other?

A polyurethane coating is a versatile product with many advantages upon other coating systems. A major disadvantage of classical, solvent based polyurethane coatings, are the volatile organic compounds (VOCs) present in the wet state. New regulations force formulators to keep the VOC content below 350 g/l. Recent developments dealt with this problem. Developers have succeeded in making a polyurethane dispersion in water, eliminating most of the volatile organic solvents.

However, the costs of a so called water borne polyurethane are higher than that of a solvent based polyurethane. A question that may arise is whether or not the dispersed polyurethane performs the same way as the classical, solvent based, polyurethanes and whether or not it is worth the money.

Besides possible differences in performance, processing techniques may differ. The goal of this investigation is to give an overview of the differences between the performance, processing and cost between a polyurethane dispersion and solvent based polyurethanes. The major formulations of both types will be summarized and compared to find the best coating."""

        self.title = 'title'
        self.essay = Essay(self.title, essay_text)

    def test_chars_count(self):
        """Test Essay chars count."""
        self.assertEqual(self.essay.chars_count, 1292)

    def test_words_count(self):
        """Test Essay words count."""
        self.assertEqual(self.essay.words_count, 216)

    def test_paragraphs_count(self):
        """Test Essay paragraphs count."""
        self.assertEqual(self.essay.paragraphs_count, 4)

    def test_str__(self):
        """Test paragraph string."""
        self.assertEqual(str(self.essay), self.title)

    def test_rpr__(self):
        """Test paragraph string."""
        self.assertEqual(repr(self.essay), 'Essay({!r})'.format(self.title))
