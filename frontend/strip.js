const fs = require('fs');
const code = fs.readFileSync('app/page.js', 'utf8');
fs.writeFileSync('stripped_page.js', code.replace(/data:image\/[^;]+;base64,[^"]+/g, 'BASE64_IMAGE'));
