'use client';
import { useState, useRef } from 'react';

export default function PageContent() {
    const [messages, setMessages] = useState([
        { role: 'assistant', content: "Bonjour ! Je suis Rafiki, ton tuteur IA pour le Bac. Pose-moi une question sur le programme de Maths, Physique, ou Anglais !" }
    ]);
    const [input, setInput] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const [sessionId, setSessionId] = useState(null);
    const [pendingDocumentText, setPendingDocumentText] = useState(null);
    const fileInputRef = useRef(null);

    const handleFileUpload = async (e) => {
        const file = e.target.files[0];
        if (!file) return;

        setIsLoading(true);
        const formData = new FormData();
        formData.append('file', file);
        formData.append('subject', "Mathématiques");

        try {
            // 1. Upload and Extract
            const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/upload`, {
                method: 'POST',
                body: formData
            });
            const data = await response.json();
            
            if (data.session_id) {
                setSessionId(data.session_id);
                setPendingDocumentText(data.extracted_text);
                
                // Show the extracted text as a user message, then wait for them to type
                setMessages(prev => [...prev, { 
                    role: 'user', 
                    content: `[Document Extrait]\n${data.extracted_text}` 
                }]);
            }
        } catch (error) {
            setMessages(prev => [...prev, { role: 'assistant', content: "Erreur lors de l'extraction de l'image/PDF." }]);
        } finally {
            setIsLoading(false);
            e.target.value = null; // Reset input
        }
    };

    const sendMessage = async () => {
        if (!input.trim() || isLoading) return;
        
        // Show the user's typed question in the UI
        const newMessages = [...messages, { role: 'user', content: input }];
        setMessages(newMessages);
        
        // Combine the pending document text with their question for the AI prompt
        const finalQuestion = pendingDocumentText 
            ? `[Document Extrait]\n${pendingDocumentText}\n\n[Question de l'étudiant]: ${input}`
            : input;
            
        setInput("");
        setIsLoading(true);

        try {
            const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/ask`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ 
                    question: finalQuestion, 
                    subject: "Mathématiques",
                    session_id: sessionId
                })
            });
            const data = await response.json();
            setMessages([...newMessages, { role: 'assistant', content: data.answer }]);
            
            // Persist session_id from backend for conversation memory
            if (data.session_id) {
                setSessionId(data.session_id);
            }
            
            // Clear the pending document text so it's not sent again on the next question
            setPendingDocumentText(null); 
            
        } catch (error) {
            setMessages([...newMessages, { role: 'assistant', content: "Erreur de connexion au serveur (Avez-vous débloqué la page Localtunnel dans votre navigateur ?)." }]);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <main className="flex-1 flex flex-col mx-8 mb-6 bg-surface-container-lowest rounded-3xl shadow-[0_8px_30px_rgba(0,0,0,0.04)] overflow-hidden relative border border-outline-variant">
            <div className="px-8 py-5 border-b border-outline-variant shrink-0">
                <h2 className="text-lg font-bold text-on-background">AI Tutor Chat</h2>
            </div>
            
            {/* Chat Canvas */}
            <div className="flex-1 overflow-y-auto px-8 py-6 flex flex-col gap-6">
                <div className="w-full flex justify-center py-2">
                    <span className="font-medium text-xs text-on-surface-variant">Aujourd'hui</span>
                </div>

                {messages.map((msg, index) => (
                    msg.role === 'user' ? (
                        <div key={index} className="flex gap-3 justify-end w-full">
                            <div className="bg-primary-container text-on-primary-container rounded-2xl p-5 max-w-[85%] md:max-w-[70%]">
                                <div className="font-bold text-sm mb-1 text-right">Toi</div>
                                <p className="text-sm whitespace-pre-wrap">{msg.content}</p>
                            </div>
                        </div>
                    ) : (
                        <div key={index} className="flex gap-4 w-full">
                            <div className="w-10 h-10 rounded-full bg-surface-container-high flex items-center justify-center flex-shrink-0 mt-1">
                                <span className="material-symbols-outlined text-[24px] text-on-surface-variant">psychology</span>
                            </div>
                            <div className="bg-surface-container text-on-surface rounded-2xl p-5 max-w-[85%] md:max-w-[70%]">
                                <div className="font-bold text-sm mb-1">Rafiki AI</div>
                                <p className="text-sm mb-3 whitespace-pre-wrap">{msg.content}</p>
                            </div>
                        </div>
                    )
                ))}

                {isLoading && (
                    <>
                        <div className="w-full flex justify-center mt-2 opacity-70">
                            <p className="text-xs font-medium text-on-surface-variant flex items-center gap-2">
                                <span className="material-symbols-outlined text-[14px] animate-spin">sync</span>
                                L'IA analyse les données, cela peut prendre 10-30 secondes...
                            </p>
                        </div>
                        <div className="flex gap-4 w-full mt-2">
                            <div className="w-10 h-10 rounded-full bg-surface-container-high flex items-center justify-center flex-shrink-0">
                                <span className="material-symbols-outlined text-[24px] text-on-surface-variant">psychology</span>
                            </div>
                            <div className="bg-surface-container text-on-surface rounded-2xl py-4 px-5 flex items-center gap-1.5 h-12">
                                <div className="w-2 h-2 rounded-full bg-outline-variant typing-dot animate-bounce"></div>
                                <div className="w-2 h-2 rounded-full bg-outline-variant typing-dot animate-bounce" style={{animationDelay: '0.2s'}}></div>
                                <div className="w-2 h-2 rounded-full bg-outline-variant typing-dot animate-bounce" style={{animationDelay: '0.4s'}}></div>
                            </div>
                        </div>
                    </>
                )}
                
                <div className="h-32 shrink-0"></div> {/* Spacer for absolute input */}
            </div>

            {/* Input Area */}
            <div className="absolute bottom-0 left-0 w-full bg-surface-container-lowest pt-2 pb-6 px-8 z-50 flex flex-col gap-3">
                <div className="flex items-center gap-3">
                    <input 
                        type="file" 
                        ref={fileInputRef} 
                        onChange={handleFileUpload} 
                        className="hidden" 
                        accept="image/*,.pdf" 
                    />
                    <button 
                        onClick={() => fileInputRef.current?.click()}
                        disabled={isLoading}
                        className="p-2 text-on-surface-variant hover:text-on-surface transition-colors rounded-full shrink-0 disabled:opacity-50">
                        <span className="material-symbols-outlined text-[24px] transform -rotate-45">attachment</span>
                    </button>
                    <div className="flex-1 flex items-center bg-surface-container-lowest border border-outline-variant rounded-full px-4 py-1 shadow-sm focus-within:border-primary focus-within:ring-1 focus-within:ring-primary transition-all h-12">
                        <input 
                            type="text"
                            value={input}
                            onChange={(e) => setInput(e.target.value)}
                            onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
                            className="flex-1 bg-transparent border-none focus:ring-0 py-3 text-sm text-on-surface placeholder:text-on-surface-variant outline-none" 
                            placeholder="Pose une question sur le programme..." 
                        />
                        <button 
                            onClick={sendMessage}
                            disabled={isLoading}
                            className="p-2 text-outline-variant hover:text-primary transition-colors flex items-center justify-center shrink-0 disabled:opacity-50 cursor-pointer">
                            <span className="material-symbols-outlined text-[24px]">send</span>
                        </button>
                    </div>
                </div>
            </div>
        </main>
    );
}
