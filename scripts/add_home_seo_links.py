from pathlib import Path

for name, resource, label, heading, copy, cards in [
    ("index.html", "resources/", "Resources", "Start with the video task you need to solve.", "Explore practical workflows for turning specific long-form sources into social-ready short videos.", [("ai-clip-maker/", "AI clip maker", "Find highlights, add captions and reframe podcasts, interviews and webinars."), ("long-video-to-shorts/", "Long video to Shorts", "Turn one full recording into a library of focused vertical clips."), ("podcast-clips/", "Podcast clips", "Extract quotable moments and keep hosts and guests in frame."), ("stream-highlights/", "Stream highlights", "Recover gameplay, reactions and turning points from long replays.")]),
    ("zh.html", "zh/resources/", "教程与案例", "从你要解决的视频任务开始。", "查看针对不同长视频素材的短视频制作流程。", [("zh/ai-clip-maker/", "AI 视频切片", "从播客、访谈和 Webinar 中提取高光并生成字幕。"), ("zh/long-video-to-shorts/", "长视频转短视频", "把一条完整录制拆成一组竖屏短片。"), ("zh/podcast-clips/", "播客切片", "提取金句并保持主持人与嘉宾在画面中。"), ("zh/stream-highlights/", "直播高光", "从长直播回放中整理操作、反应和转折时刻。")]),
]:
    path = Path(name)
    text = path.read_text(encoding="utf-8")
    nav_marker = '<nav class="nav-links"'
    start = text.index(nav_marker)
    insert_at = text.index(">", start) + 1
    text = text[:insert_at] + f'<a href="{resource}">{label}</a>' + text[insert_at:]
    cards_html = "".join(f'<article class="card"><h3><a href="{url}">{title}</a></h3><p>{body}</p></article>' for url, title, body in cards)
    section = f'<section class="section"><div class="container"><div class="section-heading"><div class="eyebrow">{label}</div><h2>{heading}</h2><p>{copy}</p></div><div class="cards">{cards_html}</div></div></section>'
    text = text.replace('<section class="section" id="faq">', section + '<section class="section" id="faq">', 1)
    path.write_text(text, encoding="utf-8")
