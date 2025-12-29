INDEX_HTML = """
<!DOCTYPE html>
<html lang="en" class="dark:bg-[#212121]">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Proxify AI</title>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Proxify AI</title>
    <script src="https://cdn.tailwindcss.com">function toggleCoding() {
            codingEnabled = !codingEnabled;
            if(codingEnabled) { reasoningEnabled = false; checkToggles(); }
            checkToggles();
        }

        function toggleReasoning() {
            reasoningEnabled = !reasoningEnabled;
            if(reasoningEnabled) { codingEnabled = false; checkToggles(); }
            checkToggles();
        }

        function checkToggles() {
            const cBtn = document.getElementById("coding-btn");
            const cBadge = document.getElementById("coding-badge");
            const rBtn = document.getElementById("reasoning-btn");
            const rBadge = document.getElementById("reasoning-badge");

            if (codingEnabled) {
                cBtn.classList.add("text-accent", "bg-accent/10");
                cBadge.classList.remove("hidden");
            } else {
                cBtn.classList.remove("text-accent", "bg-accent/10");
                cBadge.classList.add("hidden");
            }

            if (reasoningEnabled) {
                rBtn.classList.add("text-accent", "bg-accent/10");
                rBadge.classList.remove("hidden");
            } else {
                rBtn.classList.remove("text-accent", "bg-accent/10");
                rBadge.classList.add("hidden");
            }
        }
        </script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        accent: '#3b82f6',
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        mono: ['Geist Mono', 'monospace']
                    },
                    boxShadow: {
                        'glow': '0 0 20px -5px rgba(99, 102, 241, 0.2)',
                    }
                }
            }
        }
    function toggleCoding() {
            codingEnabled = !codingEnabled;
            if(codingEnabled) { reasoningEnabled = false; checkToggles(); }
            checkToggles();
        }

        function toggleReasoning() {
            reasoningEnabled = !reasoningEnabled;
            if(reasoningEnabled) { codingEnabled = false; checkToggles(); }
            checkToggles();
        }

        function checkToggles() {
            const cBtn = document.getElementById("coding-btn");
            const cBadge = document.getElementById("coding-badge");
            const rBtn = document.getElementById("reasoning-btn");
            const rBadge = document.getElementById("reasoning-badge");

            if (codingEnabled) {
                cBtn.classList.add("text-accent", "bg-accent/10");
                cBadge.classList.remove("hidden");
            } else {
                cBtn.classList.remove("text-accent", "bg-accent/10");
                cBadge.classList.add("hidden");
            }

            if (reasoningEnabled) {
                rBtn.classList.add("text-accent", "bg-accent/10");
                rBadge.classList.remove("hidden");
            } else {
                rBtn.classList.remove("text-accent", "bg-accent/10");
                rBadge.classList.add("hidden");
            }
        }
        </script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/geist-mono@1.0.0/dist/geist-mono.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js">function toggleCoding() {
            codingEnabled = !codingEnabled;
            if(codingEnabled) { reasoningEnabled = false; checkToggles(); }
            checkToggles();
        }

        function toggleReasoning() {
            reasoningEnabled = !reasoningEnabled;
            if(reasoningEnabled) { codingEnabled = false; checkToggles(); }
            checkToggles();
        }

        function checkToggles() {
            const cBtn = document.getElementById("coding-btn");
            const cBadge = document.getElementById("coding-badge");
            const rBtn = document.getElementById("reasoning-btn");
            const rBadge = document.getElementById("reasoning-badge");

            if (codingEnabled) {
                cBtn.classList.add("text-accent", "bg-accent/10");
                cBadge.classList.remove("hidden");
            } else {
                cBtn.classList.remove("text-accent", "bg-accent/10");
                cBadge.classList.add("hidden");
            }

            if (reasoningEnabled) {
                rBtn.classList.add("text-accent", "bg-accent/10");
                rBadge.classList.remove("hidden");
            } else {
                rBtn.classList.remove("text-accent", "bg-accent/10");
                rBadge.classList.add("hidden");
            }
        }
        </script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js">function toggleCoding() {
            codingEnabled = !codingEnabled;
            if(codingEnabled) { reasoningEnabled = false; checkToggles(); }
            checkToggles();
        }

        function toggleReasoning() {
            reasoningEnabled = !reasoningEnabled;
            if(reasoningEnabled) { codingEnabled = false; checkToggles(); }
            checkToggles();
        }

        function checkToggles() {
            const cBtn = document.getElementById("coding-btn");
            const cBadge = document.getElementById("coding-badge");
            const rBtn = document.getElementById("reasoning-btn");
            const rBadge = document.getElementById("reasoning-badge");

            if (codingEnabled) {
                cBtn.classList.add("text-accent", "bg-accent/10");
                cBadge.classList.remove("hidden");
            } else {
                cBtn.classList.remove("text-accent", "bg-accent/10");
                cBadge.classList.add("hidden");
            }

            if (reasoningEnabled) {
                rBtn.classList.add("text-accent", "bg-accent/10");
                rBadge.classList.remove("hidden");
            } else {
                rBtn.classList.remove("text-accent", "bg-accent/10");
                rBadge.classList.add("hidden");
            }
        }
        </script>
    
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
        
        .sidebar { background-color: var(--bg-secondary); border-right: 1px solid var(--border-color); }
        .chat-bubble-user { background-color: #f3f4f6; color: #111827; border-radius: 1.2rem; padding: 0.75rem 1rem; }
        .dark .chat-bubble-user { background-color: #1f2937; color: #ffffff; }
        
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

        html, body { height: 100%; overflow: hidden; }
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
        .prose code { font-family: 'Geist Mono', monospace; color: #6366f1; background: rgba(99, 102, 241, 0.1); padding: 0.2em 0.4em; border-radius: 0.25rem; font-size: 0.85em; }
        
        .dark .prose { color: #e4e4e7; }
        .prose { color: #111827; }

        #chat-container { 
            height: 100%; 
            overflow-y: auto; 
            padding-bottom: 170px; /* Space for input */
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
            #chat-container { padding-bottom: 150px; padding-top: 70px; }
            #sidebar { position: fixed; top: 0; left: 0; bottom: 0; z-index: 60; }
            .input-container-fixed { padding: 0.75rem; }
        }
        
        #context-menu { display: none; position: fixed; z-index: 100; }
        #drag-overlay { pointer-events: none; opacity: 0; transition: opacity 0.2s; }
        #drag-overlay.active { pointer-events: auto; opacity: 1; }
    </style>
    <!-- Supabase removed - using local authentication API -->

    <style>
    .typing-indicator { display: inline-flex; align-items: center; gap: 6px; padding: 12px 16px; background: #f3f4f6; border-radius: 12px; border-bottom-left-radius: 4px; margin-bottom: 8px; width: fit-content; min-height: 24px; }
    .dark .typing-indicator { background: rgba(255, 255, 255, 0.1); }
    .typing-dot { width: 8px; height: 8px; background-color: #6b7280; border-radius: 50%; animation: typing-bounce 1.4s infinite ease-in-out both; }
    .dark .typing-dot { background-color: #9ca3af; }
    .typing-dot:nth-child(1) { animation-delay: -0.32s; }
    .typing-dot:nth-child(2) { animation-delay: -0.16s; }
    @keyframes typing-bounce { 0%, 80%, 100% { transform: scale(0); opacity: 0.5; } 40% { transform: scale(1); opacity: 1; } }
    </style>

</head>
<body class="h-full flex overflow-hidden" onclick="hideContextMenu()">
    <!-- Auth Modal -->
    <div id="auth-modal" class="fixed inset-0 z-[80] bg-black/60 backdrop-blur-sm hidden flex items-center justify-center p-4" style="display: none;">
        <div class="bg-white dark:bg-[#18181b] rounded-2xl shadow-2xl w-full max-w-sm border border-gray-200 dark:border-[#27272a] overflow-hidden transform transition-all p-6 relative">
            <button onclick="closeAuthModal()" class="absolute top-4 right-4 text-gray-400 hover:text-gray-600 dark:hover:text-gray-200">
                <svg class="w-6 h-6"><use href="#icon-x"></use></svg>
            </button>
            <h2 id="auth-title" class="text-2xl font-bold mb-6 text-center">Вход в систему</h2>
            <form id="auth-form" class="space-y-4">
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
                <button onclick="toggleAuthMode()" class="text-accent font-medium hover:underline ml-1"><span id="auth-switch-btn">Регистрация</span></button>
            </div>
        </div>
    </div>

    <!-- Profile Modal (UPDATED WITH NEW BUTTONS) -->
    <div id="profile-modal" class="fixed inset-0 z-[80] bg-black/60 backdrop-blur-sm hidden flex items-center justify-center p-4" style="display: none;">
        <div class="bg-white dark:bg-[#18181b] rounded-2xl shadow-2xl w-full max-w-sm border border-gray-200 dark:border-[#27272a] overflow-hidden transform transition-all p-6 relative">
            <button onclick="closeProfileModal()" class="absolute top-4 right-4 text-gray-400 hover:text-gray-600 dark:hover:text-gray-200">
                <svg class="w-6 h-6"><use href="#icon-x"></use></svg>
            </button>

            <div class="text-center mb-6">
                <div class="w-24 h-24 mx-auto rounded-full bg-gradient-to-br from-accent to-purple-600 flex items-center justify-center text-white text-3xl font-bold shadow-lg mb-3 overflow-hidden relative cursor-pointer group" onclick="document.getElementById('avatar-upload').click()">
                    <img id="profile-avatar-img" class="w-full h-full object-cover hidden" />
                    <span id="profile-avatar-text">?</span>
                    <div class="absolute inset-0 bg-black/50 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity rounded-full">
                        <svg class="w-8 h-8 text-white"><use href="#icon-image"></use></svg>
                    </div>
                </div>
                <input type="file" id="avatar-upload" class="hidden" accept="image/*" onchange="uploadAvatar(this)">

                <h2 class="text-xl font-bold" id="profile-email">guest@example.com</h2>
<div id="profile-plan-badge" class="mt-2 inline-block px-3 py-1 rounded-full text-xs font-bold bg-gray-200 text-gray-700">Free Plan</div>
                <p class="text-sm text-green-500 font-medium">● Аккаунт активен</p>
            </div>

            <div class="space-y-3">
                <button onclick="openChangePasswordModal()" class="w-full bg-gray-100 dark:bg-white/5 hover:bg-gray-200 dark:hover:bg-white/10 p-3 rounded-xl flex justify-between items-center transition-colors">
                    <span class="text-sm font-medium">Сменить пароль</span>
                    <svg class="w-4 h-4 text-gray-500"><use href="#icon-settings"></use></svg>
                </button>

                 <div class="bg-gray-50 dark:bg-white/5 p-3 rounded-xl flex justify-between items-center">
                    <span class="text-sm text-gray-500">Синхронизация</span>
                    <span class="text-sm font-medium text-accent">Включена</span>
                </div>
            </div>

            <div class="mt-6 pt-6 border-t border-gray-200 dark:border-[#27272a] space-y-4">
                
    <!-- ADMIN PANEL BTN -->
    <div id="admin-panel-btn-container" class="hidden pt-4 border-t border-gray-200 dark:border-[#27272a]">
         <button onclick="openAdminPanel()" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 rounded-xl transition-all flex items-center justify-center gap-2">
            <svg class="w-5 h-5"><use href="#icon-settings"></use></svg>
            Админ Панель
        </button>
    </div>
    
    <div class="flex justify-between items-center pt-2">
         <span class="text-sm font-medium text-gray-700 dark:text-gray-300">Выйти</span>
         <button onclick="handleLogout()" class="px-4 py-1.5 border border-gray-400 text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-white/10 rounded-full text-xs font-medium transition-all">
            Выйти
         </button>
    </div>
    
<!-- LOGOUT ALL DEVICES -->
                <div class="flex justify-between items-center">
                     <span class="text-sm font-medium text-gray-700 dark:text-gray-300">Выйти со всех устройств</span>
                     <button onclick="handleLogoutGlobal()" class="px-4 py-1.5 border border-red-500 text-red-500 hover:bg-red-500 hover:text-white rounded-full text-xs font-medium transition-all">
                        Выйти
                     </button>
                </div>

                <!-- DELETE ACCOUNT -->
                <div class="flex justify-between items-center">
                     <span class="text-sm font-medium text-gray-700 dark:text-gray-300">Удалить аккаунт</span>
                     <button onclick="handleDeleteAccount()" class="px-4 py-1.5 border border-red-500 text-red-500 hover:bg-red-500 hover:text-white rounded-full text-xs font-medium transition-all">
                        Удалить
                     </button>
                </div>
            </div>

             <!-- REGULAR LOGOUT (Hidden or moved? The image didn't show the big red button anymore, but let's keep it just in case or assume 'Exit all devices' replaces it? 
                  The image shows "Exit from all devices" AND "Delete account". It doesn't show the big "Log out" button. 
                  But usually you need a simple "Log out". 
                  Let's assume the user replaced the big button with these options. 
                  OR kept it? The prompt says "Add these buttons". It implies addition.
                  But looking at the screenshot, it looks like a list at the bottom.
                  I will keep the main logout button or replace it? 
                  The screenshot shows a clean list. I will match the screenshot style for these two items.
             -->

        </div>
    </div>

    <!-- Change Password Modal -->
    <div id="password-modal" class="fixed inset-0 z-[90] bg-black/60 backdrop-blur-sm hidden flex items-center justify-center p-4" style="display: none;">
        <div class="bg-white dark:bg-[#18181b] rounded-2xl shadow-2xl w-full max-w-sm border border-gray-200 dark:border-[#27272a] overflow-hidden transform transition-all p-6 relative">
            <button onclick="closePasswordModal()" class="absolute top-4 right-4 text-gray-400 hover:text-gray-600 dark:hover:text-gray-200">
                <svg class="w-6 h-6"><use href="#icon-x"></use></svg>
            </button>
            <h2 class="text-xl font-bold mb-6 text-center">Смена пароля</h2>
            <form id="password-form" class="space-y-4">
                <div>
                    <label class="block text-sm font-medium mb-1">Текущий пароль</label>
                    <input type="password" id="current-password" required class="w-full bg-gray-100 dark:bg-black/20 border border-gray-200 dark:border-[#27272a] rounded-xl px-4 py-3 outline-none focus:ring-2 ring-accent/50 transition-all" placeholder="Для проверки">
                </div>
                <div>
                    <label class="block text-sm font-medium mb-1">Новый пароль</label>
                    <input type="password" id="new-password" required minlength="6" class="w-full bg-gray-100 dark:bg-black/20 border border-gray-200 dark:border-[#27272a] rounded-xl px-4 py-3 outline-none focus:ring-2 ring-accent/50 transition-all">
                </div>
                <div class="flex gap-3 pt-2">
                    <button type="button" onclick="closePasswordModal()" class="flex-1 bg-gray-200 dark:bg-white/10 hover:bg-gray-300 dark:hover:bg-white/20 text-gray-800 dark:text-white font-bold py-3 rounded-xl transition-all">Отмена</button>
                    <button type="submit" id="password-submit" class="flex-1 bg-accent hover:bg-accent/90 text-white font-bold py-3 rounded-xl transition-all shadow-lg shadow-accent/25">Обновить</button>
                </div>
            </form>
        </div>
    </div>


    <!-- Настройки Modal -->
    <div id="settings-modal" class="fixed inset-0 z-[70] bg-black/50 backdrop-blur-sm hidden flex items-center justify-center p-4">
        <div class="bg-white dark:bg-[#18181b] rounded-2xl shadow-2xl w-full max-w-md border border-gray-200 dark:border-[#27272a] overflow-hidden transform transition-all">
            <div class="p-4 border-b border-gray-200 dark:border-[#27272a] flex justify-between items-center">
                <h3 class="font-semibold text-lg">Настройки</h3>
                <button onclick="toggleНастройки()" class="p-1 hover:bg-gray-100 dark:hover:bg-white/10 rounded-xl transition">
                    <svg class="w-5 h-5"><use href="#icon-x"></use></svg>
                </button>
            </div>
            <div class="p-6 space-y-6">
                <div class="flex items-center justify-between">
                    <div class="flex flex-col">
                        <span class="font-medium">Темная тема</span>
                        <span class="text-xs text-gray-500">Переключить тему оформления</span>
                    </div>
                    <button id="theme-toggle" onclick="toggleTheme()" class="w-12 h-6 rounded-full bg-gray-200 dark:bg-accent relative transition-colors">
                        <div class="w-4 h-4 rounded-full bg-white absolute top-1 left-1 transition-transform dark:translate-x-6 shadow-sm"></div>
                    </button>
                </div>
                
                <div class="space-y-2">
                    <label class="font-medium block">Модель ИИ</label>
                    <select id="model-select" onchange="saveНастройки()" class="w-full bg-gray-100 dark:bg-black/20 border border-gray-200 dark:border-[#27272a] rounded-xl px-3 py-2.5 outline-none focus:ring-2 ring-accent/50 text-sm dark:text-white dark:bg-[#18181b]">
                        <option value="auto">Auto (Smart)</option>
                        <option value="google/gemini-2.5-flash">Gemini 2.5 Flash</option>
                        <option value="google/gemini-2.5-pro">Gemini 2.5 Pro</option>
                        <option value="google/gemini-3-pro-preview">Gemini 3 Pro</option>
                            <option value="cognitivecomputations/dolphin-mistral-24b-venice-edition:free">Dolphin Mistral (Uncensored)</option>
                            <option value="nex-agi/deepseek-v3.1-nex-n1:free">DeepSeek Chat v3.1</option>
                    </select>
                    <p class="text-xs text-gray-500">Выберите модель или режим Авто.</p>
                </div>
                    <div class="space-y-2">
                        <label class="font-medium block">Модель для кода</label>
                        <select id="coding-model-select" onchange="saveНастройки()" class="w-full bg-gray-100 dark:bg-black/20 border border-gray-200 dark:border-27272a rounded-xl px-3 py-2.5 outline-none focus:ring-2 ring-accent/50 text-sm dark:text-white dark:bg-18181b">
                            <option value="kwaipilot/kat-coder-pro:free">KAT-Coder-Pro V1</option>
                        </select>
                        <p class="text-xs text-gray-500">Модель для режима кодинга.</p>
                    </div>

                    <div class="space-y-2 mt-4">
                        <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Экспорт данных</label>
                        <button onclick="exportAllChats()" class="w-full bg-accent hover:bg-accent/90 text-white rounded-xl px-4 py-2.5 font-medium transition-colors flex items-center justify-center gap-2">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/>
                            </svg>
                            Скачать все чаты
                        </button>
                    </div>
            </div>
        </div>
    </div>

    <div id="drag-overlay" class="fixed inset-0 z-[100] bg-black/80 backdrop-blur-sm flex items-center justify-center border-4 border-dashed border-accent/50 m-4 rounded-3xl">
        <div class="text-center animate-bounce">
            <svg class="w-16 h-16 mx-auto text-accent mb-4"><use href="#icon-file"></use></svg>
            <h2 class="text-2xl font-bold text-white">Перетащите файлы сюда</h2>
        </div>
    </div>

    <svg style="display: none;">
        <symbol id="icon-plus" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></symbol>
        <symbol id="icon-chat" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></symbol>
        <symbol id="icon-settings" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></symbol>
        <symbol id="icon-image" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></symbol>
        <symbol id="icon-file" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><polyline points="13 2 13 9 20 9"/></symbol>
        <symbol id="icon-globe" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></symbol>
        <symbol id="icon-send" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></symbol>
        <symbol id="icon-trash" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></symbol>
        <symbol id="icon-menu" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></symbol>
        <symbol id="icon-x" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></symbol>
        <symbol id="icon-copy" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></symbol>
        <symbol id="icon-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></symbol>
        <symbol id="icon-refresh" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 4v6h-6"></path><path d="M1 20v-6h6"></path><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path></symbol>
        <symbol id="icon-volume" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></symbol>
    </svg>
    
    <div id="context-menu" class="bg-white dark:bg-zinc-900 border border-gray-200 dark:border-zinc-800 rounded-xl shadow-xl py-1 min-w-[160px]">
        <button id="ctx-delete-btn" class="w-full text-left px-4 py-2 text-sm text-red-500 hover:bg-gray-100 dark:hover:bg-white/5 flex items-center gap-2 transition-colors">
            <svg class="w-4 h-4"><use href="#icon-trash"></use></svg>
            Удалить чат
        </button>
    </div>

    <div id="mobile-overlay" onclick="toggleSidebar()" class="fixed inset-0 bg-black/60 z-40 hidden backdrop-blur-sm transition-opacity"></div>

    <aside id="sidebar" class="w-72 sidebar border-r border-gray-200 dark:border-[#27272a] flex flex-col transform -translate-x-full md:translate-x-0 transition-transform duration-300 shadow-2xl h-full z-50">
        
    <div id="user-profile-section" class="p-4 border-b border-gray-200 dark:border-[#27272a] flex items-center gap-3 cursor-pointer hover:bg-gray-50 dark:hover:bg-white/5 transition-colors" onclick="handleProfileClick()">
        <div class="w-10 h-10 rounded-full bg-gradient-to-br from-accent to-purple-600 flex items-center justify-center text-white font-bold shadow-lg overflow-hidden relative" id="user-avatar">
            <img id="sidebar-avatar-img" class="w-full h-full object-cover hidden" />
            <span id="sidebar-avatar-text">?</span>
        </div>
        <div class="flex-1 min-w-0">
            <p class="font-medium truncate" id="user-email-sidebar">Гость</p>
            <p class="text-xs text-gray-500 truncate" id="user-status-sidebar">Нажмите для входа</p>
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
        <!-- КНОПКА АНАЛИТИКИ В МЕНЮ -->
<a href="/analytics" target="_blank" class="flex items-center gap-3 px-3 py-3 mt-2 text-sm text-gray-100 transition-colors duration-200 rounded-md hover:bg-gray-800 cursor-pointer">
    <span class="text-xl">📊</span>
    <span>Нейро Новости</span>
</a>
        <div class="flex-1 overflow-y-auto p-3 space-y-1" id="chat-list"></div>
        
        <div class="p-4 border-t border-gray-200 dark:border-[#27272a] bg-gray-50/50 dark:bg-black/20 flex items-center justify-between">
            <button onclick="toggleНастройки()" class="flex items-center gap-2 text-sm text-gray-600 dark:text-gray-400 hover:text-black dark:hover:text-white transition-colors px-2 py-1 rounded-xl hover:bg-gray-200 dark:hover:bg-white/5">
                <svg class="w-4 h-4"><use href="#icon-settings"></use></svg>
                Настройки
            </button>
            <button onclick="clearHistory()" class="p-2 text-gray-400 hover:text-red-500 transition-colors" title="Очистить всё">
                <svg class="w-4 h-4"><use href="#icon-trash"></use></svg>
            </button>
        </div>
    </aside>

    <main class="flex-1 flex flex-col h-full relative w-full overflow-hidden">
        <header class="h-14 border-b border-gray-200 dark:border-[#27272a] flex items-center justify-between px-4 md:px-6 bg-white/90 dark:bg-[#09090b]/90 backdrop-blur-md z-30 absolute top-0 w-full">
            <div class="flex items-center gap-4">
                <button onclick="toggleSidebar()" class="md:hidden text-gray-500 dark:text-gray-400 hover:text-black dark:hover:text-white p-1">
                    <svg class="w-6 h-6"><use href="#icon-menu"></use></svg>
                </button>
                <div class="flex items-center gap-2">
                    <span class="font-semibold text-black dark:text-white">Proxify <span class="text-accent">AI</span></span>
                </div>
            </div>
        </header>

        <div id="chat-container" class="w-full px-4 md:px-8 space-y-6"></div>

        <div class="input-container-fixed">
            <div class="max-w-3xl mx-auto relative">
                <div id="attach-preview-wrap" class="hidden absolute -top-24 left-0 z-0 animate-[fadeIn_0.2s] flex gap-2 overflow-x-auto px-2">
                    <div id="img-preview-box" class="relative group hidden">
                        <img id="img-preview" class="h-20 rounded-xl border border-gray-200 dark:border-white/10 shadow-lg object-cover bg-white dark:bg-[#18181b]">
                        <button onclick="clearImage()" class="absolute top-2 right-2 bg-gray-800 text-white border border-white/10 rounded-full p-1 hover:bg-red-500 transition">
                            <svg class="w-3 h-3"><use href="#icon-x"></use></svg>
                        </button>
                    </div>
                    <div id="file-preview-box" class="relative group hidden h-20 p-3 bg-white dark:bg-[#18181b] border border-gray-200 dark:border-white/10 rounded-xl flex items-center gap-2 min-w-[120px]">
                        <div class="bg-gray-100 dark:bg-white/10 p-2 rounded-xl"><svg class="w-5 h-5 text-accent"><use href="#icon-file"></use></svg></div>
                        <span id="file-name" class="text-xs text-gray-500 dark:text-gray-400 truncate max-w-[100px]">file.txt</span>
                        <button onclick="clearFile()" class="absolute top-2 right-2 bg-gray-800 text-white border border-white/10 rounded-full p-1 hover:bg-red-500 transition">
                            <svg class="w-3 h-3"><use href="#icon-x"></use></svg>
                        </button>
                    </div>
                </div>

                <div class="input-box-wrapper rounded-3xl flex flex-col relative z-50">
                    <textarea id="user-input" rows="1" placeholder="Спросите что-нибудь..." 
                        class="w-full bg-transparent text-black dark:text-gray-200 placeholder-gray-400 dark:placeholder-gray-500 outline-none resize-none px-4 md:px-5 pt-3 md:pt-4 pb-2 min-h-[48px] md:min-h-[54px] max-h-48 font-sans text-[16px] leading-relaxed rounded-t-3xl"
                        oninput="this.style.height='auto';this.style.height=this.scrollHeight+'px'"
                        onkeydown="if(event.key==='Enter'&&!event.shiftKey){event.preventDefault();send()}"></textarea>

                    <div class="flex items-center justify-between px-3 pb-3 pt-1">
                        <div class="flex items-center gap-1">
<input type="file" id="universal-in" class="hidden" multiple onchange="handleUniversalUpload(event)">
<button onclick="document.getElementById('universal-in').click()" class="p-2 text-gray-400 dark:text-gray-500 hover:text-accent dark:hover:text-accent hover:bg-gray-50 dark:hover:bg-white/5 rounded-xl transition-colors" title="Прикрепить файл или фото">
    <!-- Icon Paperclip -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-5 h-5">
        <path d="m21.44 11.05-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"></path>
    </svg>
</button>

                            <button id="web-btn" onclick="toggleWeb()" class="p-2 text-gray-400 dark:text-gray-500 hover:text-accent dark:hover:text-accent hover:bg-gray-50 dark:hover:bg-white/5 rounded-xl transition-all flex items-center gap-2">
                                <svg class="w-5 h-5"><use href="#icon-globe"></use></svg>
                                <span id="web-badge" class="text-[10px] font-bold hidden bg-accent text-white px-1 rounded">ON</span>
                            </button>
                            <button id="coding-btn" onclick="toggleCoding()" class="p-2 text-gray-400 dark:text-gray-500 hover:text-accent dark:hover:text-accent hover:bg-gray-50 dark:hover:bg-white/5 rounded-xl transition-all flex items-center gap-2">
                                <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <polyline points="16 18 22 12 16 6"></polyline>
                                    <polyline points="8 6 2 12 8 18"></polyline>
                                </svg>
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
    let currentSessionToken = null;
    
    // Load session from localStorage on page load
    window.addEventListener('DOMContentLoaded', async () => {
        // Try to restore session from localStorage
        const storedSession = localStorage.getItem('session_token');
        const storedUser = localStorage.getItem('current_user');
        
        if (storedSession && storedUser) {
            currentSessionToken = storedSession;
            try {
                currentUser = JSON.parse(storedUser);
                // Update UI to show logged in state
                updateUserUI(currentUser);
                loadRemoteChats();
                loadUserAvatar();
            } catch (e) {
                console.error('Error restoring session:', e);
                // Clear invalid session data
                localStorage.removeItem('session_token');
                localStorage.removeItem('current_user');
            }
        }
        
        await init();
    });
    
        function handlePaste(e) {
            const items = (e.clipboardData || e.originalEvent.clipboardData).items;
            for (let i = 0; i < items.length; i++) {
                if (items[i].type.indexOf("image") !== -1) {
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

        let chats = [];
        let isChatsLoaded = false;
        let activeChatId = null;
        let imgBase64 = null;
        let fileContent = null;
        let fileName = null;
        let isBusy = false;
        let webEnabled = false
        let codingEnabled = false;
        let reasoningEnabled = false;
        let contextChatId = null;
        
        let userНастройки = JSON.parse(localStorage.getItem('settings') || '{"theme": "dark", "model": "auto"}');

        const WELCOME_HTML = `
            <div id="welcome" class="h-full flex flex-col items-center justify-center text-center opacity-0 animate-[fadeIn_0.5s_forwards] pt-20">
                <div class="w-20 h-20 bg-gray-100 dark:bg-white/5 rounded-3xl flex items-center justify-center mb-6 border border-gray-200 dark:border-white/5">
                    <svg class="w-10 h-10 text-gray-400 dark:text-gray-600"><use href="#icon-chat"></use></svg>
                </div>
                <h2 class="text-xl font-medium text-black dark:text-white mb-2">Чем могу помочь?</h2>
            </div>
        `;

        // init handled by DOMContentLoaded

        function init() {
            document.addEventListener('paste', handlePaste); initAuth(); 
            applyTheme(userНастройки.theme);
            document.getElementById('model-select').value = userНастройки.model;
            if(userНастройки.coding_model) document.getElementById('coding-model-select').value = userНастройки.coding_model;
            
            if (!Array.isArray(chats)) chats = [];
            chats = chats.filter(c => c && (c.messages.length > 0 || (chats.length > 0 && c.id === chats[0].id)));
            
            if (chats.length === 0) createChatInternal();
            else loadChat(chats[0].id);
            renderList();
            document.getElementById('ctx-delete-btn').onclick = deleteContextChat;
        }
        
        const dropZone = document.body;
        const overlay = document.getElementById('drag-overlay');

        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            dropZone.addEventListener(eventName, preventDefaults, false);
        });

        function preventDefaults(e) { e.preventDefault(); e.stopPropagation(); }
        dropZone.addEventListener('dragenter', () => overlay.classList.add('active'));
        overlay.addEventListener('dragleave', (e) => { if (e.target === overlay) overlay.classList.remove('active'); });
        dropZone.addEventListener('drop', handleDrop, false);

        function handleDrop(e) {
            overlay.classList.remove('active');
            const files = e.dataTransfer.files;
            if (files.length > 0) handleFiles(files[0]);
        }
        function handleFiles(file) {
            if (file.type.startsWith('image/')) processImage(file);
            else processDoc(file);
        }

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

        function toggleНастройки() {
            const modal = document.getElementById('settings-modal');
            modal.classList.toggle('hidden');
        }

        function toggleTheme() {
            userНастройки.theme = userНастройки.theme === 'dark' ? 'light' : 'dark';
            saveНастройки();
            applyTheme(userНастройки.theme);
        }

        function applyTheme(theme) {
            const html = document.documentElement;
            if (theme === 'dark') html.classList.add('dark');
            else html.classList.remove('dark');
        }

        
        function exportAllChats() {
            const data = JSON.stringify({
                chats: chats,
                settings: userНастройки,
                exportDate: new Date().toISOString()
            }, null, 2);

            const blob = new Blob([data], { type: 'application/json' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `chatgpt-clone-export-${new Date().toISOString().split('T')[0]}.json`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }

        function saveНастройки() {
            const model = document.getElementById('model-select').value;
            const codingModel = document.getElementById('coding-model-select').value;
            userНастройки.model = model;
            userНастройки.coding_model = codingModel;
            localStorage.setItem('settings', JSON.stringify(userНастройки));
        }

        function handleNewChatClick() {
            const current = chats.find(c => c.id === activeChatId);
            if (current && current.messages.length === 0) {
                document.getElementById('user-input').focus();
                if(window.innerWidth < 768) toggleSidebar();
                return;
            }
            createChatInternal();
        }

        function createChatInternal() {
            const newChat = { id: Date.now().toString(), title: 'Новый чат', messages: [] };
            chats.unshift(newChat);
            save();
            loadChat(newChat.id);
            if (window.innerWidth < 768 && !document.getElementById('sidebar').classList.contains('-translate-x-full')) {
                toggleSidebar();
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
                    // FIX: Ensure content is decoded before displaying
                    let cleanContent = m.content;
                    try {
                        // Only decode if it looks like URL-encoded garbage
                        if (m.content.includes('%20') || m.content.includes('%3C')) {
                             cleanContent = decodeURIComponent(m.content);
                        }
                    } catch(e) {}
                    appendMsg(m.role, cleanContent, m.image_url, false, idx);
                });
            }
            
            renderList();
            scrollToBottom();

            // Apply syntax highlighting to all code blocks
            setTimeout(() => {
                document.querySelectorAll('pre code').forEach(el => {
                    hljs.highlightElement(el);
                });
                addКопироватьButtonsToCode();
            }, 100);

        }

        function save() {
            
            renderList(); saveRemoteChats(); 
        }

        function renderList() {
            const list = document.getElementById('chat-list');
            list.innerHTML = '';
            chats.forEach(c => {
                const btn = document.createElement('button');
                const active = c.id === activeChatId;
                
                let baseClasses = "w-full text-left px-3 py-3 rounded-xl text-sm truncate flex items-center gap-3 mb-1 transition-colors";
                let activeClasses = "bg-gray-200 dark:bg-white/10 text-black dark:text-white font-medium border border-gray-300 dark:border-white/5";
                let inactiveClasses = "text-gray-500 dark:text-gray-400 hover:text-black dark:hover:text-white hover:bg-gray-100 dark:hover:bg-white/5 border border-transparent";
                
                btn.className = `${baseClasses} ${active ? activeClasses : inactiveClasses}`;
                
                btn.onclick = () => { loadChat(c.id); if(window.innerWidth < 768) toggleSidebar(); };
                btn.oncontextmenu = (e) => showContextMenu(e, c.id);
                btn.innerHTML = `<svg class="w-4 h-4 opacity-70"><use href="#icon-chat"></use></svg><span class="truncate">${c.title}</span>`;
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
            menu.style.left = `${x}px`;
            menu.style.top = `${y}px`;
        }

        function hideContextMenu() {
            document.getElementById('context-menu').style.display = 'none';
            contextChatId = null;
        }

        function deleteContextChat() {
            if (!contextChatId) return;
            chats = chats.filter(c => c.id !== contextChatId);
            if (chats.length === 0) createChatInternal();
            else if (activeChatId === contextChatId) loadChat(chats[0].id);
            else save(); 
            hideContextMenu();
        }

        async function clearHistory() {
            if(confirm('Удалить все чаты? Это действие нельзя отменить.')) {
                chats = [];
                activeChatId = null;
                await save();
                renderList();
                document.getElementById('chat-container').innerHTML = '';
                createChatInternal();
            }
        }

        async function submitRequest(messages) {
            const currentChat = chats.find(c => c.id === activeChatId);
            
            const loadingHTML = `<div class="typing-indicator"><div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div></div>`;
            const aiDiv = appendMsg('assistant', loadingHTML, null, true, currentChat.messages.length);
            const contentArea = aiDiv.querySelector('.content-area');
            const actionDivWrapper = aiDiv.querySelector('.action-wrapper');
            
            let fullResponse = "";

            try {
                const res = await fetch('/api/chat', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                messages: messages,
                web_search: webEnabled,
                model: userНастройки.model,
                coding_mode: codingEnabled,
                coding_model: userНастройки.coding_model || "kwaipilot/kat-coder-pro:free",
                reasoning_mode: reasoningEnabled
            })
                });

                const reader = res.body.getReader();
                const dec = new TextDecoder();
                // contentArea.innerHTML = "";

                while (true) {
                    const {done, value} = await reader.read();
                    if (done) break;
                    const chunk = dec.decode(value, {stream: true});
                    fullResponse += chunk;

                    if (fullResponse.includes("<!-- IMAGE_WIDGET -->")) {
                        contentArea.innerHTML = fullResponse;
                    } else {
                        contentArea.innerHTML = marked.parse(fullResponse);
                        contentArea.querySelectorAll('pre code').forEach(el => hljs.highlightElement(el)); addКопироватьButtonsToCode();
                    }
                    const el = document.getElementById('chat-container');
                    const distanceFromBottom = el.scrollHeight - el.scrollTop - el.clientHeight;
                    if (distanceFromBottom < 200) {
                        scrollToBottom();
                    }
                }
                
                currentChat.messages.push({ role: 'assistant', content: fullResponse });
                save();
                
                const idx = currentChat.messages.length - 1;
                actionDivWrapper.innerHTML = getActionButtonsHTML(idx);

            } catch (e) {
                contentArea.innerHTML = `<span class="text-red-400">Error: ${e.message}</span>`;
            } finally {
                scrollToBottom();
                isBusy = false;
                document.getElementById('send-btn').disabled = false;
                document.getElementById('user-input').focus();
            }
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
                txt += `\\n\\n[Content of ${fName}]:\\n\\`\\`\\`\\n${fContent}\\n\\`\\`\\``;
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
            currentChat.messages.push({ role: 'user', content: txt, image_url: img });
            
            if (currentChat.messages.length === 1) {
                currentChat.title = txt.substring(0, 30) || "Новый чат";
            }
            save();

            const displayTxt = fName ? (input.value.trim() ? input.value.trim() + `\n(Attached: ${fName})` : `(Attached: ${fName})`) : txt;
            appendMsg('user', displayTxt, img);
            setTimeout(() => scrollToBottom(), 50);
            
            await submitRequest([...currentChat.messages]);
        }

        function appendMsg(role, text, img, anim = true, index = 0) {
            const box = document.getElementById('chat-container');
            const div = document.createElement('div');
            div.className = `w-full max-w-3xl mx-auto px-0 md:px-0 relative z-0 ${anim ? 'animate-[fadeIn_0.3s_ease-out]' : ''}`;
            
            if (role === 'user') {
                div.innerHTML = `
                    <div class="flex justify-end pl-8 md:pl-10">
                        <div class="flex flex-col items-end gap-2 max-w-full">
                            ${img ? `<img src="${img}" class="h-32 rounded-xl border border-gray-300 dark:border-white/10 mb-1 cursor-pointer hover:opacity-90" onclick="window.open(this.src)">` : ''}
                            <div class="chat-bubble-user border border-gray-200 dark:border-white/5 shadow-sm max-w-full break-words">
                                <p class="whitespace-pre-wrap leading-relaxed">${text.replace(/</g, "&lt;").replace(/>/g, "&gt;")}</p>
                            </div>
                        </div>
                    </div>
                `;
            } else {
                const actionsHTML = (!anim) ? getActionButtonsHTML(index) : '';
                let innerContent = "";
                if (text.includes("<!-- IMAGE_WIDGET -->") || text.includes("typing-indicator")) {
                     innerContent = text;
                } else {
                     innerContent = marked.parse(text);
                }

                div.innerHTML = `
                    <div class="flex gap-3 md:gap-4 pr-0 md:pr-4 group relative">
                        <div class="w-8 h-8 rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center flex-shrink-0 mt-1 shadow-lg shadow-indigo-500/20">
                            <svg class="w-4 h-4 text-white"><use href="#icon-chat"></use></svg>
                        </div>
                        <div class="flex-1 min-w-0 overflow-hidden">
                            <div class="content-area prose prose-invert max-w-none text-gray-800 dark:text-gray-300 leading-7 text-[16px] break-words">
                                ${innerContent}
                            </div>
                            <div class="action-wrapper flex items-center gap-3 mt-2 opacity-50 hover:opacity-100 transition-opacity z-20 relative">
                                ${actionsHTML}
                            </div>
                        </div>
                    </div>
                `;
            }
            box.appendChild(div);
            return div;
        }

        function getActionButtonsHTML(index) {
            return `
                <button onclick="copyToClipboard(this, ${index})" class="p-1 text-gray-400 dark:text-gray-500 hover:text-black dark:hover:text-white transition-colors cursor-pointer relative z-30" title="Копировать">
                    <svg class="w-4 h-4 pointer-events-none"><use href="#icon-copy"></use></svg>
                </button>
                <button onclick="regenerateResponse(${index})" class="p-1 text-gray-400 dark:text-gray-500 hover:text-black dark:hover:text-white transition-colors cursor-pointer relative z-30" title="Перегенерировать">
                    <svg class="w-4 h-4 pointer-events-none"><use href="#icon-refresh"></use></svg>
                </button>
                <button onclick="speakResponse(${index})" class="p-1 text-gray-400 dark:text-gray-500 hover:text-black dark:hover:text-white transition-colors cursor-pointer relative z-30" title="Озвучить">
                    <svg class="w-4 h-4 pointer-events-none"><use href="#icon-volume"></use></svg>
                </button>
                <button onclick="deleteMessage(${index})" class="p-1 text-gray-400 dark:text-gray-500 hover:text-red-500 dark:hover:text-red-400 transition-colors cursor-pointer relative z-30" title="Удалить">
                    <svg class="w-4 h-4 pointer-events-none"><use href="#icon-trash"></use></svg>
                </button>
            `;
        }

        function fallbackКопироватьTextToClipboard(text, btn) {
            var textArea = document.createElement("textarea");
            textArea.value = text;
            textArea.style.top = "0";
            textArea.style.left = "0";
            textArea.style.position = "fixed";
            document.body.appendChild(textArea);
            textArea.focus();
            textArea.select();
            try {
                var successful = document.execCommand('copy');
                if (successful) showCheck(btn);
            } catch (err) {
                console.error('Fallback: Oops, unable to copy', err);
            }
            document.body.removeChild(textArea);
        }

        async function copyToClipboard(btn, index) {
            const chat = chats.find(c => c.id === activeChatId);
            const text = chat.messages[index].content;
            if (!navigator.clipboard) {
                fallbackКопироватьTextToClipboard(text, btn);
                return;
            }
            try {
                await navigator.clipboard.writeText(text);
                showCheck(btn);
            } catch (err) {
                fallbackКопироватьTextToClipboard(text, btn);
            }
        }

        function showCheck(btn) {
            const originalHTML = btn.innerHTML;
            btn.innerHTML = `<svg class="w-4 h-4 text-green-500 dark:text-green-400 pointer-events-none"><use href="#icon-check"></use></svg>`;
            setTimeout(() => btn.innerHTML = originalHTML, 2000);
        }

        
        function speakResponse(index) {
            const currentChat = chats.find(c => c.id === activeChatId);
            if (!currentChat || !currentChat.messages[index]) return;
            window.speechSynthesis.cancel();
            const utterance = new SpeechSynthesisUtterance(currentChat.messages[index].content);
            utterance.lang = 'ru-RU';
            const voices = window.speechSynthesis.getVoices();
            const ruVoice = voices.find(v => v.lang.includes('ru'));
            if (ruVoice) utterance.voice = ruVoice;
            window.speechSynthesis.speak(utterance);
        }
function regenerateResponse(index) {
            if (isBusy) return;
            const chat = chats.find(c => c.id === activeChatId);
            if (index > 0) {
                chat.messages = chat.messages.slice(0, index); 
                save();
                loadChat(activeChatId); 
                isBusy = true;
                submitRequest([...chat.messages]);
            }
        }

        async function shareResponse(btn, index) {
            const chat = chats.find(c => c.id === activeChatId);
            const text = chat.messages[index].content;
            if (navigator.share) {
                try {
                    await navigator.share({title: 'AI Response', text: text});
                    return;
                } catch (err) {}
            }
            copyToClipboard(btn, index);
        }

        function scrollToBottom() {
            const el = document.getElementById('chat-container');
            el.scrollTop = el.scrollHeight;
        }

        function addКопироватьButtonsToCode() {
            document.querySelectorAll('pre code').forEach(codeBlock => {
                const pre = codeBlock.parentElement;
                if (pre.querySelector('.code-copy-btn')) return;

                const button = document.createElement('button');
                button.className = 'code-copy-btn';
                button.innerHTML = 'Копировать';

                button.onclick = async () => {
                    const code = codeBlock.textContent;
                    try {
                        await navigator.clipboard.writeText(code);
                        button.textContent = 'Copied!';
                        button.classList.add('copied');
                        setTimeout(() => {
                            button.textContent = 'Копировать';
                            button.classList.remove('copied');
                        }, 2000);
                    } catch (err) {
                        // Fallback for older browsers
                        const textarea = document.createElement('textarea');
                        textarea.value = code;
                        textarea.style.position = 'fixed';
                        textarea.style.opacity = '0';
                        document.body.appendChild(textarea);
                        textarea.select();
                        try {
                            document.execCommand('copy');
                            button.textContent = 'Copied!';
                            button.classList.add('copied');
                            setTimeout(() => {
                                button.textContent = 'Копировать';
                                button.classList.remove('copied');
                            }, 2000);
                        } catch (e) {
                            button.textContent = 'Failed';
                        }
                        document.body.removeChild(textarea);
                    }
                };

                pre.appendChild(button);
            });
        }

        // --- UNIVERSAL UPLOAD HANDLER (ALLOW ALL, SAFE READ) ---
        function handleUniversalUpload(e) {
            const files = e.target.files;
            if (!files || files.length === 0) return;

            const f = files[0];
            
            // Если это картинка — обрабатываем как картинку (превью и т.д.)
            if (f.type.startsWith('image/')) {
                processImage(f);
            } 
            // Все остальные файлы (код, тексты, логи и т.д.) обрабатываем как документы
            else {
                // processDoc просто читает содержимое файла как текст (readAsText)
                // Это безопасно, так как мы не выполняем этот код, а просто получаем строку
                processDoc(f);
            }
            
            // Сбрасываем value, чтобы можно было загрузить тот же файл снова
            e.target.value = '';
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
                fileContent = rawContent; // Сохраняем оригинал для отправки в AI

                // Экранируем HTML-теги для безопасного отображения в интерфейсе
                // Заменяем < на &lt;, > на &gt; и т.д.
                const safePreview = rawContent
                    .replace(/&/g, "&amp;")
                    .replace(/</g, "&lt;")
                    .replace(/>/g, "&gt;")
                    .replace(/"/g, "&quot;")
                    .replace(/'/g, "&#039;");

                document.getElementById('file-name').innerText = fileName;
                
                // Если у вас есть блок предпросмотра содержимого, обновляем его безопасно:
                // (Если такого блока нет, этот шаг можно пропустить, но он не помешает)
                // document.getElementById('some-preview-div').innerText = safePreview;

                document.getElementById('file-preview-box').classList.remove('hidden');
                document.getElementById('file-preview-box').classList.add('flex');
                document.getElementById('attach-preview-wrap').classList.remove('hidden');
            };
            
            // Читаем как текст, а не как DataURL
            r.readAsText(f);
        }

        function clearImage() {
            imgBase64 = null;
            
            // Если мы используем универсальный инпут, сбрасываем его
            var uniInput = document.getElementById('universal-in');
            if (uniInput) uniInput.value = '';

            // Если вдруг остался старый, сбрасываем и его (на всякий случай)
            var oldImgInput = document.getElementById('img-in');
            if (oldImgInput) oldImgInput.value = '';

            document.getElementById('img-preview-box').classList.add('hidden');
            checkHidePreview();
        }

        function clearFile() {
            fileContent = null;
            fileName = null;

            // Аналогично для файла
            var uniInput = document.getElementById('universal-in');
            if (uniInput) uniInput.value = '';

            var oldDocInput = document.getElementById('doc-in');
            if (oldDocInput) oldDocInput.value = '';

            document.getElementById('file-preview-box').classList.add('hidden');
            document.getElementById('file-preview-box').classList.remove('flex');
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
        
        const style = document.createElement("style");
        style.innerText = "@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }";
        document.head.appendChild(style);
    function toggleCoding() {
            codingEnabled = !codingEnabled;
            if(codingEnabled) { reasoningEnabled = false; checkToggles(); }
            checkToggles();
        }

        function toggleReasoning() {
            reasoningEnabled = !reasoningEnabled;
            if(reasoningEnabled) { codingEnabled = false; checkToggles(); }
            checkToggles();
        }

        function checkToggles() {
            const cBtn = document.getElementById("coding-btn");
            const cBadge = document.getElementById("coding-badge");
            const rBtn = document.getElementById("reasoning-btn");
            const rBadge = document.getElementById("reasoning-badge");

            if (codingEnabled) {
                cBtn.classList.add("text-accent", "bg-accent/10");
                cBadge.classList.remove("hidden");
            } else {
                cBtn.classList.remove("text-accent", "bg-accent/10");
                cBadge.classList.add("hidden");
            }

            if (reasoningEnabled) {
                rBtn.classList.add("text-accent", "bg-accent/10");
                rBadge.classList.remove("hidden");
            } else {
                rBtn.classList.remove("text-accent", "bg-accent/10");
                rBadge.classList.add("hidden");
            }
        }
        
        // --- SUPABASE & AUTH LOGIC ---
                        
        
                let isSignUp = false;

        async function initAuth() {
            console.log("Initializing Local Auth...");
            
            // Check if we have a valid session in localStorage
            if (currentSessionToken && currentUser) {
                try {
                    // Verify the session is still valid
                    const response = await fetch('/api/auth/me', {
                        headers: {
                            'Authorization': `Bearer ${currentSessionToken}`
                        }
                    });
                    
                    if (response.ok) {
                        const data = await response.json();
                        updateUserUI(data.user);
                        loadRemoteChats();
                        loadUserAvatar();
                    } else {
                        // Session is invalid, clear it
                        localStorage.removeItem('session_token');
                        localStorage.removeItem('current_user');
                        updateUserUI(null);
                    }
                } catch (error) {
                    console.error('Error verifying session:', error);
                    localStorage.removeItem('session_token');
                    localStorage.removeItem('current_user');
                    updateUserUI(null);
                }
            } else {
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

            if(user) {
                const letter = user.email ? user.email[0].toUpperCase() : 'U';
                const email = user.email;

                if(em) em.textContent = email;
                if(st) st.textContent = 'Онлайн';
                if(bigEm) bigEm.textContent = email;

                if(sideText) sideText.textContent = letter;
                if(profText) profText.textContent = letter;

                document.getElementById('auth-modal').style.display = 'none';
            } else {
                if(em) em.textContent = 'Гость';
                if(st) st.textContent = 'Нажмите для входа';
                if(sideText) sideText.textContent = '?';
                document.getElementById('profile-modal').style.display = 'none';
            }
        }

        function resetAvatarUI() {
             const sideImg = document.getElementById('sidebar-avatar-img');
             const profImg = document.getElementById('profile-avatar-img');
             const sideText = document.getElementById('sidebar-avatar-text');
             const profText = document.getElementById('profile-avatar-text');

             sideImg.classList.add('hidden');
             profImg.classList.add('hidden');
             sideText.style.display = 'block';
             profText.style.display = 'block';
        }

        function updateAvatarUI(url) {
            if (!url) return;
            const freshUrl = url + '?t=' + new Date().getTime();

            const sideImg = document.getElementById('sidebar-avatar-img');
            const profImg = document.getElementById('profile-avatar-img');
            const sideText = document.getElementById('sidebar-avatar-text');
            const profText = document.getElementById('profile-avatar-text');

            sideImg.src = freshUrl;
            sideImg.classList.remove('hidden');
            sideText.style.display = 'none';

            profImg.src = freshUrl;
            profImg.classList.remove('hidden');
            profText.style.display = 'none';
        }

        async function uploadAvatar(input) {
            if (!input.files || !input.files[0]) return;
            const file = input.files[0];
            const fileExt = file.name.split('.').pop();
            const fileName = `${currentUser.id}.${fileExt}`;
            const filePath = `avatars/${fileName}`;

            try {
                const { error: uploadError } = await sb.storage
                    .from('avatars')
                    .upload(filePath, file, { upsert: true });

                if (uploadError) throw uploadError;

                const { data } = sb.storage.from('avatars').getPublicUrl(filePath);

                const { error: updateError } = await sb.auth.updateUser({
                    data: { avatar_url: data.publicUrl }
                });

                if (updateError) throw updateError;

                updateAvatarUI(data.publicUrl);
                alert('Аватар обновлен!');
            } catch (error) {
                alert('Ошибка загрузки: ' + error.message);
            }
        }

        async function loadUserAvatar() {
            const { data: { user } } = await sb.auth.getUser();
            if (user && user.user_metadata && user.user_metadata.avatar_url) {
                updateAvatarUI(user.user_metadata.avatar_url);
            }
        }

        function openChangePasswordModal() {
            closeProfileModal();
            document.getElementById('password-modal').style.display = 'flex';
            document.getElementById('password-modal').classList.remove('hidden');
        }

        function closePasswordModal() {
            document.getElementById('password-modal').style.display = 'none';
            document.getElementById('password-modal').classList.add('hidden');
            handleProfileClick();
        }

        document.getElementById('password-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const currentPassword = document.getElementById('current-password').value;
            const newPassword = document.getElementById('new-password').value;
            const btn = document.getElementById('password-submit');

            btn.disabled = true;
            btn.textContent = 'Проверка...';

            try {
                const { error: signInError } = await sb.auth.signInWithPassword({
                    email: currentUser.email,
                    password: currentPassword
                });

                if (signInError) throw new Error("Неверный текущий пароль");

                btn.textContent = 'Обновление...';
                const { error: updateError } = await sb.auth.updateUser({ password: newPassword });

                if (updateError) throw updateError;

                alert('Пароль успешно изменен!');
                closePasswordModal();

            } catch (error) {
                alert('Ошибка: ' + error.message);
            } finally {
                btn.disabled = false;
                btn.textContent = 'Обновить';
            }
        });

        function handleProfileClick() {
            if(currentUser) {
                document.getElementById('profile-modal').style.display = 'flex';
                document.getElementById('profile-modal').classList.remove('hidden');
            } else {
                document.getElementById('auth-modal').style.display = 'flex';
                document.getElementById('auth-modal').classList.remove('hidden');
            }
        }

        function closeAuthModal() { 
            document.getElementById('auth-modal').style.display = 'none';
            document.getElementById('auth-modal').classList.add('hidden');
        }

        function closeProfileModal() { 
            document.getElementById('profile-modal').style.display = 'none'; 
            document.getElementById('profile-modal').classList.add('hidden');
        }

        // --- NEW BUTTON HANDLERS ---

        async function handleLogoutGlobal() {
             if(confirm('Выйти со всех устройств? Вам придется войти заново везде.')) {
                // scope: 'global' signs out all sessions
                const { error } = await sb.auth.signOut({ scope: 'global' });
                if(error) alert('Ошибка: ' + error.message);
                else {
                    closeProfileModal();
                    location.reload();
                }
             }
        }

        // --- NEW BUTTON HANDLERS (FIXED: NO ASYNC/AWAIT) ---

        function handleLogoutGlobal() {
             if(confirm('Выйти со всех устройств? Вам придется войти заново везде.')) {
                // Используем обычный .then вместо await
                sb.auth.signOut({ scope: 'global' }).then(function(resp) {
                    if(resp.error) {
                        alert('Ошибка: ' + resp.error.message);
                    } else {
                        closeProfileModal();
                        location.reload();
                    }
                });
             }
        }

        function handleDeleteAccount() {
             var ok = confirm("ВНИМАНИЕ: Все данные будут удалены. Продолжить?");
             if (!ok) return;

             sb.rpc("delete_own_account")
               .then(function(resp) {
                   if (resp.error) throw resp.error;
                   // Выходим ПОСЛЕ удаления аккаунта
                   return sb.auth.signOut();
               })
               .then(function() {
                   // Перезагружаем страницу ПОСЛЕ выхода
                   alert("Аккаунт удален.");
                   closeProfileModal();
                   location.reload();
               })
               .catch(function(e) {
                   console.error(e);
                   alert("Ошибка удаления.");
               });
        }

        function handleLogout() {
            // Regular logout (local)
            if(confirm('Вы уверены, что хотите выйти?')) {
                sb.auth.signOut().then(() => {
                    closeProfileModal();
                    location.reload();
                });
            }
        }

        function toggleAuthMode() {
            isSignUp = !isSignUp;
            document.getElementById('auth-title').textContent = isSignUp ? 'Регистрация' : 'Вход в систему';
            document.getElementById('auth-submit').textContent = isSignUp ? 'Зарегистрироваться' : 'Войти';
            document.getElementById('auth-switch-btn').textContent = isSignUp ? 'Войти' : 'Регистрация';
            document.getElementById('auth-switch-text').textContent = isSignUp ? 'Уже есть аккаунт?' : 'Нет аккаунта?';
        }

        document.getElementById('auth-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const btn = document.getElementById('auth-submit');

            btn.disabled = true;
            const originalText = btn.textContent;
            btn.textContent = 'Загрузка...';

            try {
                if(isSignUp) {
                    const response = await fetch('/api/auth/signup', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ email, password })
                    });
                    
                    if(response.ok) {
                        const data = await response.json();
                        // Store session token and user info
                        currentSessionToken = data.session_token;
                        currentUser = data.user;
                        localStorage.setItem('session_token', currentSessionToken);
                        localStorage.setItem('current_user', JSON.stringify(currentUser));
                        
                        alert('Регистрация успешна! Добро пожаловать!');
                        closeAuthModal();
                    } else {
                        const errorData = await response.json();
                        throw new Error(errorData.detail || 'Ошибка регистрации');
                    }
                } else {
                    const response = await fetch('/api/auth/signin', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ email, password })
                    });
                    
                    if(response.ok) {
                        const data = await response.json();
                        // Store session token and user info
                        currentSessionToken = data.session_token;
                        currentUser = data.user;
                        localStorage.setItem('session_token', currentSessionToken);
                        localStorage.setItem('current_user', JSON.stringify(currentUser));
                        
                        updateUserUI(data.user);
                        loadUserAvatar();
                        closeAuthModal();
                    } else {
                        const errorData = await response.json();
                        throw new Error(errorData.detail || 'Ошибка входа');
                    }
                }
            } catch(e) {
                alert(e.message);
                btn.disabled = false;
                btn.textContent = originalText;
            } finally {
                 btn.disabled = false;
                 btn.textContent = originalText;
            }
            }
        });

        async function saveRemoteChats() {
            if(!currentUser) return;
            await sb.from('user_data').upsert({ 
                user_id: currentUser.id, 
                data: { chats, settings: userНастройки }
            }, { onConflict: 'user_id' });
        }

        
        async function loadRemoteChats() {
            if(!currentUser) return;
            const list = document.getElementById('chat-list');
            if(list) list.innerHTML = '<div class="p-4 text-center text-gray-500 animate-pulse">Загрузка чатов...</div>';

            const { data, error } = await sb.from('user_data').select('data').eq('user_id', currentUser.id).maybeSingle();

            let serverChats = [];
            let serverSettings = null;

            if (data?.data) {
                serverChats = data.data.chats || [];
                serverSettings = data.data.settings;
            }

            const localBackup = localStorage.getItem('chats');
            let localChats = [];
            try { if(localBackup) localChats = JSON.parse(localBackup); } catch(e){}

            if (serverChats.length === 0 && localChats.length > 0) {
                console.log("Migrating local chats to server...");
                chats = localChats;
                await saveRemoteChats(); 
            } else {
                chats = serverChats;
            }

            if (serverSettings) {
                userНастройки = { ...userНастройки, ...serverSettings };
                applyTheme(userНастройки.theme);
                if(userНастройки.model) document.getElementById('model-select').value = userНастройки.model;
            }

            renderList();
            if(chats.length) loadChat(chats[0].id);
        }


        // --- ADMIN & PRO LOGIC ---
        const ADMIN_EMAIL = "krimex1@mail.ru";
        let userPlan = 'free'; 

        const originalUpdateUserUI = updateUserUI;
        updateUserUI = function(user) {
            originalUpdateUserUI(user);
            if(user) {
                if(user.email === ADMIN_EMAIL) {
                    document.getElementById('admin-panel-btn-container').classList.remove('hidden');
                } else {
                    document.getElementById('admin-panel-btn-container').classList.add('hidden');
                }
                checkUserPlan(user);
            }
        };

        async function checkUserPlan(user) {
            if(!user) return;
            const { data: profile } = await sb.from('profiles').select('plan').eq('id', user.id).single();
            userPlan = profile?.plan || 'free';
            updatePlanUI(userPlan);
            setTimeout(enforceModelRestriction, 200);
        }

        function updatePlanUI(plan) {
            const badge = document.getElementById('profile-plan-badge');
            if(!badge) return;
            if(plan === 'pro') {
                badge.textContent = 'PRO Plan';
                badge.className = 'mt-2 inline-block px-3 py-1 rounded-full text-xs font-bold bg-gradient-to-r from-amber-400 to-orange-500 text-white shadow-lg shadow-orange-500/30';
            } else {
                badge.textContent = 'Free Plan';
                badge.className = 'mt-2 inline-block px-3 py-1 rounded-full text-xs font-bold bg-gray-200 dark:bg-white/10 text-gray-500 dark:text-gray-400';
            }
        }

        function enforceModelRestriction() {
            const select = document.getElementById('model-select');
            if(!select) return;
            const isPro = (userPlan === 'pro' || (currentUser && currentUser.email === ADMIN_EMAIL));
            const msgId = 'pro-lock-msg';

            if(!isPro) {
                if(select.value !== 'auto') {
                    select.value = 'auto';
                    select.dispatchEvent(new Event('change'));
                }
                select.disabled = true; 
                let msg = document.getElementById(msgId);
                if(!msg) {
                    msg = document.createElement('div');
                    msg.id = msgId;
                    msg.className = 'mt-2 p-2 bg-amber-500/10 text-amber-600 dark:text-amber-400 text-xs rounded-lg border border-amber-500/20';
                    msg.innerHTML = '🔒 Выбор моделей доступен только в <b>PRO</b> версии. Используется режим <b>Auto</b>.';
                    select.parentNode.appendChild(msg);
                }
            } else {
                select.disabled = false;
                const msg = document.getElementById(msgId);
                if(msg) msg.remove();
            }
        }

        const origOpenSettings = window.openSettingsModal;
        window.openSettingsModal = function() {
            if(origOpenSettings) origOpenSettings();
            setTimeout(enforceModelRestriction, 50);
        };
        document.addEventListener('change', (e) => {
            if(e.target && e.target.id === 'model-select') enforceModelRestriction();
        });

        // --- ADMIN PANEL FUNCTIONS ---
        async function openAdminPanel() {
            closeProfileModal();
            document.getElementById('admin-modal').style.display = 'flex';
            document.getElementById('admin-modal').classList.remove('hidden');
            loadAdminUsers();
        }
        function closeAdminModal() {
            document.getElementById('admin-modal').style.display = 'none';
            document.getElementById('admin-modal').classList.add('hidden');
        }
        function switchAdminTab(tab) {
            document.getElementById('view-users').className = tab === 'users' ? 'block' : 'hidden';
            document.getElementById('view-sql').className = tab === 'sql' ? 'block' : 'hidden';
            document.getElementById('tab-users').className = tab === 'users' ? 'pb-2 border-b-2 border-blue-500 font-bold' : 'pb-2 border-b-2 border-transparent text-gray-500 hover:text-gray-800 dark:hover:text-gray-200';
            document.getElementById('tab-sql').className = tab === 'sql' ? 'pb-2 border-b-2 border-blue-500 font-bold' : 'pb-2 border-b-2 border-transparent text-gray-500 hover:text-gray-800 dark:hover:text-gray-200';
        }

        async function loadAdminUsers() {
            const tbody = document.getElementById('admin-users-list');
            tbody.innerHTML = '<tr><td colspan="4" class="p-4 text-center">Загрузка...</td></tr>';
            const { data: profiles, error } = await sb.from('profiles').select('*').order('email', { ascending: true });

            if(error) {
                tbody.innerHTML = `<tr><td colspan="4" class="p-4 text-center text-red-500">Ошибка: ${error.message} <br> <button onclick="switchAdminTab('sql')" class="underline">Исправить права (SQL)</button></td></tr>`;
                return;
            }
            if(!profiles || profiles.length === 0) {
                 tbody.innerHTML = `<tr><td colspan="4" class="p-4 text-center text-gray-500">Список пуст. <button onclick="switchAdminTab('sql')" class="underline">Импортировать пользователей</button></td></tr>`;
                 return;
            }

            tbody.innerHTML = '';
            profiles.forEach(u => {
                const tr = document.createElement('tr');
                tr.className = 'border-b border-gray-100 dark:border-white/5 hover:bg-gray-50 dark:hover:bg-white/5';

                tr.innerHTML = `
                    <td class="p-3 font-medium">${u.email || 'Неизвестно'}</td>
                    <td class="p-3 text-xs text-gray-500 font-mono select-all">${u.id}</td>
                    <td class="p-3">
                        <span class="px-2 py-1 rounded text-xs font-bold ${u.plan === 'pro' ? 'bg-amber-100 text-amber-600' : 'bg-gray-100 text-gray-500'}">
                            ${(u.plan || 'free').toUpperCase()}
                        </span>
                    </td>
                    <td class="p-3 flex gap-2 flex-wrap">
                        ${u.plan === 'free' || !u.plan
                            ? `<button onclick="setPlan('${u.id}', 'pro')" class="px-3 py-1 bg-green-500 text-white rounded-lg text-xs hover:bg-green-600">PRO</button>`
                            : `<button onclick="setPlan('${u.id}', 'free')" class="px-3 py-1 bg-gray-500 text-white rounded-lg text-xs hover:bg-gray-600">Снять</button>`
                        }
                        <button onclick="adminChangePass('${u.id}', '${u.email}')" class="px-3 py-1 bg-blue-500/10 text-blue-500 rounded-lg text-xs hover:bg-blue-500 hover:text-white">Пароль</button>
                        <button onclick="adminDeleteUser('${u.id}')" class="px-3 py-1 bg-red-500/10 text-red-500 rounded-lg text-xs hover:bg-red-500 hover:text-white">Удалить</button>
                    </td>
                `;
                tbody.appendChild(tr);
            });
        }

        async function setPlan(targetUserId, newPlan) {
            const { error } = await sb.from('profiles').update({ plan: newPlan }).eq('id', targetUserId);
            if(error) {
                alert("Ошибка! Выполните SQL код во вкладке 'Исправление ошибок': " + error.message);
                switchAdminTab('sql');
            } else {
                loadAdminUsers();
                if(currentUser && currentUser.id === targetUserId) {
                    userPlan = newPlan;
                    updatePlanUI(newPlan);
                    enforceModelRestriction();
                }
            }
        }

        async function adminChangePass(uid, email) {
            const newPass = prompt(`Введите новый пароль для ${email}:`);
            if(!newPass || newPass.length < 6) return alert("Пароль должен быть длиннее 6 символов");
            const { error } = await sb.rpc('admin_update_password', { target_user_id: uid, new_password: newPass });
            if(error) {
                console.error(error);
                alert("Ошибка! Выполните SQL код во вкладке 'Исправление ошибок': " + error.message);
                switchAdminTab('sql');
            } else {
                alert("Пароль успешно изменен!");
            }
        }

        async function adminDeleteUser(uid) {
            if(!confirm("Удалить пользователя навсегда?")) return;
            const { error } = await sb.rpc('admin_delete_user', { target_user_id: uid });
            if(error) {
                console.error(error);
                alert("Ошибка! Выполните SQL код во вкладке 'Исправление ошибок': " + error.message);
                switchAdminTab('sql');
            } else {
                await sb.from('profiles').delete().eq('id', uid);
                loadAdminUsers();
                alert("Пользователь удален.");
            }
        }

        async function deleteMessage(index) {
            if (!confirm("Удалить пару сообщений (вопрос + ответ)?")) return;

            const currentChat = chats.find(c => c.id === activeChatId);
            if (!currentChat || !currentChat.messages[index]) return;

            const msg = currentChat.messages[index];

            // Smart Pair Deletion  
            if (msg.role === 'user' && index < currentChat.messages.length - 1 && currentChat.messages[index + 1].role === 'assistant') {
                // Delete user message and next assistant message
                currentChat.messages.splice(index, 2);
            } else if (msg.role === 'assistant' && index > 0 && currentChat.messages[index - 1].role === 'user') {
                // Delete previous user message and current assistant message
                currentChat.messages.splice(index - 1, 2);
            } else {
                // Delete single message if no pair found
                currentChat.messages.splice(index, 1);
            }

            await save();
            loadChat(activeChatId);
        }

</script>

    <!-- Admin Modal -->
    <div id="admin-modal" class="fixed inset-0 z-[100] bg-black/80 backdrop-blur-sm hidden flex items-center justify-center p-4" style="display: none;">
        <div class="bg-white dark:bg-[#18181b] rounded-2xl shadow-2xl w-full max-w-5xl h-[85vh] flex flex-col border border-gray-200 dark:border-[#27272a] overflow-hidden relative">
            <div class="p-6 border-b border-gray-200 dark:border-[#27272a] flex justify-between items-center bg-gray-50 dark:bg-black/20">
                <h2 class="text-2xl font-bold">Панель Администратора</h2>
                <button onclick="closeAdminModal()" class="text-gray-400 hover:text-gray-600 dark:hover:text-gray-200">
                    <svg class="w-6 h-6"><use href="#icon-x"></use></svg>
                </button>
            </div>

            <div class="flex-1 overflow-auto p-6">
                <!-- TABS -->
                <div class="flex gap-4 mb-6 border-b border-gray-200 dark:border-[#27272a]">
                    <button onclick="switchAdminTab('users')" id="tab-users" class="pb-2 border-b-2 border-blue-500 font-bold">Пользователи</button>
                    <button onclick="switchAdminTab('sql')" id="tab-sql" class="pb-2 border-b-2 border-transparent text-gray-500 hover:text-gray-800 dark:hover:text-gray-200">Исправление ошибок (SQL)</button>
                </div>

                <!-- USERS TAB -->
                <div id="view-users" class="block">
                    <div class="overflow-x-auto">
                        <table class="w-full text-left border-collapse">
                            <thead>
                                <tr class="text-sm text-gray-500 border-b border-gray-200 dark:border-[#27272a]">
                                    <th class="p-3">Email</th>
                                    <th class="p-3">ID</th>
                                    <th class="p-3">План</th>
                                    <th class="p-3">Управление</th>
                                </tr>
                            </thead>
                            <tbody id="admin-users-list" class="text-sm">
                                <tr><td colspan="4" class="p-4 text-center text-gray-500">Загрузка...</td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- SQL TAB -->
                <div id="view-sql" class="hidden">
                    <div class="bg-red-50 dark:bg-red-900/20 text-red-800 dark:text-red-200 p-4 rounded-xl mb-6 text-sm">
                        <h3 class="font-bold text-lg mb-2">🔥 Исправление ошибки "Permission Denied"</h3>
                        <p class="mb-2">Если вы видите ошибку при выдаче PRO или смене пароля, значит старый SQL код был слишком строгим. Выполните этот <b>НОВЫЙ КОД</b> в <a href="https://supabase.com/dashboard/project/_/sql" target="_blank" class="underline hover:text-red-600">Supabase SQL Editor</a>:</p>

                        <div class="relative group">
                            <textarea readonly class="w-full h-64 bg-black/80 text-green-400 font-mono text-xs p-3 rounded-lg border border-white/10 resize-y focus:outline-none" onclick="this.select()">
-- 1. Сбрасываем старые политики, которые вызывали ошибку
drop policy if exists "Update profiles" on public.profiles;
drop policy if exists "Users can update own profile" on public.profiles;
drop policy if exists "Update own" on public.profiles;
drop policy if exists "Public profiles" on public.profiles;

-- 2. Создаем НОВУЮ, правильную политику для таблицы profiles
-- Разрешает обновление, если ты владелец ИЛИ если твой email в токене = admin
create policy "Update profiles safe" on public.profiles for update
using (
  (auth.uid() = id) 
  OR 
  ((auth.jwt() ->> 'email') = 'krimex1@mail.ru')
);

-- Разрешаем чтение всем
create policy "Read profiles" on public.profiles for select using (true);

-- 3. Исправляем RPC функции (удаление и пароль)
-- Используем auth.jwt() вместо select from auth.users чтобы избежать ошибки доступа
create or replace function admin_update_password(target_user_id uuid, new_password text)
returns void as $$
begin
  if (auth.jwt() ->> 'email') = 'krimex1@mail.ru' then
    update auth.users set encrypted_password = crypt(new_password, gen_salt('bf')) where id = target_user_id;
  else
    raise exception 'Access Denied: You are not krimex1@mail.ru';
  end if;
end;
$$ language plpgsql security definer;

create or replace function admin_delete_user(target_user_id uuid)
returns void as $$
begin
  if (auth.jwt() ->> 'email') = 'krimex1@mail.ru' then
    delete from auth.users where id = target_user_id;
  else
    raise exception 'Access Denied: You are not krimex1@mail.ru';
  end if;
end;
$$ language plpgsql security definer;
                            </textarea>
                            <div class="absolute top-2 right-2 text-xs text-gray-400 pointer-events-none group-hover:text-white">Нажмите чтобы выделить</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""
