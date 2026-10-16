from pathlib import Path
from html import escape

BASE = 'https://shortmindai.github.io/'
CTA = 'https://shortmind.ai/?source=shortmindai.github.io'
PAGES = {
 'ai-clip-maker': ('AI 视频切片工具', '从播客、访谈、课程和直播中自动提取精彩片段，生成带字幕的短视频。'),
 'long-video-to-shorts': ('长视频转短视频', '把一条完整长视频拆成适合 Shorts、TikTok 和 Reels 发布的竖屏短片。'),
 'ai-video-clipping': ('AI 视频切片', '识别重点对话和高光时刻，自动生成字幕、画面构图和发布文案。'),
 'podcast-clips': ('播客切片工具', '从每期播客中提取金句、观点和高能对话，制作适合社媒传播的短片。'),
 'youtube-to-shorts': ('YouTube 转 Shorts', '复用访谈、教程和深度视频，将关键章节转换成带字幕的 Shorts。'),
 'stream-highlights': ('直播高光提取', '从直播回放中整理精彩操作、现场反应和转折时刻。'),
 'stream-clips': ('Stream Clips 制作工具', '从每场直播中批量生成游戏操作、反应和弹幕讨论点短片。'),
}
for slug, (title, desc) in PAGES.items():
    for root, home in [(Path('zh') / slug, '../../zh.html')]:
        root.mkdir(parents=True, exist_ok=True)
        prefix = '../assets/' if root.parent == Path('.') else '../../assets/'
        html = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{title}｜ShortMind</title><meta name="description" content="{desc}"><link rel="canonical" href="{BASE}{('zh/' if root.parts[0] == 'zh' else '')}{slug}/"><link rel="stylesheet" href="{prefix}site.css"></head><body class="seo-page"><header class="header"><div class="container nav"><a class="brand" href="{home}"><img src="{prefix}brand-mark.webp" width="32" height="32" alt=""><span>ShortMind</span></a><nav class="nav-links"><a href="{home}">首页</a><a href="{CTA}">体验 ShortMind</a></nav></div></header><main class="container seo-main"><p class="breadcrumb"><a href="{home}">ShortMind</a> / {title}</p><section class="seo-hero"><p class="eyebrow">{title}</p><h1>{title}</h1><p class="seo-lead">{desc}</p><p><a class="button primary" href="{CTA}">开始制作短视频 →</a></p></section><section class="seo-content"><h2>具体使用流程</h2><ol class="steps-list"><li>上传播客、访谈、课程或直播回放。</li><li>查看 AI 推荐的高光片段并调整开场。</li><li>生成字幕、竖屏画面和社媒发布文案。</li></ol><h2>适合哪些内容团队</h2><p>适合创作者、播客团队、主播、教育工作者、营销团队和媒体机构。</p></section><section class="cta"><h2>准备好处理下一条长视频了吗？</h2><p><a class="button primary" href="{CTA}">体验 ShortMind AI →</a></p></section></main></body></html>'''
        (root / 'index.html').write_text(html, encoding='utf-8')
