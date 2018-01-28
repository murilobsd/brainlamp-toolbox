from unittest import TestCase

from brainlamp_toolbox.text import Paragraph


class TestParagraph(TestCase):

    def setUp(self):
        self.sample_text = """This family was a victim of a problem they could have avoided-a problem that, according to Florida park rangers, hundreds of visitors suffer each year." Several times a month," ranger Rod Torres of O'Leno State Park said, "people get scared and leave the park in the middle of the night." Those people picked the wrong kind of park to visit. Not that there was anything wrong with the park: The hikers camped next to them loved the wild isolation of it. But it just wasn't the kind of place the couple from New Jersey had in mind when they decided to camp out on this trip through Florida."""

        self.p1 = Paragraph(1)
        self.p2 = Paragraph(2)

    def test_not_content(self):
        """Test to see if there is content."""
        self.assertEqual(self.p1.content, [])

    def test_p1_value(self):
        """Test checking the paragraph number 1."""
        self.assertEqual(self.p1.value, 1)

    def test_p2_value(self):
        """Test checking the paragraph number 2."""
        self.assertEqual(self.p2.value, 2)

    def test_not_content(self):
        """Test not content."""
        self.assertEqual(self.p1.count_lines, 0)

    def test_add_content(self):
        """Test by add content."""
        self.p2.add_content(self.sample_text)
        self.assertEqual(self.p2.count_lines, 1)

    def test_string_paragraph(self):
        """."""
        self.p2.add_content(self.sample_text)
        self.assertEqual(str(self.p2), self.sample_text)

    def test_words(self):
        """."""
        word = 'family'
        self.p2.add_content(self.sample_text)

        self.assertEqual(word in self.p2.words, True)

    def test_count_words(self):
        """."""
        self.p2.add_content(self.sample_text)

        self.assertEqual(self.p2.count_words, 111)

    def test_count_lines(self):
        """."""
        self.p2.add_content(self.sample_text)
        self.p2.add_content(self.sample_text)

        self.assertEqual(self.p2.count_lines, 2)

    def test_sentences(self):
        """."""
        sentence = 'This family was a victim of a problem they could have avoided-a problem that, according to Florida park rangers, hundreds of visitors suffer each year'

        self.p2.add_content(self.sample_text)

        self.assertEqual(sentence in self.p2.sentences, True)

    def test_count_sentences(self):
        """."""
        self.p2.add_content(self.sample_text)

        self.assertEqual(self.p2.count_sentences, 6)
