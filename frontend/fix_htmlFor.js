const fs = require('fs');
const path = require('path');

function walkDir(dir) {
    let results = [];
    const list = fs.readdirSync(dir);
    list.forEach((file) => {
        file = path.join(dir, file);
        const stat = fs.statSync(file);
        if (stat && stat.isDirectory()) {
            results = results.concat(walkDir(file));
        } else {
            if (file.endsWith('.js') || file.endsWith('.jsx')) {
                results.push(file);
            }
        }
    });
    return results;
}

const dirsToCheck = ['app', 'components'];
dirsToCheck.forEach(dir => {
    const files = walkDir(dir);
    files.forEach(file => {
        let content = fs.readFileSync(file, 'utf8');
        let changed = false;
        
        // Replace for="..." with htmlFor="..."
        if (content.match(/\bfor="/)) {
            content = content.replace(/\bfor="/g, 'htmlFor="');
            changed = true;
        }

        if (changed) {
            fs.writeFileSync(file, content);
            console.log(`Fixed ${file}`);
        }
    });
});
