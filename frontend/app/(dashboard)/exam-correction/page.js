import Link from 'next/link';

export default function PageContent() {
    return (
        <>
<main className="flex-1 flex flex-col h-full overflow-y-auto w-full relative">

{/*  Page Content  */}
<div className="px-margin-mobile md:px-margin-desktop py-8 max-w-container-max mx-auto w-full flex flex-col gap-gutter">
{/*  Header Section  */}
<div className="flex flex-col gap-2 mb-4">
<h2 className="font-headline-lg text-headline-lg text-on-surface">Exam Correction</h2>
<p className="font-body-md text-body-md text-on-surface-variant max-w-2xl">Upload your full exam paper to receive an in-depth analysis, professor-grade feedback, and a detailed breakdown of your marks.</p>
</div>
{/*  Upload Zone  */}
<div className="bg-surface-container-lowest card-shadow rounded-[24px] border-2 border-dashed border-outline-variant p-card-padding flex flex-col items-center justify-center text-center gap-4 cursor-pointer transition-all duration-300 hover:border-primary hover:bg-surface-bright min-h-[280px]" id="drop-zone">
<div className="w-16 h-16 rounded-full bg-surface-container flex items-center justify-center text-primary mb-2">
<span className="material-symbols-outlined text-4xl">upload_file</span>
</div>
<div>
<h3 className="font-headline-sm text-headline-sm text-on-surface mb-1">Drag &amp; Drop your exam pages here</h3>
<p className="font-body-sm text-body-sm text-on-surface-variant">Supported formats: PDF, JPG, PNG (Max 20MB / up to 10 pages)</p>
</div>
<button className="mt-4 bg-primary text-on-primary font-label-md text-label-md py-3 px-8 rounded-full shadow-sm hover:bg-surface-tint hover:shadow-md transition-all">
                    Browse Files
                </button>
</div>
{/*  Analysis Status (Mocked Active State)  */}
<div className="bg-primary-container text-on-primary-container rounded-[24px] p-card-padding flex flex-col md:flex-row items-center justify-between gap-6 card-shadow mt-4">
<div className="flex items-center gap-4 w-full md:w-auto">
<div className="animate-spin text-on-primary-container">
<span className="material-symbols-outlined text-3xl">hourglass_empty</span>
</div>
<div>
<h4 className="font-headline-sm text-headline-sm">Analysing Exam...</h4>
<p className="font-body-sm text-body-sm opacity-90">Processing Page 3 of 5. Verifying mathematical proofs.</p>
</div>
</div>
<div className="w-full md:w-64 bg-surface-container/30 rounded-full h-2 overflow-hidden">
<div className="bg-on-primary-container h-full rounded-full" style={{"width":"60%"}}></div>
</div>
</div>
<hr className="border-outline-variant/30 my-4" />
{/*  Results Section (Bento Layout)  */}
<div className="grid grid-cols-1 md:grid-cols-12 gap-gutter">
{/*  Left Column: Overview & Feedback  */}
<div className="md:col-span-4 flex flex-col gap-gutter">
{/*  Overall Score Card  */}
<div className="bg-surface-container-lowest card-shadow rounded-[24px] p-card-padding flex flex-col items-center justify-center text-center">
<h3 className="font-headline-sm text-headline-sm text-on-surface mb-6 w-full text-left">Overall Score</h3>
<div className="relative w-40 h-40 rounded-full border-8 border-surface-container flex items-center justify-center mb-4">
{/*  SVG Gauge Simulation  */}
<svg className="absolute top-0 left-0 w-full h-full -rotate-90" viewBox="0 0 100 100">
<circle className="transition-all duration-1000" cx="50" cy="50" fill="none" r="46" stroke="#5cb399" strokeDasharray="289" strokeDashoffset="57" strokeWidth="8"></circle>
</svg>
<div className="flex flex-col items-center">
<span className="font-headline-xl text-headline-xl text-primary">16</span>
<span className="font-label-sm text-label-sm text-on-surface-variant border-t border-outline-variant pt-1 w-8">20</span>
</div>
</div>
<p className="font-label-md text-label-md text-primary bg-primary-container/20 px-4 py-1.5 rounded-full">
                            Excellent Work
                        </p>
</div>
{/*  Professor Feedback Card  */}
<div className="bg-surface-container-lowest card-shadow rounded-[24px] p-card-padding relative overflow-hidden">
{/*  Decorative Quote Icon  */}
<div className="absolute -top-4 -left-4 text-tertiary-container/30">
<span className="material-symbols-outlined text-8xl fill">format_quote</span>
</div>
<div className="relative z-10">
<div className="flex items-center gap-3 mb-4">
<div className="w-10 h-10 rounded-full bg-secondary-container flex items-center justify-center text-on-secondary-container">
<span className="material-symbols-outlined">school</span>
</div>
<h3 className="font-headline-sm text-headline-sm text-on-surface">Professor's Note</h3>
</div>
<p className="font-body-md text-body-md text-on-surface-variant italic mb-4">
                                "Solid understanding of the core algebraic concepts. You structured your proofs beautifully in Part A. However, pay closer attention to sign errors in integration problems (Part C) to secure those final points."
                            </p>
<div className="flex gap-2 flex-wrap">
<span className="bg-surface-container px-3 py-1 rounded-full font-label-sm text-label-sm text-on-surface">Rigorous Logic</span>
<span className="bg-error-container text-on-error-container px-3 py-1 rounded-full font-label-sm text-label-sm">Calculation Errors</span>
</div>
</div>
</div>
</div>
{/*  Right Column: Detailed Breakdown  */}
<div className="md:col-span-8 flex flex-col gap-gutter">
<div className="bg-surface-container-lowest card-shadow rounded-[24px] p-card-padding h-full">
<div className="flex justify-between items-center mb-6">
<h3 className="font-headline-sm text-headline-sm text-on-surface">Detailed Breakdown</h3>
<button className="text-primary hover:text-surface-tint font-label-md text-label-md flex items-center gap-1 transition-colors">
<span className="material-symbols-outlined text-sm">download</span> Export PDF
                            </button>
</div>
{/*  Question List  */}
<div className="flex flex-col gap-4">
{/*  Q1  */}
<div className="group border border-outline-variant/50 rounded-xl p-4 hover:border-primary/50 hover:bg-surface-bright transition-all cursor-pointer">
<div className="flex justify-between items-start mb-2">
<div className="flex items-center gap-3">
<div className="bg-primary/10 text-primary w-8 h-8 rounded-full flex items-center justify-center font-label-md text-label-md">Q1</div>
<h4 className="font-label-md text-label-md text-on-surface">Complex Numbers &amp; Geometry</h4>
</div>
<div className="font-label-md text-label-md text-primary bg-primary/10 px-3 py-1 rounded-full">
                                        4 / 4 pts
                                    </div>
</div>
<p className="font-body-sm text-body-sm text-on-surface-variant ml-11">Flawless execution. The geometric interpretation was clearly articulated.</p>
</div>
{/*  Q2  */}
<div className="group border border-outline-variant/50 rounded-xl p-4 hover:border-primary/50 hover:bg-surface-bright transition-all cursor-pointer">
<div className="flex justify-between items-start mb-2">
<div className="flex items-center gap-3">
<div className="bg-primary/10 text-primary w-8 h-8 rounded-full flex items-center justify-center font-label-md text-label-md">Q2</div>
<h4 className="font-label-md text-label-md text-on-surface">Sequences &amp; Induction</h4>
</div>
<div className="font-label-md text-label-md text-secondary bg-secondary-container px-3 py-1 rounded-full">
                                        3.5 / 4 pts
                                    </div>
</div>
<p className="font-body-sm text-body-sm text-on-surface-variant ml-11">Good approach, but you missed stating the base case explicitly before jumping into the inductive step.</p>
</div>
{/*  Q3  */}
<div className="group border border-error-container rounded-xl p-4 bg-error-container/10 transition-all cursor-pointer">
<div className="flex justify-between items-start mb-2">
<div className="flex items-center gap-3">
<div className="bg-error/10 text-error w-8 h-8 rounded-full flex items-center justify-center font-label-md text-label-md">Q3</div>
<h4 className="font-label-md text-label-md text-on-surface">Integration by Parts</h4>
</div>
<div className="font-label-md text-label-md text-error bg-error/10 px-3 py-1 rounded-full">
                                        2 / 5 pts
                                    </div>
</div>
<p className="font-body-sm text-body-sm text-on-surface-variant ml-11">A critical sign error in the second line led to an incorrect final result. Review the rule: ∫u dv = uv - ∫v du.</p>
<div className="ml-11 mt-3">
<button className="text-on-surface border border-outline-variant rounded-full px-4 py-1.5 font-label-sm text-label-sm hover:bg-surface-container flex items-center gap-2">
<span className="material-symbols-outlined text-sm">play_circle</span> Review Topic
                                    </button>
</div>
</div>
{/*  Q4  */}
<div className="group border border-outline-variant/50 rounded-xl p-4 hover:border-primary/50 hover:bg-surface-bright transition-all cursor-pointer">
<div className="flex justify-between items-start mb-2">
<div className="flex items-center gap-3">
<div className="bg-primary/10 text-primary w-8 h-8 rounded-full flex items-center justify-center font-label-md text-label-md">Q4</div>
<h4 className="font-label-md text-label-md text-on-surface">Probability &amp; Trees</h4>
</div>
<div className="font-label-md text-label-md text-primary bg-primary/10 px-3 py-1 rounded-full">
                                        6.5 / 7 pts
                                    </div>
</div>
<p className="font-body-sm text-body-sm text-on-surface-variant ml-11">Almost perfect. Just a minor rounding discrepancy in the final decimal representation.</p>
</div>
</div>
</div>
</div>
</div>
</div>
{/*  Footer  */}

</main>
        </>
    );
}
