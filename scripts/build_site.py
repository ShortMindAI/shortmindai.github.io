"""Build the dependency-free bilingual GitHub Pages site and optimize supplied assets.

Run with Python + Pillow. Source material stays outside this repository.
"""
from pathlib import Path
from html import escape
import json
import argparse
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
MATERIALS = ROOT / "brand-materials"
BASE = "https://shortmindai.github.io/"
WEBSITE = "https://shortmind.ai"
WEBSITE_LINK = WEBSITE + "/?source=shortmindai.github.io"
REPO = "https://github.com/ShortMindAI/shortmindai.github.io"
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

CONTENT = {
    "en": {
        "title": "ShortMind AI — Long Video to Shorts & AI Video Clipping",
        "description": "Convert long video to shorts with ShortMind AI. Find highlights, add captions, reframe clips, and publish to TikTok, Reels and YouTube Shorts.",
        "skip": "Skip to content", "features": "Features", "workflow": "How it works", "faq": "FAQ", "visit": "Visit website", "github": "View GitHub repository",
        "eyebrow": "AI VIDEO CLIPPING · LONG VIDEO TO SHORTS · PODCAST CLIPS · STREAM HIGHLIGHTS · STREAM CLIPS",
        "heading": "One long video. In minutes.", "accent": "100+ viral-potential shorts.",
        "lead": "ShortMind AI automatically identifies high-potential moments, moves the hook to the opening, generates scroll-stopping titles and captions, produces viral-potential short videos in batches, and publishes them to TikTok, YouTube and other social platforms.",
        "note": "Explore the product on shortmind.ai · Find this website on GitHub",
        "hero_alt": "ShortMind workflow preview: a long video becomes scored vertical clips for social publishing",
        "feature_eyebrow": "LESS REPETITION. MORE CREATION.", "feature_heading": "From hidden highlights to your next short.",
        "feature_copy": "An AI content growth engine for creators and teams with a library of long-form videos.",
        "cards": [
            ("AI highlight detection", "Find compelling moments through dialogue, key ideas and emotional cues, without watching the same video again and again."),
            ("Viral Score & stronger hooks", "Compare clips with a 0–100 Viral Score and bring engaging moments to the opening. Use the score to guide your editorial decisions."),
            ("Dynamic, multilingual captions", "Generate subtitles and choose caption styles to make your clips easier to follow across languages."),
            ("AI reframing", "Keep faces and subjects in focus as you adapt videos to 9:16, 1:1 and 4:5 formats for social feeds."),
            ("B-roll & publishing copy", "Enrich your story with relevant B-roll and generate titles, descriptions and hashtags for each clip."),
            ("Social publishing", "Bring editing and distribution together for TikTok, YouTube Shorts, Instagram Reels, LinkedIn, Facebook and X."),
        ],
        "workflow_eyebrow": "ONE CONNECTED WORKFLOW", "workflow_heading": "Start long. Publish short.",
        "workflow_copy": "Spend more time shaping your story and less time on repetitive editing tasks.",
        "steps": [("Import your long video", "Start with a podcast, interview, course, livestream or another long-form recording."), ("Let AI find the moments", "Review suggested clips, compare scores, and refine captions, hooks and framing."), ("Prepare and publish", "Create platform-ready short videos and manage your social publishing workflow.")],
        "showcases": [("output", "Your highlights, in one place", "Review generated clips and their scores before choosing what to share.", "ShortMind product screenshot showing generated short clips and Viral Scores"), ("publish", "Keep your publishing connected", "Prepare posts and schedules in the same workflow as your clips.", "ShortMind product screenshot showing the social post scheduling interface")],
        "audience": "Made for podcasters, educators, interview hosts, livestream creators, sports publishers, marketing teams and media agencies.",
        "use_cases_label": "Use cases", "use_cases_heading": "Your long videos. Your next content library.",
        "use_cases_copy": "From product demos to podcasts, turn long video into shorts suited to your audience and publishing goals.",
        "use_cases": [
            ("commerce", "E-commerce & livestreams", "Keep your product demos working.", "Turn live product demonstrations and buying questions into short clips that explain what makes your product useful.", ["Highlight product benefits and buying moments", "Prepare captioned demos for social feeds"]),
            ("brand", "Marketing teams", "One event. A full campaign library.", "Repurpose webinars, launches and brand events into a collection of product reveals, customer proof points and campaign clips.", ["Extract key messages from long recordings", "Prepare multiple formats and publishing schedules"]),
            ("courses", "Courses & education", "Give every lesson a new audience.", "Turn detailed lessons into focused knowledge clips, quick explainers and course previews that introduce your teaching.", ["Find key concepts and practical takeaways", "Add captions and adapt lessons for mobile"]),
            ("podcasters", "Podcasts & interviews", "Let your best conversations travel.", "Find memorable quotes and strong opinions in each episode, then package them into short videos for Shorts, Reels and TikTok.", ["Compare hooks and clip potential", "Keep hosts and guests in frame"]),
            ("sports", "Sports & events", "Share the moments fans remember.", "Create highlight clips from game recordings, including decisive plays, reactions and turning points, while the conversation is still active.", ["Collect standout moments in one place", "Reframe action for vertical viewing"]),
            ("film", "Film & media teams", "Build anticipation from your footage.", "Turn long footage into teasers built around memorable scenes, standout lines and dramatic moments for your next release campaign.", ["Create trailer and hook variations", "Reuse footage across social formats"]),
        ],
        "faq_heading": "A few things to know.",
        "questions": [("What is ShortMind AI?", "ShortMind is an AI video clipping and content repurposing platform. It helps creators turn long-form videos into short clips with highlights, captions, reframing and social publishing tools."), ("Does every video produce 100+ shorts?", "100+ viral-ready shorts describes the product’s content repurposing ambition. The number of useful clips depends on the source video’s length, content and settings. A Viral Score is an estimate, and does not guarantee reach or virality."), ("Where can I try ShortMind?", "Visit shortmind.ai for the current product, available features, plans and account access. This GitHub Pages site introduces the brand and links to the official website."), ("What is in the GitHub repository?", "The linked repository contains this static brand website and its documentation. To use the ShortMind video product, visit the official website.")],
        "cta_heading": "Make more of the content you already have.", "cta_copy": "Discover ShortMind’s AI video clipping tools and turn your next long video into a new content library.",
        "copyright": "ShortMind · AI video clipping & content repurposing", "preview": "Product preview", "docs": "English README",
    },
    "zh": {
        "title": "ShortMind AI — 长视频转短视频、AI 视频切片与内容再利用",
        "description": "ShortMind AI 长视频转短视频工具，自动识别精彩片段、生成字幕、智能重构画面，实现 AI 视频切片与内容再利用，并分发至 TikTok、Reels 与 YouTube Shorts 等平台。",
        "skip": "跳到正文", "features": "核心功能", "workflow": "使用流程", "faq": "常见问题", "visit": "访问官网", "github": "查看 GitHub 仓库",
        "eyebrow": "AI 视频切片 · 长视频转短视频 · 播客切片 · 直播高光 · 直播切片",
        "heading": "一条长视频，释放更多可能。", "accent": "100+ 条潜力短视频。",
        "lead": "ShortMind AI 自动识别高潜力片段，把爆点前置到开头，生成网感标题与字幕，批量产出爆款短视频，并一键分发到 TikTok、YouTube 等社媒平台。",
        "note": "在 shortmind.ai 体验产品 · 在 GitHub 查看本站项目",
        "hero_alt": "ShortMind 工作流预览：将长视频转换为带评分的竖屏短视频并进行社媒分发",
        "feature_eyebrow": "减少重复工作，专注内容创作", "feature_heading": "从精彩瞬间，到下一条好内容。",
        "feature_copy": "面向创作者与内容团队的 AI 内容增长引擎，让已有长视频持续创造价值。",
        "cards": [
            ("AI 精彩片段识别", "分析对话、关键观点与情绪变化，自动发现值得传播的片段，减少反复观看长视频的时间。"),
            ("Viral Score 与 Hook 前置", "通过 0–100 分的潜力评分比较候选片段，将吸引人的内容放在开头，辅助选片与编辑决策。"),
            ("动态与多语言字幕", "自动生成字幕，搭配不同字幕样式，帮助观众跨语言理解你的内容。"),
            ("AI 智能重构画面", "识别人脸与主体，适配 9:16、1:1 和 4:5 等社媒画幅，让画面焦点跟随内容。"),
            ("B-Roll 与发布文案", "补充相关素材画面，生成标题、描述与标签，让故事表达和发布准备更高效。"),
            ("多平台社媒分发", "连接剪辑与发布流程，面向 TikTok、YouTube Shorts、Instagram Reels、LinkedIn、Facebook 和 X。"),
        ],
        "workflow_eyebrow": "一个连贯的内容工作流", "workflow_heading": "从长视频开始，以短视频传播。",
        "workflow_copy": "把时间留给故事与创意，让 AI 帮你完成重复的剪辑工作。",
        "steps": [("导入长视频", "从播客、访谈、课程、直播或其他长视频素材开始。"), ("AI 寻找精彩瞬间", "查看候选片段与评分，调整字幕、开场钩子及画面构图。"), ("准备与发布", "生成适合社媒的短视频，在同一流程中管理发布与排期。")],
        "showcases": [("output", "精彩片段，一目了然", "集中查看生成的短视频及评分，再决定优先分享哪些内容。", "ShortMind 产品截图：生成的短视频列表与 Viral Score 评分"), ("publish", "让剪辑与发布紧密相连", "在短视频工作流中准备社媒帖子与发布排期。", "ShortMind 产品截图：社媒帖子发布与排期界面")],
        "audience": "适合播客创作者、教育工作者、访谈节目、电商直播、体育内容、企业营销团队及媒体机构。",
        "use_cases_label": "应用场景", "use_cases_heading": "不同的长视频，都有新的传播方式。",
        "use_cases_copy": "从直播带货到播客访谈，用长视频转短视频连接不同受众，让已有素材成为持续更新的内容库。",
        "use_cases": [
            ("commerce", "电商与直播带货", "让一次商品演示，持续展示卖点。", "将直播中的产品讲解、使用演示和购买疑问拆成短视频，让观众更快理解商品的特点与价值。", ["提取产品亮点与成交时刻", "生成适合社媒的带字幕演示短片"]),
            ("brand", "企业营销团队", "一场发布会，变成整套营销素材。", "把 Webinar、产品发布会和品牌活动转成产品亮点、客户观点与关键时刻短片，为后续营销持续提供素材。", ["从长录制中提炼核心信息", "准备多种画幅与发布排期"]),
            ("courses", "课程与知识分享", "把一堂长课，拆成易懂的知识短片。", "从课程里发现清晰的知识点、实用技巧与教学亮点，生成讲解短片和课程预告，让更多人认识你的内容。", ["提炼核心概念与课程要点", "添加字幕并适配移动端观看"]),
            ("podcasters", "播客与访谈节目", "让一段好对话，被更多人听见。", "从每期节目中找到金句、观点与高能对话，包装成适合 Shorts、Reels 和 TikTok 的短视频。", ["比较开场钩子与片段传播潜力", "智能重构主持人与嘉宾画面"]),
            ("sports", "体育赛事与活动", "让值得回看的瞬间，及时传播。", "从比赛录制中提取关键进球、精彩表现、现场反应和转折时刻，制作便于分享的赛事高光片段。", ["集中整理关键瞬间与高光片段", "适配竖屏构图与社媒传播"]),
            ("film", "影视宣发与媒体机构", "把长素材，变成有记忆点的预告。", "围绕精彩镜头、关键台词与剧情张力制作预告短片，为作品宣发、自媒体与 MCN 内容矩阵准备不同版本。", ["生成预告片段与开场变体", "复用素材并适配不同社媒画幅"]),
        ],
        "faq_heading": "你可能想了解。",
        "questions": [("ShortMind AI 是什么？", "ShortMind 是 AI 视频切片与内容再利用平台，帮助创作者将长视频转为短视频，提供精彩片段识别、字幕、智能重构画面与社媒分发等能力。"), ("每条视频都能生成 100+ 条短视频吗？", "100+ 条潜力短视频表达的是产品的内容再利用方向。实际可用片段数量取决于原视频时长、内容与设置。Viral Score 是辅助判断的预测评分，不保证播放量或爆款结果。"), ("在哪里体验 ShortMind？", "请访问 shortmind.ai，了解当前产品功能、套餐并登录使用。这个 GitHub Pages 页面用于品牌介绍与官网导航。"), ("GitHub 仓库包含什么？", "页面链接的仓库包含这个静态品牌站点与文档。使用 ShortMind 视频产品，请前往官方网站。")],
        "cta_heading": "让已有内容，拥有新的生命力。", "cta_copy": "探索 ShortMind 的 AI 视频切片工具，把下一条长视频变成新的内容素材库。",
        "copyright": "ShortMind · AI 视频切片与内容再利用", "preview": "产品预览", "docs": "中文 README",
    },
}


