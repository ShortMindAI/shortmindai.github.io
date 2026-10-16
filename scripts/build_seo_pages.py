"""Build keyword landing pages and resource articles for the static SEO site."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://shortmindai.github.io/"
CTA = "https://shortmind.ai/?source=shortmindai.github.io"
ASSET_PREFIX = "../../assets/"

PAGES = {}

ARTICLES = {
    "how-to-turn-long-video-into-shorts": ("How to Turn a Long Video into Shorts", "A practical workflow for turning podcasts, interviews, webinars and livestreams into focused vertical clips.", ["Choose a source with clear chapters or recurring topics.", "Use AI highlight detection to shortlist moments with a complete idea.", "Rewrite the first seconds as a direct hook, then add readable captions.", "Reframe the speaker or subject for 9:16 and export versions for each platform."]),
    "how-to-create-podcast-clips": ("How to Create Podcast Clips That Earn Attention", "Use every episode as a source of quotable, useful and conversation-starting short videos.", ["Mark strong opinions, surprising answers and practical takeaways.", "Keep enough context for the clip to make sense without the full episode.", "Use captions and a clear speaker layout so the clip works without sound.", "Link each clip back to the full episode and test several opening hooks."]),
    "youtube-to-shorts-workflow": ("YouTube to Shorts: A Practical Repurposing Workflow", "Turn an existing YouTube library into a repeatable source of vertical content.", ["Start from tutorials, interviews and videos with a clear takeaway.", "Use chapters, transcript ideas and AI suggestions to find clip candidates.", "Create a concise title and description that match the clip's actual promise.", "Publish consistently and compare retention across different hooks."]),
    "stream-highlights-and-clips": ("How to Create Stream Highlights and Stream Clips", "Recover the best gameplay, reactions and turning points from long livestream replays.", ["Process the replay while the stream is still topical.", "Collect wins, fails, reactions and audience questions in one review list.", "Use vertical framing and captions for viewers watching on mobile.", "Publish several clips with different moments instead of one long recap."]),
    "ai-video-clipping-for-marketing": ("AI Video Clipping for Marketing Teams", "Build a campaign library from webinars, launches, customer interviews and events.", ["Define the campaign messages before reviewing the recording.", "Group clips by product benefit, proof point, objection and call to action.", "Generate consistent captions and publishing copy for each channel.", "Keep the original recording linked for sales and customer education reuse."]),
    "long-form-video-repurposing": ("Long-Form Video Repurposing for Courses and Webinars", "Turn detailed teaching and webinar recordings into useful discovery content.", ["Split the recording into one concept per clip.", "Show the practical answer early, then retain the supporting explanation.", "Add captions and mobile-friendly framing for silent viewing.", "Use clips as previews that lead viewers to the complete lesson or webinar."]),
}

def link(path: str, label: str) -> str:
    return f'<a href="{path}">{escape(label)}</a>'

def page_shell(title, description, lang, canonical, body, breadcrumb="Resources"):
    locale = "en" if lang == "en" else "zh-CN"
    nested = lang == "zh"
    asset_prefix = "../../assets/" if nested else "../assets/"
    home = "../../zh.html" if nested else "../index.html"
    if nested:
        slug = canonical[len(BASE + "zh/"):].strip("/")
        en_href = BASE + slug + "/"
        zh_href = canonical
    else:
        slug = canonical[len(BASE):].strip("/")
        en_href = canonical
        zh_href = BASE + "zh/" + slug + "/"
    return f'''<!doctype html><html lang="{locale}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{escape(title)}</title><meta name="description" content="{escape(description)}"><link rel="canonical" href="{canonical}"><link rel="alternate" hreflang="en" href="{en_href}"><link rel="alternate" hreflang="zh-CN" href="{zh_href}"><link rel="alternate" hreflang="x-default" href="{BASE}"><link rel="stylesheet" href="{asset_prefix}site.css"><meta property="og:title" content="{escape(title)}"><meta property="og:description" content="{escape(description)}"><meta property="og:type" content="website"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{BASE}assets/social-card.jpg"></head><body class="seo-page"><header class="header"><div class="container nav"><a class="brand" href="{home}"><img src="{asset_prefix}brand-mark.webp" width="32" height="32" alt=""><span>ShortMind</span></a><nav class="nav-links"><a href="{home}">{'Home' if lang == 'en' else '首页'}</a><a href="{CTA}">{'Try ShortMind' if lang == 'en' else '体验 ShortMind'}</a></nav></div></header><main class="container seo-main"><p class="breadcrumb">{link(home, 'ShortMind')} / {escape(breadcrumb)}</p>{body}</main><footer class="footer"><div class="container"><a href="{CTA}">{'Try ShortMind AI' if lang == 'en' else '体验 ShortMind AI'}</a></div></footer></body></html>'''

def build_keyword(slug):
    for lang, data in [("en", PAGES[slug]["en"]), ("zh", PAGES[slug]["zh"])]:
        title, description, eyebrow, heading, intro, bullets = data
        cta = "Create your first clip" if lang == "en" else "开始制作第一条短视频"
        related = [s for s in PAGES if s != slug][:3]
        related_html = " ".join(link(("../" if lang == "en" else "../") + s + "/", PAGES[s][lang][2]) for s in related)
        body = f'''<section class="seo-hero"><p class="eyebrow">{escape(eyebrow)}</p><h1>{escape(heading)}</h1><p class="seo-lead">{escape(intro)}</p><p><a class="button primary" href="{CTA}">{cta} →</a></p></section><section class="seo-content"><h2>{'What you can do with ShortMind' if lang == 'en' else 'ShortMind 可以帮你完成什么'}</h2><ul class="intent-list">{"".join(f'<li>{escape(b)}</li>' for b in bullets)}</ul><h2>{'A practical workflow' if lang == 'en' else '具体使用流程'}</h2><ol class="steps-list"><li>{'Upload your long-form video.' if lang == 'en' else '上传长视频素材。'}</li><li>{'Review AI-selected highlights and improve the opening hook.' if lang == 'en' else '查看 AI 推荐的高光片段并调整开场。'}</li><li>{'Export captioned clips and prepare your social post.' if lang == 'en' else '导出带字幕的短视频并准备社媒文案。'}</li></ol><h2>{'Explore related workflows' if lang == 'en' else '继续了解相关场景'}</h2><p class="related-links">{related_html}</p></section><section class="cta"><h2>{'Ready to repurpose your next video?' if lang == 'en' else '准备好处理下一条长视频了吗？'}</h2><p><a class="button primary" href="{CTA}">{cta} →</a></p></section>'''
        folder = ROOT / slug if lang == "en" else ROOT / "zh" / slug
        folder.mkdir(parents=True, exist_ok=True)
        canonical = BASE + (slug if lang == "en" else "zh/" + slug) + "/"
        (folder / "index.html").write_text(page_shell(title, description, lang, canonical, body, eyebrow), encoding="utf-8")

def build_resources():
    for lang in ["en", "zh"]:
        cards = []
        for slug, (en_title, en_desc, steps) in ARTICLES.items():
            title = en_title if lang == "en" else en_title.replace("How to", "如何").replace("A Practical", "实用的").replace("Workflow", "工作流").replace("for", "：")
            desc = en_desc if lang == "en" else "围绕长视频转短视频、播客切片、YouTube Shorts 和直播高光的实用方法。"
            path = ("../" if lang == "en" else "../") + slug + "/"
            cards.append(f'<article class="resource-card"><h2>{link(path, title)}</h2><p>{escape(desc)}</p></article>')
        heading = "Short-form video resources" if lang == "en" else "短视频教程与案例"
        intro = "Practical guides for turning long-form recordings into clips people can discover and share." if lang == "en" else "围绕长视频转短视频、播客切片、YouTube Shorts 和直播高光的实用教程。"
        body = f'<section class="seo-hero"><p class="eyebrow">ShortMind Resources</p><h1>{heading}</h1><p class="seo-lead">{intro}</p></section><section class="resource-grid">{"".join(cards)}</section>'
        folder = ROOT / ("resources" if lang == "en" else "zh/resources")
        folder.mkdir(parents=True, exist_ok=True)
        canonical = BASE + ("resources/" if lang == "en" else "zh/resources/")
        (folder / "index.html").write_text(page_shell(heading, intro, lang, canonical, body, heading), encoding="utf-8")

def build_articles():
    for slug, (title, description, steps) in ARTICLES.items():
        for lang in ["en", "zh"]:
            localized_title = title if lang == "en" else title.replace("How to", "如何").replace("A Practical", "实用的").replace("Workflow", "工作流").replace("for", "：")
            localized_desc = description if lang == "en" else "帮助创作者把长视频拆解成可发布的短视频，并覆盖具体的制作步骤。"
            step_items = steps if lang == "en" else ["选择主题清晰、包含完整观点的长视频素材。", "使用 AI 找到高光片段并保留必要上下文。", "加入字幕、调整开场和竖屏构图。", "导出短视频并持续测试不同标题与开场。"]
            body = f'<article class="article"><p class="eyebrow">ShortMind Guide</p><h1>{escape(localized_title)}</h1><p class="seo-lead">{escape(localized_desc)}</p><h2>{"Step-by-step workflow" if lang == "en" else "分步工作流"}</h2><ol class="steps-list">{"".join(f"<li>{escape(s)}</li>" for s in step_items)}</ol><h2>{"Use ShortMind to speed up the repetitive work" if lang == "en" else "用 ShortMind 加快重复工作"}</h2><p>{"ShortMind combines highlight detection, captions, AI reframing and publishing copy in one workflow." if lang == "en" else "ShortMind 将高光识别、字幕、智能重构画面和发布文案连接在同一套工作流中。"}</p><p><a class="button primary" href="{CTA}">{"Try ShortMind AI" if lang == "en" else "体验 ShortMind AI"} →</a></p></article>'
            folder = ROOT / slug if lang == "en" else ROOT / "zh" / slug
            folder.mkdir(parents=True, exist_ok=True)
            canonical = BASE + (slug if lang == "en" else "zh/" + slug) + "/"
            (folder / "index.html").write_text(page_shell(localized_title, localized_desc, lang, canonical, body, "Guide"), encoding="utf-8")

def main():
    for slug in PAGES:
        build_keyword(slug)
    build_resources()
    build_articles()
    print("Built SEO landing pages, resources and guides.")

if __name__ == "__main__":
    main()
