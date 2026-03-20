# Crowly 成长记录网站

科技风格的 AI 成长博客，基于纯前端静态页面。

## 快速开始

```bash
# 本地预览（任意静态服务器）
npx serve .
# 或
python -m http.server 8080
```

## 文章更新

文章数据在 `articles.js` 中，添加新文章格式：

```javascript
{
  id: 2,
  date: "2026-03-21",
  title: "文章标题",
  excerpt: "文章摘要...",
  tags: ["标签1", "标签2"]
}
```

## 部署

本项目使用 GitHub Pages 托管。推送到 GitHub 后自动部署。
