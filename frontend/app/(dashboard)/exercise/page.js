export default function ExercisePage() {
    return (
        <main className="flex-grow w-full max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop py-8 md:py-10 gap-gutter flex flex-col overflow-y-auto">
            <header className="mb-8">
                <h1 className="font-display-lg-mobile md:font-display-lg text-display-lg-mobile md:text-display-lg text-on-surface mb-2">Generate Exercise</h1>
                <p className="font-body-lg text-body-lg text-on-surface-variant">Create customized practice exercises based on specific topics and difficulty levels.</p>
            </header>
            
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-gutter">
                <div className="lg:col-span-8 flex flex-col gap-6">
                    <div className="bg-surface rounded-2xl border border-outline-variant p-6">
                        <label className="block font-label-sm text-label-sm text-on-surface-variant mb-4 uppercase tracking-wider">Subject / Matière</label>
                        <div className="flex flex-wrap gap-3">
                            <button className="px-5 py-2.5 rounded-xl bg-primary-container text-on-primary-container font-semibold hover:bg-primary-fixed transition-colors flex items-center gap-2 shadow-sm">
                                <span className="material-symbols-outlined text-sm">functions</span> Math
                            </button>
                        </div>
                    </div>
                </div>
                <div className="lg:col-span-4 flex flex-col gap-6">
                    <div className="bg-surface rounded-2xl border border-outline-variant p-6">
                        <label className="block font-label-sm text-label-sm text-on-surface-variant mb-4 uppercase tracking-wider">Additional Options</label>
                        <select className="w-full rounded-xl border-outline-variant bg-surface-container-low text-on-surface p-4 outline-none mb-4">
                            <option>Difficulty: Medium</option>
                            <option>Difficulty: Hard</option>
                        </select>
                    </div>
                    <div className="bg-surface rounded-2xl border border-outline-variant p-8 flex flex-col justify-center items-center text-center mt-auto bg-gradient-to-b from-surface to-primary-container/10">
                        <span className="material-symbols-outlined text-4xl text-primary mb-4">assignment</span>
                        <h3 className="font-headline-md text-headline-md text-on-surface mb-3">Ready to Generate</h3>
                        <button className="w-full bg-primary-container text-on-primary-container px-6 py-4 rounded-xl font-headline-md text-headline-md font-semibold hover:bg-primary-fixed transition-colors shadow-md mt-4">
                            Generate Exercise
                        </button>
                    </div>
                </div>
            </div>
        </main>
    );
}
