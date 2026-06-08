import Link from 'next/link';

export default function PageContent() {
    return (
        <>

<main className="flex-1 flex flex-col h-full overflow-y-auto w-full relative">
<div className="p-margin-mobile md:p-margin-desktop max-w-container-max mx-auto w-full pb-24 mt-4">
{/*  Page Header  */}
<header className="mb-8">
<h2 className="font-headline-lg text-headline-lg text-on-surface mb-2">Chapter Summaries</h2>
<p className="font-body-md text-body-md text-on-surface-variant max-w-2xl">Select a chapter from your current subject to instantly generate a concise, focused study summary. Or, upload your own notes for custom generation.</p>
</header>
{/*  Bento Grid Layout  */}
<div className="grid grid-cols-1 lg:grid-cols-12 gap-gutter">
{/*  Main Flow: Select & Generate (Left/Main Column)  */}
<div className="lg:col-span-8 flex flex-col gap-gutter">
{/*  Subject Context Header Card  */}
<div className="bg-primary-container text-on-primary-container rounded-2xl p-card-padding flex items-center justify-between shadow-sm relative overflow-hidden group">
<div className="relative z-10">
<span className="font-label-sm text-label-sm uppercase tracking-wider opacity-80 block mb-1">Current Subject</span>
<h3 className="font-headline-md text-headline-md flex items-center gap-3">
<span className="material-symbols-outlined icon-fill text-3xl">functions</span>
                                Mathématiques
                            </h3>
</div>
{/*  Decorative background pattern (CSS only)  */}
<div className="absolute right-0 top-0 bottom-0 w-1/2 bg-gradient-to-l from-white/10 to-transparent pointer-events-none rounded-r-2xl"></div>
<span className="material-symbols-outlined text-8xl absolute -right-4 -bottom-6 opacity-10 pointer-events-none transform -rotate-12 group-hover:rotate-0 transition-transform duration-500">calculate</span>
</div>
{/*  Chapter Selection Card  */}
<div className="bg-surface-container-lowest rounded-2xl shadow-sm border border-surface-container-low flex-1 flex flex-col min-h-[400px]">
<div className="p-card-padding border-b border-surface-container flex justify-between items-center">
<div>
<h4 className="font-headline-sm text-headline-sm text-on-surface">Select a Chapter</h4>
<p className="font-body-sm text-body-sm text-on-surface-variant">Choose one topic to summarize.</p>
</div>
<div className="relative">
<span className="material-symbols-outlined absolute left-3 top-1/2 transform -translate-y-1/2 text-on-surface-variant">search</span>
<input className="pl-10 pr-4 py-2 bg-surface-container-low border-none rounded-full font-body-sm text-body-sm text-on-surface focus:ring-2 focus:ring-primary outline-none w-48 transition-all" placeholder="Search chapters..." type="text" />
</div>
</div>
{/*  Scrollable Chapter List  */}
<div className="flex-1 overflow-y-auto custom-scrollbar p-2">
{/*  Selected Item  */}
<label className="flex items-center p-4 m-2 rounded-xl bg-surface-bright border border-primary-fixed cursor-pointer transition-all hover:shadow-sm">
<div className="w-10 h-10 rounded-full bg-primary-container text-on-primary-container flex items-center justify-center mr-4 shrink-0">
<span className="material-symbols-outlined icon-fill">analytics</span>
</div>
<div className="flex-1">
<h5 className="font-label-md text-label-md text-on-surface">Étude de Fonctions</h5>
<p className="font-body-sm text-body-sm text-on-surface-variant">Derivatives, limits, and variations.</p>
</div>
<input defaultChecked="" className="w-5 h-5 text-primary border-outline focus:ring-primary bg-surface-container-lowest ml-4 cursor-pointer" name="chapter" type="radio" />
</label>
{/*  Unselected Items  */}
<label className="flex items-center p-4 m-2 rounded-xl hover:bg-surface-container cursor-pointer transition-all border border-transparent">
<div className="w-10 h-10 rounded-full bg-surface-container-high text-on-surface-variant flex items-center justify-center mr-4 shrink-0">
<span className="material-symbols-outlined">data_object</span>
</div>
<div className="flex-1">
<h5 className="font-label-md text-label-md text-on-surface">Nombres Complexes</h5>
<p className="font-body-sm text-body-sm text-on-surface-variant">Algebraic and geometric forms.</p>
</div>
<input className="w-5 h-5 text-primary border-outline focus:ring-primary bg-surface-container-lowest ml-4 cursor-pointer" name="chapter" type="radio" />
</label>
<label className="flex items-center p-4 m-2 rounded-xl hover:bg-surface-container cursor-pointer transition-all border border-transparent">
<div className="w-10 h-10 rounded-full bg-surface-container-high text-on-surface-variant flex items-center justify-center mr-4 shrink-0">
<span className="material-symbols-outlined">trending_up</span>
</div>
<div className="flex-1">
<h5 className="font-label-md text-label-md text-on-surface">Suites Numériques</h5>
<p className="font-body-sm text-body-sm text-on-surface-variant">Arithmetic and geometric sequences.</p>
</div>
<input className="w-5 h-5 text-primary border-outline focus:ring-primary bg-surface-container-lowest ml-4 cursor-pointer" name="chapter" type="radio" />
</label>
<label className="flex items-center p-4 m-2 rounded-xl hover:bg-surface-container cursor-pointer transition-all border border-transparent opacity-60">
<div className="w-10 h-10 rounded-full bg-surface-container-high text-on-surface-variant flex items-center justify-center mr-4 shrink-0">
<span className="material-symbols-outlined">functions</span>
</div>
<div className="flex-1">
<h5 className="font-label-md text-label-md text-on-surface">Calcul Intégral</h5>
<p className="font-body-sm text-body-sm text-on-surface-variant">Area computation and primitives.</p>
</div>
<input className="w-5 h-5 text-outline border-outline bg-surface-container-low ml-4 cursor-not-allowed" disabled="" name="chapter" type="radio" />
<span className="text-xs bg-surface-container-high px-2 py-1 rounded text-on-surface-variant ml-2">Locked</span>
</label>
</div>
{/*  Action Footer  */}

</div>
</div>
{/*  Custom Upload (Right Column)  */}
<div className="lg:col-span-4 h-full">
<div className="bg-surface-container-lowest rounded-2xl shadow-sm border border-surface-container-low p-card-padding h-full flex flex-col relative overflow-hidden group">
{/*  Coming Soon Tag  */}
<div className="absolute top-6 right-6 bg-secondary-container text-on-secondary-container font-label-sm text-label-sm px-3 py-1 rounded-full flex items-center gap-1 z-10">
<span className="material-symbols-outlined text-[14px]">science</span>
                            Beta
                        </div>
<div className="mb-6">
<div className="w-12 h-12 rounded-xl bg-tertiary-container text-on-tertiary-container flex items-center justify-center mb-4">
<span className="material-symbols-outlined icon-fill">upload_file</span>
</div>
<h4 className="font-headline-sm text-headline-sm text-on-surface mb-1">Custom Notes</h4>
<p className="font-body-sm text-body-sm text-on-surface-variant">Upload your own handwritten notes or PDF slides to generate a personalized summary.</p>
</div>
{/*  Drag & Drop Zone  */}
<div className="flex-1 min-h-[200px] border-2 border-dashed border-outline-variant hover:border-primary bg-surface-container-low hover:bg-surface-bright rounded-xl flex flex-col items-center justify-center p-6 text-center transition-colors cursor-pointer mb-6 group-hover:border-primary/50">
<span className="material-symbols-outlined text-4xl text-tertiary mb-3">cloud_upload</span>
<p className="font-label-md text-label-md text-on-surface mb-1">Drag &amp; drop files here</p>
<p className="font-body-sm text-body-sm text-on-surface-variant">or click to browse</p>
<div className="flex gap-2 mt-4">
<span className="bg-surface-container-high text-on-surface-variant font-label-sm text-[10px] px-2 py-1 rounded">PDF</span>
<span className="bg-surface-container-high text-on-surface-variant font-label-sm text-[10px] px-2 py-1 rounded">JPG/PNG</span>
<span className="bg-surface-container-high text-on-surface-variant font-label-sm text-[10px] px-2 py-1 rounded">Max 10MB</span>
</div>
</div>
<button className="w-full bg-surface-container-highest hover:bg-surface-dim text-on-surface font-label-md text-label-md py-3 rounded-full transition-colors flex items-center justify-center gap-2" disabled="">
<span className="material-symbols-outlined">summarize</span>
                            Summarize Upload
                        </button>
</div>
</div>
</div>
</div>
</main>
        </>
    );
}
