import re

LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def turn_links_into_footnotes(text: str) -> str:
    result = []
    for paragraph in text.split("\n\n"):
        links = _find_inline_links(paragraph)
        paragraph = _transform_urls(paragraph, links)
        paragraph = _append_anchors(paragraph, links)
        result.append(paragraph)
    return "".join(result)


def _find_inline_links(paragraph: str) -> dict:
    links = dict(LINK_PATTERN.findall(paragraph))
    return links


def _transform_urls(paragraph: str, links: dict) -> str:
    result = []
    for line in paragraph.split("\n"):
        if (re.search(LINK_PATTERN, line)):
            result.append(_transform_link(links, line))
        else:
            result.append(line)
    return "\n".join(result)


def _transform_link(links: dict, line: str) -> str:
    for text_link, url in links.items():
        line = line.replace(f"({url})", "")
        number_of_anchor = list(links.keys()).index(text_link) + 1
        line = line.replace(
            f"[{text_link}]", f"{text_link} [^{text_link}{number_of_anchor}]")
        return line


def _append_anchors(paragraph: str, links: dict) -> str:
    paragraph += "\n"
    for text_link, url in links.items():
        number_of_anchor = list(links.keys()).index(text_link) + 1
        paragraph += f"\n[^{text_link}{number_of_anchor}]: {url}"
    return paragraph
