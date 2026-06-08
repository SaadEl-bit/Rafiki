import Link from 'next/link';

export default function PageContent() {
    return (
        <>
<main className="flex-1 h-full overflow-y-auto p-margin-mobile md:p-margin-desktop max-w-container-max mx-auto w-full">
<div className="mb-8">
<h1 className="font-headline-lg text-headline-lg text-on-surface mb-2">Create Custom Mock Exam</h1>
<p className="font-body-md text-body-md text-on-surface-variant">Configure parameters to generate a targeted practice session.</p>
</div>
{/*  Bento Grid Layout  */}
<div className="grid grid-cols-1 lg:grid-cols-12 gap-gutter">
{/*  Left Column: Configuration  */}
<div className="lg:col-span-7 space-y-gutter">
{/*  Subject & Chapters Card  */}
<div className="bg-surface-container-lowest rounded-xl p-card-padding shadow-sm border border-outline-variant/30">
<h3 className="font-headline-sm text-headline-sm text-on-surface mb-6 flex items-center gap-2">
<span className="material-symbols-outlined text-primary">menu_book</span>
                            Curriculum Scope
                        </h3>
<div className="space-y-6">
<div>
<label className="block font-label-md text-label-md text-on-surface-variant mb-2">Subject Context</label>
<select className="w-full bg-surface-container-low border border-outline-variant rounded-lg px-4 py-3 font-body-md text-body-md text-on-surface focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent">
<option>Mathématiques (Current)</option>
<option>Physique-Chimie</option>
<option>English</option>
</select>
</div>
<div>
<label className="block font-label-md text-label-md text-on-surface-variant mb-3">Select Chapters</label>
<div className="flex flex-wrap gap-2">
<button className="px-4 py-2 rounded-full border border-primary bg-primary-container/10 text-primary font-label-sm text-label-sm hover:bg-primary-container/20 transition-colors">
                                        Calculus Basics
                                    </button>
<button className="px-4 py-2 rounded-full border border-outline-variant bg-surface text-on-surface-variant font-label-sm text-label-sm hover:bg-surface-container-low transition-colors">
                                        Algebraic Structures
                                    </button>
<button className="px-4 py-2 rounded-full border border-primary bg-primary-container/10 text-primary font-label-sm text-label-sm hover:bg-primary-container/20 transition-colors">
                                        Geometry &amp; Vectors
                                    </button>
<button className="px-4 py-2 rounded-full border border-outline-variant bg-surface text-on-surface-variant font-label-sm text-label-sm hover:bg-surface-container-low transition-colors">
                                        Probability
                                    </button>
</div>
</div>
</div>
</div>
{/*  Difficulty Card  */}
<div className="bg-surface-container-lowest rounded-xl p-card-padding shadow-sm border border-outline-variant/30">
<h3 className="font-headline-sm text-headline-sm text-on-surface mb-6 flex items-center gap-2">
<span className="material-symbols-outlined text-secondary">trending_up</span>
                            Difficulty Level
                        </h3>
<div className="flex flex-col sm:flex-row gap-4">
<label className="flex-1 cursor-pointer">
<input className="peer sr-only" name="difficulty" type="radio" value="easy" />
<div className="p-4 rounded-xl border border-outline-variant peer-defaultChecked:border-secondary peer-defaultChecked:bg-secondary-container/20 transition-all text-center">
<span className="block font-label-md text-label-md text-on-surface mb-1">Foundational</span>
<span className="block font-label-sm text-label-sm text-on-surface-variant">Core concepts &amp; direct application</span>
</div>
</label>
<label className="flex-1 cursor-pointer">
<input defaultChecked="" className="peer sr-only" name="difficulty" type="radio" value="medium" />
<div className="p-4 rounded-xl border border-outline-variant peer-defaultChecked:border-secondary peer-defaultChecked:bg-secondary-container/20 transition-all text-center">
<span className="block font-label-md text-label-md text-on-surface mb-1">Standard</span>
<span className="block font-label-sm text-label-sm text-on-surface-variant">Typical Baccalaureate level</span>
</div>
</label>
<label className="flex-1 cursor-pointer">
<input className="peer sr-only" name="difficulty" type="radio" value="hard" />
<div className="p-4 rounded-xl border border-outline-variant peer-defaultChecked:border-secondary peer-defaultChecked:bg-secondary-container/20 transition-all text-center">
<span className="block font-label-md text-label-md text-on-surface mb-1">Advanced</span>
<span className="block font-label-sm text-label-sm text-on-surface-variant">Complex synthesis problems</span>
</div>
</label>
</div>
</div>
{/*  Action Area  */}
<div className="pt-4">
<button className="w-full bg-primary-container text-on-primary-container font-headline-sm text-headline-sm py-4 rounded-xl shadow-sm hover:opacity-90 transition-opacity flex justify-center items-center gap-2">
<span className="material-symbols-outlined">generating_tokens</span>
                            Generate Mock Exam
                        </button>
</div>
</div>
{/*  Right Column: Live Preview  */}
<div className="lg:col-span-5 h-full">
<div className="bg-surface-container-high rounded-xl p-card-padding shadow-inner h-full border border-surface-dim flex flex-col">
<div className="flex justify-between items-center mb-6 border-b border-outline-variant/50 pb-4">
<h3 className="font-headline-sm text-headline-sm text-on-surface">Blueprint Preview</h3>
<div className="flex items-center gap-1 text-on-surface-variant bg-surface-container-lowest px-3 py-1 rounded-full text-label-sm font-label-sm shadow-sm">
<span className="material-symbols-outlined text-[16px]">timer</span>
                                Est: 120 mins
                            </div>
</div>
<div className="flex-1 space-y-4 overflow-y-auto">
{/*  Preview Section 1  */}
<div className="bg-surface-container-lowest p-4 rounded-lg shadow-sm border border-outline-variant/30 relative overflow-hidden">
<div className="absolute left-0 top-0 bottom-0 w-1 bg-primary"></div>
<div className="flex justify-between items-start mb-2 pl-2">
<h4 className="font-label-md text-label-md text-on-surface">Part I: Calculus Fundamentals</h4>
<span className="text-label-sm font-label-sm text-tertiary">4 Exercises</span>
</div>
<p className="font-body-sm text-body-sm text-on-surface-variant pl-2">Focus on limits, derivatives, and basic integration techniques.</p>
</div>
{/*  Preview Section 2  */}
<div className="bg-surface-container-lowest p-4 rounded-lg shadow-sm border border-outline-variant/30 relative overflow-hidden">
<div className="absolute left-0 top-0 bottom-0 w-1 bg-secondary"></div>
<div className="flex justify-between items-start mb-2 pl-2">
<h4 className="font-label-md text-label-md text-on-surface">Part II: Analytic Geometry</h4>
<span className="text-label-sm font-label-sm text-tertiary">2 Complex Problems</span>
</div>
<p className="font-body-sm text-body-sm text-on-surface-variant pl-2">Synthesis problems involving spatial vectors and coordinate geometry.</p>
</div>
{/*  Placeholder empty state  */}
<div className="border-2 border-dashed border-outline-variant/50 rounded-lg p-6 text-center text-on-surface-variant flex flex-col items-center justify-center mt-4 opacity-50">
<span className="material-symbols-outlined text-[32px] mb-2">add_circle</span>
<p className="font-label-sm text-label-sm">Select more chapters to populate</p>
</div>
</div>
</div>
</div>
</div>
</main>
        </>
    );
}
