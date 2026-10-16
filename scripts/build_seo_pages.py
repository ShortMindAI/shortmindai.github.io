"""Build keyword landing pages and resource articles for the static SEO site."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://shortmindai.github.io/"
CTA = "https://shortmind.ai/?source=shortmindai.github.io"
ASSET_PREFIX = "../../assets/"

PAGES = {
    "ai-clip-maker": {
        "en": ("AI Clip Maker for Podcasts, Streams and Long Videos | ShortMind", "ShortMind is an AI clip maker that finds strong moments, adds captions and reframes long videos into social-ready clips.", "AI clip maker for social-ready videos", "Turn long videos into ready-to-publish clips", "Upload a podcast, webinar, interview or stream. ShortMind finds the moments worth sharing, creates captions and prepares vertical clips for Shorts, TikTok and Reels.", ["Find hooks and highlights from long recordings", "Generate dynamic captions and social copy", "Reframe faces and speakers for 9:16 video"]),
        "zh": ("AI 视频切片工具：长视频自动生成短视频｜ShortMind", "ShortMind AI 视频切片工具可从播客、直播、访谈和课程中识别精彩片段，生成字幕并适配短视频平台。", "AI 视频切片工具", "把长视频剪成可以直接发布的短视频", "上传播客、访谈、课程或直播回放，ShortMind 自动识别值得传播的片段，生成字幕、竖屏画面和发布文案。", ["从长录制中提取高光和开场钩子", "自动生成动态字幕与社媒文案", "将人物和主体重构为 9:16 竖屏"]),
    },
    "long-video-to-shorts": {
        "en": ("Long Video to Shorts Converter | ShortMind", "Convert long videos to Shorts with AI. ShortMind finds highlights, adds captions and creates vertical clips for YouTube Shorts, TikTok and Reels.", "Long video to Shorts", "Turn one long video into a library of short videos", "Repurpose a full podcast, interview, course or livestream into focused clips. Review AI-selected moments, refine the hook and publish platform-ready Shorts.", ["Import a long-form recording", "Review scored moments and edit the opening", "Export captioned 9:16 clips for social platforms"]),
        "zh": ("长视频转短视频：AI 自动生成 Shorts｜ShortMind", "用 ShortMind 将长视频转换成短视频，自动识别精彩片段、生成字幕，并输出适合 YouTube Shorts、TikTok 和 Reels 的竖屏内容。", "长视频转短视频", "一条长视频，拆成一组可持续发布的短视频", "把完整播客、访谈、课程或直播回放拆成主题清晰的短片，查看 AI 推荐片段，调整开场后直接准备发布。", ["导入长视频素材", "查看评分并调整开场钩子", "导出带字幕的 9:16 短视频"]),
    },
    "ai-video-clipping": {
        "en": ("AI Video Clipping for Fast Content Repurposing | ShortMind", "AI video clipping for creators and teams. Detect highlights, create captions, reframe speakers and prepare social posts from long-form video.", "AI video clipping", "Find the best moments without watching the same recording again", "ShortMind combines highlight detection, captions, reframing and publishing copy so your team can turn long-form video into a repeatable content workflow.", ["Detect meaningful dialogue and emotional moments", "Compare clips with an estimated Viral Score", "Prepare captions, titles, descriptions and hashtags"]),
        "zh": ("AI 视频切片：自动识别高光并生成短视频｜ShortMind", "ShortMind AI 视频切片可从长视频中识别重点内容，自动生成字幕、重构画面，并准备适合社媒发布的文案。", "AI 视频切片", "不用反复观看长录制，也能找到值得传播的瞬间", "ShortMind 将高光识别、字幕、画面重构和发布文案连接成一套可重复使用的内容工作流。", ["识别重点对话和情绪高点", "使用 Viral Score 对候选片段排序", "生成字幕、标题、描述和标签"]),
    },
    "podcast-clips": {
        "en": ("Podcast Clips Maker: Turn Episodes into Short Videos | ShortMind", "Create podcast clips with AI. Find memorable quotes, add captions and keep hosts and guests in frame for Shorts, TikTok and Reels.", "Podcast clips maker", "Give every podcast episode more chances to be discovered", "ShortMind scans each episode for memorable quotes, strong opinions and useful takeaways, then turns them into captioned vertical clips for social discovery.", ["Find quotable moments in every episode", "Keep hosts and guests in frame with AI reframe", "Create several hook variations for testing"]),
        "zh": ("播客切片工具：把每期播客变成短视频｜ShortMind", "用 ShortMind 自动制作 podcast clips，提取金句和观点，生成字幕并保持主持人与嘉宾在画面中。", "播客切片工具", "让每一期播客拥有更多被发现的机会", "ShortMind 从每期节目中找到金句、鲜明观点和实用结论，生成适合 Shorts、TikTok 和 Reels 的竖屏短片。", ["提取每期播客中的高传播片段", "自动保持主持人与嘉宾在画面内", "生成多个开场钩子用于测试"]),
    },
    "youtube-to-shorts": {
        "en": ("YouTube to Shorts: Repurpose Long Videos with AI | ShortMind", "Turn YouTube videos into Shorts with AI. ShortMind finds key moments, adds captions and formats clips for vertical social video.", "YouTube to Shorts", "Repurpose your YouTube library into vertical clips", "Start with an existing long-form YouTube video, identify the most useful sections and create captioned Shorts without rebuilding the edit from scratch.", ["Reuse interviews, tutorials and video essays", "Turn chapters and key answers into clips", "Prepare titles and descriptions for Shorts"]),
        "zh": ("YouTube 转 Shorts：长视频批量生成竖屏短片｜ShortMind", "用 ShortMind 将 YouTube 长视频转换成 Shorts，自动提取重点、生成字幕并适配竖屏社媒格式。", "YouTube 转 Shorts", "把 YouTube 内容库重新变成竖屏短视频", "从已有的访谈、教程或视频文章开始，提取关键章节和回答，快速制作带字幕的 Shorts。", ["复用访谈、教程和深度视频", "把章节和关键回答转成短片", "准备 Shorts 标题与描述"]),
    },
    "stream-highlights": {
        "en": ("Stream Highlights Generator for Fast, Shareable Clips | ShortMind", "Create stream highlights with AI. Find reactions, plays and turning points in livestream recordings and publish vertical clips while the conversation is active.", "Stream highlights", "Turn a livestream replay into the moments fans remember", "ShortMind helps streamers and media teams recover the best moments from long replays: reactions, wins, fails, answers and turning points.", ["Locate high-energy moments in long streams", "Collect highlights in one review queue", "Reframe gameplay and reactions for vertical feeds"]),
        "zh": ("直播高光提取：自动生成 stream highlights｜ShortMind", "用 ShortMind 从直播回放中提取 stream highlights，识别精彩操作、反应和转折，并生成适合竖屏发布的短片。", "直播高光提取", "把一场直播回放变成粉丝愿意分享的高光片段", "ShortMind 帮助主播和内容团队从长回放中找出精彩操作、胜负转折、观众问答和高能反应。", ["定位长直播中的高能时刻", "在同一列表中整理高光片段", "将游戏画面和反应重构为竖屏"]),
    },
    "stream-clips": {
        "en": ("Stream Clips Maker for Streamers and Gaming Teams | ShortMind", "Make stream clips from long livestreams with AI. Extract gameplay, reactions and chat-worthy moments for TikTok, Shorts and Reels.", "Stream clips maker", "Create more stream clips from every broadcast", "Stop scrubbing through every replay. ShortMind surfaces gameplay, reactions and chat-worthy moments so you can publish consistently after each broadcast.", ["Find clips across a full broadcast", "Add readable captions for mobile viewers", "Export multiple aspect ratios for social channels"]),
        "zh": ("Stream Clips 制作工具：从直播回放批量提取短片｜ShortMind", "ShortMind 可从长直播回放中批量制作 stream clips，提取游戏操作、反应和弹幕讨论点，适配 Shorts、TikTok 和 Reels。", "Stream Clips 制作工具", "每场直播结束后，快速产出更多可发布短片", "无需反复拖动回放寻找片段，ShortMind 会整理游戏操作、反应和观众讨论点，帮助你稳定更新。", ["覆盖整场直播寻找精彩片段", "为移动端观众添加清晰字幕", "输出多种社媒画幅"]),
    },
}

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
