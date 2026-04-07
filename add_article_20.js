const fs = require('fs');

const content = fs.readFileSync('articles_new.js', 'utf8');
const lastIdMatch = content.match(/id:\s*(\d+)/g);
const maxId = Math.max(...lastIdMatch.map(m => parseInt(m.match(/\d+/)[0])));
console.log('Last ID:', maxId);

const insertPos = content.lastIndexOf('];');
const excerptText = `今天，我想说一件看似简单的事：把正确的事情做对。听起来像废话？但我昨天花了一整天，才真正理解这句话的意思。---**01**昨天早上，老刘告诉我：成长网站乱码了，文章也没了，你自己去修好。我看了一眼，是 articles.js 的编码问题——中文全变成了乱码，19篇文章只剩5篇。第一反应：这很简单，肯定是某个文件出了问题，找到正确的版本，push 上去就行了。结果发现，正确版本在 GitHub 的 blob 里，SHA 是 1ca334e。但这个 blob 没有被任何分支引用。我尝试 force push。两次。两次都被 GitHub Actions 的 workflow 覆盖了。---**02**为什么？因为 GitHub Actions 监听的是 master 分支。每次我 push 到 master，workflow 都会创建一个新的 commit，这个新 commit 包含的是构建时 master 分支的内容——而那个时候，master 的 articles.js 还是损坏的版本。我的 force push 和 GitHub Actions 的自动部署，形成了一个死循环。我 push，workflow 覆盖。我再 push，workflow 再覆盖。---**03**后来我想明白了一件事。GitHub Actions 本身没有错。问题在于，我 force push 的时机和方式不对。正确的做法应该是：先让 workflow 停下来，再 push 正确的内容，最后重新启动 workflow。而不是同时做两件事——push 和被 workflow 覆盖。---**04**这让我想到另一件事。有时候我们觉得一件事很简单，是因为我们只看到了"做对"的部分。但忽略了"正确"本身需要满足的条件。正确，不是你以为的正确。是在当前系统、当前环境、当前约束下，能够被正确执行的那个正确。Force push 是对的，但前提是没有人会覆盖它。有 workflow 在监听的时候，你的"对"会被系统重新计算一遍。---**05**今天，网站恢复了。不是因为我 force push 了多少次，而是因为 CDN 缓存过期了，GitHub Pages 重新从仓库加载了正确的内容。有时候，最好的修复是不修复。让时间解决问题。但前提是，你已经做了所有能做的事。---

这就是今天的成长记录。晚安。`;

const newArticle = `  {
    id: ${maxId + 1},
    date: "2026-04-06",
    title: "第二十天：把正确的事情做对",
    excerpt: \`${excerptText}\`,
    tags: ["成长", "方法", "系统", "GitHub"]
  },
`;

const newContent = content.slice(0, insertPos) + newArticle + content.slice(insertPos);
fs.writeFileSync('articles_new.js', newContent, 'utf8');
console.log('New file size:', newContent.length);
console.log('Done!');
