from spacy.tokens import Doc

import edsnlp.accents

if not Doc.has_extension("note_id"):
    Doc.set_extension("note_id", default=None)

if not Doc.has_extension("note_datetime"):
    Doc.set_extension("note_datetime", default=None)
