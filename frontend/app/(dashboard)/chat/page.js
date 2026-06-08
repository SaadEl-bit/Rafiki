import Link from 'next/link';

export default function PageContent() {
    return (
        <>
<main className="flex-1 flex flex-col mx-8 mb-6 bg-surface-container-lowest rounded-3xl shadow-[0_8px_30px_rgba(0,0,0,0.04)] overflow-hidden relative border border-outline-variant">
<div className="px-8 py-5 border-b border-outline-variant shrink-0">
<h2 className="text-lg font-bold text-on-background">AI Tutor Chat</h2>
</div>
{/*  Chat Canvas  */}
<div className="flex-1 overflow-y-auto px-8 py-6 flex flex-col gap-6">
<div className="w-full flex justify-center py-2">
<span className="font-medium text-xs text-on-surface-variant">Aujourd&apos;hui, 14:30</span>
</div>
{/*  Student Message  */}
<div className="flex gap-3 justify-end w-full">
<div className="bg-primary-container text-on-primary-container rounded-2xl p-5 max-w-[85%] md:max-w-[70%]">
<div className="font-bold text-sm mb-1 text-right">Alex</div>
<p className="text-sm">Salut Rafiki, je bloque sur la dérivée de la fonction \( f(x) = x^2 \ln(x) \). Tu peux m&apos;aider avec les étapes ?</p>
</div>
</div>
{/*  AI Message  */}
<div className="flex gap-4 w-full">
<div className="w-10 h-10 rounded-full bg-surface-container-high flex items-center justify-center flex-shrink-0 mt-1">
<span className="material-symbols-outlined text-[24px] text-on-surface-variant">psychology</span>
</div>
<div className="bg-surface-container text-on-surface rounded-2xl p-5 max-w-[85%] md:max-w-[70%]">
<div className="font-bold text-sm mb-1">MaxAI</div>
<p className="text-sm mb-3">Bonjour ! Bien sûr, révisons cela ensemble pour le Bac.</p>
<p className="text-sm mb-2">Pour dériver \( f(x) = x^2 \ln(x) \), on doit utiliser la formule de la dérivée d'un produit \( (uv)' = u'v + uv' \).</p>
<div className="math-block py-2 font-mono text-sm overflow-x-auto text-on-surface-variant">
                        Posons :<br />
                        \( u(x) = x^2 \)  =&gt;  \( u'(x) = 2x \)<br />
                        \( v(x) = \ln(x) \) =&gt;  \( v'(x) = \frac{"{1}"}{"{x}"} \)
                    </div>
<p className="text-sm mt-2">Ensuite, on applique la formule :</p>
<p className="font-bold text-on-surface my-2 inline-block">
                        \( f'(x) = 2x \ln(x) + x^2 (\frac{"{1}"}{"{x}"}) \)
                    </p>
<p className="text-sm mt-2">Est-ce que tu peux simplifier la deuxième partie de l&apos;expression ?</p>
</div>
</div>
{/*  Loading Message (System)  */}
<div className="w-full flex justify-center mt-2 opacity-70">
<p className="text-xs font-medium text-on-surface-variant flex items-center gap-2">
<span className="material-symbols-outlined text-[14px] animate-spin">sync</span>
                    The AI is waking up, this may take up to 20 seconds...
                </p>
</div>
{/*  AI Typing Indicator  */}
<div className="flex gap-4 w-full mt-2">
<div className="w-10 h-10 rounded-full bg-surface-container-high flex items-center justify-center flex-shrink-0">
<span className="material-symbols-outlined text-[24px] text-on-surface-variant">psychology</span>
</div>
<div className="bg-surface-container text-on-surface rounded-2xl py-4 px-5 flex items-center gap-1.5 h-12">
<div className="w-2 h-2 rounded-full bg-outline-variant typing-dot"></div>
<div className="w-2 h-2 rounded-full bg-outline-variant typing-dot"></div>
<div className="w-2 h-2 rounded-full bg-outline-variant typing-dot"></div>
</div>
</div>
<div className="h-32 shrink-0"></div> {/*  Spacer for absolute input  */}
</div>
{/*  Input Area  */}
<div className="absolute bottom-0 left-0 w-full bg-surface-container-lowest pt-2 pb-6 px-8 z-50 flex flex-col gap-3">
{/*  Subject Selector / Quick Actions  */}
<div className="flex gap-2 overflow-x-auto pb-1 scrollbar-hide">
<button className="whitespace-nowrap px-4 py-1.5 rounded-full bg-primary text-on-primary text-sm font-medium hover:bg-primary/90 transition-colors">
                    Explain a concept
                </button>
<button className="whitespace-nowrap px-4 py-1.5 rounded-full bg-primary-container text-on-primary-container text-sm font-medium hover:bg-primary hover:text-on-primary transition-colors">
                    Check my code
                </button>
<button className="whitespace-nowrap px-4 py-1.5 rounded-full bg-primary-container text-on-primary-container text-sm font-medium hover:bg-primary hover:text-on-primary transition-colors">
                    Practice quiz
                </button>
<button className="whitespace-nowrap px-4 py-1.5 rounded-full bg-primary-container text-on-primary-container text-sm font-medium hover:bg-primary hover:text-on-primary transition-colors">
                    Study plan
                </button>
</div>
<div className="flex items-center gap-3">
<button className="p-2 text-on-surface-variant hover:text-on-surface transition-colors rounded-full shrink-0">
<span className="material-symbols-outlined text-[24px] transform -rotate-45">attachment</span>
</button>
<div className="flex-1 flex items-center bg-surface-container-lowest border border-outline-variant rounded-full px-4 py-1 shadow-sm focus-within:border-primary focus-within:ring-1 focus-within:ring-primary transition-all h-12">
<textarea className="flex-1 bg-transparent border-none focus:ring-0 resize-none py-3 text-sm text-on-surface placeholder:text-on-surface-variant leading-tight" placeholder="Ask anything or attach a file for help..." rows="1" style={{"overflowY":"hidden"}}></textarea>
<button className="p-2 text-outline-variant hover:text-primary transition-colors flex items-center justify-center shrink-0">
<span className="material-symbols-outlined text-[24px]">send</span>
</button>
</div>
</div>

</div>
</main>
        </>
    );
}
