import functools


class Common(object):
    @staticmethod
    def _join_lines_if_not_contain(lines, content, splitter):
        lines_filter_by_content = filter(lambda l: content not in l, lines)
        return functools.reduce(lambda x, y: x + splitter + y, lines_filter_by_content)
