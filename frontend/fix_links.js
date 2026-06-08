const fs = require('fs');
let code = fs.readFileSync('app/page.js', 'utf8');
code = code.replace(/\/app\/chat/g, '/chat');
code = code.replace(/\/app\/correction/g, '/correction');
code = code.replace(/<button([^>]*)>View Feature<\/button>/g, '<Link href="#"$1>View Feature</Link>');
code = code.replace(/<a([^>]*)href="\#"([^>]*)>/g, '<Link$1href="#"$2>');
code = code.replace(/<\/a>/g, '</Link>');

fs.writeFileSync('app/page.js', code);
console.log('Fixed links in page.js');
