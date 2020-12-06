import optparse

from ingredient_phrase_tagger.training import labelled_data
from ingredient_phrase_tagger.training import translator


class Cli(object):

    def __init__(self, argv):
        self.opts = self._parse_args(argv)

    def run(self):
        """
        Generates training data in the CRF++ format for the ingredient
        tagging task
        """
        with open(
                self.opts.data_path, encoding='utf-8') as data_file, open(
                    self.opts.output_path, 'w',
                    encoding='utf-8') as output_file:
            data_reader = labelled_data.Reader(data_file)
            for row in data_reader:
                output_file.write(translator.translate_row(row))

    def _parse_args(self, argv):
        """
        Parse the command-line arguments into a dict.
        """

        opts = optparse.OptionParser()

        opts.add_option(
            "--data-path",
            default="nyt-ingredients-snapshot-2015.csv",
            help="(%default)")

        opts.add_option("--output-path", default="output_data.crf")

        (options, args) = opts.parse_args(argv)
        return options
