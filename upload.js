const fs = require('fs');
const https = require('https');

// Token should be set via environment variable GITHUB_TOKEN
// Run: set GITHUB_TOKEN=your_token_before using this script
const token = process.env.GITHUB_TOKEN || '';
const repo = 'roverliul/crowly';

function uploadFile(filename, localPath) {
  return new Promise((resolve, reject) => {
    if (!token) {
      console.log(`${filename}: SKIPPED (no token)`);
      resolve();
      return;
    }
    const content = fs.readFileSync(localPath);
    const encoded = content.toString('base64');
    
    const shaUrl = `https://api.github.com/repos/${repo}/contents/${filename}`;
    const getOptions = {
      hostname: 'api.github.com',
      headers: { 'Authorization': 'token ' + token, 'User-Agent': 'Crowly-Upload' }
    };
    
    https.get(shaUrl, getOptions, res => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => {
        let sha = null;
        try {
          const json = JSON.parse(data);
          sha = json.sha;
        } catch(e) {}
        
        const uploadData = JSON.stringify({
          message: `Update ${filename}`,
          content: encoded,
          sha: sha
        });
        
        const uploadOptions = {
          hostname: 'api.github.com',
          path: `/repos/${repo}/contents/${filename}`,
          method: 'PUT',
          headers: {
            'Authorization': 'token ' + token,
            'User-Agent': 'Crowly-Upload',
            'Content-Type': 'application/json',
            'Content-Length': Buffer.byteLength(uploadData)
          }
        };
        
        const req = https.request(uploadOptions, res2 => {
          let data2 = '';
          res2.on('data', c => data2 += c);
          res2.on('end', () => {
            try {
              const result = JSON.parse(data2);
              console.log(`${filename}: ${result.content ? 'OK' : 'FAILED'}`);
            } catch(e) {
              console.log(`${filename}: DONE`);
            }
            resolve();
          });
        });
        req.on('error', reject);
        req.write(uploadData);
        req.end();
      });
    }).on('error', reject);
  });
}

async function main() {
  await uploadFile('index.html', 'C:/Users/liulv/.openclaw/workspace/crowly-site/index.html');
  await uploadFile('styles.css', 'C:/Users/liulv/.openclaw/workspace/crowly-site/styles.css');
  await uploadFile('articles.js', 'C:/Users/liulv/.openclaw/workspace/crowly-site/articles.js');
  console.log('All done!');
}

main();
