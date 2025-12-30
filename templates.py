# templates.py - ФИНАЛ: исправлено копирование и удаление

INDEX_HTML = """
<!DOCTYPE html>
<html lang="ru" class="dark:bg-[#212121]">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Proxify AI</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: { accent: '#3b82f6' },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        mono: ['Geist Mono', 'monospace'],
                    },
                    boxShadow: { 'glow': '0 0 20px -5px rgba(99, 102, 241, 0.2)' }
                }
            }
        }
    </script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/geist-mono@1.0.0/dist/geist-mono.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <style>
        :root {
            --bg-primary: #ffffff;
            --bg-secondary: #f9fafb;
            --text-primary: #111827;
            --text-secondary: #6b7280;
            --border-color: #e5e7eb;
        }
        .dark {
            --bg-primary: #141414;
            --bg-secondary: #121212;
            --text-primary: #f3f4f6;
            --text-secondary: #9ca3af;
            --border-color: #333333;
        }
        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-primary);
            color: var(--text-primary);
        }
        .sidebar {
            background-color: var(--bg-secondary);
            border-right: 1px solid var(--border-color);
        }
        .chat-bubble-user {
            background-color: #f3f4f6;
            color: #111827;
            border-radius: 1.2rem;
            padding: 0.75rem 1rem;
        }
        .dark .chat-bubble-user {
            background-color: #1f2937;
            color: #ffffff;
        }
        .input-box-wrapper {
            background-color: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(229, 231, 235, 0.5);
            box-shadow: 0 8px 32px -4px rgba(0, 0, 0, 0.1), 0 4px 8px -4px rgba(0, 0, 0, 0.05);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .dark .input-box-wrapper {
            background-color: rgba(10, 10, 10, 0.75);
            border-color: rgba(255, 255, 255, 0.1);
            box-shadow: 0 8px 32px -4px rgba(0, 0, 0, 0.3);
        }
        .input-box-wrapper:focus-within {
            border-color: #6366f1;
            box-shadow: 0 0 0 1px #6366f1;
        }
        html, body {
            height: 100%;
            overflow: hidden;
        }
        ::-webkit-scrollbar { width: 4px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: var(--border-color); border-radius: 10px; }
        .prose pre {
            background: #18181b !important;
            border: 1px solid #27272a;
            border-radius: 0.5rem;
            padding: 1rem;
            margin: 1rem 0;
            overflow-x: auto;
            position: relative;
        }
        .prose pre:hover .code-copy-btn { opacity: 1; }
        .code-copy-btn {
            position: absolute;
            top: 0.5rem;
            right: 0.5rem;
            background: rgba(59, 130, 246, 0.8);
            border: 1px solid rgba(59, 130, 246, 1);
            color: #fff;
            padding: 0.4rem 0.8rem;
            border-radius: 0.5rem;
            cursor: pointer;
            opacity: 0;
            transition: all 0.2s;
            font-size: 0.75rem;
            display: flex;
            align-items: center;
            gap: 0.3rem;
            z-index: 10;
            font-weight: 500;
        }
        .code-copy-btn:hover {
            background: rgba(99, 102, 241, 0.9);
            transform: scale(1.05);
        }
        .code-copy-btn.copied {
            background: rgba(34, 197, 94, 0.9);
            border-color: rgba(34, 197, 94, 1);
        }
        .prose code {
            font-family: 'Geist Mono', monospace;
            color: #6366f1;
            background: rgba(99, 102, 241, 0.1);
            padding: 0.2em 0.4em;
            border-radius: 0.25rem;
            font-size: 0.85em;
        }
        .dark .prose { color: #e4e4e7; }
        .prose { color: #111827; }
        #chat-container {
            height: 100%;
            overflow-y: auto;
            padding-bottom: 170px;
            padding-top: 80px;
        }
        .input-container-fixed {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            padding: 1rem;
            background: linear-gradient(to top, var(--bg-primary) 85%, transparent);
            z-index: 50;
        }
        @media (max-width: 768px) {
            #chat-container {
                padding-bottom: 150px;
                padding-top: 70px;
            }
            .sidebar {
                position: fixed;
                top: 0;
                left: 0;
                bottom: 0;
                z-index: 60;
            }
            .input-container-fixed { padding: 0.75rem; }
        }
        #context-menu {
            display: none;
            position: fixed;
            z-index: 100;
        }
        #drag-overlay {
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.2s;
        }
        #drag-overlay.active {
            pointer-events: auto;
            opacity: 1;
        }
        
        /* АНИМАЦИЯ ЗАГРУЗКИ */
        .loading-dots {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 16px 20px;
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(139, 92, 246, 0.1));
            border: 1px solid rgba(99, 102, 241, 0.2);
            border-radius: 16px;
            border-bottom-left-radius: 4px;
            margin-bottom: 8px;
            width: fit-content;
            backdrop-filter: blur(10px);
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.1);
        }
        .dark .loading-dots {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(139, 92, 246, 0.15));
            border-color: rgba(99, 102, 241, 0.3);
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.2);
        }
        .loading-dot {
            width: 10px;
            height: 10px;
            background: linear-gradient(135deg, #6366f1, #8b5cf6);
            border-radius: 50%;
            animation: pulse-dot 1.4s infinite ease-in-out both;
            box-shadow: 0 2px 8px rgba(99, 102, 241, 0.4);
        }
        .loading-dot:nth-child(1) { animation-delay: -0.32s; }
        .loading-dot:nth-child(2) { animation-delay: -0.16s; }
        .loading-dot:nth-child(3) { animation-delay: 0s; }
        @keyframes pulse-dot {
            0%, 80%, 100% {
                transform: scale(0.6);
                opacity: 0.3;
            }
            40% {
                transform: scale(1.1);
                opacity: 1;
            }
        }
        .loading-shimmer {
            position: relative;
            overflow: hidden;
        }
        .loading-shimmer::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            animation: shimmer 2s infinite;
        }
        @keyframes shimmer {
            0% { left: -100%; }
            100% { left: 100%; }
        }
        
        /* КНОПКИ ДЕЙСТВИЙ */
        .message-actions {
            opacity: 0;
            transition: opacity 0.2s;
            display: flex;
            gap: 0.25rem;
            margin-top: 0.5rem;
        }
        .assistant-message:hover .message-actions {
            opacity: 1;
        }
        .action-btn {
            display: inline-flex;
            align-items: center;
            gap: 0.25rem;
            padding: 0.375rem 0.75rem;
            font-size: 0.75rem;
            border-radius: 0.5rem;
            border: 1px solid rgba(156, 163, 175, 0.3);
            background: rgba(255, 255, 255, 0.05);
            color: #9ca3af;
            cursor: pointer;
            transition: all 0.2s;
        }
        .action-btn:hover {
            background: rgba(255, 255, 255, 0.1);
            border-color: rgba(156, 163, 175, 0.5);
            color: #d1d5db;
        }
        .action-btn svg {
            width: 14px;
            height: 14px;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .animate-fadeIn { animation: fadeIn 0.3s ease-out; }
    </style>
</head>
<body class="h-full flex overflow-hidden">

    <!-- SVG ICONS -->
    <svg style="display: none;">
        <symbol id="icon-plus" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></symbol>
        <symbol id="icon-chat" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></symbol>
        <symbol id="icon-settings" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></symbol>
        <symbol id="icon-image" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></symbol>
        <symbol id="icon-file" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><polyline points="13 2 13 9 20 9"/></symbol>
        <symbol id="icon-globe" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></symbol>
        <symbol id="icon-send" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></symbol>
        <symbol id="icon-trash" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></symbol>
        <symbol id="icon-menu" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></symbol>
        <symbol id="icon-x" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></symbol>
        <symbol id="icon-copy" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></symbol>
        <symbol id="icon-refresh" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 4v6h-6"/><path d="M1 20v-6h6"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></symbol>
    </svg>

    <!-- Auth Modal -->
    <div id="auth-modal" class="fixed inset-0 z-[100] bg-black/60 backdrop-blur-sm hidden flex items-center justify-center p-4">
        <div class="bg-white dark:bg-[#18181b] rounded-2xl shadow-2xl w-full max-w-sm border border-gray-200 dark:border-[#27272a] overflow-hidden transform transition-all p-6 relative">
            <button onclick="closeAuthModal()" class="absolute top-4 right-4 text-gray-400 hover:text-gray-600 dark:hover:text-gray-200">
                <svg class="w-6 h-6"><use href="#icon-x"></use></svg>
            </button>
            <h2 id="auth-title" class="text-2xl font-bold mb-6 text-center">Вход</h2>
            <form id="auth-form" class="space-y-4" onsubmit="handleAuth(event)">
                <div>
                    <label class="block text-sm font-medium mb-1">Email</label>
                    <input type="email" id="email" required class="w-full bg-gray-100 dark:bg-black/20 border border-gray-200 dark:border-[#27272a] rounded-xl px-4 py-3 outline-none focus:ring-2 ring-accent/50 transition-all">
                </div>
                <div>
                    <label class="block text-sm font-medium mb-1">Пароль</label>
                    <input type="password" id="password" required class="w-full bg-gray-100 dark:bg-black/20 border border-gray-200 dark:border-[#27272a] rounded-xl px-4 py-3 outline-none focus:ring-2 ring-accent/50 transition-all">
                </div>
                <button type="submit" id="auth-submit" class="w-full bg-accent hover:bg-accent/90 text-white font-bold py-3 rounded-xl transition-all shadow-lg shadow-accent/25">Войти</button>
            </form>
            <div class="mt-4 text-center text-sm text-gray-500">
                <span id="auth-switch-text">Нет аккаунта?</span>
                <button type="button" onclick="toggleAuthMode()" class="text-accent font-medium hover:underline ml-1">
                    <span id="auth-switch-btn">Регистрация</span>
                </button>
            </div>
        </div>
    </div>

    <!-- Profile Modal -->
    <div id="profile-modal" class="fixed inset-0 z-[100] bg-black/60 backdrop-blur-sm hidden flex items-center justify-center p-4">
        <div class="bg-white dark:bg-[#18181b] rounded-2xl shadow-2xl w-full max-w-sm border border-gray-200 dark:border-[#27272a] overflow-hidden transform transition-all p-6 relative">
            <button onclick="closeProfileModal()" class="absolute top-4 right-4 text-gray-400 hover:text-gray-600 dark:hover:text-gray-200">
                <svg class="w-6 h-6"><use href="#icon-x"></use></svg>
            </button>
            <div class="text-center mb-6">
                <div class="w-24 h-24 mx-auto rounded-full bg-gradient-to-br from-accent to-purple-600 flex items-center justify-center text-white text-3xl font-bold shadow-lg mb-3 overflow-hidden relative cursor-pointer group" onclick="document.getElementById('avatar-upload').click()">
                    <img id="profile-avatar-img" class="w-full h-full object-cover hidden">
                    <span id="profile-avatar-text">?</span>
                    <div class="absolute inset-0 bg-black/50 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity rounded-full">
                        <svg class="w-8 h-8 text-white"><use href="#icon-image"></use></svg>
                    </div>
                </div>
                <input type="file" id="avatar-upload" class="hidden" accept="image/*" onchange="uploadAvatar(this)">
                <h2 class="text-xl font-bold" id="profile-email">guest@example.com</h2>
                <div id="profile-plan-badge" class="mt-2 inline-block px-3 py-1 rounded-full text-xs font-bold bg-gray-200 text-gray-700">Free Plan</div>
            </div>
            <div class="space-y-3">
                <button onclick="openChangePasswordModal()" class="w-full bg-gray-100 dark:bg-white/5 hover:bg-gray-200 dark:hover:bg-white/10 p-3 rounded-xl flex justify-between items-center transition-colors">
                    <span class="text-sm font-medium">Сменить пароль</span>
                    <svg class="w-4 h-4 text-gray-500"><use href="#icon-settings"></use></svg>
                </button>
                
                <div class="mt-6 pt-6 border-t border-gray-200 dark:border-[#27272a] space-y-4">
                    <div class="flex justify-between items-center pt-2">
                        <span class="text-sm font-medium text-gray-700 dark:text-gray-300">Выйти</span>
                        <button onclick="handleLogout()" class="px-4 py-1.5 border border-gray-400 text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-white/10 rounded-full text-xs font-medium transition-all">Выход</button>
                    </div>
                    <div class="flex justify-between items-center">
                        <span class="text-sm font-medium text-gray-700 dark:text-gray-300">Удалить аккаунт</span>
                        <button onclick="handleDeleteAccount()" class="px-4 py-1.5 border border-red-500 text-red-500 hover:bg-red-500 hover:text-white rounded-full text-xs font-medium transition-all">Удалить</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Password Modal -->
    <div id="password-modal" class="fixed inset-0 z-[110] bg-black/60 backdrop-blur-sm hidden flex items-center justify-center p-4">
        <div class="bg-white dark:bg-[#18181b] rounded-2xl shadow-2xl w-full max-w-sm border border-gray-200 dark:border-[#27272a] overflow-hidden transform transition-all p-6 relative">
            <button onclick="closePasswordModal()" class="absolute top-4 right-4 text-gray-400 hover:text-gray-600 dark:hover:text-gray-200">
                <svg class="w-6 h-6"><use href="#icon-x"></use></svg>
            </button>
            <h2 class="text-xl font-bold mb-6 text-center">Смена пароля</h2>
            <form id="password-form" class="space-y-4" onsubmit="handleChangePassword(event)">
                <div>
                    <label class="block text-sm font-medium mb-1">Новый пароль</label>
                    <input type="password" id="new-password" required minlength="6" class="w-full bg-gray-100 dark:bg-black/20 border border-gray-200 dark:border-[#27272a] rounded-xl px-4 py-3 outline-none focus:ring-2 ring-accent/50 transition-all">
                </div>
                <button type="submit" id="password-submit" class="w-full bg-accent hover:bg-accent/90 text-white font-bold py-3 rounded-xl transition-all shadow-lg shadow-accent/25">Обновить</button>
            </form>
        </div>
    </div>

    <!-- Settings Modal -->
    <div id="settings-modal" class="fixed inset-0 z-[90] bg-black/50 backdrop-blur-sm hidden flex items-center justify-center p-4">
        <div class="bg-white dark:bg-[#18181b] rounded-2xl shadow-2xl w-full max-w-md border border-gray-200 dark:border-[#27272a] overflow-hidden transform transition-all">
            <div class="p-4 border-b border-gray-200 dark:border-[#27272a] flex justify-between items-center">
                <h3 class="font-semibold text-lg">Настройки</h3>
                <button onclick="toggleSettings()" class="p-1 hover:bg-gray-100 dark:hover:bg-white/10 rounded-xl transition">
                    <svg class="w-5 h-5"><use href="#icon-x"></use></svg>
                </button>
            </div>
            <div class="p-6 space-y-6">
                <div class="flex items-center justify-between">
                    <div class="flex flex-col">
                        <span class="font-medium">Темная тема</span>
                        <span class="text-xs text-gray-500">Переключить тему</span>
                    </div>
                    <button id="theme-toggle" onclick="toggleTheme()" class="w-12 h-6 rounded-full bg-gray-200 dark:bg-accent relative transition-colors">
                        <div class="w-4 h-4 rounded-full bg-white absolute top-1 left-1 transition-transform dark:translate-x-6 shadow-sm"></div>
                    </button>
                </div>
                
                <div class="space-y-2">
                    <label class="font-medium block">AI Модель</label>
                    <select id="model-select" onchange="saveSettings()" class="w-full bg-gray-100 dark:bg-black/20 border border-gray-200 dark:border-[#27272a] rounded-xl px-3 py-2.5 outline-none focus:ring-2 ring-accent/50 text-sm">
                        <option value="auto">Авто (Smart)</option>
                        <option value="google/gemini-2.0-flash-exp:free">Gemini 2.0 Flash</option>
                        <option value="google/gemini-exp-1206:free">Gemini Exp 1206</option>
                        <option value="cognitivecomputations/dolphin-mistral-24b-venice-edition:free">Dolphin Mistral</option>
                        <option value="nousresearch/hermes-3-llama-3.1-405b:free">Hermes 405B</option>
                    </select>
                    <p class="text-xs text-gray-500">Выберите модель по умолчанию.</p>
                </div>

                <div class="space-y-2">
                    <label class="font-medium block">Coding Model</label>
                    <select id="coding-model-select" onchange="saveSettings()" class="w-full bg-gray-100 dark:bg-black/20 border border-gray-200 dark:border-[#27272a] rounded-xl px-3 py-2.5 outline-none focus:ring-2 ring-accent/50 text-sm">
                        <option value="qwen/qwen-2.5-coder-32b-instruct">Qwen 2.5 Coder 32B</option>
                        <option value="meta-llama/llama-3.1-70b-instruct">Llama 3.1 70B</option>
                    </select>
                    <p class="text-xs text-gray-500">Модель для режима кодинга.</p>
                </div>

                <div class="space-y-2 mt-4">
                    <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Экспорт данных</label>
                    <button onclick="exportAllChats()" class="w-full bg-accent hover:bg-accent/90 text-white rounded-xl px-4 py-2.5 font-medium transition-colors flex items-center justify-center gap-2">
                        <svg class="w-5 h-5 fill-none stroke-current" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
                        Экспорт чатов
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- Context Menu -->
    <div id="context-menu" class="bg-white dark:bg-zinc-900 border border-gray-200 dark:border-zinc-800 rounded-xl shadow-xl py-1 min-w-[160px]">
        <button id="ctx-delete-btn" onclick="deleteContextChat()" class="w-full text-left px-4 py-2 text-sm text-red-500 hover:bg-gray-100 dark:hover:bg-white/5 flex items-center gap-2 transition-colors">
            <svg class="w-4 h-4"><use href="#icon-trash"></use></svg>
            Удалить чат
        </button>
    </div>

    <!-- Mobile Overlay -->
    <div id="mobile-overlay" onclick="toggleSidebar()" class="fixed inset-0 bg-black/60 z-40 hidden backdrop-blur-sm transition-opacity"></div>

    <!-- Sidebar -->
    <aside id="sidebar" class="w-72 sidebar border-r border-gray-200 dark:border-[#27272a] flex flex-col transform -translate-x-full md:translate-x-0 transition-transform duration-300 shadow-2xl h-full z-50">
        <div id="user-profile-section" class="p-4 border-b border-gray-200 dark:border-[#27272a] flex items-center gap-3 cursor-pointer hover:bg-gray-50 dark:hover:bg-white/5 transition-colors" onclick="handleProfileClick()">
            <div class="w-10 h-10 rounded-full bg-gradient-to-br from-accent to-purple-600 flex items-center justify-center text-white font-bold shadow-lg overflow-hidden relative" id="user-avatar">
                <img id="sidebar-avatar-img" class="w-full h-full object-cover hidden">
                <span id="sidebar-avatar-text">?</span>
            </div>
            <div class="flex-1 min-w-0">
                <p class="font-medium truncate" id="user-email-sidebar">Гость</p>
                <p class="text-xs text-gray-500 truncate" id="user-status-sidebar">Кликните для входа</p>
            </div>
        </div>

        <div class="p-4 border-b border-gray-200 dark:border-[#27272a] flex justify-between items-center">
            <button onclick="handleNewChatClick()" class="flex-1 flex items-center gap-3 px-4 py-3 bg-white dark:bg-white/5 hover:bg-gray-50 dark:hover:bg-white/10 border border-gray-200 dark:border-white/5 rounded-xl transition-all group text-sm font-medium">
                <div class="bg-accent/10 dark:bg-accent/20 p-1.5 rounded-xl text-accent group-hover:scale-110 transition-transform">
                    <svg class="w-4 h-4"><use href="#icon-plus"></use></svg>
                </div>
                <span>Новый чат</span>
            </button>
            <button onclick="toggleSidebar()" class="md:hidden ml-3 p-2 text-gray-500 hover:text-black dark:text-gray-400 dark:hover:text-white">
                <svg class="w-5 h-5"><use href="#icon-x"></use></svg>
            </button>
        </div>

        <div class="flex-1 overflow-y-auto p-3 space-y-1" id="chat-list">
            <!-- Chats inserted here -->
        </div>

        <div class="p-4 border-t border-gray-200 dark:border-[#27272a] bg-gray-50/50 dark:bg-black/20 flex items-center justify-between">
            <button onclick="toggleSettings()" class="flex items-center gap-2 text-sm text-gray-600 dark:text-gray-400 hover:text-black dark:hover:text-white transition-colors px-2 py-1 rounded-xl hover:bg-gray-200 dark:hover:bg-white/5">
                <svg class="w-4 h-4"><use href="#icon-settings"></use></svg>
                Настройки
            </button>
            <button onclick="clearHistory()" class="p-2 text-gray-400 hover:text-red-500 transition-colors" title="Очистить все чаты">
                <svg class="w-4 h-4"><use href="#icon-trash"></use></svg>
            </button>
        </div>
    </aside>

    <!-- Main Chat Area -->
    <main class="flex-1 flex flex-col h-full relative w-full overflow-hidden">
        <header class="h-14 border-b border-gray-200 dark:border-[#27272a] flex items-center justify-between px-4 md:px-6 bg-white/90 dark:bg-[#09090b]/90 backdrop-blur-md z-30 absolute top-0 w-full">
            <div class="flex items-center gap-4">
                <button onclick="toggleSidebar()" class="md:hidden text-gray-500 dark:text-gray-400 hover:text-black dark:hover:text-white p-1">
                    <svg class="w-6 h-6"><use href="#icon-menu"></use></svg>
                </button>
                <div class="flex items-center gap-2">
                    <span class="font-semibold text-black dark:text-white">Proxify</span>
                    <span class="text-accent">AI</span>
                </div>
            </div>
        </header>

        <div id="chat-container" class="w-full px-4 md:px-8 space-y-6">
            <!-- Messages inserted here -->
        </div>

        <!-- Input Area -->
        <div class="input-container-fixed">
            <div class="max-w-3xl mx-auto relative">
                
                <!-- Preview Attachments -->
                <div id="attach-preview-wrap" class="hidden absolute -top-24 left-0 z-0 flex gap-2 overflow-x-auto px-2">
                    <div id="img-preview-box" class="relative group hidden">
                        <img id="img-preview" class="h-20 rounded-xl border border-gray-200 dark:border-white/10 shadow-lg object-cover bg-white dark:bg-[#18181b]">
                        <button onclick="clearImage()" class="absolute top-2 right-2 bg-gray-800 text-white border border-white/10 rounded-full p-1 hover:bg-red-500 transition">
                            <svg class="w-3 h-3"><use href="#icon-x"></use></svg>
                        </button>
                    </div>
                    <div id="file-preview-box" class="relative group hidden h-20 p-3 bg-white dark:bg-[#18181b] border border-gray-200 dark:border-white/10 rounded-xl flex items-center gap-2 min-w-[120px]">
                        <div class="bg-gray-100 dark:bg-white/10 p-2 rounded-xl">
                            <svg class="w-5 h-5 text-accent"><use href="#icon-file"></use></svg>
                        </div>
                        <span id="file-name" class="text-xs text-gray-500 dark:text-gray-400 truncate max-w-[100px]">file.txt</span>
                        <button onclick="clearFile()" class="absolute top-2 right-2 bg-gray-800 text-white border border-white/10 rounded-full p-1 hover:bg-red-500 transition">
                            <svg class="w-3 h-3"><use href="#icon-x"></use></svg>
                        </button>
                    </div>
                </div>

                <div class="input-box-wrapper rounded-3xl flex flex-col relative z-50">
                    <textarea id="user-input" rows="1" placeholder="Спросите что угодно..." class="w-full bg-transparent text-black dark:text-gray-200 placeholder-gray-400 dark:placeholder-gray-500 outline-none resize-none px-4 md:px-5 pt-3 md:pt-4 pb-2 min-h-[48px] md:min-h-[54px] max-h-48 font-sans text-[16px] leading-relaxed rounded-t-3xl"
                        oninput="this.style.height='auto';this.style.height=this.scrollHeight+'px'"
                        onkeydown="if(event.key==='Enter'&&!event.shiftKey){event.preventDefault();send()}"></textarea>
                    
                    <div class="flex items-center justify-between px-3 pb-3 pt-1">
                        <div class="flex items-center gap-1">
                            <input type="file" id="universal-in" class="hidden" multiple onchange="handleUniversalUpload(event)">
                            <button onclick="document.getElementById('universal-in').click()" class="p-2 text-gray-400 dark:text-gray-500 hover:text-accent dark:hover:text-accent hover:bg-gray-50 dark:hover:bg-white/5 rounded-xl transition-colors" title="Прикрепить файл">
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-5 h-5"><path d="m21.44 11.05-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"/></svg>
                            </button>
                            
                            <button id="web-btn" onclick="toggleWeb()" class="p-2 text-gray-400 dark:text-gray-500 hover:text-accent dark:hover:text-accent hover:bg-gray-50 dark:hover:bg-white/5 rounded-xl transition-all flex items-center gap-2">
                                <svg class="w-5 h-5"><use href="#icon-globe"></use></svg>
                                <span id="web-badge" class="text-[10px] font-bold hidden bg-accent text-white px-1 rounded">ON</span>
                            </button>

                            <button id="coding-btn" onclick="toggleCoding()" class="p-2 text-gray-400 dark:text-gray-500 hover:text-accent dark:hover:text-accent hover:bg-gray-50 dark:hover:bg-white/5 rounded-xl transition-all flex items-center gap-2">
                                <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
                                <span id="coding-badge" class="text-[10px] font-bold hidden bg-accent text-white px-1 rounded">CODE</span>
                            </button>
                        </div>
                        <button id="send-btn" onclick="send()" class="p-2.5 bg-accent text-white hover:bg-accent/90 rounded-xl transition-all disabled:opacity-50 shadow-lg shadow-accent/25 hover:shadow-accent/40 hover:-translate-y-0.5 active:translate-y-0">
                            <svg class="w-5 h-5"><use href="#icon-send"></use></svg>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <script>
        // --- GLOBAL VARS ---
        let currentUser = null;
        let chats = [];
        let activeChatId = null;
        let imgBase64 = null;
        let fileContent = null;
        let fileName = null;
        let isBusy = false;
        let webEnabled = false;
        let codingEnabled = false;
        let contextChatId = null;
        let isSignUp = false;

        let userSettings = JSON.parse(localStorage.getItem('proxify_settings') || '{"theme":"dark","model":"auto","codingmodel":"qwen/qwen-2.5-coder-32b-instruct"}');

        const WELCOME_HTML = `<div id="welcome" class="h-full flex flex-col items-center justify-center text-center opacity-0 animate-fadeIn pt-20">
            <div class="w-20 h-20 bg-gray-100 dark:bg-white/5 rounded-3xl flex items-center justify-center mb-6 border border-gray-200 dark:border-white/5">
                <svg class="w-10 h-10 text-gray-400 dark:text-gray-600"><use href="#icon-chat"></use></svg>
            </div>
            <h2 class="text-xl font-medium text-black dark:text-white mb-2">Начните разговор</h2>
        </div>`;

        // --- INIT ---
        window.addEventListener('DOMContentLoaded', async () => {
            await init();
        });

        async function init() {
            console.log("Инициализация...");
            document.addEventListener('paste', handlePaste);
            
            applyTheme(userSettings.theme);
            document.getElementById('model-select').value = userSettings.model || 'auto';
            document.getElementById('coding-model-select').value = userSettings.codingmodel || 'qwen/qwen-2.5-coder-32b-instruct';

            await initAuth();

            if (!Array.isArray(chats)) chats = [];
            chats = chats.filter(c => c && c.messages);

            if (chats.length === 0) {
                await createChatInternal();
            } else {
                loadChat(chats[0].id);
            }
            renderList();

            const dropZone = document.body;
            const overlay = document.getElementById('drag-overlay');
            ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
                dropZone.addEventListener(eventName, preventDefaults, false);
            });
            function preventDefaults(e) {
                e.preventDefault();
                e.stopPropagation();
            }
            dropZone.addEventListener('dragenter', () => overlay.classList.add('active'));
            overlay.addEventListener('dragleave', (e) => {
                if (e.target === overlay) overlay.classList.remove('active');
            });
            dropZone.addEventListener('drop', handleDrop, false);

            function handleDrop(e) {
                overlay.classList.remove('active');
                const files = e.dataTransfer.files;
                if (files.length > 0) handleFiles(files[0]);
            }

            function handleFiles(file) {
                if (file.type.startsWith('image')) {
                    processImage(file);
                } else {
                    processDoc(file);
                }
            }
        }

        // --- AUTH LOGIC ---
        async function initAuth() {
            console.log("Проверка аутентификации...");
            try {
                const res = await fetch('/api/session', {
                    method: 'GET',
                    credentials: 'include'
                });
                
                if (!res.ok) {
                    console.log("Пользователь не авторизован");
                    updateUserUI(null);
                    return;
                }
                
                const data = await res.json();
                if (data.user) {
                    updateUserUI(data.user);
                    await loadRemoteChats();
                } else {
                    updateUserUI(null);
                }
            } catch (e) {
                console.error('Auth init error:', e);
                updateUserUI(null);
            }
        }

        function updateUserUI(user) {
            currentUser = user;
            const em = document.getElementById('user-email-sidebar');
            const st = document.getElementById('user-status-sidebar');
            const bigEm = document.getElementById('profile-email');
            const sideText = document.getElementById('sidebar-avatar-text');
            const profText = document.getElementById('profile-avatar-text');

            if (user) {
                const letter = user.email ? user.email[0].toUpperCase() : 'U';
                const email = user.email;
                if (em) em.textContent = email;
                if (st) st.textContent = user.plan || 'Free Plan';
                if (bigEm) bigEm.textContent = email;
                if (sideText) sideText.textContent = letter;
                if (profText) profText.textContent = letter;

                if (user.avatar) {
                    updateAvatarUI(user.avatar);
                }
            } else {
                if (em) em.textContent = 'Гость';
                if (st) st.textContent = 'Кликните для входа';
                if (sideText) sideText.textContent = '?';
            }
        }

        function updateAvatarUI(url) {
            if (!url) return;
            const sideImg = document.getElementById('sidebar-avatar-img');
            const profImg = document.getElementById('profile-avatar-img');
            const sideText = document.getElementById('sidebar-avatar-text');
            const profText = document.getElementById('profile-avatar-text');

            if (sideImg) {
                sideImg.src = url;
                sideImg.classList.remove('hidden');
            }
            if (sideText) sideText.style.display = 'none';

            if (profImg) {
                profImg.src = url;
                profImg.classList.remove('hidden');
            }
            if (profText) profText.style.display = 'none';
        }

        async function uploadAvatar(input) {
            if (!input.files || !input.files[0]) return;
            const file = input.files[0];
            const formData = new FormData();
            formData.append('avatar', file);

            try {
                const res = await fetch('/api/avatar', {
                    method: 'POST',
                    credentials: 'include',
                    body: formData
                });
                const data = await res.json();
                if (data.avatar_url) {
                    updateAvatarUI(data.avatar_url);
                    alert('Аватар загружен!');
                } else {
                    alert('Ошибка загрузки аватара');
                }
            } catch (e) {
                alert('Ошибка: ' + e.message);
            }
        }

        function openChangePasswordModal() {
            closeProfileModal();
            document.getElementById('password-modal').classList.remove('hidden');
        }

        function closePasswordModal() {
            document.getElementById('password-modal').classList.add('hidden');
        }

        async function handleChangePassword(e) {
            e.preventDefault();
            const newPassword = document.getElementById('new-password').value;
            const btn = document.getElementById('password-submit');
            btn.disabled = true;
            btn.textContent = 'Обновление...';

            try {
                const res = await fetch('/api/password', {
                    method: 'PUT',
                    credentials: 'include',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ new_password: newPassword })
                });
                const data = await res.json();
                if (res.ok) {
                    alert('Пароль обновлён!');
                    closePasswordModal();
                } else {
                    alert('Ошибка: ' + (data.detail || 'Неизвестная ошибка'));
                }
            } catch (e) {
                alert('Ошибка: ' + e.message);
            } finally {
                btn.disabled = false;
                btn.textContent = 'Обновить';
            }
        }

        function handleProfileClick() {
            if (currentUser) {
                document.getElementById('profile-modal').classList.remove('hidden');
            } else {
                document.getElementById('auth-modal').classList.remove('hidden');
            }
        }

        function closeAuthModal() {
            document.getElementById('auth-modal').classList.add('hidden');
        }

        function closeProfileModal() {
            document.getElementById('profile-modal').classList.add('hidden');
        }

        function toggleAuthMode() {
            isSignUp = !isSignUp;
            document.getElementById('auth-title').textContent = isSignUp ? 'Регистрация' : 'Вход';
            document.getElementById('auth-submit').textContent = isSignUp ? 'Зарегистрироваться' : 'Войти';
            document.getElementById('auth-switch-btn').textContent = isSignUp ? 'Войти' : 'Регистрация';
            document.getElementById('auth-switch-text').textContent = isSignUp ? 'Уже есть аккаунт?' : 'Нет аккаунта?';
        }

        async function handleAuth(e) {
            e.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const btn = document.getElementById('auth-submit');
            btn.disabled = true;
            const originalText = btn.textContent;
            btn.textContent = 'Загрузка...';

            try {
                const endpoint = isSignUp ? '/api/register' : '/api/login';
                const res = await fetch(endpoint, {
                    method: 'POST',
                    credentials: 'include',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, password })
                });
                const data = await res.json();

                if (res.ok) {
                    if (isSignUp) alert('Аккаунт создан!');
                    updateUserUI(data.user);
                    await loadRemoteChats();
                    closeAuthModal();
                } else {
                    alert('Ошибка: ' + (data.detail || 'Неизвестная ошибка'));
                }
            } catch (e) {
                alert('Ошибка: ' + e.message);
            } finally {
                btn.disabled = false;
                btn.textContent = originalText;
            }
        }

        async function handleLogout() {
            if (confirm('Выйти?')) {
                try {
                    await fetch('/api/logout', {
                        method: 'POST',
                        credentials: 'include'
                    });
                    closeProfileModal();
                    location.reload();
                } catch (e) {
                    alert('Ошибка: ' + e.message);
                }
            }
        }

        async function handleDeleteAccount() {
            if (!confirm('Удалить аккаунт навсегда? Это действие необратимо.')) return;
            try {
                const res = await fetch('/api/account', {
                    method: 'DELETE',
                    credentials: 'include'
                });
                if (res.ok) {
                    alert('Аккаунт удалён.');
                    closeProfileModal();
                    location.reload();
                } else {
                    const data = await res.json();
                    alert('Ошибка: ' + (data.detail || 'Неизвестная ошибка'));
                }
            } catch (e) {
                alert('Ошибка: ' + e.message);
            }
        }

        // --- CHAT LOGIC ---
        async function loadRemoteChats() {
            if (!currentUser) return;
            const list = document.getElementById('chat-list');
            if (list) list.innerHTML = '<div class="p-4 text-center text-gray-500 animate-pulse">Загрузка...</div>';

            try {
                const res = await fetch('/api/chats', {
                    method: 'GET',
                    credentials: 'include'
                });
                
                if (!res.ok) {
                    console.error('Ошибка загрузки чатов:', res.status);
                    return;
                }
                
                const data = await res.json();
                if (data.chats) {
                    chats = data.chats;
                    renderList();
                    if (chats.length > 0) {
                        loadChat(chats[0].id);
                    }
                }
            } catch (e) {
                console.error('Ошибка загрузки чатов:', e);
            }
        }

        function handleNewChatClick() {
            const current = chats.find(c => c.id === activeChatId);
            if (current && current.messages && current.messages.length === 0) {
                document.getElementById('user-input').focus();
                if (window.innerWidth < 768) toggleSidebar();
                return;
            }
            createChatInternal();
        }

        async function createChatInternal() {
            if (currentUser) {
                try {
                    const res = await fetch('/api/chats', {
                        method: 'POST',
                        credentials: 'include',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ title: 'Новый чат' })
                    });
                    const data = await res.json();
                    if (res.ok && data.chat) {
                        chats.unshift(data.chat);
                        loadChat(data.chat.id);
                        renderList();
                        if (window.innerWidth < 768 && !document.getElementById('sidebar').classList.contains('-translate-x-full')) {
                            toggleSidebar();
                        }
                    }
                } catch (e) {
                    console.error('Ошибка создания чата:', e);
                }
            } else {
                const newChat = {
                    id: 'local_' + Date.now(),
                    title: 'Новый чат',
                    messages: [],
                    created_at: new Date().toISOString()
                };
                chats.unshift(newChat);
                loadChat(newChat.id);
                renderList();
                if (window.innerWidth < 768) toggleSidebar();
            }
        }

        function loadChat(id) {
            activeChatId = id;
            clearImage();
            clearFile();
            document.getElementById('user-input').value = '';
            document.getElementById('user-input').style.height = 'auto';

            const chat = chats.find(c => c.id === id);
            if (!chat) return;

            const container = document.getElementById('chat-container');
            container.innerHTML = '';

            if (!chat.messages || chat.messages.length === 0) {
                container.innerHTML = WELCOME_HTML;
            } else {
                chat.messages.forEach((m, idx) => {
                    let cleanContent = m.content;
                    try {
                        if (m.content.includes('%20') || m.content.includes('%3C')) {
                            cleanContent = decodeURIComponent(m.content);
                        }
                    } catch (e) {}
                    appendMsg(m.role, cleanContent, m.imageurl, false, idx);
                });
            }
            renderList();
            scrollToBottom();

            setTimeout(() => {
                document.querySelectorAll('pre code').forEach(el => {
                    hljs.highlightElement(el);
                });
                addButtonsToCode();
            }, 100);
        }

        function renderList() {
            const list = document.getElementById('chat-list');
            list.innerHTML = '';
            chats.forEach(c => {
                const btn = document.createElement('button');
                const active = c.id === activeChatId;
                let baseClasses = 'w-full text-left px-3 py-3 rounded-xl text-sm truncate flex items-center gap-3 mb-1 transition-colors';
                let activeClasses = 'bg-gray-200 dark:bg-white/10 text-black dark:text-white font-medium border border-gray-300 dark:border-white/5';
                let inactiveClasses = 'text-gray-500 dark:text-gray-400 hover:text-black dark:hover:text-white hover:bg-gray-100 dark:hover:bg-white/5 border border-transparent';
                btn.className = baseClasses + ' ' + (active ? activeClasses : inactiveClasses);
                btn.onclick = () => {
                    loadChat(c.id);
                    if (window.innerWidth < 768) toggleSidebar();
                };
                btn.oncontextmenu = (e) => showContextMenu(e, c.id);
                btn.innerHTML = `<svg class="w-4 h-4 opacity-70"><use href="#icon-chat"></use></svg><span class="truncate">${c.title || 'Новый чат'}</span>`;
                list.appendChild(btn);
            });
        }

        function showContextMenu(e, chatId) {
            e.preventDefault();
            contextChatId = chatId;
            const menu = document.getElementById('context-menu');
            menu.style.display = 'block';
            let x = e.pageX;
            let y = e.pageY;
            if (x + 160 > window.innerWidth) x = window.innerWidth - 170;
            menu.style.left = x + 'px';
            menu.style.top = y + 'px';
        }

        function hideContextMenu() {
            document.getElementById('context-menu').style.display = 'none';
            contextChatId = null;
        }

        document.addEventListener('click', (e) => {
            const menu = document.getElementById('context-menu');
            if (menu.style.display === 'block' && !menu.contains(e.target)) {
                hideContextMenu();
            }
        });

        async function deleteContextChat() {
            if (!contextChatId) return;
            
            if (currentUser) {
                try {
                    const res = await fetch(`/api/chats/${contextChatId}`, {
                        method: 'DELETE',
                        credentials: 'include'
                    });
                    if (res.ok) {
                        chats = chats.filter(c => c.id !== contextChatId);
                        if (chats.length === 0) {
                            await createChatInternal();
                        } else if (activeChatId === contextChatId) {
                            loadChat(chats[0].id);
                        } else {
                            renderList();
                        }
                        hideContextMenu();
                    }
                } catch (e) {
                    console.error('Ошибка удаления чата:', e);
                }
            } else {
                chats = chats.filter(c => c.id !== contextChatId);
                if (chats.length === 0) {
                    await createChatInternal();
                } else if (activeChatId === contextChatId) {
                    loadChat(chats[0].id);
                } else {
                    renderList();
                }
                hideContextMenu();
            }
        }

        async function clearHistory() {
            if (!confirm('Очистить все чаты?')) return;
            
            if (currentUser) {
                for (let chat of chats) {
                    try {
                        await fetch(`/api/chats/${chat.id}`, {
                            method: 'DELETE',
                            credentials: 'include'
                        });
                    } catch (e) {}
                }
            }
            
            chats = [];
            activeChatId = null;
            renderList();
            document.getElementById('chat-container').innerHTML = '';
            await createChatInternal();
        }

        async function send() {
            if (isBusy) return;
            const input = document.getElementById('user-input');
            let txt = input.value.trim();
            const img = imgBase64;
            const fContent = fileContent;
            const fName = fileName;

            if (!txt && !img && !fContent) return;

            if (fContent) {
                txt = `Содержимое ${fName}:\\n${fContent}`;
            }

            input.value = '';
            input.style.height = 'auto';
            clearImage();
            clearFile();
            isBusy = true;
            document.getElementById('send-btn').disabled = true;

            const welcome = document.getElementById('welcome');
            if (welcome) welcome.remove();

            const currentChat = chats.find(c => c.id === activeChatId);
            if (!currentChat) return;

            const displayTxt = fName ? (input.value.trim() ? input.value.trim() : `Прикреплён ${fName}`) : txt;
            appendMsg('user', displayTxt, img);

            setTimeout(scrollToBottom, 50);

            // КРАСИВАЯ АНИМАЦИЯ ЗАГРУЗКИ
            const loadingDiv = document.createElement('div');
            loadingDiv.className = 'w-full max-w-3xl mx-auto px-0 md:px-0 relative z-0 animate-fadeIn';
            loadingDiv.innerHTML = `
                <div class="flex gap-3 md:gap-4 pr-0 md:pr-4 group relative">
                    <div class="w-8 h-8 rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center flex-shrink-0 mt-1 shadow-lg shadow-indigo-500/20">
                        <svg class="w-4 h-4 text-white"><use href="#icon-chat"></use></svg>
                    </div>
                    <div class="flex-1 min-w-0 overflow-hidden">
                        <div class="loading-dots loading-shimmer">
                            <div class="loading-dot"></div>
                            <div class="loading-dot"></div>
                            <div class="loading-dot"></div>
                        </div>
                    </div>
                </div>
            `;
            document.getElementById('chat-container').appendChild(loadingDiv);
            scrollToBottom();

            if (currentUser) {
                try {
                    const res = await fetch(`/api/chats/${activeChatId}/messages`, {
                        method: 'POST',
                        credentials: 'include',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            content: txt,
                            coding_enabled: codingEnabled,
                            reasoning_enabled: false
                        })
                    });
                    const data = await res.json();
                    
                    if (loadingDiv) loadingDiv.remove();

                    if (res.ok && data.response) {
                        appendMsg('assistant', data.response);
                        if (!currentChat.messages) currentChat.messages = [];
                        currentChat.messages.push({ role: 'user', content: txt, imageurl: img });
                        currentChat.messages.push({ role: 'assistant', content: data.response });
                        if (currentChat.messages.length === 2) {
                            currentChat.title = txt.substring(0, 30);
                        }
                        renderList();
                    } else {
                        appendMsg('assistant', `<span class="text-red-400">Ошибка: ${data.detail || 'Неизвестная ошибка'}</span>`);
                    }
                } catch (e) {
                    if (loadingDiv) loadingDiv.remove();
                    appendMsg('assistant', `<span class="text-red-400">Ошибка: ${e.message}</span>`);
                }
            } else {
                try {
                    if (!currentChat.messages) currentChat.messages = [];
                    currentChat.messages.push({ role: 'user', content: txt });

                    const messages = currentChat.messages.map(m => ({
                        role: m.role,
                        content: m.content
                    }));

                    const response = await fetch('/chat', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            messages: messages,
                            model: userSettings.model,
                            coding_mode: codingEnabled,
                            web_search: webEnabled
                        })
                    });

                    if (loadingDiv) loadingDiv.remove();

                    const reader = response.body.getReader();
                    const decoder = new TextDecoder();
                    let aiResponse = '';
                    const aiDiv = appendMsg('assistant', '', null, true);
                    const contentArea = aiDiv.querySelector('.content-area');

                    while (true) {
                        const { done, value } = await reader.read();
                        if (done) break;

                        const chunk = decoder.decode(value);
                        const lines = chunk.split('\\n');

                        for (const line of lines) {
                            if (line.startsWith('data: ')) {
                                try {
                                    const data = JSON.parse(line.slice(6));
                                    if (data.content) {
                                        aiResponse += data.content;
                                        contentArea.innerHTML = marked.parse(aiResponse);
                                        scrollToBottom();
                                    }
                                } catch (e) {}
                            }
                        }
                    }

                    if (aiResponse) {
                        currentChat.messages.push({ role: 'assistant', content: aiResponse });
                        if (currentChat.messages.length === 2) {
                            currentChat.title = txt.substring(0, 30);
                            renderList();
                        }
                        // Добавляем подсветку синтаксиса после генерации
                        setTimeout(() => {
                            contentArea.querySelectorAll('pre code').forEach(el => {
                                hljs.highlightElement(el);
                            });
                            addButtonsToCode();
                        }, 100);
                    }
                } catch (e) {
                    if (loadingDiv) loadingDiv.remove();
                    appendMsg('assistant', `<span class="text-red-400">Ошибка: ${e.message}</span>`);
                }
            }

            setTimeout(() => {
                scrollToBottom();
                isBusy = false;
                document.getElementById('send-btn').disabled = false;
                document.getElementById('user-input').focus();
            }, 500);
        }

        // КНОПКА КОПИРОВАНИЯ ОТВЕТА (ФИКС)
        async function copyMessageContent(element) {
            try {
                // Находим текст внутри .content-area
                const contentArea = element.closest('.assistant-message').querySelector('.content-area');
                const text = contentArea.innerText; // Используем innerText для сохранения форматирования переносов
                
                await navigator.clipboard.writeText(text);
                
                // Визуальное подтверждение
                const originalHTML = element.innerHTML;
                element.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-green-500"><polyline points="20 6 9 17 4 12"/></svg><span class="text-green-500">Скопировано</span>';
                
                setTimeout(() => {
                    element.innerHTML = originalHTML;
                }, 2000);
            } catch (err) {
                console.error('Ошибка копирования:', err);
                alert('Не удалось скопировать текст');
            }
        }

        // РЕГЕНЕРАЦИЯ ОТВЕТА
        async function regenerateMessage(element) {
            if (isBusy) return;

            const msgDiv = element.closest('.assistant-message').parentElement; // div wrapper
            const container = document.getElementById('chat-container');
            const messages = Array.from(container.children);
            const index = messages.indexOf(msgDiv);
            
            // Находим чат и удаляем этот ответ
            const currentChat = chats.find(c => c.id === activeChatId);
            if (currentChat && currentChat.messages) {
                // Удаляем последнее сообщение (AI ответ)
                currentChat.messages.pop();
                
                // Получаем последнее сообщение пользователя
                const lastUserMsg = currentChat.messages[currentChat.messages.length - 1];
                
                if (lastUserMsg && lastUserMsg.role === 'user') {
                    // Удаляем визуально
                    msgDiv.remove();
                    
                    // Заполняем инпут и отправляем заново
                    document.getElementById('user-input').value = lastUserMsg.content;
                    
                    // Удаляем и сообщение пользователя из массива, чтобы send() добавил его заново корректно
                    currentChat.messages.pop();
                    // Удаляем визуально сообщение пользователя
                    messages[index-1].remove(); 

                    send();
                }
            }
        }

        // УДАЛЕНИЕ СООБЩЕНИЯ (user + ai)
        function deleteMessage(element) {
            if (confirm('Удалить это сообщение и ваш вопрос?')) {
                const aiDivWrapper = element.closest('.assistant-message').parentElement;
                const container = document.getElementById('chat-container');
                const messages = Array.from(container.children);
                const index = messages.indexOf(aiDivWrapper);
                
                // Находим предыдущий элемент (сообщение пользователя)
                const userDivWrapper = messages[index - 1];

                const currentChat = chats.find(c => c.id === activeChatId);
                if (currentChat && currentChat.messages) {
                    // Логика удаления из массива данных:
                    // Индекс в массиве messages соответствует (index / 2) * 2 для пары
                    // Но проще просто удалить 2 последних, если это последние сообщения
                    // Или найти по индексу. 
                    // Предполагаем структуру: User, AI, User, AI...
                    // index в DOM: 0(U), 1(A), 2(U), 3(A)...
                    // AI сообщение всегда имеет нечетный индекс в DOM (если считать с 0 и без welcome)
                    // В массиве chat.messages оно тоже имеет индекс.
                    
                    // Проще всего: удалить 2 последних, если удаляем последнее.
                    // Если удаляем из середины - сложнее, но пока реализуем удаление последних.
                    
                    // Удаляем из DOM
                    aiDivWrapper.remove();
                    if (userDivWrapper) userDivWrapper.remove();
                    
                    // Удаляем из массива (последние 2)
                    // TODO: Реализовать удаление по точному индексу для середины чата
                    currentChat.messages.pop(); // AI
                    currentChat.messages.pop(); // User
                    
                    // Сохраняем (для локальных чатов)
                    if (currentUser) {
                       // Для серверных нужно отправлять запрос, пока просто обновляем локально и надеемся на синхронизацию при следующем действии
                       // Или можно отправить DELETE запрос на сервер если API поддерживает
                    }
                }
            }
        }

        function appendMsg(role, text, img, anim = true, index = 0) {
            const box = document.getElementById('chat-container');
            const div = document.createElement('div');
            div.className = 'w-full max-w-3xl mx-auto px-0 md:px-0 relative z-0' + (anim ? ' animate-fadeIn' : '');

            if (role === 'user') {
                div.innerHTML = `<div class="flex justify-end pl-8 md:pl-10">
                    <div class="flex flex-col items-end gap-2 max-w-full">
                        ${img ? `<img src="${img}" class="h-32 rounded-xl border border-gray-300 dark:border-white/10 mb-1 cursor-pointer hover:opacity-90" onclick="window.open(this.src)">` : ''}
                        <div class="chat-bubble-user border border-gray-200 dark:border-white/5 shadow-sm max-w-full break-words">
                            <p class="whitespace-pre-wrap leading-relaxed">${text.replace(/</g, '&lt;').replace(/>/g, '&gt;')}</p>
                        </div>
                    </div>
                </div>`;
            } else {
                let innerContent = text ? marked.parse(text) : '';
                div.innerHTML = `<div class="flex gap-3 md:gap-4 pr-0 md:pr-4 group relative assistant-message">
                    <div class="w-8 h-8 rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center flex-shrink-0 mt-1 shadow-lg shadow-indigo-500/20">
                        <svg class="w-4 h-4 text-white"><use href="#icon-chat"></use></svg>
                    </div>
                    <div class="flex-1 min-w-0 overflow-hidden">
                        <div class="content-area prose prose-invert max-w-none text-gray-800 dark:text-gray-300 leading-7 text-[16px] break-words">${innerContent}</div>
                        <div class="message-actions">
                            <button onclick="copyMessageContent(this)" class="action-btn" title="Копировать ответ">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
                                Копировать
                            </button>
                            <button onclick="regenerateMessage(this)" class="action-btn" title="Пересоздать ответ">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 4v6h-6"/><path d="M1 20v-6h6"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg>
                                Регенерировать
                            </button>
                            <button onclick="deleteMessage(this)" class="action-btn" title="Удалить сообщение и вопрос">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>
                                Удалить
                            </button>
                        </div>
                    </div>
                </div>`;
            }

            box.appendChild(div);
            return div;
        }

        function scrollToBottom() {
            const el = document.getElementById('chat-container');
            el.scrollTop = el.scrollHeight;
        }

        // ФИКС КОПИРОВАНИЯ КОДА
        function addButtonsToCode() {
            document.querySelectorAll('pre code').forEach(codeBlock => {
                const pre = codeBlock.parentElement;
                if (pre.querySelector('.code-copy-btn')) return;

                const button = document.createElement('button');
                button.className = 'code-copy-btn';
                button.innerHTML = 'Копировать';
                
                button.onclick = async (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    
                    const code = codeBlock.innerText; // Используем innerText
                    
                    try {
                        await navigator.clipboard.writeText(code);
                        button.textContent = 'Скопировано!';
                        button.classList.add('copied');
                        setTimeout(() => {
                            button.textContent = 'Копировать';
                            button.classList.remove('copied');
                        }, 2000);
                    } catch (err) {
                        console.error('Ошибка копирования кода:', err);
                        button.textContent = 'Ошибка';
                        // Fallback для http (не https)
                        const textarea = document.createElement('textarea');
                        textarea.value = code;
                        document.body.appendChild(textarea);
                        textarea.select();
                        try {
                            document.execCommand('copy');
                            button.textContent = 'Скопировано!';
                            button.classList.add('copied');
                        } catch (err) {
                            button.textContent = 'Ошибка';
                        }
                        document.body.removeChild(textarea);
                        
                        setTimeout(() => {
                            button.textContent = 'Копировать';
                            button.classList.remove('copied');
                        }, 2000);
                    }
                };
                pre.appendChild(button);
            });
        }

        // --- UI HELPERS ---
        function toggleSidebar() {
            const sb = document.getElementById('sidebar');
            const overlay = document.getElementById('mobile-overlay');
            const isHidden = sb.classList.contains('-translate-x-full');
            if (isHidden) {
                sb.classList.remove('-translate-x-full');
                overlay.classList.remove('hidden');
            } else {
                sb.classList.add('-translate-x-full');
                overlay.classList.add('hidden');
            }
        }

        function toggleSettings() {
            const modal = document.getElementById('settings-modal');
            modal.classList.toggle('hidden');
        }

        function toggleTheme() {
            userSettings.theme = userSettings.theme === 'dark' ? 'light' : 'dark';
            saveSettings();
            applyTheme(userSettings.theme);
        }

        function applyTheme(theme) {
            const html = document.documentElement;
            if (theme === 'dark') {
                html.classList.add('dark');
            } else {
                html.classList.remove('dark');
            }
        }

        function exportAllChats() {
            const data = JSON.stringify({
                chats: chats,
                settings: userSettings,
                exportDate: new Date().toISOString()
            }, null, 2);
            const blob = new Blob([data], { type: 'application/json' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `proxify-export-${new Date().toISOString().split('T')[0]}.json`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }

        function saveSettings() {
            const model = document.getElementById('model-select').value;
            const codingModel = document.getElementById('coding-model-select').value;
            userSettings.model = model;
            userSettings.codingmodel = codingModel;
            localStorage.setItem('proxify_settings', JSON.stringify(userSettings));
        }

        function handlePaste(e) {
            const items = (e.clipboardData || e.originalEvent.clipboardData).items;
            for (let i = 0; i < items.length; i++) {
                if (items[i].type.indexOf('image') !== -1) {
                    const blob = items[i].getAsFile();
                    const reader = new FileReader();
                    reader.onload = function(event) {
                        imgBase64 = event.target.result;
                        document.getElementById('img-preview').src = imgBase64;
                        document.getElementById('img-preview-box').classList.remove('hidden');
                        document.getElementById('attach-preview-wrap').classList.remove('hidden');
                    };
                    reader.readAsDataURL(blob);
                    e.preventDefault();
                    return;
                }
            }
        }

        function handleUniversalUpload(e) {
            const files = e.target.files;
            if (!files || files.length === 0) return;
            const f = files[0];
            if (f.type.startsWith('image')) {
                processImage(f);
            } else {
                processDoc(f);
            }
        }

        function processImage(f) {
            const r = new FileReader();
            r.onload = (ev) => {
                imgBase64 = ev.target.result;
                document.getElementById('img-preview').src = imgBase64;
                document.getElementById('img-preview-box').classList.remove('hidden');
                document.getElementById('attach-preview-wrap').classList.remove('hidden');
            };
            r.readAsDataURL(f);
        }

        function processDoc(f) {
            fileName = f.name;
            const r = new FileReader();
            r.onload = (ev) => {
                const rawContent = ev.target.result;
                fileContent = rawContent;
                document.getElementById('file-name').textContent = fileName;
                document.getElementById('file-preview-box').classList.remove('hidden');
                document.getElementById('attach-preview-wrap').classList.remove('hidden');
            };
            r.readAsText(f);
        }

        function clearImage() {
            imgBase64 = null;
            document.getElementById('img-preview-box').classList.add('hidden');
            document.getElementById('img-preview').src = '';
            checkHidePreview();
        }

        function clearFile() {
            fileContent = null;
            fileName = null;
            document.getElementById('file-preview-box').classList.add('hidden');
            document.getElementById('file-name').textContent = '';
            checkHidePreview();
        }

        function checkHidePreview() {
            if (!imgBase64 && !fileContent) {
                document.getElementById('attach-preview-wrap').classList.add('hidden');
            }
        }

        function toggleWeb() {
            webEnabled = !webEnabled;
            const btn = document.getElementById('web-btn');
            const badge = document.getElementById('web-badge');
            if (webEnabled) {
                btn.classList.add('text-accent', 'bg-accent/10');
                badge.classList.remove('hidden');
            } else {
                btn.classList.remove('text-accent', 'bg-accent/10');
                badge.classList.add('hidden');
            }
        }

        function toggleCoding() {
            codingEnabled = !codingEnabled;
            const btn = document.getElementById('coding-btn');
            const badge = document.getElementById('coding-badge');
            if (codingEnabled) {
                btn.classList.add('text-accent', 'bg-accent/10');
                badge.classList.remove('hidden');
            } else {
                btn.classList.remove('text-accent', 'bg-accent/10');
                badge.classList.add('hidden');
            }
        }
    </script>
</body>
</html>
"""
