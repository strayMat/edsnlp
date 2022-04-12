modifier_pattern = r"(?P<modifier>[cpyraums])"
tumour_pattern = r"t\s?(?P<tumour>([0-4]|x|is))"
node_pattern = r"n\s?(?P<node>([0-3]|x))"
metastasis_pattern = r"m\s?(?P<metastasis>[01])"

tnm_pattern = f"({modifier_pattern}\\s?)?"
tnm_pattern += r"\s*" + tumour_pattern
tnm_pattern += r"\s*" + node_pattern
tnm_pattern += r"\s*" + metastasis_pattern
