from GenericDocument import GenericDocument
from PartType import Part


class HTMLDocument(GenericDocument):

    @classmethod
    def escape_html(cls, text):
        return (
            text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#39;")
        )

    def render_heading1(self, text):
        text = f"<h1>{self.escape_html(text)}</h1>"
        return text.replace("\n", "</br>")

    def render_heading2(self, text):
        text = f"<h2>{self.escape_html(text)}</h2>"
        return text.replace("\n", "</br>")

    def render_heading3(self, text):
        text = f"<h3>{self.escape_html(text)}</h3>"
        return text.replace("\n", "</br>")

    def render_paragraph(self, text):
        text = f"<p>{self.escape_html(text)}</p>"
        return text.replace("\n", "</br>")

    def render_codeblock(self, text):
        return f"<code>{self.escape_html(text)}</code>"


html = HTMLDocument()

html.add_heading3("Heading 3.1")
html.add_heading3("Heading 3.2")
html.add_heading2("Heading 2")
html.add_heading1("Heading 1")
html.add_heading3("Heading 3.3")
html.add_codeblock("Put that cookie down!")
html.add_heading3("Heading 3.4")
html.add_heading3("Heading 3.5")
html.add_paragraph("Paragraph")

html.merge_consecutive(Part.HEADING3)

html.render()
print(html)