def optimize_assets():
    for lang in CONTENT:
        folder = MATERIALS / "shortmind宣传物料-中英文" / ("shortmind宣传物料-英文" if lang == "en" else "shortmind宣传物料-中文")
        for name, source in [("hero", "hero-banner"), ("output", "output-reslut"), ("publish", "publish")]:
            with Image.open(folder / f"shortmind-{source}-{lang}.png") as original:
                image = original.convert("RGB")
                for width in ([640, 1120] if name == "hero" else [640, 960]):
                    resized = image.resize((width, round(image.height * width / image.width)), Image.Resampling.LANCZOS)
                    resized.save(ASSETS / f"{name}-{lang}-{width}.webp", "WEBP", quality=80, method=6)
                if name == "hero" and lang == "en":
                    ImageOps.fit(image, (1200, 630), method=Image.Resampling.LANCZOS).save(ASSETS / "social-card.jpg", quality=85, optimize=True)
    with Image.open(MATERIALS / "a15ff4a4-cde8-4a74-b999-3a23c9855b18.png") as logo:
        logo.save(ASSETS / "brand-mark.webp", "WEBP", lossless=True, method=6)
        logo.resize((32, 32), Image.Resampling.LANCZOS).save(ASSETS / "favicon.png", optimize=True)


def picture(name, lang, alt, hero=False):
    width = 1120 if hero else 960
    sizes = "(max-width: 1152px) calc(100vw - 48px), 1120px" if hero else "(max-width: 540px) calc(100vw - 32px), (max-width: 1152px) calc((100vw - 72px) / 2), 548px"
    priority = 'fetchpriority="high"' if hero else 'loading="lazy"'
    return f'<img src="assets/{name}-{lang}-{width}.webp" srcset="assets/{name}-{lang}-640.webp 640w, assets/{name}-{lang}-{width}.webp {width}w" sizes="{sizes}" width="{width}" height="{round(width * 9 / 16)}" alt="{escape(alt)}" {priority} decoding="async">'


