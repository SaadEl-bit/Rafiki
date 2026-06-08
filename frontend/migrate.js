const fs = require('fs');
const path = require('path');

const exportsDir = 'h:/Study/Projects/M3allem/Github/Frontend Design/stitch_exports';
const appDir = 'h:/Study/Projects/M3allem/Github/Rafiki/frontend/app';

function htmlToJsx(html) {
    let jsx = html.replace(/class=/g, 'className=');
    // Basic replacements for JSX
    jsx = jsx.replace(/<!--(.*?)-->/g, '{/* $1 */}');
    jsx = jsx.replace(/<img(.*?)>/g, (match) => {
        if (!match.endsWith('/>')) {
            return match.replace(/>$/, ' />');
        }
        return match;
    });
    jsx = jsx.replace(/<input(.*?)>/g, (match) => {
        if (!match.endsWith('/>')) {
            return match.replace(/>$/, ' />');
        }
        return match;
    });
    jsx = jsx.replace(/<br>/g, '<br />');
    jsx = jsx.replace(/<hr>/g, '<hr />');
    jsx = jsx.replace(/style="(.*?)"/g, (match, styleString) => {
        // Very basic inline style converter for the few ones that exist
        if (!styleString.trim()) return '';
        const styleObj = {};
        styleString.split(';').forEach(rule => {
            const [key, value] = rule.split(':');
            if (key && value) {
                const camelKey = key.trim().replace(/-([a-z])/g, g => g[1].toUpperCase());
                styleObj[camelKey] = value.trim();
            }
        });
        return `style={${JSON.stringify(styleObj)}}`;
    });
    return jsx;
}

function extractMainContent(htmlString, isLanding = false) {
    if (isLanding) {
        // For landing page, extract everything inside <body>...</body>
        const bodyMatch = htmlString.match(/<body[^>]*>([\s\S]*?)<\/body>/);
        if (bodyMatch) return htmlStringToComponent(bodyMatch[1], 'HomePage');
    } else {
        // For dashboard pages, extract <main>...</main>
        const mainMatch = htmlString.match(/<main[^>]*>([\s\S]*?)<\/main>/);
        if (mainMatch) {
            // Include the <main> tag itself
            const mainHtml = `<main${htmlString.match(/<main([^>]*)>/)[1]}>${mainMatch[1]}</main>`;
            return htmlStringToComponent(mainHtml, 'PageContent');
        }
    }
    return '';
}

function htmlStringToComponent(html, componentName) {
    let jsx = htmlToJsx(html);
    return `import Link from 'next/link';\n\nexport default function ${componentName}() {\n    return (\n        <>\n${jsx}\n        </>\n    );\n}\n`;
}

// 1. Landing Page
const landingHtml = fs.readFileSync(path.join(exportsDir, 'landing_page.html'), 'utf8');
fs.writeFileSync(path.join(appDir, 'page.js'), extractMainContent(landingHtml, true));

// 2. Chat
const chatHtml = fs.readFileSync(path.join(exportsDir, 'ai_chat.html'), 'utf8');
fs.writeFileSync(path.join(appDir, '(dashboard)/chat/page.js'), extractMainContent(chatHtml, false));

// 3. Correction
const correctionHtml = fs.readFileSync(path.join(exportsDir, 'exercise_correction.html'), 'utf8');
fs.writeFileSync(path.join(appDir, '(dashboard)/correction/page.js'), extractMainContent(correctionHtml, false));

// 4. Resume
const resumeHtml = fs.readFileSync(path.join(exportsDir, 'resume_generation.html'), 'utf8');
fs.writeFileSync(path.join(appDir, '(dashboard)/resume/page.js'), extractMainContent(resumeHtml, false));

// 5. Exam Gen
const examGenHtml = fs.readFileSync(path.join(exportsDir, 'exam_generation.html'), 'utf8');
const examGenDir = path.join(appDir, '(dashboard)/exam-gen');
if (!fs.existsSync(examGenDir)) fs.mkdirSync(examGenDir, { recursive: true });
fs.writeFileSync(path.join(examGenDir, 'page.js'), extractMainContent(examGenHtml, false));

// 6. Exam Correction
const examCorrHtml = fs.readFileSync(path.join(exportsDir, 'exam_correction.html'), 'utf8');
const examCorrDir = path.join(appDir, '(dashboard)/exam-correction');
if (!fs.existsSync(examCorrDir)) fs.mkdirSync(examCorrDir, { recursive: true });
fs.writeFileSync(path.join(examCorrDir, 'page.js'), extractMainContent(examCorrHtml, false));

// 7. Cadre
const cadreHtml = fs.readFileSync(path.join(exportsDir, 'cadre_referenciel.html'), 'utf8');
fs.writeFileSync(path.join(appDir, '(dashboard)/cadre/page.js'), extractMainContent(cadreHtml, false));

console.log("Migration complete!");
