const fs = require('fs');
let code = fs.readFileSync('app/page.js', 'utf8');
code = code.replace(/<a className="text-on-surface-variant hover:text-primary transition-colors cursor-pointer font-medium" href="#features">Features<\/Link>/g, '<Link className="text-on-surface-variant hover:text-primary transition-colors cursor-pointer font-medium" href="#features">Features</Link>');
code = code.replace(/<a className="text-on-surface-variant hover:text-primary transition-colors cursor-pointer font-medium" href="#how-it-works">How it Works<\/Link>/g, '<Link className="text-on-surface-variant hover:text-primary transition-colors cursor-pointer font-medium" href="#how-it-works">How it Works</Link>');
code = code.replace(/<a className="bg-primary text-on-primary font-semibold px-6 py-3 rounded-xl hover:bg-primary\/90 transition-colors duration-200 flex items-center gap-2" href="\/chat">([^<]*)<\/Link>/g, '<Link className="bg-primary text-on-primary font-semibold px-6 py-3 rounded-xl hover:bg-primary/90 transition-colors duration-200 flex items-center gap-2" href="/chat">$1</Link>');
code = code.replace(/<a className="bg-surface-container-lowest text-primary font-bold px-6 py-2 rounded-xl hover:bg-surface-container-low transition-colors duration-200" href="\/correction">([^<]*)<\/Link>/g, '<Link className="bg-surface-container-lowest text-primary font-bold px-6 py-2 rounded-xl hover:bg-surface-container-low transition-colors duration-200" href="/correction">$1</Link>');
fs.writeFileSync('app/page.js', code);
console.log('Restored links in page.js');
