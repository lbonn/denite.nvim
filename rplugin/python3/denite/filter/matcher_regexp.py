# ============================================================================
# FILE: matcher_regexp.py
# AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
# License: MIT license
# ============================================================================

import re
from .base import Base
from denite.util import split_input, convert2regex_pattern


class Filter(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'matcher_regexp'
        self.description = 'regexp matcher'

    def filter(self, context):
        if context['input'] == '':
            return context['candidates']
        candidates = context['candidates']
        for pattern in split_input(context['input']):
            try:
                p = re.compile(pattern, flags=re.IGNORECASE
                               if context['ignorecase'] else 0)
            except Exception:
                return []
            candidates = [x for x in candidates if p.search(x['word'])]
        return candidates

    def convert_pattern(self, input_str):
        return convert2regex_pattern(input_str)
