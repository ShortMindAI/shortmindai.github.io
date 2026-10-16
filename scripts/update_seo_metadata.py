from pathlib import Path
import re

BASE = "https://shortmindai.github.io/"
for file, title, desc in [
    ("index.html", "ShortMind AI | Long Video to Shorts & AI Video Clipping", "Turn podcasts, interviews, webinars and livestreams into captioned short videos with ShortMind AI."),
    ("zh.html", "ShortMind AI｜长视频转短视频与 AI 视频切片", "ShortMind AI 将播客、访谈、课程和直播回放转换成带字幕的短视频，适配 YouTube Shorts、TikTok 和 Reels。"),
]:
    path = Path(file)
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", text, count=1, flags=re.S)
    text = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{desc}">', text, count=1)
    for attr, value in [("og:title", title), ("og:description", desc), ("twitter:title", title), ("twitter:description", desc)]:
        text = re.sub(rf'(<meta (?:property|name)="{re.escape(attr)}" content=").*?(">)', rf"\g<1>{value}\g<2>", text, count=1)
    path.write_text(text, encoding="utf-8")

slugs = ["ai-clip-maker", "long-video-to-shorts", "ai-video-clipping", "podcast-clips", "youtube-to-shorts", "stream-highlights", "stream-clips", "resources", "how-to-turn-long-video-into-shorts", "how-to-create-podcast-clips", "youtube-to-shorts-workflow", "stream-highlights-and-clips", "ai-video-clipping-for-marketing", "long-form-video-repurposing"]
urls = [""] + [f"{slug}/" for slug in slugs] + [f"zh/{slug}/" for slug in slugs]
xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
xml.extend(f"  <url><loc>{BASE}{url}</loc></url>" for url in urls)
xml.append("</urlset>")
Path("sitemap.xml").write_text("\n".join(xml) + "\n", encoding="utf-8")
