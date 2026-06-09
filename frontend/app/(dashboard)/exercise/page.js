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
    const [showSolution, setShowSolution] = useState(false);

    const subjectNames = { maths: "Mathématiques", physics: "Physique-Chimie", english: "Anglais" };

    useEffect(() => {
        fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/generate/topics`)
            .then(res => res.json())
            .then(data => {
                setTopicsData(data);
                const firstTopics = data[Object.keys(data)[0]]?.topics || [];
                if (firstTopics.length > 0) setTopic(firstTopics[0]);
            })
            .catch(() => {});
    }, []);

    const currentTopics = topicsData[subject]?.topics || [];

    const handleSubjectChange = (newSubject) => {
        setSubject(newSubject);
        setTopic(topicsData[newSubject]?.topics?.[0] || "");
        setResult(null);
        setError("");
    };

    const generate = async () => {
        if (!topic) return;
        setLoading(true);
        setResult(null);
        setError("");
        setShowSolution(false);
        try {
            const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/generate/exercise`, {
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

    return (
        <main className="flex-grow h-full overflow-y-auto w-full max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop py-8 md:py-10 flex flex-col">
            <header className="mb-6">
                <h1 className="font-display-lg-mobile md:font-display-lg text-display-lg-mobile md:text-display-lg text-on-surface mb-2">
                    Exercise Generation
                </h1>
                <p className="font-body-lg text-body-lg text-on-surface-variant">
                    Génère un exercice corrigé sur un thème spécifique du programme.
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
                            Topic / Thème
                        </label>
                        <select
                            value={topic}
                            onChange={(e) => setTopic(e.target.value)}
                            className="w-full rounded-xl border border-outline-variant bg-surface-container-low text-on-surface px-4 py-3 outline-none focus:ring-2 focus:ring-primary-fixed-dim transition-all"
                        >
                            {currentTopics.map((t, i) => (
                                <option key={i} value={t}>{t}</option>
                            ))}
                        </select>
                    </div>
                    <button
                        onClick={generate}
                        disabled={loading || !topic}
                        className="shrink-0 bg-primary-container text-on-primary-container px-8 py-3 rounded-xl font-semibold hover:bg-primary-fixed transition-colors shadow-md disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
                    >
                        {loading ? (
                            <><span className="material-symbols-outlined text-sm animate-spin">sync</span> Generating...</>
                        ) : (
                            <><span className="material-symbols-outlined text-sm">auto_awesome</span> Generate Exercise</>
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
            {result && (
                <div className="bg-surface rounded-2xl border border-outline-variant overflow-hidden">
                    <div className="p-6 md:p-8 prose prose-sm max-w-none">
                        <style>{`
                            .katex { font-size: 1.1em; }
                            .katex-display { margin: 1rem 0; overflow-x: auto; overflow-y: hidden; padding: 0.5rem 0; }
                            .prose h2 { font-size: 1.4rem; font-weight: 700; color: #1e293b; margin-top: 1.5rem; margin-bottom: 1rem; padding-bottom: 0.5rem; border-bottom: 2px solid #e2e8f0; }
                            .prose h3 { font-size: 1.2rem; font-weight: 600; color: #334155; margin-top: 1.25rem; margin-bottom: 0.75rem; }
                            .prose p { margin-bottom: 0.75rem; line-height: 1.7; color: #334155; }
                            .prose strong { font-weight: 700; color: #1e293b; }
                        `}</style>
                        <ReactMarkdown
                            remarkPlugins={[remarkMath, remarkGfm]}
                            rehypePlugins={[rehypeKatex]}
                        >
                            {result.exercise}
                        </ReactMarkdown>

                        <button
                            onClick={() => setShowSolution(!showSolution)}
                            className="mt-6 w-full flex items-center justify-center gap-2 bg-primary-container text-on-primary-container px-6 py-3.5 rounded-xl font-semibold hover:bg-primary-fixed transition-colors"
                        >
                            <span className="material-symbols-outlined text-sm">{showSolution ? 'visibility_off' : 'visibility'}</span>
                            {showSolution ? "Masquer la solution" : "Afficher la solution"}
                        </button>

                        {showSolution && (
                            <div className="mt-6 pt-6 border-t border-outline-variant">
                                <ReactMarkdown
                                    remarkPlugins={[remarkMath, remarkGfm]}
                                    rehypePlugins={[rehypeKatex]}
                                >
                                    {result.solution}
                                </ReactMarkdown>
                            </div>
                        )}
                    </div>
                </div>
            )}
        </main>
    );
}
