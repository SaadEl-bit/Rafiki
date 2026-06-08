import Link from 'next/link';

export default function PageContent() {
    return (
        <>
<main className="flex-1 flex flex-col h-full overflow-y-auto pt-6 px-gutter pb-margin-desktop max-w-container-max w-full">
{/*  Page Header  */}
<div className="mb-8">
<h1 className="font-headline-lg text-headline-lg text-on-surface mb-2">Cadre Référenciel</h1>
<p className="font-body-lg text-body-lg text-on-surface-variant">Official 2nd Bac Curriculum &amp; Exam Weighting</p>
</div>
{/*  Subject Selector  */}
<div className="flex gap-4 mb-8 overflow-x-auto pb-2 scrollbar-hide">
<button className="px-6 py-3 rounded-full bg-primary-container text-on-primary-container font-label-md text-label-md shadow-sm transition-transform hover:scale-105 whitespace-nowrap">
                Mathématiques
            </button>
<button className="px-6 py-3 rounded-full bg-surface-container-highest text-on-surface-variant hover:bg-surface-variant font-label-md text-label-md transition-colors whitespace-nowrap">
                Physique-Chimie
            </button>
<button className="px-6 py-3 rounded-full bg-surface-container-highest text-on-surface-variant hover:bg-surface-variant font-label-md text-label-md transition-colors whitespace-nowrap">
                English
            </button>
</div>
{/*  Bento Grid Layout  */}
<div className="grid grid-cols-1 lg:grid-cols-12 gap-gutter">
{/*  Left Column: Curriculum Breakdown (Accordions)  */}
<div className="lg:col-span-8 flex flex-col gap-6">
{/*  Domain 1: Analyse  */}
<div className="bg-surface-container-lowest rounded-[24px] ambient-shadow overflow-hidden group">
<div className="h-2 w-full bg-primary-container"></div>
<div className="p-card-padding">
<div className="flex justify-between items-center cursor-pointer">
<div className="flex items-center gap-4">
<div className="w-12 h-12 rounded-xl bg-primary-container/20 flex items-center justify-center text-primary">
<span className="material-symbols-outlined">function</span>
</div>
<div>
<h3 className="font-headline-sm text-headline-sm text-on-surface">Analyse</h3>
<p className="font-body-sm text-body-sm text-on-surface-variant mt-1">Limites, Continuité, Dérivation, Étude de fonctions</p>
</div>
</div>
<span className="material-symbols-outlined text-on-surface-variant transition-transform duration-300">expand_more</span>
</div>
<div className="hidden mt-6 pt-6 border-t border-surface-container-high">
<ul className="space-y-4">
<li className="flex items-start gap-3">
<span className="material-symbols-outlined text-primary-container text-[20px] mt-0.5">check_circle</span>
<div>
<h4 className="font-label-md text-label-md text-on-surface">Limites et Continuité</h4>
<p className="font-body-sm text-body-sm text-on-surface-variant">Calcul de limites, théorèmes de valeurs intermédiaires.</p>
</div>
</li>
<li className="flex items-start gap-3">
<span className="material-symbols-outlined text-primary-container text-[20px] mt-0.5">check_circle</span>
<div>
<h4 className="font-label-md text-label-md text-on-surface">Dérivation et Étude de Fonctions</h4>
<p className="font-body-sm text-body-sm text-on-surface-variant">Fonctions logarithmiques, exponentielles et rationnelles.</p>
</div>
</li>
<li className="flex items-start gap-3">
<span className="material-symbols-outlined text-primary-container text-[20px] mt-0.5">check_circle</span>
<div>
<h4 className="font-label-md text-label-md text-on-surface">Calcul Intégral</h4>
<p className="font-body-sm text-body-sm text-on-surface-variant">Intégration par parties, calcul d&apos;aires et de volumes.</p>
</div>
</li>
</ul>
</div>
</div>
</div>
{/*  Domain 2: Algèbre  */}
<div className="bg-surface-container-lowest rounded-[24px] ambient-shadow overflow-hidden group">
<div className="h-2 w-full bg-secondary-container"></div>
<div className="p-card-padding">
<div className="flex justify-between items-center cursor-pointer">
<div className="flex items-center gap-4">
<div className="w-12 h-12 rounded-xl bg-secondary-container/20 flex items-center justify-center text-secondary">
<span className="material-symbols-outlined">calculate</span>
</div>
<div>
<h3 className="font-headline-sm text-headline-sm text-on-surface">Algèbre</h3>
<p className="font-body-sm text-body-sm text-on-surface-variant mt-1">Nombres Complexes, Suites Numériques</p>
</div>
</div>
<span className="material-symbols-outlined text-on-surface-variant transition-transform duration-300">expand_more</span>
</div>
<div className="hidden mt-6 pt-6 border-t border-surface-container-high">
<ul className="space-y-4">
<li className="flex items-start gap-3">
<span className="material-symbols-outlined text-secondary-container text-[20px] mt-0.5">check_circle</span>
<div>
<h4 className="font-label-md text-label-md text-on-surface">Nombres Complexes</h4>
<p className="font-body-sm text-body-sm text-on-surface-variant">Forme algébrique, trigonométrique, géométrie complexe.</p>
</div>
</li>
<li className="flex items-start gap-3">
<span className="material-symbols-outlined text-secondary-container text-[20px] mt-0.5">check_circle</span>
<div>
<h4 className="font-label-md text-label-md text-on-surface">Suites Numériques</h4>
<p className="font-body-sm text-body-sm text-on-surface-variant">Récurrence, convergence, suites arithmétiques et géométriques.</p>
</div>
</li>
</ul>
</div>
</div>
</div>
{/*  Domain 3: Géométrie  */}
<div className="bg-surface-container-lowest rounded-[24px] ambient-shadow overflow-hidden group">
<div className="h-2 w-full bg-tertiary-container"></div>
<div className="p-card-padding">
<div className="flex justify-between items-center cursor-pointer">
<div className="flex items-center gap-4">
<div className="w-12 h-12 rounded-xl bg-tertiary-container/20 flex items-center justify-center text-tertiary">
<span className="material-symbols-outlined">architecture</span>
</div>
<div>
<h3 className="font-headline-sm text-headline-sm text-on-surface">Géométrie</h3>
<p className="font-body-sm text-body-sm text-on-surface-variant mt-1">Produit Scalaire, Géométrie dans l&apos;espace</p>
</div>
</div>
<span className="material-symbols-outlined text-on-surface-variant transition-transform duration-300">expand_more</span>
</div>
<div className="hidden mt-6 pt-6 border-t border-surface-container-high">
<ul className="space-y-4">
<li className="flex items-start gap-3">
<span className="material-symbols-outlined text-tertiary-container text-[20px] mt-0.5">check_circle</span>
<div>
<h4 className="font-label-md text-label-md text-on-surface">Géométrie Analytique Spatiale</h4>
<p className="font-body-sm text-body-sm text-on-surface-variant">Équations de plans, droites, distances dans l&apos;espace.</p>
</div>
</li>
</ul>
</div>
</div>
</div>
</div>
{/*  Right Column: Key Stats Panel  */}
<div className="lg:col-span-4 flex flex-col gap-6">
{/*  Quick Stats Card  */}
<div className="bg-surface-container-lowest rounded-[24px] p-card-padding ambient-shadow">
<h3 className="font-headline-md text-headline-md text-on-surface mb-6">Exam Details</h3>
<div className="space-y-6">
<div className="flex items-center gap-4 bg-surface-container-low p-4 rounded-xl">
<div className="w-10 h-10 rounded-full bg-primary-container/20 flex items-center justify-center text-primary">
<span className="material-symbols-outlined">grade</span>
</div>
<div>
<p className="font-label-sm text-label-sm text-on-surface-variant uppercase tracking-wider">Coefficient</p>
<p className="font-headline-sm text-headline-sm text-on-surface font-bold">7</p>
</div>
</div>
<div className="flex items-center gap-4 bg-surface-container-low p-4 rounded-xl">
<div className="w-10 h-10 rounded-full bg-secondary-container/20 flex items-center justify-center text-secondary">
<span className="material-symbols-outlined">timer</span>
</div>
<div>
<p className="font-label-sm text-label-sm text-on-surface-variant uppercase tracking-wider">Duration</p>
<p className="font-headline-sm text-headline-sm text-on-surface font-bold">4 Hours</p>
</div>
</div>
</div>
</div>
{/*  Weighting Breakdown Card  */}
<div className="bg-surface-container-lowest rounded-[24px] p-card-padding ambient-shadow">
<h3 className="font-headline-md text-headline-md text-on-surface mb-6">Weighting by Domain</h3>
<div className="space-y-4">
{/*  Analyze Bar  */}
<div>
<div className="flex justify-between items-center mb-2">
<span className="font-label-md text-label-md text-on-surface">Analyse</span>
<span className="font-label-md text-label-md text-primary font-bold">50%</span>
</div>
<div className="w-full bg-surface-container-highest rounded-full h-2.5">
<div className="bg-primary-container h-2.5 rounded-full" style={{"width":"50%"}}></div>
</div>
</div>
{/*  Algebra Bar  */}
<div>
<div className="flex justify-between items-center mb-2">
<span className="font-label-md text-label-md text-on-surface">Algèbre</span>
<span className="font-label-md text-label-md text-secondary font-bold">25%</span>
</div>
<div className="w-full bg-surface-container-highest rounded-full h-2.5">
<div className="bg-secondary-container h-2.5 rounded-full" style={{"width":"25%"}}></div>
</div>
</div>
{/*  Geometry Bar  */}
<div>
<div className="flex justify-between items-center mb-2">
<span className="font-label-md text-label-md text-on-surface">Géométrie</span>
<span className="font-label-md text-label-md text-tertiary font-bold">25%</span>
</div>
<div className="w-full bg-surface-container-highest rounded-full h-2.5">
<div className="bg-tertiary-container h-2.5 rounded-full" style={{"width":"25%"}}></div>
</div>
</div>
</div>
<div className="mt-6 pt-6 border-t border-surface-container-high text-center">
<p className="font-body-sm text-body-sm text-on-surface-variant italic">Based on Ministry of Education 2024 directives.</p>
</div>
</div>
</div>
</div>
</main>
        </>
    );
}
