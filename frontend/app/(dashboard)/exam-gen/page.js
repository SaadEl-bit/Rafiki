'use client';
import { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import remarkGfm from 'remark-gfm';

export default function PageContent() {
    const [topicsData, setTopicsData] = useState({});
    const [subject, setSubject] = useState("maths");
    const [topic, setTopic] = useState("");
    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState(null);
    const [error, setError] = useState("");
    const [expandedCorr, setExpandedCorr] = useState({});

    const subjectNames = { maths: "Mathématiques", physics: "Physique-Chimie", english: "Anglais" };

    useEffect(() => {
        fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/generate/topics`)
            .then(res => res.json())
            .then(data => setTopicsData(data))
            .catch(() => {});
    }, []);

    const currentTopics = topicsData[subject]?.topics || [];

    const handleSubjectChange = (newSubject) => {
        setSubject(newSubject);
        setTopic("");
        setResult(null);
        setError("");
    };

    const generate = async () => {
        setLoading(true);
        setResult(null);
        setError("");
        setExpandedCorr({});
        try {
            const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/generate/exam`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ subject, topic }),
            });
            if (!res.ok) {
                const err = await res.json();
                throw new Error(err.detail || "Erreur lors de la génération");
            }
            const data = await res.json();
            setResult(data);
        } catch (e) {
            setError(e.message);
        } finally {
            setLoading(false);
        }
    };

    const toggleCorr = (idx) => {
        setExpandedCorr(prev => ({ ...prev, [idx]: !prev[idx] }));
    };

    return (
        <main className="flex-grow h-full overflow-y-auto w-full max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop py-8 md:py-10 flex flex-col">
            <header className="mb-6">
                <h1 className="font-display-lg-mobile md:font-display-lg text-display-lg-mobile md:text-display-lg text-on-surface mb-2">
                    Exam Generation
                </h1>
                <p className="font-body-lg text-body-lg text-on-surface-variant">
                    Génère un examen complet corrigé, adapté au programme du 2ème Bac.
                </p>
            </header>

            {/* Subject Tabs */}
            <div className="flex flex-wrap gap-3 mb-6">
                {Object.entries(subjectNames).map(([key, name]) => (
                    <button
                        key={key}
                        onClick={() => handleSubjectChange(key)}
                        className={`px-5 py-2.5 rounded-xl font-semibold transition-colors shadow-sm ${
                            subject === key
                            ? 'bg-primary-container text-on-primary-container'
                            : 'border border-outline-variant bg-surface text-on-surface-variant hover:bg-surface-container'
                        }`}
                    >
                        {name}
                    </button>
                ))}
            </div>

            {/* Topic + Generate */}
            <div className="bg-surface rounded-2xl border border-outline-variant p-6 mb-6">
                <div className="flex flex-col md:flex-row gap-4 items-end">
                    <div className="flex-1 w-full">
                        <label className="block font-label-sm text-label-sm text-on-surface-variant mb-2 uppercase tracking-wider">
                            Topic (optional)
                        </label>
                        <select
                            value={topic}
                            onChange={(e) => setTopic(e.target.value)}
                            className="w-full rounded-xl border border-outline-variant bg-surface-container-low text-on-surface px-4 py-3 outline-none focus:ring-2 focus:ring-primary-fixed-dim transition-all"
                        >
                            <option value="">— All topics / Général —</option>
                            {currentTopics.map((t, i) => (
                                <option key={i} value={t}>{t}</option>
                            ))}
                        </select>
                    </div>
                    <button
                        onClick={generate}
                        disabled={loading}
                        className="shrink-0 bg-primary-container text-on-primary-container px-8 py-3 rounded-xl font-semibold hover:bg-primary-fixed transition-colors shadow-md disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
                    >
                        {loading ? (
                            <><span className="material-symbols-outlined text-sm animate-spin">sync</span> Generating...</>
                        ) : (
                            <><span className="material-symbols-outlined text-sm">auto_awesome</span> Generate Exam</>
                        )}
                    </button>
                </div>
            </div>

            {/* Error */}
            {error && (
                <div className="bg-error-container text-on-error-container rounded-2xl border border-error p-4 mb-6">
                    {error}
                </div>
            )}

            {/* Result */}
            {result && result.pairs && (
                <div className="bg-surface rounded-2xl border border-outline-variant overflow-hidden">
                    <div className="p-6 md:p-8">
                        <h2 className="font-headline-lg text-headline-lg text-on-surface mb-6">
                            {result.exam_title || `Examen de ${result.subject}`}
                        </h2>

                        <div className="space-y-4">
                            {result.pairs.map((pair, idx) => (
                                <div key={idx} className="bg-surface-container-low rounded-xl border border-outline-variant overflow-hidden">
                                    {/* Question */}
                                    <div className="p-5 prose prose-sm max-w-none">
                                        <style>{`
                                            .katex { font-size: 1.1em; }
                                            .katex-display { margin: 0.75rem 0; overflow-x: auto; }
                                            .prose p { margin-bottom: 0.5rem; line-height: 1.6; color: #334155; }
                                        `}</style>
                                        <span className="inline-block bg-primary-container text-on-primary-container text-xs font-bold px-2 py-0.5 rounded-md mb-2">
                                            {pair.question}
                                        </span>
                                        <ReactMarkdown
                                            remarkPlugins={[remarkMath, remarkGfm]}
                                            rehypePlugins={[rehypeKatex]}
                                        >
                                            {pair.question_text}
                                        </ReactMarkdown>
                                    </div>

                                    {/* Correction toggle */}
                                    <button
                                        onClick={() => toggleCorr(idx)}
                                        className="w-full flex items-center justify-between px-5 py-3 bg-surface hover:bg-surface-container-high transition-colors border-t border-outline-variant"
                                    >
                                        <span className="font-semibold text-sm text-on-surface-variant flex items-center gap-2">
                                            <span className="material-symbols-outlined text-sm">lightbulb</span>
                                            Correction
                                        </span>
                                        <span className="material-symbols-outlined text-on-surface-variant text-sm transition-transform"
                                            style={{ transform: expandedCorr[idx] ? 'rotate(180deg)' : 'rotate(0deg)' }}>
                                            expand_more
                                        </span>
                                    </button>

                                    {/* Correction content */}
                                    {expandedCorr[idx] && (
                                        <div className="px-5 pb-5 pt-3 bg-surface prose prose-sm max-w-none">
                                            <ReactMarkdown
                                                remarkPlugins={[remarkMath, remarkGfm]}
                                                rehypePlugins={[rehypeKatex]}
                                            >
                                                {pair.correction}
                                            </ReactMarkdown>
                                        </div>
                                    )}
                                </div>
                            ))}
                        </div>
                    </div>
                </div>
            )}

            {!loading && result && result.error && (
                <div className="bg-error-container text-on-error-container rounded-2xl border border-error p-4 mb-6">
                    {result.error}
                </div>
            )}
        </main>
    );
}
