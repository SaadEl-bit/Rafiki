import Link from 'next/link';

export default function HomePage() {
    return (
        <>

{/*  TopNavBar  */}
<nav className="bg-surface-container-lowest font-body-md text-body-md full-width top-0 sticky shadow-sm z-50">
<div className="flex justify-between items-center w-full px-margin-mobile md:px-margin-desktop py-4 max-w-container-max mx-auto">
<div className="flex items-center gap-2">
<img alt="Rafiki Logo" className="h-8 w-8 object-contain rounded-md" src="BASE64_IMAGE" />
<span className="text-headline-md font-headline-md text-primary">Rafiki.</span>
</div>
<div className="hidden md:flex gap-6 items-center">
<a className="text-on-surface-variant hover:text-primary transition-colors cursor-pointer font-medium" href="#features">Features</a>
<a className="text-on-surface-variant hover:text-primary transition-colors cursor-pointer font-medium" href="#how-it-works">How it Works</a>
</div>
<div className="flex items-center gap-4 text-on-surface-variant"><div className="flex items-center gap-4 cursor-pointer" style={{"opacity":"0"}}>https://lh3.googleusercontent.com/aida-public/AB6AXuCosNhg4tLdjKIgDAQt0vWiyr2-W8D2CKAvNLfgAgEb8xOQb-szd7Y-uHp84AIDHgMDdlfq1K70cvKBxmV7S1v7-mWszCFmus8looeeMSgVSuWyeKIaYxoPpulU7htV_ovxTsHUtoKGvtT0U0DMr0AiCmHiEfqjXkdv8CJTNDYijJE4OVbdm7DZs4tAsoNaIuVeVzNp9WcPeFGvPqTy_zeqKGlbVWbrXuuyFxcbNrz5he8fMOQ3Jo3CchnnclYxQF36f6EmKQ5ht_4A</div></div>
</div>
</nav>
<main className="flex-grow">
{/*  Hero Section  */}
<section className="py-12 px-margin-mobile md:px-margin-desktop bg-surface flex flex-col items-center justify-center relative overflow-hidden flex-grow">
<div className="max-w-container-max w-full mx-auto">
<div className="bg-primary rounded-[32px] p-8 md:p-16 flex flex-col relative overflow-hidden shadow-lg">
{/*  Decorative abstract shapes inside banner  */}
<div className="absolute top-0 right-0 w-96 h-96 bg-white opacity-10 rounded-full translate-x-1/3 -translate-y-1/3 pointer-events-none"></div>
<div className="absolute bottom-0 left-10 w-64 h-64 bg-white opacity-10 rounded-full translate-y-1/3 pointer-events-none"></div>
<div className="max-w-2xl z-10 space-y-6 relative">
<h1 className="font-headline-xl text-headline-lg md:text-headline-xl text-on-primary leading-tight">
                        Unlock Your Potential with<br />
                        Rafiki (<span className="font-arabic-brand">رفيقي</span>)
                    </h1>
<p className="font-body-lg text-body-lg text-on-primary/90 max-w-xl">
                        رفيقك في الدراسة — Ton compagnon pour le Bac.<br />
                        Personalized paths and 24/7 automated tutoring for Moroccan students.
                    </p>
<div className="mt-8 bg-surface-container-lowest rounded-2xl p-2 flex items-center shadow-lg max-w-xl">
<span className="material-symbols-outlined text-primary ml-3 mr-2" data-icon="search">search</span>
<input className="flex-grow bg-transparent border-none focus:ring-0 text-on-surface placeholder-on-surface-variant font-body-md py-3" placeholder="Ask a question or search for a subject..." type="text" />
<a className="bg-primary text-on-primary font-semibold px-6 py-3 rounded-xl hover:bg-primary/90 transition-colors duration-200 flex items-center gap-2" href="/app/chat">
                            Start Learning
                        </a>
</div>
</div>
<div className="mt-16 z-10 flex flex-col sm:flex-row items-center justify-between border-t border-on-primary/20 pt-6">
<p className="text-on-primary font-medium mb-4 sm:mb-0">Join Now and Get AI-Powered Tutor Access to Excel in Your Bac</p>
<a className="bg-surface-container-lowest text-primary font-bold px-6 py-2 rounded-xl hover:bg-surface-container-low transition-colors duration-200" href="/app/correction">
                        Correct my Exercise
                    </a>
</div>
</div>
</div>
</section>
{/*  Subjects Banner  */}
<section className="py-8 px-margin-mobile md:px-margin-desktop bg-surface flex-grow">
<div className="max-w-container-max mx-auto flex flex-col md:flex-row gap-6 items-center">
<h3 className="font-headline-md text-xl font-bold text-on-surface whitespace-nowrap">Popular Subjects</h3>
<div className="flex flex-wrap gap-4">
<div className="flex items-center gap-2 bg-surface-container-lowest px-6 py-3 rounded-2xl shadow-[0_2px_12px_rgba(0,0,0,0.04)] border border-outline-variant hover:shadow-[0_4px_20px_rgba(0,0,0,0.08)] transition-shadow">
<span className="font-body-md text-body-md font-semibold text-on-surface">Maths</span>
</div>
<div className="flex items-center gap-2 bg-surface-container-lowest px-6 py-3 rounded-2xl shadow-[0_2px_12px_rgba(0,0,0,0.04)] border border-outline-variant hover:shadow-[0_4px_20px_rgba(0,0,0,0.08)] transition-shadow">
<span className="font-body-md text-body-md font-semibold text-on-surface">Physics-Chem</span>
</div>
<div className="flex items-center gap-2 bg-surface-container-lowest px-6 py-3 rounded-2xl shadow-[0_2px_12px_rgba(0,0,0,0.04)] border border-outline-variant hover:shadow-[0_4px_20px_rgba(0,0,0,0.08)] transition-shadow">
<span className="font-body-md text-body-md font-semibold text-on-surface">English</span>
</div>
</div>
</div>
</section>
{/*  Features Section  */}
<section className="py-16 px-margin-mobile md:px-margin-desktop bg-surface-container-low flex-grow" id="features">
<div className="max-w-container-max mx-auto">
<div className="mb-10">
<h2 className="font-headline-md text-3xl font-bold text-on-surface mb-2">Empowering Your Bac Journey</h2>
</div>
<div className="grid grid-cols-1 md:grid-cols-3 gap-8">
{/*  Feature 1  */}
<div className="bg-surface-container-lowest rounded-[24px] shadow-[0_4px_24px_rgba(0,0,0,0.04)] overflow-hidden flex flex-col border border-outline-variant transition-transform hover:-translate-y-1 duration-300">
<div className="bg-primary h-32 p-6 relative overflow-hidden">
<div className="absolute right-0 bottom-0 opacity-20 transform translate-x-1/4 translate-y-1/4">
<span className="material-symbols-outlined text-8xl text-on-primary" data-icon="forum">forum</span>
</div>
<div className="bg-surface-container-lowest rounded-2xl h-14 w-14 flex items-center justify-center text-primary absolute -bottom-7 left-6 shadow-md">
<span className="material-symbols-outlined" data-icon="forum">forum</span>
</div>
</div>
<div className="p-6 pt-12 flex-grow flex flex-col">
<h3 className="font-headline-md text-xl font-bold text-on-surface mb-3">Q&amp;A Chat</h3>
<p className="font-body-md text-on-surface-variant mb-6 flex-grow leading-relaxed">Stuck on a concept? Chat with Rafiki anytime to get clear, step-by-step explanations tailored to the national curriculum.</p>
<button className="bg-primary text-on-primary px-5 py-2.5 rounded-xl text-sm font-semibold w-max hover:bg-primary/90 transition-colors">View Feature</button>
</div>
</div>
{/*  Feature 2  */}
<div className="bg-surface-container-lowest rounded-[24px] shadow-[0_4px_24px_rgba(0,0,0,0.04)] overflow-hidden flex flex-col border border-outline-variant transition-transform hover:-translate-y-1 duration-300">
<div className="bg-secondary h-32 p-6 relative overflow-hidden">
<div className="absolute right-0 bottom-0 opacity-20 transform translate-x-1/4 translate-y-1/4">
<span className="material-symbols-outlined text-8xl text-on-secondary" data-icon="grading">grading</span>
</div>
<div className="bg-surface-container-lowest rounded-2xl h-14 w-14 flex items-center justify-center text-secondary absolute -bottom-7 left-6 shadow-md">
<span className="material-symbols-outlined" data-icon="grading">grading</span>
</div>
</div>
<div className="p-6 pt-12 flex-grow flex flex-col">
<h3 className="font-headline-md text-xl font-bold text-on-surface mb-3">Exercise Correction</h3>
<p className="font-body-md text-on-surface-variant mb-6 flex-grow leading-relaxed">Upload your past exams or homework. Rafiki reviews your work, points out mistakes, and guides you to the correct solution.</p>
<button className="bg-secondary text-on-secondary px-5 py-2.5 rounded-xl text-sm font-semibold w-max hover:bg-secondary/90 transition-colors">View Feature</button>
</div>
</div>
{/*  Feature 3  */}
<div className="bg-surface-container-lowest rounded-[24px] shadow-[0_4px_24px_rgba(0,0,0,0.04)] overflow-hidden flex flex-col border border-outline-variant transition-transform hover:-translate-y-1 duration-300">
<div className="bg-tertiary h-32 p-6 relative overflow-hidden">
<div className="absolute right-0 bottom-0 opacity-20 transform translate-x-1/4 translate-y-1/4">
<span className="material-symbols-outlined text-8xl text-on-tertiary" data-icon="description">description</span>
</div>
<div className="bg-surface-container-lowest rounded-2xl h-14 w-14 flex items-center justify-center text-tertiary absolute -bottom-7 left-6 shadow-md">
<span className="material-symbols-outlined" data-icon="description">description</span>
</div>
</div>
<div className="p-6 pt-12 flex-grow flex flex-col">
<h3 className="font-headline-md text-xl font-bold text-on-surface mb-3">Resume Generation</h3>
<p className="font-body-md text-on-surface-variant mb-6 flex-grow leading-relaxed">Automatically generate comprehensive summary sheets from your lessons to streamline your final revision process.</p>
<button className="bg-tertiary text-on-tertiary px-5 py-2.5 rounded-xl text-sm font-semibold w-max hover:bg-tertiary/90 transition-colors">View Feature</button>
</div>
</div>
{/*  Feature 4  */}
<div className="bg-surface-container-lowest rounded-[24px] shadow-[0_4px_24px_rgba(0,0,0,0.04)] overflow-hidden flex flex-col border border-outline-variant transition-transform hover:-translate-y-1 duration-300">
<div className="bg-primary-container h-32 p-6 relative overflow-hidden">
<div className="absolute right-0 bottom-0 opacity-20 transform translate-x-1/4 translate-y-1/4">
<span className="material-symbols-outlined text-8xl text-on-primary-container" data-icon="assignment">assignment</span>
</div>
<div className="bg-surface-container-lowest rounded-2xl h-14 w-14 flex items-center justify-center text-primary-container absolute -bottom-7 left-6 shadow-md">
<span className="material-symbols-outlined" data-icon="assignment">assignment</span>
</div>
</div>
<div className="p-6 pt-12 flex-grow flex flex-col">
<h3 className="font-headline-md text-xl font-bold text-on-surface mb-3">Exercise Generation</h3>
<p className="font-body-md text-on-surface-variant mb-6 flex-grow leading-relaxed">Create customized practice exercises based on specific topics and difficulty levels to test your knowledge.</p>
<button className="bg-primary-container text-on-primary-container px-5 py-2.5 rounded-xl text-sm font-semibold w-max hover:bg-primary-container/90 transition-colors">View Feature</button>
</div>
</div>
{/*  Feature 5  */}
<div className="bg-surface-container-lowest rounded-[24px] shadow-[0_4px_24px_rgba(0,0,0,0.04)] overflow-hidden flex flex-col border border-outline-variant transition-transform hover:-translate-y-1 duration-300">
<div className="bg-secondary-container h-32 p-6 relative overflow-hidden">
<div className="absolute right-0 bottom-0 opacity-20 transform translate-x-1/4 translate-y-1/4">
<span className="material-symbols-outlined text-8xl text-on-secondary-container" data-icon="quiz">quiz</span>
</div>
<div className="bg-surface-container-lowest rounded-2xl h-14 w-14 flex items-center justify-center text-secondary-container absolute -bottom-7 left-6 shadow-md">
<span className="material-symbols-outlined" data-icon="quiz">quiz</span>
</div>
</div>
<div className="p-6 pt-12 flex-grow flex flex-col">
<h3 className="font-headline-md text-xl font-bold text-on-surface mb-3">Exam Generation</h3>
<p className="font-body-md text-on-surface-variant mb-6 flex-grow leading-relaxed">Simulate real exam conditions by generating full mock exams that match the national Baccalaureate structure.</p>
<button className="bg-secondary-container text-on-secondary-container px-5 py-2.5 rounded-xl text-sm font-semibold w-max hover:bg-secondary-container/90 transition-colors">View Feature</button>
</div>
</div>
{/*  Feature 6  */}
<div className="bg-surface-container-lowest rounded-[24px] shadow-[0_4px_24px_rgba(0,0,0,0.04)] overflow-hidden flex flex-col border border-outline-variant transition-transform hover:-translate-y-1 duration-300">
<div className="bg-tertiary-container h-32 p-6 relative overflow-hidden">
<div className="absolute right-0 bottom-0 opacity-20 transform translate-x-1/4 translate-y-1/4">
<span className="material-symbols-outlined text-8xl text-on-tertiary-container" data-icon="check_circle">check_circle</span>
</div>
<div className="bg-surface-container-lowest rounded-2xl h-14 w-14 flex items-center justify-center text-tertiary-container absolute -bottom-7 left-6 shadow-md">
<span className="material-symbols-outlined" data-icon="check_circle">check_circle</span>
</div>
</div>
<div className="p-6 pt-12 flex-grow flex flex-col">
<h3 className="font-headline-md text-xl font-bold text-on-surface mb-3">Exam Correction</h3>
<p className="font-body-md text-on-surface-variant mb-6 flex-grow leading-relaxed">Submit your mock exams for detailed grading and feedback to identify areas for improvement before the big day.</p>
<button className="bg-tertiary-container text-on-tertiary-container px-5 py-2.5 rounded-xl text-sm font-semibold w-max hover:bg-tertiary-container/90 transition-colors">View Feature</button>
</div>
</div>
</div>
</div>
</section>
{/*  How It Works Section  */}
<section className="py-20 px-margin-mobile md:px-margin-desktop bg-surface flex-grow" id="how-it-works">
<div className="max-w-container-max mx-auto">
<div className="text-center mb-16">
<h2 className="font-headline-md text-3xl font-bold text-on-surface mb-4">How It Works</h2>
<p className="font-body-md text-body-md text-on-surface-variant">Simple steps to accelerate your learning.</p>
</div>
<div className="flex flex-col md:flex-row items-start justify-center gap-12 md:gap-8 relative">
{/*  Connector Line (Desktop)  */}
<div className="hidden md:block absolute top-10 left-[15%] right-[15%] h-0.5 bg-outline-variant z-0"></div>
{/*  Step 1  */}
<div className="flex flex-col items-center text-center z-10 w-full md:w-1/3 group">
<div className="h-20 w-20 rounded-2xl bg-surface-container-lowest text-primary flex items-center justify-center font-headline-xl text-3xl font-bold mb-6 shadow-md border-2 border-primary group-hover:bg-primary group-hover:text-on-primary transition-all duration-300">1</div>
<h4 className="font-headline-md text-xl font-bold text-on-surface mb-3">Choose Subject</h4>
<p className="font-body-md text-on-surface-variant">Select the subject you want to focus on.</p>
</div>
{/*  Step 2  */}
<div className="flex flex-col items-center text-center z-10 w-full md:w-1/3 group">
<div className="h-20 w-20 rounded-2xl bg-surface-container-lowest text-secondary flex items-center justify-center font-headline-xl text-3xl font-bold mb-6 shadow-md border-2 border-secondary group-hover:bg-secondary group-hover:text-on-secondary transition-all duration-300">2</div>
<h4 className="font-headline-md text-xl font-bold text-on-surface mb-3">Ask or Upload</h4>
<p className="font-body-md text-on-surface-variant">Type your question or drop an image of your exercise.</p>
</div>
{/*  Step 3  */}
<div className="flex flex-col items-center text-center z-10 w-full md:w-1/3 group">
<div className="h-20 w-20 rounded-2xl bg-surface-container-lowest text-tertiary flex items-center justify-center font-headline-xl text-3xl font-bold mb-6 shadow-md border-2 border-tertiary group-hover:bg-tertiary group-hover:text-on-tertiary transition-all duration-300">3</div>
<h4 className="font-headline-md text-xl font-bold text-on-surface mb-3">Get Answer</h4>
<p className="font-body-md text-on-surface-variant">Receive detailed explanations and corrections.</p>
</div>
</div>
</div>
</section>
</main>
{/*  Footer  */}










        </>
    );
}
