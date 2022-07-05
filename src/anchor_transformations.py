import re


def turn_links_into_footnotes(text: str) -> str:
    result = []
    for paragraph in text.split("\n\n"):
        links = _find_inline_links(paragraph)
        paragraph = _transform_urls(paragraph, links)
        paragraph = _append_anchors(paragraph, links)
        result.append(paragraph)
    return "".join(result)


def _find_inline_links(paragraph: str) -> dict:
    inline_link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    links = dict(inline_link_pattern.findall(paragraph))
    return links


def _transform_urls(paragraph: str, links: dict) -> str:
    result = []
    for line in paragraph.split("\n"):
        for text_link, url in links.items():
            line = line.replace(f"({url})", "")
            number_of_anchor = list(links.keys()).index(text_link) + 1
            line = line.replace(
                f"[{text_link}]", f"{text_link} [^{text_link}{number_of_anchor}]")
            result.append(line)
    return "".join(result)


def _append_anchors(paragraph: str, links: dict) -> str:
    paragraph += "\n"
    for text_link, url in links.items():
        number_of_anchor = list(links.keys()).index(text_link) + 1
        paragraph += f"\n[^{text_link}{number_of_anchor}]: {url}"
    return paragraph