def build_page(lang):
    c = CONTENT[lang]
    file = "index.html" if lang == "en" else "zh.html"
    url = BASE if lang == "en" else BASE + file
    locale = "en" if lang == "en" else "zh-CN"
    cards = "".join(f'<article class="card"><span class="card-number">0{i}</span><h3>{escape(title)}</h3><p>{escape(body)}</p></article>' for i, (title, body) in enumerate(c["cards"], 1))
    steps = "".join(f'<article class="step"><span class="step-number">{i}</span><h3>{escape(title)}</h3><p>{escape(body)}</p></article>' for i, (title, body) in enumerate(c["steps"], 1))
    showcases = "".join(f'<article class="showcase"><figure>{picture(name, lang, alt)}</figure><h3>{title}</h3><p>{body}</p></article>' for name, title, body, alt in c["showcases"])
    questions = "".join(f'<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>' for q, a in c["questions"])
    use_cases = "".join(
        f'<article class="use-case"><img src="assets/use-case-{key}-{lang}.webp" width="640" height="640" alt="{escape(label + ("应用场景示意图" if lang == "zh" else " workflow illustration"))}" loading="lazy" decoding="async"><div class="use-case-copy"><span class="case-label">{escape(label)}</span><h3>{escape(title)}</h3><p>{escape(body)}</p><ul>{"".join(f"<li>{escape(bullet)}</li>" for bullet in bullets)}</ul></div></article>'
        for key, label, title, body, bullets in c["use_cases"]
    )
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "Organization", "@id": WEBSITE + "/#organization", "name": "ShortMind", "url": WEBSITE, "logo": BASE + "assets/brand-mark.webp"},
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": c["title"], "description": c["description"], "inLanguage": locale, "about": {"@id": WEBSITE + "/#organization"}},
        {"@type": "FAQPage", "@id": url + "#faq", "inLanguage": locale, "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c["questions"]]},
    ]}
    def button(href, label, primary=False):
        return f'<a class="button{" primary" if primary else ""}" href="{href}">{label} <span aria-hidden="true">↗</span></a>'
    actions = button(WEBSITE_LINK, c["visit"], True) + button(REPO, c["github"])
    logo = '<img src="assets/brand-mark.webp" width="32" height="32" alt=""><span>ShortMind</span>'
    html = f'''<!doctype html>
<html lang="{locale}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{c['title']}</title>
  <meta name="description" content="{c['description']}">
  <meta name="theme-color" content="#0f1011">
  <link rel="canonical" href="{url}">
  <link rel="alternate" hreflang="en" href="{BASE}">
  <link rel="alternate" hreflang="zh-CN" href="{BASE}zh.html">
  <link rel="alternate" hreflang="x-default" href="{BASE}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="ShortMind">
  <meta property="og:title" content="{c['title']}">
  <meta property="og:description" content="{c['description']}">
  <meta property="og:url" content="{url}">
  <meta property="og:locale" content="{'en_US' if lang == 'en' else 'zh_CN'}">
  <meta property="og:image" content="{BASE}assets/social-card.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="ShortMind AI video clipping workflow">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{c['title']}">
  <meta name="twitter:description" content="{c['description']}">
  <meta name="twitter:image" content="{BASE}assets/social-card.jpg">
  <link rel="icon" href="assets/favicon.png" type="image/png">
  <link rel="stylesheet" href="assets/site.css">
  <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
</head>
<body>
  <a class="skip" href="#main">{c['skip']}</a>
  <header class="header">
    <div class="container nav">
      <a class="brand" href="{file}" aria-label="ShortMind">{logo}</a>
      <nav class="nav-links" aria-label="{'Main navigation' if lang == 'en' else '主导航'}">
        <a href="#features">{c['features']}</a><a href="#workflow">{c['workflow']}</a><a href="#use-cases">{c['use_cases_label']}</a><a href="#faq">{c['faq']}</a><a href="{REPO}">GitHub ↗</a>
      </nav>
      <nav class="nav-actions" aria-label="{'Language and website' if lang == 'en' else '语言与官网'}">
        <a class="language" href="index.html" lang="en" hreflang="en" {'aria-current="page"' if lang == 'en' else ''}>EN</a>
        <a class="language" href="zh.html" lang="zh-CN" hreflang="zh-CN" {'aria-current="page"' if lang == 'zh' else ''}>中文</a>
        <a class="button primary small" href="{WEBSITE_LINK}">{c['visit']} ↗</a>
      </nav>
    </div>
  </header>
  <main id="main">
    <section class="hero">
      <div class="container">
        <div class="eyebrow">{c['eyebrow']}</div>
        <h1>{c['heading']}<span>{c['accent']}</span></h1>
        <p class="lead">{c['lead']}</p>
        <div class="actions">{actions}</div>
        <p class="note">{c['note']}</p>
        <figure class="hero-visual">{picture('hero', lang, c['hero_alt'], True)}</figure>
        <div class="platforms" aria-label="{'Social platforms' if lang == 'en' else '社媒平台'}"><span>TikTok</span><span>YouTube Shorts</span><span>Instagram Reels</span><span>LinkedIn</span><span>Facebook</span><span>X</span></div>
      </div>
    </section>
    <section class="section" id="features">
      <div class="container">
        <div class="section-heading"><div class="eyebrow">{c['feature_eyebrow']}</div><h2>{c['feature_heading']}</h2><p>{c['feature_copy']}</p></div>
        <div class="cards">{cards}</div>
      </div>
    </section>
    <section class="section workflow" id="workflow">
      <div class="container">
        <div class="section-heading"><div class="eyebrow">{c['workflow_eyebrow']}</div><h2>{c['workflow_heading']}</h2><p>{c['workflow_copy']}</p></div>
        <div class="steps">{steps}</div>
        <div class="showcases">{showcases}</div>
        <p class="audience">{c['audience']}</p>
      </div>
    </section>
    <section class="section" id="use-cases" aria-labelledby="use-cases-title"><div class="container"><div class="section-heading"><div class="eyebrow">{c['use_cases_label']}</div><h2 id="use-cases-title">{c['use_cases_heading']}</h2><p>{c['use_cases_copy']}</p></div><div class="use-cases-grid">{use_cases}</div></div></section>
    <section class="section" id="faq"><div class="container faq"><div class="section-heading"><div class="eyebrow">{c['faq']}</div><h2>{c['faq_heading']}</h2></div>{questions}</div></section>
    <section class="section"><div class="container"><div class="cta"><h2>{c['cta_heading']}</h2><p>{c['cta_copy']}</p><div class="actions">{actions}</div></div></div></section>
  </main>
  <footer class="footer"><div class="container"><div class="footer-inner"><a class="brand" href="{file}">{logo}</a><nav class="footer-links" aria-label="{'Footer navigation' if lang == 'en' else '页脚导航'}"><a href="{WEBSITE_LINK}">shortmind.ai ↗</a><a href="{REPO}">GitHub ↗</a><a href="{'README.en.md' if lang == 'en' else 'README.md'}">{c['docs']}</a></nav></div><p class="copyright">© 2026 {c['copyright']}</p></div></footer>
</body>
</html>
'''
    (ROOT / file).write_text(html, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--materials", type=Path, default=MATERIALS, help="Brand material directory")
    parser.add_argument("--pages-only", action="store_true", help="Reuse committed image assets")
    args = parser.parse_args()
    MATERIALS = args.materials
    if not args.pages_only:
        optimize_assets()
    for lang in CONTENT:
        build_page(lang)
    print("Built index.html, zh.html and optimized image assets.")
