import re

def clean_html(raw_html):
    """Limpia etiquetas HTML básicas del texto."""
    if not raw_html:
        return ""
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext.strip()
