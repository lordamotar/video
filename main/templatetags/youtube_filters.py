from django import template
import re

register = template.Library()

@register.filter
def youtube_embed(url):
    """
    Преобразует YouTube URL в встраиваемый формат.
    Пример: https://www.youtube.com/watch?v=dQw4w9WgXcQ -> https://www.youtube.com/embed/dQw4w9WgXcQ
    """
    pattern = r'(https?://)?(www\.)?(youtube|youtu\.be)/(watch\?v=)?(?P<id>[a-zA-Z0-9_-]+)'
    match = re.search(pattern, url)
    if match:
        video_id = match.group('id')
        return f'https://www.youtube.com/embed/{video_id}'
    return url  # Возвращаем оригинальную ссылку, если это не YouTube
