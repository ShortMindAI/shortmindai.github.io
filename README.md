# ShortMind AI

**ShortMind AI 自动识别高潜力片段，把爆点前置到开头，生成网感标题与字幕，批量产出爆款短视频，并一键分发到 TikTok、YouTube 等社媒平台。**

[English](README.en.md) · [官方网站](https://shortmind.ai/?source=shortmindai.github.io) · [品牌主页](https://shortmindai.github.io/) · [GitHub 仓库](https://github.com/ShortMindAI/shortmindai.github.io)

![ShortMind 将长视频转换为短视频并进行社媒分发的工作流](assets/hero-zh-1120.webp)

## 关于 ShortMind

ShortMind AI 是面向创作者、企业和营销团队的 AI 视频切片与内容再利用平台。它从长视频中发现有传播价值的片段，辅助生成短视频，并将字幕、画面重构、发布文案及社媒分发连接成一个工作流。

「100+ 条潜力短视频」表达产品的内容再利用方向；实际可用片段数量取决于原视频时长、内容与设置，评分不保证播放量或爆款结果。

## SEO 使用场景与教程

ShortMind 覆盖 AI 视频切片、长视频转短视频和内容再利用等实际需求。你可以查看 [播客切片](zh/podcast-clips/)、[YouTube 转 Shorts](zh/youtube-to-shorts/)、[直播高光](zh/stream-highlights/) 和 [Stream Clips](zh/stream-clips/) 页面。

- [AI 视频切片工具](zh/ai-clip-maker/)：适合播客、访谈和 Webinar
- [长视频转短视频](zh/long-video-to-shorts/)：从完整录制生成短视频
- [AI 视频切片工作流](zh/ai-video-clipping/)：字幕、开场钩子和画面重构
- [短视频教程与案例](zh/resources/)：按业务场景学习内容再利用

当前内容中心包含 20 篇围绕 AI 视频切片、长视频转短视频、播客切片、YouTube 转 Shorts、直播高光和 Stream Clips 的中文教程与场景案例。

## 核心能力

| 能力 | 用途 |
| --- | --- |
| AI 精彩片段识别 | 根据对话、关键观点与情绪变化发现候选片段，减少人工反复选片。 |
| Viral Score | 用 0–100 分的预测评分辅助比较片段的钩子、节奏与传播潜力。 |
| Hook 自动前置 | 将吸引人的内容放到开头，构建更清晰的短视频开场。 |
| AI 字幕 | 自动生成动态、多语言字幕，选择合适的字幕样式。 |
| AI Reframe | 识别人脸与主体，适配 9:16、1:1、4:5 等社媒画幅。 |
| B-Roll 与文案 | 补充相关素材，生成标题、描述与 Hashtag 标签。 |
| 社媒分发 | 连接剪辑与 TikTok、YouTube Shorts、Instagram Reels、LinkedIn、Facebook、X 等平台的发布流程。 |

适合播客、访谈、课程、电商直播、体育内容、企业营销、媒体机构与 MCN 团队，尤其适合已有长视频素材库的内容团队。当前功能、支持平台与套餐以[官方网站](https://shortmind.ai/?source=shortmindai.github.io)为准。

## 使用流程

1. 在官网导入长视频素材。
2. 查看 AI 推荐片段与评分，调整字幕、开场和画面构图。
3. 生成适合社媒的短视频，准备发布文案与排期。

## 本仓库

本仓库维护 ShortMind 的静态品牌介绍站点，包含英文首页、中文页面与说明文档。视频处理产品通过官网提供服务。

```text
index.html            英文首页
zh.html               中文页面
404.html              自定义错误页面
assets/               共享 CSS、WebP 图片、图标和社交分享图
README.md             中文说明
README.en.md          英文说明
robots.txt            爬虫与 sitemap 地址
sitemap.xml           中英文页面索引
scripts/build_site.py 页面生成与图片压缩脚本
```

## 本地预览与维护

站点无需 Node.js、构建框架或客户端 JavaScript。运行以下命令后访问 `http://localhost:8000`：

```bash
python -m http.server 8000
```

修改 `scripts/build_site.py` 中的双语文案后重新生成页面。脚本需要 Python 3.9+ 与 Pillow（`python -m pip install Pillow`）：

```bash
python scripts/build_site.py --pages-only
```

重新压缩图片时，传入包含原始 PNG 与「shortmind宣传物料-中英文」子目录的物料路径：

```bash
python scripts/build_site.py --materials "你的品牌物料目录"
```

## GitHub Pages 部署

账号主页 `https://shortmindai.github.io/` 对应的仓库必须命名为 `shortmindai.github.io`。将本站文件放在该仓库根目录，在 **Settings → Pages** 选择 **Deploy from a branch → main → / (root)**，保存后等待部署成功。`.nojekyll` 用于直接发布静态文件。

当前 Git remote 指向 `ShortMindAI/shortmindai.github.io`，与账号主页地址一致。部署到其他地址时，要同步调整脚本中的 `BASE`、`robots.txt`、`sitemap.xml` 及 `404.html` 的根路径，使链接与 canonical 符合实际网址。

## SEO 与加载优化

- 页面正文直接包含在 HTML 中，使用语义化标题、导航与 FAQ。
- 中英文页面分别提供标题、描述、canonical 和互相对应的 `hreflang`。
- 包含 Organization、WebPage、FAQPage JSON-LD，以及 Open Graph / Twitter 分享信息。结构化数据不保证搜索结果展示形式。
- 图片采用压缩 WebP 与响应式 `srcset`；首屏图片高优先级，后续截图延迟加载，显式声明尺寸以减少布局跳动。
- 社交分享图使用 JPEG 兼容预览服务；采用系统字体，无第三方脚本或前端运行时。

ShortMind — 让已有内容，拥有新的生命力。
