"use client";

import Link from 'next/link';
import { usePathname } from 'next/navigation';

export default function Sidebar() {
    const pathname = usePathname();
    
    const navItems = [
        { path: '/', icon: 'home', label: 'Home' },
        { path: '/chat', icon: 'chat', label: 'Chat' },
        { path: '/correction', icon: 'fact_check', label: 'Correction' },
        { path: '/resume', icon: 'description', label: 'Resume Generation' },
        { path: '/exercise', icon: 'assignment', label: 'Exercise Generation' },
        { path: '/exam-gen', icon: 'quiz', label: 'Exam Generation' },
        { path: '/exam-correction', icon: 'grading', label: 'Exam Correction' },
        { path: '/cadre', icon: 'menu_book', label: 'Cadre Référenciel' },
    ];

    return (
        <aside className="w-64 bg-surface-container-lowest border-r border-outline-variant flex-col h-screen hidden md:flex shrink-0">
            <div className="px-6 py-8">
                <div className="flex items-center gap-2">
                    <span className="font-headline-md text-headline-md text-on-background flex items-center">
                        <span className="text-primary text-[32px] mr-1 leading-none">R</span>Rafiki
                    </span>
                </div>
                <p className="text-xs text-on-surface-variant mt-1 font-medium">Baccalaureate Companion</p>
            </div>
            
            <nav className="flex-1 px-4 flex flex-col gap-2 overflow-y-auto">
                {navItems.map((item) => {
                    const isActive = pathname === item.path;
                    return (
                        <Link 
                            key={item.path} 
                            href={item.path}
                            className={`flex items-center gap-3 px-4 py-3 rounded-xl transition-colors font-medium ${
                                isActive 
                                ? 'bg-primary text-on-primary shadow-sm' 
                                : 'text-on-surface-variant hover:bg-surface-container-low'
                            }`}
                        >
                            <span className={`material-symbols-outlined text-[20px] ${isActive ? 'fill-icon' : ''}`}>{item.icon}</span>
                            {item.label}
                        </Link>
                    );
                })}
            </nav>
        </aside>
    );
}
