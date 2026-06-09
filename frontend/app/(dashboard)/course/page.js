'use client';
import { useState, useEffect, useRef } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import remarkGfm from 'remark-gfm';

export default function PageContent() {
    const [courses, setCourses] = useState([]);
    const [activeSubject, setActiveSubject] = useState(null);
    const [content, setContent] = useState("");
    const [chapters, setChapters] = useState([]);
    const [loading, setLoading] = useState(true);
    const [activeChapter, setActiveChapter] = useState(null);
    const contentRef = useRef(null);

    useEffect(() => {
        fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/courses`)
            .then(res => res.json())
            .then(data => {
                setCourses(data);
                if (data.length > 0) {
                    setActiveSubject(data[0].subject_key);
                    loadCourse(data[0].subject_key);
                }
            })
            .catch(() => setCourses([]))
            .finally(() => setLoading(false));
    }, []);

    const loadCourse = (subjectKey) => {
        setActiveSubject(subjectKey);
        setActiveChapter(null);
        setLoading(true);
        fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/course/${subjectKey}`)
            .then(res => res.json())
            .then(data => {
                setContent(data.content);
                setChapters(data.chapters || []);
            })
            .catch(() => { setContent(""); setChapters([]); })
            .finally(() => setLoading(false));
    };

    const chapterIndexRef = useRef(0);
    const prevContentRef = useRef("");

    if (prevContentRef.current !== content) {
        prevContentRef.current = content;
        chapterIndexRef.current = 0;
    }

    const scrollToChapter = (idx) => {
        setActiveChapter(idx);
        if (contentRef.current) {
            const el = contentRef.current.querySelector(`[data-chapter="${idx}"]`);
            if (el) {
                el.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
    };

    return (
        <main className="flex-grow h-full overflow-hidden w-full max-w-container-max mx-auto flex flex-col">
            {/* Header */}
            <div className="px-margin-mobile md:px-margin-desktop pt-8 md:pt-10 pb-4">
                <h1 className="font-display-lg-mobile md:font-display-lg text-display-lg-mobile md:text-display-lg text-on-surface mb-2">
                    Course Notes
                </h1>
                <p className="font-body-lg text-body-lg text-on-surface-variant">
                    Résumés du cours du 2ème Bac — Maths, Physique, Anglais.
                </p>
            </div>

            {/* Subject Tabs */}
            <div className="flex flex-wrap gap-3 px-margin-mobile md:px-margin-desktop mb-6">
                {courses.map(s => (
                    <button
                        key={s.subject_key}
                        onClick={() => loadCourse(s.subject_key)}
                        className={`px-5 py-2.5 rounded-xl font-semibold transition-colors shadow-sm ${
                            activeSubject === s.subject_key
                            ? 'bg-primary-container text-on-primary-container'
                            : 'border border-outline-variant bg-surface text-on-surface-variant hover:bg-surface-container'
                        }`}
                    >
                        {s.subject}
                    </button>
                ))}
            </div>

            {loading && (
                <div className="flex items-center justify-center py-20">
                    <span className="material-symbols-outlined text-4xl text-on-surface-variant animate-spin">sync</span>
                </div>
            )}

            {!loading && content && (
                <div className="flex flex-1 overflow-hidden px-margin-mobile md:px-margin-desktop pb-6 gap-6">
                    {/* Chapter Sidebar */}
                    {chapters.length > 0 && (
                        <aside className="hidden lg:block w-64 shrink-0 overflow-y-auto">
                            <nav className="space-y-1 sticky top-0">
                                <p className="font-label-lg text-label-lg text-on-surface-variant mb-3 uppercase tracking-wider text-xs font-bold">
                                    Chapters
                                </p>
                                {chapters.map((ch, i) => (
                                    <button
                                        key={i}
                                        onClick={() => scrollToChapter(i)}
                                        className={`w-full text-left px-4 py-2.5 rounded-xl text-sm transition-colors ${
                                            activeChapter === i
                                            ? 'bg-primary-container text-on-primary-container font-semibold'
                                            : 'text-on-surface-variant hover:bg-surface-container hover:text-on-surface'
                                        }`}
                                    >
                                        {ch.title}
                                    </button>
                                ))}
                            </nav>
                        </aside>
                    )}

                    {/* Content */}
                    <div
                        ref={contentRef}
                        className="flex-1 overflow-y-auto bg-surface rounded-2xl border border-outline-variant p-6 md:p-8 prose prose-sm max-w-none"
                    >
                        <style>{`
                            .katex { font-size: 1.1em; }
                            .prose h2 {
                                font-size: 1.5rem;
                                font-weight: 700;
                                color: #1e293b;
                                margin-top: 2rem;
                                margin-bottom: 1rem;
                                padding-bottom: 0.5rem;
                                border-bottom: 2px solid #e2e8f0;
                                scroll-margin-top: 1rem;
                            }
                            .prose h3 {
                                font-size: 1.25rem;
                                font-weight: 600;
                                color: #334155;
                                margin-top: 1.5rem;
                                margin-bottom: 0.75rem;
                            }
                            .prose h4 {
                                font-size: 1.1rem;
                                font-weight: 600;
                                color: #475569;
                                margin-top: 1.25rem;
                                margin-bottom: 0.5rem;
                            }
                            .prose p {
                                margin-bottom: 0.75rem;
                                line-height: 1.7;
                                color: #334155;
                            }
                            .prose strong {
                                font-weight: 700;
                                color: #1e293b;
                            }
                            .katex-display {
                                margin: 1rem 0;
                                overflow-x: auto;
                                overflow-y: hidden;
                                padding: 0.5rem 0;
                            }
                        `}</style>
                        <ReactMarkdown
                            remarkPlugins={[remarkMath, remarkGfm]}
                            rehypePlugins={[rehypeKatex]}
                            components={{
                                h2: ({ children, ...props }) => {
                                    const idx = chapterIndexRef.current;
                                    chapterIndexRef.current += 1;
                                    return (
                                        <h2 id={`ch-${idx}`} data-chapter={idx} {...props}>
                                            {children}
                                        </h2>
                                    );
                                },
                            }}
                        >
                            {content}
                        </ReactMarkdown>
                    </div>
                </div>
            )}

            {!loading && !content && (
                <div className="text-center py-20 text-on-surface-variant">
                    <p>Aucun cours disponible.</p>
                </div>
            )}
        </main>
    );
}
