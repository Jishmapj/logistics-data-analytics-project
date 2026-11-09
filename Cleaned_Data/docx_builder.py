import zipfile
import html

def escape(text):
    return html.escape(str(text), quote=False).replace("&apos;", "'")

class DocxBuilder:
    def __init__(self):
        self.body_elements = []

    def add_title(self, title, subtitle=None, author="Logistics Analytics Team", date="November 2026"):
        p = f"""<w:p>
            <w:pPr><w:jc w:val="center"/><w:spacing w:before="360" w:after="120"/></w:pPr>
            <w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:b/><w:sz w:val="48"/><w:color w:val="1B365D"/></w:rPr><w:t>{escape(title)}</w:t></w:r>
        </w:p>"""
        self.body_elements.append(p)
        if subtitle:
            p_sub = f"""<w:p>
                <w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="240"/></w:pPr>
                <w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="24"/><w:color w:val="4B6B94"/></w:rPr><w:t>{escape(subtitle)}</w:t></w:r>
            </w:p>"""
            self.body_elements.append(p_sub)
        meta = f"""<w:p>
            <w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="480"/></w:pPr>
            <w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:i/><w:sz w:val="20"/><w:color w:val="666666"/></w:rPr><w:t>{escape(author)} | {escape(date)}</w:t></w:r>
        </w:p>"""
        self.body_elements.append(meta)

    def add_heading_1(self, text):
        p = f"""<w:p>
            <w:pPr>
                <w:spacing w:before="360" w:after="120"/>
                <w:pBdr><w:bottom w:val="single" w:sz="12" w:space="4" w:color="1B365D"/></w:pBdr>
            </w:pPr>
            <w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:b/><w:sz w:val="32"/><w:color w:val="1B365D"/></w:rPr><w:t>{escape(text)}</w:t></w:r>
        </w:p>"""
        self.body_elements.append(p)

    def add_heading_2(self, text):
        p = f"""<w:p>
            <w:pPr><w:spacing w:before="240" w:after="80"/></w:pPr>
            <w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:b/><w:sz w:val="26"/><w:color w:val="3B5998"/></w:rPr><w:t>{escape(text)}</w:t></w:r>
        </w:p>"""
        self.body_elements.append(p)

    def add_heading_3(self, text):
        p = f"""<w:p>
            <w:pPr><w:spacing w:before="160" w:after="60"/></w:pPr>
            <w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:b/><w:sz w:val="22"/><w:color w:val="2B2D42"/></w:rPr><w:t>{escape(text)}</w:t></w:r>
        </w:p>"""
        self.body_elements.append(p)

    def add_paragraph(self, text, bold_prefix=None, italic=False):
        runs = []
        if bold_prefix:
            runs.append(f"""<w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:b/><w:sz w:val="21"/><w:color w:val="222222"/></w:rPr><w:t xml:space="preserve">{escape(bold_prefix)} </w:t></w:r>""")
        i_tag = "<w:i/>" if italic else ""
        runs.append(f"""<w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>{i_tag}<w:sz w:val="21"/><w:color w:val="333333"/></w:rPr><w:t xml:space="preserve">{escape(text)}</w:t></w:r>""")
        
        p = f"""<w:p>
            <w:pPr><w:spacing w:before="0" w:after="120" w:line="276" w:lineRule="auto"/></w:pPr>
            {''.join(runs)}
        </w:p>"""
        self.body_elements.append(p)

    def add_bullet(self, text, bold_prefix=None):
        runs = []
        if bold_prefix:
            runs.append(f"""<w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:b/><w:sz w:val="21"/><w:color w:val="222222"/></w:rPr><w:t xml:space="preserve">{escape(bold_prefix)} </w:t></w:r>""")
        runs.append(f"""<w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="21"/><w:color w:val="333333"/></w:rPr><w:t xml:space="preserve">{escape(text)}</w:t></w:r>""")
        
        p = f"""<w:p>
            <w:pPr>
                <w:ind w:left="480" w:hanging="240"/>
                <w:spacing w:before="40" w:after="60" w:line="260" w:lineRule="auto"/>
            </w:pPr>
            <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="21"/><w:color w:val="1B365D"/></w:rPr><w:t xml:space="preserve">&#8226;  </w:t></w:r>
            {''.join(runs)}
        </w:p>"""
        self.body_elements.append(p)

    def add_callout(self, title, text):
        p = f"""<w:p>
            <w:pPr>
                <w:pBdr><w:left w:val="single" w:sz="24" w:space="12" w:color="1B365D"/></w:pBdr>
                <w:shd w:val="clear" w:color="auto" w:fill="F0F4F8"/>
                <w:ind w:left="240" w:right="240"/>
                <w:spacing w:before="120" w:after="120"/>
            </w:pPr>
            <w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:b/><w:sz w:val="21"/><w:color w:val="1B365D"/></w:rPr><w:t xml:space="preserve">{escape(title)}: </w:t></w:r>
            <w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="20"/><w:color w:val="333333"/></w:rPr><w:t xml:space="preserve">{escape(text)}</w:t></w:r>
        </w:p>"""
        self.body_elements.append(p)

    def add_code_block(self, code_text):
        lines = code_text.strip().split("\n")
        runs = []
        for i, line in enumerate(lines):
            runs.append(f"""<w:r><w:rPr><w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/><w:sz w:val="18"/><w:color w:val="222222"/></w:rPr><w:t xml:space="preserve">{escape(line)}</w:t></w:r>""")
            if i < len(lines) - 1:
                runs.append("<w:r><w:br/></w:r>")
        p = f"""<w:p>
            <w:pPr>
                <w:pBdr>
                    <w:top w:val="single" w:sz="6" w:space="6" w:color="D1D5DB"/>
                    <w:left w:val="single" w:sz="18" w:space="6" w:color="4B6B94"/>
                    <w:bottom w:val="single" w:sz="6" w:space="6" w:color="D1D5DB"/>
                    <w:right w:val="single" w:sz="6" w:space="6" w:color="D1D5DB"/>
                </w:pBdr>
                <w:shd w:val="clear" w:color="auto" w:fill="F8F9FA"/>
                <w:ind w:left="180" w:right="180"/>
                <w:spacing w:before="100" w:after="140" w:line="220" w:lineRule="auto"/>
            </w:pPr>
            {''.join(runs)}
        </w:p>"""
        self.body_elements.append(p)

    def add_table(self, headers, rows, col_widths=None):
        num_cols = len(headers)
        if not col_widths:
            default_w = 9360 // num_cols
            col_widths = [default_w] * num_cols

        grid_cols = "".join([f'<w:gridCol w:w="{w}"/>' for w in col_widths])

        # Header Row
        hdr_cells = []
        for i, h in enumerate(headers):
            cell = f"""<w:tc>
                <w:tcPr>
                    <w:tcW w:w="{col_widths[i]}" w:type="dxa"/>
                    <w:shd w:val="clear" w:color="auto" w:fill="1B365D"/>
                    <w:tcMar><w:top w:w="120"/><w:left w:w="140"/><w:bottom w:w="120"/><w:right w:w="140"/></w:tcMar>
                </w:tcPr>
                <w:p>
                    <w:pPr><w:spacing w:before="0" w:after="0"/></w:pPr>
                    <w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:b/><w:sz w:val="19"/><w:color w:val="FFFFFF"/></w:rPr><w:t>{escape(h)}</w:t></w:r>
                </w:p>
            </w:tc>"""
            hdr_cells.append(cell)
        
        tr_header = f"""<w:tr>
            <w:trPr><w:tblHeader/></w:trPr>
            {''.join(hdr_cells)}
        </w:tr>"""

        body_rows = []
        for r_idx, row in enumerate(rows):
            bg_color = "F8FAFC" if (r_idx % 2 == 1) else "FFFFFF"
            r_cells = []
            for c_idx, val in enumerate(row):
                w = col_widths[c_idx] if c_idx < len(col_widths) else col_widths[-1]
                cell = f"""<w:tc>
                    <w:tcPr>
                        <w:tcW w:w="{w}" w:type="dxa"/>
                        <w:shd w:val="clear" w:color="auto" w:fill="{bg_color}"/>
                        <w:tcMar><w:top w:w="80"/><w:left w:w="140"/><w:bottom w:w="80"/><w:right w:w="140"/></w:tcMar>
                    </w:tcPr>
                    <w:p>
                        <w:pPr><w:spacing w:before="0" w:after="0"/></w:pPr>
                        <w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="18"/><w:color w:val="333333"/></w:rPr><w:t>{escape(str(val))}</w:t></w:r>
                    </w:p>
                </w:tc>"""
                r_cells.append(cell)
            tr = f"""<w:tr>{''.join(r_cells)}</w:tr>"""
            body_rows.append(tr)

        tbl = f"""<w:tbl>
            <w:tblPr>
                <w:tblW w:w="9360" w:type="dxa"/>
                <w:jc w:val="center"/>
                <w:tblBorders>
                    <w:top w:val="single" w:sz="6" w:space="0" w:color="D1D5DB"/>
                    <w:left w:val="single" w:sz="6" w:space="0" w:color="D1D5DB"/>
                    <w:bottom w:val="single" w:sz="6" w:space="0" w:color="D1D5DB"/>
                    <w:right w:val="single" w:sz="6" w:space="0" w:color="D1D5DB"/>
                    <w:insideH w:val="single" w:sz="4" w:space="0" w:color="E5E7EB"/>
                    <w:insideV w:val="single" w:sz="4" w:space="0" w:color="E5E7EB"/>
                </w:tblBorders>
            </w:tblPr>
            <w:tblGrid>{grid_cols}</w:tblGrid>
            {tr_header}
            {''.join(body_rows)}
        </w:tbl>
        <w:p><w:pPr><w:spacing w:before="0" w:after="120"/></w:pPr></w:p>"""
        self.body_elements.append(tbl)

    def save(self, filepath):
        content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>"""

        rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""

        document_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>"""

        styles = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults>
    <w:rPrDefault>
      <w:rPr>
        <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
        <w:sz w:val="22"/>
        <w:color w:val="333333"/>
      </w:rPr>
    </w:rPrDefault>
  </w:docDefaults>
