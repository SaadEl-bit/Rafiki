'use client';
import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';

export default function PageContent() {
    const [subjects, setSubjects] = useState([]);
    const [activeSubject, setActiveSubject] = useState(null);
    const [search, setSearch] = useState("");
    const [expandedDomains, setExpandedDomains] = useState({});
    const [expandedSubs, setExpandedSubs] = useState({});
    const [loading, setLoading] = useState(true);
    const router = useRouter();

    useEffect(() => {
        fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/cadre`)
            .then(res => res.json())
            .then(data => {
                setSubjects(data);
                if (data.length > 0) setActiveSubject(data[0].subject_key);
            })
            .catch(() => setSubjects([]))
            .finally(() => setLoading(false));
    }, []);

    const current = subjects.find(s => s.subject_key === activeSubject);

    const toggleDomain = (idx) => {
        setExpandedDomains(prev => ({ ...prev, [idx]: !prev[idx] }));
    };

    const toggleSub = (idx) => {
        setExpandedSubs(prev => ({ ...prev, [idx]: !prev[idx] }));
    };

    const askAI = (objective) => {
        const text = objective.code
            ? `Explique l'objectif ${objective.code} du programme : ${objective.text}`
            : objective.text;
        const subjectName = current?.subject || "";
        router.push(`/chat?q=${encodeURIComponent(text)}&subject=${encodeURIComponent(subjectName)}`);
    };

    const filterObjectives = (objs) => {
        if (!search.trim()) return objs;
        const q = search.toLowerCase();
        return objs.filter(o =>
            o.text.toLowerCase().includes(q) ||
            (o.code && o.code.toLowerCase().includes(q))
        );
    };

    return (
        <main className="flex-grow h-full overflow-y-auto w-full max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop py-8 md:py-10 gap-gutter flex flex-col">
            <header className="mb-6">
                <h1 className="font-display-lg-mobile md:font-display-lg text-display-lg-mobile md:text-display-lg text-on-surface mb-2">
                    Cadre Référenciel <span className="font-arabic-brand text-primary opacity-80 text-xl ml-2 inline-block align-middle">الإطار المرجعي</span>
                </h1>
                <p className="font-body-lg text-body-lg text-on-surface-variant">
                    Programme officiel du 2ème Bac — objectifs d'apprentissage par matière.
                </p>
            </header>

            {/* Search */}
            <div className="mb-6">
                <input
                    type="text"
                    value={search}
                    onChange={(e) => setSearch(e.target.value)}
                    placeholder="Rechercher un objectif par mot-clé ou code..."
                    className="w-full rounded-xl border border-outline-variant bg-surface-container-low text-on-surface placeholder:text-on-surface-variant px-5 py-3.5 focus:ring-2 focus:ring-primary-fixed-dim focus:border-transparent outline-none transition-all"
                />
            </div>

            {/* Subject Tabs */}
            <div className="flex flex-wrap gap-3 mb-6">
                {subjects.map(s => (
                    <button
                        key={s.subject_key}
                        onClick={() => { setActiveSubject(s.subject_key); setSearch(""); }}
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

            {!loading && current && current.type === "objectives" && (
                <div className="space-y-4">
                    {current.domains.map((domain, di) => {
                        const filteredSubs = domain.sub_domains.map(sub => ({
                            ...sub,
                            objectives: filterObjectives(sub.objectives),
                        })).filter(sub => sub.objectives.length > 0 || !search);
                        if (filteredSubs.length === 0 && search) return null;

                        return (
                            <div key={di} className="bg-surface rounded-2xl border border-outline-variant overflow-hidden">
                                <button
                                    onClick={() => toggleDomain(di)}
                                    className="w-full flex items-center justify-between p-5 hover:bg-surface-container-low transition-colors text-left"
                                >
                                    <h2 className="font-headline-md text-headline-md text-on-surface">{domain.name}</h2>
                                    <span className="material-symbols-outlined text-on-surface-variant transition-transform"
                                        style={{ transform: expandedDomains[di] ? 'rotate(180deg)' : 'rotate(0deg)' }}>
                                        expand_more
                                    </span>
                                </button>

                                {expandedDomains[di] && (
                                    <div className="px-5 pb-5 space-y-3">
                                        {filteredSubs.map((sub, si) => (
                                            <div key={si} className="bg-surface-container-low rounded-xl overflow-hidden">
                                                <button
                                                    onClick={() => toggleSub(`${di}-${si}`)}
                                                    className="w-full flex items-center justify-between p-4 hover:bg-surface-container transition-colors text-left"
                                                >
                                                    <h3 className="font-label-lg text-label-lg text-on-surface font-semibold">{sub.name}</h3>
                                                    <span className="material-symbols-outlined text-on-surface-variant transition-transform text-sm"
                                                        style={{ transform: expandedSubs[`${di}-${si}`] ? 'rotate(180deg)' : 'rotate(0deg)' }}>
                                                        expand_more
                                                    </span>
                                                </button>

                                                {expandedSubs[`${di}-${si}`] && (
                                                    <div className="px-4 pb-4 space-y-2">
                                                        {sub.objectives.map((obj, oi) => (
                                                            <div key={oi}
                                                                className="flex items-start gap-3 p-3.5 rounded-xl bg-surface hover:bg-surface-container-high transition-colors group"
                                                            >
                                                                <div className="flex-1 min-w-0">
                                                                    {obj.code && (
                                                                        <span className="inline-block bg-primary-container text-on-primary-container text-xs font-bold px-2 py-0.5 rounded-md mr-2 mb-1">
                                                                            {obj.code}
                                                                        </span>
                                                                    )}
                                                                    <span className="text-sm text-on-surface">{obj.text}</span>
                                                                </div>
                                                                <button
                                                                    onClick={() => askAI(obj)}
                                                                    className="shrink-0 opacity-0 group-hover:opacity-100 transition-opacity p-2 rounded-lg bg-primary-container text-on-primary-container hover:bg-primary-fixed"
                                                                    title="Demander à Rafiki"
                                                                >
                                                                    <span className="material-symbols-outlined text-sm">auto_awesome</span>
                                                                </button>
                                                            </div>
                                                        ))}
                                                    </div>
                                                )}
                                            </div>
                                        ))}
                                    </div>
                                )}
                            </div>
                        );
                    })}
                </div>
            )}

            {!loading && current && current.type === "document" && (
                <div className="bg-surface rounded-2xl border border-outline-variant p-6">
                    {current.domains.map((domain, di) => (
                        <div key={di} className="mb-6">
                            <h2 className="font-headline-md text-headline-md text-on-surface mb-3">{domain.name}</h2>
                            {domain.sub_domains.map((sub, si) => (
                                <div key={si} className="ml-4 mb-4">
                                    <h3 className="font-label-lg text-label-lg text-on-surface font-semibold mb-2">{sub.name}</h3>
                                    {sub.objectives.map((obj, oi) => (
                                        <p key={oi} className="text-sm text-on-surface-variant ml-4 mb-1">{obj.text}</p>
                                    ))}
                                </div>
                            ))}
                        </div>
                    ))}
                    {current.sections && current.sections.length > 0 && (
                        <div className="text-sm text-on-surface-variant whitespace-pre-wrap leading-relaxed">
                            {current.sections.map((s, i) => (
                                <p key={i} className="mb-2">{s.content}</p>
                            ))}
                        </div>
                    )}
                </div>
            )}

            {!loading && !current && (
                <div className="text-center py-20 text-on-surface-variant">
                    <p>Aucune donnée disponible.</p>
                </div>
            )}
        </main>
    );
}
