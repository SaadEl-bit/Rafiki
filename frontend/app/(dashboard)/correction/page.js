'use client';
import { useState, useRef } from 'react';

export default function PageContent() {
    const [subject, setSubject] = useState("Mathématiques");
    const [file, setFile] = useState(null);
    const [notes, setNotes] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const [correction, setCorrection] = useState("");
    const fileInputRef = useRef(null);

    const handleFileSelect = (e) => {
        if (e.target.files && e.target.files[0]) {
            setFile(e.target.files[0]);
            setCorrection(""); // Clear previous correction when new file is selected
        }
    };

    const handleCorrection = async () => {
        if (!file) {
            alert("Veuillez d'abord importer un document (PDF ou image) contenant l'exercice à corriger.");
            return;
        }

        setIsLoading(true);
        setCorrection("");
        let exerciseText = notes;
        let currentSessionId = null;

        try {
            // Step 1: Upload and Extract Text (if file exists)
            if (file) {
                const formData = new FormData();
                formData.append('file', file);
                formData.append('subject', subject);
                
                const uploadRes = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/upload`, {
                    method: 'POST',
                    body: formData
                });
                
                if (!uploadRes.ok) throw new Error("Erreur lors de l'extraction (Upload)");
                
                const uploadData = await uploadRes.json();
                currentSessionId = uploadData.session_id;
                
                // Construct a strict prompt to force the model to output the math solution directly
                exerciseText = `[Texte extrait du document]:\n${uploadData.extracted_text}\n\n[Notes de l'étudiant]:\n${notes}\n\nIMPORTANT: Ne décris pas ce que tu vas faire. Donne directement la solution mathématique complète et détaillée, étape par étape, pour résoudre cet exercice.`;
            } else if (notes.trim()) {
                exerciseText = `[Texte de l'étudiant]:\n${notes}\n\nIMPORTANT: Ne décris pas ce que tu vas faire. Donne directement la solution mathématique complète et détaillée, étape par étape, pour résoudre cet exercice.`;
            }

            // Step 2: Request Correction
            const correctRes = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/correct`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    exercise_text: exerciseText,
                    subject: subject,
                    session_id: currentSessionId
                })
            });

            if (!correctRes.ok) throw new Error("Erreur de connexion au serveur de correction.");

            const correctData = await correctRes.json();
            setCorrection(correctData.correction);

        } catch (error) {
            setCorrection(`Erreur: ${error.message} (Vérifiez le tunnel Localtunnel).`);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <main className="flex-grow h-full overflow-y-auto w-full max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop py-8 md:py-10 gap-gutter flex flex-col">
            {/* Header Section */}
            <header className="mb-8">
                <h1 className="font-display-lg-mobile md:font-display-lg text-display-lg-mobile md:text-display-lg text-on-surface mb-2">
                    Exercise Correction <span className="font-arabic-brand text-primary opacity-80 text-xl ml-2 inline-block align-middle">تصحيح التمارين</span>
                </h1>
                <p className="font-body-lg text-body-lg text-on-surface-variant">Upload your exercise for a detailed, step-by-step analysis.</p>
            </header>

            <div className="grid grid-cols-1 lg:grid-cols-12 gap-gutter">
                {/* Left Column: Upload Area */}
                <div className="lg:col-span-8 flex flex-col gap-6">
                    {/* Subject Selector */}
                    <div className="bg-surface rounded-2xl border border-outline-variant p-6">
                        <label className="block font-label-sm text-label-sm text-on-surface-variant mb-4 uppercase tracking-wider">Subject / Matière</label>
                        <div className="flex flex-wrap gap-3">
                            <button 
                                onClick={() => setSubject("Mathématiques")}
                                className={`px-5 py-2.5 rounded-xl font-semibold transition-colors flex items-center gap-2 shadow-sm ${subject === "Mathématiques" ? 'bg-primary-container text-on-primary-container' : 'border border-outline-variant bg-surface text-on-surface-variant hover:bg-surface-container'}`}>
                                <span className="material-symbols-outlined text-sm">functions</span> Math
                            </button>
                            <button 
                                onClick={() => setSubject("Physique-Chimie")}
                                className={`px-5 py-2.5 rounded-xl font-semibold transition-colors flex items-center gap-2 shadow-sm ${subject === "Physique-Chimie" ? 'bg-primary-container text-on-primary-container' : 'border border-outline-variant bg-surface text-on-surface-variant hover:bg-surface-container'}`}>
                                <span className="material-symbols-outlined text-sm">science</span> Physics/Chemistry
                            </button>
                            <button 
                                onClick={() => setSubject("Anglais")}
                                className={`px-5 py-2.5 rounded-xl font-semibold transition-colors flex items-center gap-2 shadow-sm ${subject === "Anglais" ? 'bg-primary-container text-on-primary-container' : 'border border-outline-variant bg-surface text-on-surface-variant hover:bg-surface-container'}`}>
                                <span className="material-symbols-outlined text-sm">language</span> English
                            </button>
                        </div>
                    </div>

                    {/* Upload Zone */}
                    <div className="bg-surface rounded-2xl border border-outline-variant p-6 flex flex-col h-full min-h-[400px]">
                        {correction ? (
                            <div className="flex-grow p-6 bg-surface-container-lowest rounded-xl overflow-y-auto">
                                <h3 className="font-headline-md text-on-surface mb-4">Correction Détaillée :</h3>
                                <div className="text-sm text-on-surface whitespace-pre-wrap leading-relaxed">
                                    {correction}
                                </div>
                            </div>
                        ) : (
                            <div 
                                onClick={() => fileInputRef.current?.click()}
                                className="file-upload-dashed flex-grow flex flex-col items-center justify-center p-8 md:p-12 text-center transition-colors hover:bg-primary-container/10 cursor-pointer group bg-surface-container-lowest border-2 border-dashed border-outline-variant rounded-xl">
                                
                                <input 
                                    type="file" 
                                    ref={fileInputRef} 
                                    onChange={handleFileSelect} 
                                    className="hidden" 
                                    accept="image/*,.pdf" 
                                />

                                <div className="h-20 w-20 bg-primary-container/30 rounded-full flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
                                    <span className="material-symbols-outlined text-4xl text-primary-fixed-dim">
                                        {file ? "check_circle" : "upload_file"}
                                    </span>
                                </div>
                                <h3 className="font-headline-md text-headline-md text-on-surface mb-2">
                                    {file ? file.name : "Drop your exercise here"}
                                </h3>
                                <p className="font-body-md text-body-md text-on-surface-variant mb-8">
                                    {file ? "File ready for analysis." : "Or click to browse files (PDF, JPG, PNG)"}
                                </p>
                                <button className="bg-surface border border-outline-variant text-on-surface px-8 py-3 rounded-xl font-semibold hover:bg-surface-container transition-colors shadow-sm">
                                    {file ? "Change File" : "Browse Files"}
                                </button>
                                <p className="font-label-sm text-label-sm text-outline mt-6">Max file size: 10MB</p>
                            </div>
                        )}
                    </div>
                </div>

                {/* Right Column: Settings & Actions */}
                <div className="lg:col-span-4 flex flex-col gap-6">
                    {/* Additional Notes */}
                    <div className="bg-surface rounded-2xl border border-outline-variant p-6">
                        <label className="block font-label-sm text-label-sm text-on-surface-variant mb-4 uppercase tracking-wider" htmlFor="notes">Additional Notes (Optional)</label>
                        <textarea 
                            value={notes}
                            onChange={(e) => setNotes(e.target.value)}
                            className="w-full rounded-xl border-outline-variant bg-surface-container-low text-on-surface focus:ring-primary-fixed-dim focus:border-primary-fixed-dim placeholder-outline-variant resize-none p-4" 
                            id="notes" 
                            placeholder="E.g., I'm stuck on question 3b..." 
                            rows="5"
                        ></textarea>
                    </div>

                    {/* Action Area */}
                    <div className="bg-surface rounded-2xl border border-outline-variant p-8 flex flex-col justify-center items-center text-center mt-auto bg-gradient-to-b from-surface to-secondary-container/10">
                        {isLoading ? (
                            <>
                                <div className="h-16 w-16 rounded-full flex items-center justify-center mb-6">
                                    <span className="material-symbols-outlined text-4xl text-secondary-fixed-dim animate-spin">sync</span>
                                </div>
                                <h3 className="font-headline-md text-headline-md text-on-surface mb-3">Analyse en cours...</h3>
                                <p className="font-body-md text-body-md text-on-surface-variant mb-8">Notre IA lit votre exercice et génère la correction.</p>
                            </>
                        ) : (
                            <>
                                <div className="h-16 w-16 bg-secondary-fixed-dim/20 rounded-full flex items-center justify-center mb-6">
                                    <span className="material-symbols-outlined text-4xl text-secondary-fixed-dim">auto_awesome</span>
                                </div>
                                <h3 className="font-headline-md text-headline-md text-on-surface mb-3">Ready for Analysis</h3>
                                <p className="font-body-md text-body-md text-on-surface-variant mb-8">Our AI will break down the problem step-by-step.</p>
                            </>
                        )}
                        <button 
                            onClick={handleCorrection}
                            disabled={isLoading || !file}
                            className="w-full bg-primary-container text-on-primary-container px-6 py-4 rounded-xl font-headline-md text-headline-md font-semibold hover:bg-primary-fixed transition-colors shadow-md flex justify-center items-center gap-2 disabled:opacity-50">
                            {isLoading ? "Correction..." : "Correct my Exercise"}
                        </button>
                    </div>
                </div>
            </div>
        </main>
    );
}
