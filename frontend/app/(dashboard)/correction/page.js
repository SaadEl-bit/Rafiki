import Link from 'next/link';

export default function PageContent() {
    return (
        <>
<main className="flex-grow h-full overflow-y-auto w-full max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop py-8 md:py-10 gap-gutter flex flex-col">
{/*  Header Section  */}
<header className="mb-8">
<h1 className="font-display-lg-mobile md:font-display-lg text-display-lg-mobile md:text-display-lg text-on-surface mb-2">Exercise Correction <span className="font-arabic-brand text-primary opacity-80 text-xl ml-2 inline-block align-middle">تصحيح التمارين</span></h1>
<p className="font-body-lg text-body-lg text-on-surface-variant">Upload your exercise for a detailed, step-by-step analysis.</p>
</header>
<div className="grid grid-cols-1 lg:grid-cols-12 gap-gutter">
{/*  Left Column: Upload Area  */}
<div className="lg:col-span-8 flex flex-col gap-6">
{/*  Subject Selector  */}
<div className="bg-surface rounded-2xl border border-outline-variant p-6">
<label className="block font-label-sm text-label-sm text-on-surface-variant mb-4 uppercase tracking-wider">Subject / Matière</label>
<div className="flex flex-wrap gap-3">
<button className="px-5 py-2.5 rounded-xl bg-primary-container text-on-primary-container font-semibold hover:bg-primary-fixed transition-colors flex items-center gap-2 shadow-sm">
<span className="material-symbols-outlined text-sm">functions</span> Math
                        </button>
<button className="px-5 py-2.5 rounded-xl border border-outline-variant bg-surface text-on-surface-variant font-semibold hover:bg-surface-container transition-colors flex items-center gap-2">
<span className="material-symbols-outlined text-sm">biotech</span> Physics
                        </button>
<button className="px-5 py-2.5 rounded-xl border border-outline-variant bg-surface text-on-surface-variant font-semibold hover:bg-surface-container transition-colors flex items-center gap-2">
<span className="material-symbols-outlined text-sm">science</span> Chemistry
                        </button>
</div>
</div>
{/*  Upload Zone  */}
<div className="bg-surface rounded-2xl border border-outline-variant p-6 flex flex-col h-full min-h-[400px]">
<div className="file-upload-dashed flex-grow flex flex-col items-center justify-center p-8 md:p-12 text-center transition-colors hover:bg-primary-container/10 cursor-pointer group bg-surface-container-lowest">
<div className="h-20 w-20 bg-primary-container/30 rounded-full flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
<span className="material-symbols-outlined text-4xl text-primary-fixed-dim" style={{"fontVariationSettings":"&quot"}}>upload_file</span>
</div>
<h3 className="font-headline-md text-headline-md text-on-surface mb-2">Drop your exercise here</h3>
<p className="font-body-md text-body-md text-on-surface-variant mb-8">Or click to browse files (PDF, JPG, PNG)</p>
<button className="bg-surface border border-outline-variant text-on-surface px-8 py-3 rounded-xl font-semibold hover:bg-surface-container transition-colors shadow-sm">
                            Browse Files
                        </button>
<p className="font-label-sm text-label-sm text-outline mt-6">Max file size: 10MB</p>
</div>
</div>
</div>
{/*  Right Column: Settings & Actions  */}
<div className="lg:col-span-4 flex flex-col gap-6">
{/*  Additional Notes  */}
<div className="bg-surface rounded-2xl border border-outline-variant p-6">
<label className="block font-label-sm text-label-sm text-on-surface-variant mb-4 uppercase tracking-wider" htmlFor="notes">Additional Notes (Optional)</label>
<textarea className="w-full rounded-xl border-outline-variant bg-surface-container-low text-on-surface focus:ring-primary-fixed-dim focus:border-primary-fixed-dim placeholder-outline-variant resize-none p-4" id="notes" placeholder="E.g., I'm stuck on question 3b..." rows="5"></textarea>
</div>
{/*  Action Area  */}
<div className="bg-surface rounded-2xl border border-outline-variant p-8 flex flex-col justify-center items-center text-center mt-auto bg-gradient-to-b from-surface to-secondary-container/10">
<div className="h-16 w-16 bg-secondary-fixed-dim/20 rounded-full flex items-center justify-center mb-6">
<span className="material-symbols-outlined text-4xl text-secondary-fixed-dim" style={{"fontVariationSettings":"&quot"}}>auto_awesome</span>
</div>
<h3 className="font-headline-md text-headline-md text-on-surface mb-3">Ready for Analysis</h3>
<p className="font-body-md text-body-md text-on-surface-variant mb-8">Our AI will break down the problem step-by-step.</p>
<button className="w-full bg-primary-container text-on-primary-container px-6 py-4 rounded-xl font-headline-md text-headline-md font-semibold hover:bg-primary-fixed transition-colors shadow-md flex justify-center items-center gap-2">
                        Correct my Exercise
                    </button>
</div>
</div>
</div>
</main>
        </>
    );
}
