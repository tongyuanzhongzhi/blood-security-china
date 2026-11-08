#!/usr/bin/env python3
"""Manuscript_VoxSanguinis.md -> Manuscript_VoxSanguinis.docx (Vox Sanguinis free-format)."""
import re
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

SRC = "Manuscript_VoxSanguinis.md"
OUT = "Manuscript_VoxSanguinis.docx"

doc = Document()
style = doc.styles['Normal']
style.font.name = 'Times New Roman'
style.font.size = Pt(11)
style.paragraph_format.space_after = Pt(6)

def add_para(text, bold=False, size=11, align=None, italic=False, space_after=6):
    p = doc.add_paragraph()
    if align is not None:
        p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    # inline formatting: **bold**, *italic* (bold parsed first, then italic)
    parts = re.split(r'(\*\*.*?\*\*|\*[^*\n]+\*)', text)
    for part in parts:
        if not part:
            continue
        if part.startswith('**') and part.endswith('**'):
            r = p.add_run(part[2:-2])
            r.bold = True
        elif part.startswith('*') and part.endswith('*') and len(part) > 2:
            r = p.add_run(part[1:-1])
            r.italic = True
        else:
            r = p.add_run(part)
        r.font.size = Pt(size)
        r.italic = italic or r.italic
    if bold and not text.startswith('**'):
        for r in p.runs:
            r.bold = True
    return p

def add_heading(text, level=1):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(text)
    r.bold = True
    r.font.size = Pt(13 if level == 1 else 12)
    return p

def add_table_block(lines):
    # lines: list of markdown table rows starting with |
    rows = []
    for ln in lines:
        ln = ln.strip()
        if not ln.startswith('|'):
            continue
        cells = [c.strip() for c in ln.strip('|').split('|')]
        rows.append(cells)
    if not rows:
        return
    # drop separator row (---)
    rows = [r for r in rows if not all(re.fullmatch(r':?-{2,}:?', c or '-') for c in r)]
    if not rows:
        return
    ncol = max(len(r) for r in rows)
    tbl = doc.add_table(rows=len(rows), cols=ncol)
    tbl.style = 'Table Grid'
    for i, row in enumerate(rows):
        for j in range(ncol):
            cell = tbl.cell(i, j)
            cell.text = row[j] if j < len(row) else ''
            for p in cell.paragraphs:
                for r in p.runs:
                    r.font.size = Pt(9)
                    if i == 0:
                        r.bold = True

lines = open(SRC).read().split('\n')

i = 0
in_table = False
table_lines = []
while i < len(lines):
    line = lines[i].rstrip()
    stripped = line.strip()

    # main title (first # line)
    if stripped.startswith('# ') and not stripped.startswith('## '):
        add_para(stripped[2:], bold=True, size=15, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)
        i += 1
        continue

    # ## heading
    if stripped.startswith('## '):
        add_heading(stripped[3:], level=1)
        i += 1
        continue

    # ### heading
    if stripped.startswith('### '):
        add_heading(stripped[4:], level=2)
        i += 1
        continue

    # horizontal rule
    if stripped == '---':
        i += 1
        continue

    # table block (consecutive lines starting with |)
    if stripped.startswith('|'):
        table_lines = [line]
        j = i + 1
        while j < len(lines) and lines[j].strip().startswith('|'):
            table_lines.append(lines[j].rstrip())
            j += 1
        add_table_block(table_lines)
        i = j
        continue

    # Highlights bullet
    if stripped.startswith('- '):
        p = add_para(stripped[2:], size=11, space_after=2)
        p.style = doc.styles['List Bullet']
        i += 1
        continue

    # blank line
    if stripped == '':
        i += 1
        continue

    # normal paragraph
    add_para(stripped, size=11)
    i += 1

doc.save(OUT)
print(f"Saved {OUT}")

# Verify
d2 = Document(OUT)
print(f"段落数: {len(d2.paragraphs)}, 表格数: {len(d2.tables)}")
