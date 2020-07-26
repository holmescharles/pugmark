import pandas as pd
import tabulate


class MarkdownFile:

    def __init__(self, filename):
        self._file = open(filename, 'w')

    def close(self):
        self._file.close()

    def _write(self, text):
        self._file.write(text)

    def para(self, text):
        if self._file.tell() > 0:
            self._write('\n')
        self._write(text + '\n')

    def head(self, level, text):
        self.para('{} {}'.format('#' * level, text))

    def code_block(self, text, language=''):
        self.para('```{}\n{}\n```'.format(language, text))

    def table(self, data, index=True, columns=True):
        table = tabulate.tabulate(
            data, showindex=index, headers=('keys' if columns else '')
            )
        self.para(table)
