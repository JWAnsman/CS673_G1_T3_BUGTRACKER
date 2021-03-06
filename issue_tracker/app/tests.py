"""This is a basic unit test file example.
These tests are to be run when 'manage.py test' is called.
"""

from django import test
from issue_tracker.app import views


class SimpleViewTest(test.TestCase):

    def testSimple(self):
        """Verify 2+2 is 4 and the world is round."""
        self.assertEqual(2 + 2, 4)
        self.assertTrue('The world is round.')

    def testExampleView(self):
        example = views.ExampleView()
        self.assertEqual('example.html', example.template_name)