</w:styles>"""

        doc_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    {''.join(self.body_elements)}
    <w:sectPr>
      <w:pgSz w:w="12240" w:h="15840"/>
      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/>
    </w:sectPr>
  </w:body>
</w:document>"""

        with zipfile.ZipFile(filepath, "w", zipfile.ZIP_DEFLATED) as z:
            z.writestr("[Content_Types].xml", content_types)
            z.writestr("_rels/.rels", rels)
            z.writestr("word/_rels/document.xml.rels", document_rels)
            z.writestr("word/styles.xml", styles)
            z.writestr("word/document.xml", doc_xml)
        print(f"Saved DOCX document to {filepath}")

if __name__ == "__main__":
    doc = DocxBuilder()
    doc.add_title("TEST DOCUMENT", "Subtitle Here")
    doc.add_heading_1("1. Introduction")
    doc.add_paragraph("This is a paragraph with some bold prefix.", bold_prefix="Note:")
    doc.add_bullet("Item 1", bold_prefix="Bullet:")
    doc.add_callout("Strategic Insight", "Carrier allocation can yield 15% savings.")
    doc.add_code_block("import pandas as pd\ndf = pd.read_csv('test.csv')\nprint(df.head())")
    doc.add_table(["Header A", "Header B", "Header C"], [["A1", "B1", "C1"], ["A2", "B2", "C2"]])
    doc.save("test_out.docx")
