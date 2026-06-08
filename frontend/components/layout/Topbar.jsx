"use client";

import { usePathname } from 'next/navigation';

export default function Topbar() {
    const pathname = usePathname();
    
    // Determine page title based on pathname
    let pageTitle = "Dashboard";
    if (pathname === '/chat') pageTitle = "AI Tutor Chat";
    else if (pathname === '/correction') pageTitle = "Exercise Correction";
    else if (pathname === '/resume') pageTitle = "Resume Generation";
    else if (pathname === '/exercise') pageTitle = "Exercise Generation";
    else if (pathname === '/exam-gen') pageTitle = "Exam Generation";
    else if (pathname === '/exam-correction') pageTitle = "Exam Correction";
    else if (pathname === '/cadre') pageTitle = "Cadre Référenciel";

    return (
        <header className="bg-transparent h-20 flex items-center justify-between px-8 shrink-0 w-full">
            <div className="flex items-center gap-4 w-full max-w-2xl">
                <h1 className="text-xl font-bold text-on-background">{pageTitle}</h1>
                <div className="flex-1 relative ml-8 hidden md:block">
                    <span className="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-[20px]">search</span>
                    <input 
                        className="w-full bg-surface-container-lowest border-none rounded-full py-2.5 pl-10 pr-4 text-sm text-on-surface focus:ring-2 focus:ring-primary/20 shadow-[0_2px_8px_rgba(0,0,0,0.02)] outline-none" 
                        placeholder="Search here..." 
                        type="text" 
                    />
                </div>
            </div>
            <div className="flex items-center gap-5 ml-auto">
                <button className="flex items-center gap-2 text-sm font-medium text-on-surface-variant hover:text-on-surface">
                    <img 
                        alt="US Flag" 
                        className="w-5 h-5 rounded-full object-cover border border-outline-variant" 
                        src="https://lh3.googleusercontent.com/aida-public/AB6AXuAmVcSNk1yG-XJVxATbFGr5zmUH0Wmjp8Vzv3VfQM0f3zSQNjZ6agrv2TZPeUbD199cKBXEyuNxbPlcqjfQJnT6swa55Jx-ABh_--ckc00cH_nJ4F5C0ePaFa3dsVjrP9KfRL10SXKnvI2qUEt_SeXU1k2_AQ2SHgLF44SUOeDfVhyWM9E7E_fJexmoE_mWNBdyaQDLZLM-Os6iM3Oln1hHhiojN2BNrjbhpFb0QRjB7_xVpv8amlNPnyMC06L4YeYa7LxZhAiBUn4A" 
                    />
                    Eng (US)
                    <span className="material-symbols-outlined text-[16px]">expand_more</span>
                </button>
                <div className="flex items-center gap-3 text-on-surface-variant">
                    <button className="w-8 h-8 rounded-full bg-surface-container-lowest flex items-center justify-center hover:text-primary transition-colors shadow-sm">
                        <span className="material-symbols-outlined text-[20px]">chat_bubble</span>
                    </button>
                    <button className="w-8 h-8 rounded-full bg-surface-container-lowest flex items-center justify-center hover:text-primary transition-colors shadow-sm relative">
                        <span className="material-symbols-outlined text-[20px]">notifications</span>
                        <span className="absolute top-1 right-1 w-2 h-2 bg-error rounded-full"></span>
                    </button>
                    <button className="w-8 h-8 rounded-full bg-surface-container-lowest flex items-center justify-center hover:text-primary transition-colors shadow-sm">
                        <span className="material-symbols-outlined text-[20px]">settings</span>
                    </button>
                </div>
                <img 
                    alt="User profile" 
                    className="h-9 w-9 rounded-full object-cover border-2 border-surface-container-lowest shadow-sm" 
                    src="https://lh3.googleusercontent.com/aida-public/AB6AXuDi3Xuveb6973hf3ZcTvgKbR2cttPaFygOLNxpXq_xaF06GKAUx5Z3SEx2af14ncP7WrFyDf6SzFvfR5Lfv08dakgwEtErC4dpykg5zwFYv69tK0xmqiIZtvvRUtIoIWBddyIEuekbcDXy-qGxWUw0phABBYkJNIeeM5iPJawMjorq3tPAImS6wt09rr_TdC_PH5g15Aca9qvjhundh_LrWAAMcwLl1G7pzsGOU0RAvLZjfW6ufh3n5mqSRG6ELzY880hvMC3rfXUh_" 
                />
            </div>
        </header>
    );
}
