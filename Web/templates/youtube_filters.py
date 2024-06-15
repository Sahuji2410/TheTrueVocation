from django import template
import re

register = template.Library()

@register.filter
def youtube_embed_url(value):
    if value:
        match = re.search(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})', value)
        if match:
            return f"https://www.youtube.com/embed/{match.group(6)}"
    return None
