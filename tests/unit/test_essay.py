from unittest import TestCase

from brainlamp_toolbox.essay.model import Paragraph


class TestParagraph(TestCase):

    def setUp(self):
        self.sample_text = """This family was a victim of a problem they could have avoided-a problem that, according to Florida park rangers, hundreds of visitors suffer each year." Several times a month," ranger Rod Torres of O'Leno State Park said, "people get scared and leave the park in the middle of the night." Those people picked the wrong kind of park to visit. Not that there was anything wrong with the park: The hikers camped next to them loved the wild isolation of it. But it just wasn't the kind of place the couple from New Jersey had in mind when they decided to camp out on this trip through Florida."""

        self.p1 = Paragraph(self.sample_text)
        # self.p2 = Paragraph(2)

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
