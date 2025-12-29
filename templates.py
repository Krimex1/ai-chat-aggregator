INDEX_HTML = """
<!DOCTYPE html>
<html lang="en" class="dark:bg-[#212121]">
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

    <!-- Profile Modal -->
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
                <button onclick="changePassword()" class="w-full text-left px-4 py-3 rounded-xl hover:bg-gray-100 dark:hover:bg-[#18181b]/50 transition-all flex items-center gap-3">
                    <svg class="w-5 h-5 text-gray-500"><use href="#icon-lock"></use></svg>
                    <span>Сменить пароль</span>
                </button>
                <button onclick="exportChatHistory()" class="w-full text-left px-4 py-3 rounded-xl hover:bg-gray-100 dark:hover:bg-[#18181b]/50 transition-all flex items-center gap-3">
                    <svg class="w-5 h-5 text-gray-500"><use href="#icon-download"></use></svg>
                    <span>Экспорт чатов</span>
                </button>
                <button onclick="deleteAccount()" class="w-full text-left px-4 py-3 rounded-xl hover:bg-gray-100 dark:hover:bg-[#18181b]/50 transition-all flex items-center gap-3 text-red-500">
                    <svg class="w-5 h-5"><use href="#icon-trash"></use></svg>
                    <span>Удалить аккаунт</span>
                </button>
            </div>
        </div>
    </div>

    <!-- Settings Modal -->
    <div id="settings-modal" class="fixed inset-0 z-[80] bg-black/60 backdrop-blur-sm hidden flex items-center justify-center p-4" style="display: none;">
        <div class="bg-white dark:bg-[#18181b] rounded-2xl shadow-2xl w-full max-w-sm border border-gray-200 dark:border-[#27272a] overflow-hidden transform transition-all p-6 relative">
            <button onclick="closeSettingsModal()" class="absolute top-4 right-4 text-gray-400 hover:text-gray-600 dark:hover:text-gray-200">
                <svg class="w-6 h-6"><use href="#icon-x"></use></svg>
            </button>
            <h2 class="text-xl font-bold mb-6">Настройки</h2>
            <div class="space-y-4">
                <div class="flex items-center justify-between">
                    <span>Темная тема</span>
                    <button id="theme-toggle" onclick="toggleTheme()" class="w-12 h-6 bg-gray-300 dark:bg-[#27272a] rounded-full relative transition-colors">
                        <div class="w-5 h-5 bg-white dark:bg-white rounded-full absolute top-0.5 left-0.5 transition-transform"></div>
                    </button>
                </div>
                <div class="flex items-center justify-between">
                    <span>Режим кодирования</span>
                    <button id="coding-btn" onclick="toggleCoding()" class="w-12 h-6 bg-gray-300 dark:bg-[#27272a] rounded-full relative transition-colors">
                        <div class="w-5 h-5 bg-white dark:bg-white rounded-full absolute top-0.5 left-0.5 transition-transform"></div>
                    </button>
                </div>
                <div class="flex items-center justify-between">
                    <span>Режим рассуждения</span>
                    <button id="reasoning-btn" onclick="toggleReasoning()" class="w-12 h-6 bg-gray-300 dark:bg-[#27272a] rounded-full relative transition-colors">
                        <div class="w-5 h-5 bg-white dark:bg-white rounded-full absolute top-0.5 left-0.5 transition-transform"></div>
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- Sidebar -->
    <div id="sidebar" class="sidebar w-64 flex flex-col h-full fixed left-0 top-0 z-40 transition-transform duration-300">
        <div class="p-4 border-b border-gray-200 dark:border-[#27272a]">
            <div class="flex items-center gap-3 mb-6">
                <div class="w-10 h-10 rounded-lg bg-gradient-to-br from-accent to-purple-600 flex items-center justify-center text-white font-bold">P</div>
                <h1 class="text-xl font-bold">Proxify AI</h1>
            </div>
            <button onclick="handleNewChatClick()" class="w-full bg-accent hover:bg-accent/90 text-white font-medium py-2.5 rounded-xl transition-all shadow-lg shadow-accent/25 flex items-center justify-center gap-2">
                <svg class="w-5 h-5"><use href="#icon-plus"></use></svg>
                Новый чат
            </button>
        </div>

        <div class="flex-1 overflow-y-auto p-2">
            <div class="space-y-1" id="chat-history-list">
                <!-- Chat history will be populated here -->
            </div>
        </div>

        <div class="p-4 border-t border-gray-200 dark:border-[#27272a]">
            <div class="flex items-center justify-between mb-4">
                <div class="flex items-center gap-3 cursor-pointer" onclick="handleProfileClick()">
                    <div class="w-10 h-10 rounded-full bg-gradient-to-br from-accent to-purple-600 flex items-center justify-center text-white font-bold text-sm" id="sidebar-avatar">
                        ?
                    </div>
                    <div class="flex-1 min-w-0">
                        <p class="font-medium truncate" id="sidebar-email">guest@example.com</p>
                        <p class="text-xs text-gray-500 dark:text-gray-400 truncate">Free Plan</p>
                    </div>
                    <svg class="w-5 h-5 text-gray-400"><use href="#icon-chevron-down"></use></svg>
                </div>
            </div>
            
            <div class="flex gap-2">
                <button onclick="toggleНастройки()" class="flex-1 py-2.5 rounded-xl bg-gray-100 dark:bg-[#18181b] hover:bg-gray-200 dark:hover:bg-[#1f1f23] transition-all flex items-center justify-center gap-2">
                    <svg class="w-5 h-5"><use href="#icon-settings"></use></svg>
                </button>
                <button onclick="clearHistory()" class="flex-1 py-2.5 rounded-xl bg-gray-100 dark:bg-[#18181b] hover:bg-gray-200 dark:hover:bg-[#1f1f23] transition-all flex items-center justify-center gap-2">
                    <svg class="w-5 h-5"><use href="#icon-trash"></use></svg>
                </button>
            </div>
        </div>
    </div>

    <!-- Main Chat Area -->
    <div class="flex-1 flex flex-col ml-64">
        <div id="chat-container">
            <div class="max-w-3xl mx-auto px-4 py-8">
                <div class="text-center mb-12">
                    <h2 class="text-3xl font-bold mb-4">Добро пожаловать в Proxify AI</h2>
                    <p class="text-gray-600 dark:text-gray-400">Задайте вопрос, и я помогу вам найти ответ</p>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 max-w-2xl mx-auto">
                    <div class="p-4 bg-gray-100 dark:bg-[#18181b]/50 rounded-xl hover:bg-gray-200 dark:hover:bg-[#18181b] transition-all cursor-pointer" onclick="quickPrompt('Объясни концепцию машинного обучения простыми словами')">
                        <h3 class="font-medium mb-1">Объясни концепцию</h3>
                        <p class="text-sm text-gray-600 dark:text-gray-400">Машинное обучение простыми словами</p>
                    </div>
                    <div class="p-4 bg-gray-100 dark:bg-[#18181b]/50 rounded-xl hover:bg-gray-200 dark:hover:bg-[#18181b] transition-all cursor-pointer" onclick="quickPrompt('Создай план проекта на Python')">
                        <h3 class="font-medium mb-1">Создай план</h3>
                        <p class="text-sm text-gray-600 dark:text-gray-400">Проект на Python</p>
                    </div>
                    <div class="p-4 bg-gray-100 dark:bg-[#18181b]/50 rounded-xl hover:bg-gray-200 dark:hover:bg-[#18181b] transition-all cursor-pointer" onclick="quickPrompt('Напиши пример кода на JavaScript для работы с API')">
                        <h3 class="font-medium mb-1">Напиши код</h3>
                        <p class="text-sm text-gray-600 dark:text-gray-400">Работа с API на JavaScript</p>
                    </div>
                    <div class="p-4 bg-gray-100 dark:bg-[#18181b]/50 rounded-xl hover:bg-gray-200 dark:hover:bg-[#18181b] transition-all cursor-pointer" onclick="quickPrompt('Как подготовиться к собеседованию на Python разработчика?')">
                        <h3 class="font-medium mb-1">Подготовься</h3>
                        <p class="text-sm text-gray-600 dark:text-gray-400">Собеседование на Python разработчика</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Input Area -->
        <div class="input-container-fixed">
            <div class="max-w-3xl mx-auto">
                <div class="input-box-wrapper rounded-2xl p-2">
                    <div class="flex items-end gap-2">
                        <textarea 
                            id="message-input" 
                            placeholder="Напишите сообщение..." 
                            class="flex-1 bg-transparent border-0 outline-none resize-none text-base max-h-32 min-h-6 py-3 px-4"
                            onkeydown="handleKeyDown(event)"
                        ></textarea>
                        <button 
                            onclick="sendMessage()" 
                            id="send-button"
                            class="m-2 bg-accent hover:bg-accent/90 text-white rounded-xl w-11 h-11 flex items-center justify-center transition-all disabled:opacity-50"
                        >
                            <svg class="w-5 h-5"><use href="#icon-send"></use></svg>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Context Menu -->
    <div id="context-menu" class="absolute bg-white dark:bg-[#18181b] border border-gray-200 dark:border-[#27272a] rounded-xl shadow-lg py-2 z-50" style="display: none;">
        <div class="px-4 py-2 hover:bg-gray-100 dark:hover:bg-[#18181b]/50 cursor-pointer" onclick="copyMessage(this)">Копировать</div>
        <div class="px-4 py-2 hover:bg-gray-100 dark:hover:bg-[#18181b]/50 cursor-pointer" onclick="regenerateResponse(this)">Повторить</div>
        <div class="px-4 py-2 hover:bg-gray-100 dark:hover:bg-[#18181b]/50 cursor-pointer text-red-500" onclick="deleteMessage(this)">Удалить</div>
    </div>

    <!-- Icons -->
    <svg class="hidden">
        <symbol id="icon-x" viewBox="0 0 24 24">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 6 6 18M6 6l12 12"/>
        </symbol>
        <symbol id="icon-image" viewBox="0 0 24 24">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/>
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 2v6h6"/>
            <circle cx="9.5" cy="9.5" r="1.5" fill="currentColor"/>
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L9.5 17.5"/>
        </symbol>
        <symbol id="icon-lock" viewBox="0 0 24 24">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 12V9A6 6 0 1 0 6 9v3"/>
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-2v-2h2v2Z"/>
        </symbol>
        <symbol id="icon-download" viewBox="0 0 24 24">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m7 10 5 5 5-5"/>
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15V3"/>
        </symbol>
        <symbol id="icon-trash" viewBox="0 0 24 24">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6h18M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>
        </symbol>
        <symbol id="icon-chevron-down" viewBox="0 0 24 24">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m6 9 6 6 6-6"/>
        </symbol>
        <symbol id="icon-settings" viewBox="0 0 24 24">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12.22 2h-.44a2 2 0 0 0-2 1.5l-.15 1.1a2 2 0 0 1-1.82 1.7l-1.2.17a2 2 0 0 0-1.1 3.5l.7.7a2 2 0 0 1 0 2.8l-.7.7a2 2 0 0 0 1.1 3.5l1.2.17a2 2 0 0 1 1.82 1.7l.15 1.1a2 2 0 0 0 2 1.5h.44a2 2 0 0 0 2-1.5l.15-1.1a2 2 0 0 1 1.82-1.7l1.2-.17a2 2 0 0 0 1.1-3.5l-.7-.7a2 2 0 0 1 0-2.8l.7-.7a2 2 0 0 0-1.1-3.5l-1.2-.17a2 2 0 0 1-1.82-1.7l-.15-1.1A2 2 0 0 0 12.22 2Z"/>
            <circle cx="12" cy="12" r="3" fill="none" stroke="currentColor" stroke-width="2"/>
        </symbol>
        <symbol id="icon-plus" viewBox="0 0 24 24">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14M12 5v14"/>
        </symbol>
        <symbol id="icon-send" viewBox="0 0 24 24">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M22 2 11 13M22 2l-7 20-4-9-9-4 20-7Z"/>
        </symbol>
    </svg>

    <script>
        // Global variables
        let currentUser = null;
        let currentChatId = null;
        let codingEnabled = false;
        let reasoningEnabled = false;
        let isProcessing = false;
        let messageQueue = [];

        // DOM Elements
        const chatContainer = document.getElementById('chat-container');
        const messageInput = document.getElementById('message-input');
        const sendButton = document.getElementById('send-button');

        // Initialize the app
        document.addEventListener('DOMContentLoaded', function() {
            initializeApp();
        });

        // Initialize the app
        function initializeApp() {
            loadTheme();
            setupEventListeners();
            checkAuthStatus();
        }

        // Check authentication status
        async function checkAuthStatus() {
            try {
                const response = await fetch('/api/session');
                if (response.ok) {
                    const data = await response.json();
                    if (data.user) {
                        currentUser = data.user;
                        updateUserInterface();
                        loadChatHistory();
                    } else {
                        showAuthModal();
                    }
                } else {
                    showAuthModal();
                }
            } catch (error) {
                console.error('Error checking auth status:', error);
                showAuthModal();
            }
        }

        // Show auth modal
        function showAuthModal() {
            document.getElementById('auth-modal').style.display = 'flex';
            document.getElementById('auth-title').textContent = 'Вход в систему';
            document.getElementById('auth-submit').textContent = 'Войти';
            document.getElementById('auth-switch-text').textContent = 'Нет аккаунта?';
            document.getElementById('auth-switch-btn').textContent = 'Регистрация';
            document.getElementById('auth-form').onsubmit = handleLogin;
        }

        // Close auth modal
        function closeAuthModal() {
            document.getElementById('auth-modal').style.display = 'none';
        }

        // Toggle auth mode (login/register)
        function toggleAuthMode() {
            const isLogin = document.getElementById('auth-submit').textContent === 'Войти';
            if (isLogin) {
                // Switch to register
                document.getElementById('auth-title').textContent = 'Создать аккаунт';
                document.getElementById('auth-submit').textContent = 'Зарегистрироваться';
                document.getElementById('auth-switch-text').textContent = 'Уже есть аккаунт?';
                document.getElementById('auth-switch-btn').textContent = 'Вход';
                document.getElementById('auth-form').onsubmit = handleRegister;
            } else {
                // Switch to login
                document.getElementById('auth-title').textContent = 'Вход в систему';
                document.getElementById('auth-submit').textContent = 'Войти';
                document.getElementById('auth-switch-text').textContent = 'Нет аккаунта?';
                document.getElementById('auth-switch-btn').textContent = 'Регистрация';
                document.getElementById('auth-form').onsubmit = handleLogin;
            }
        }

        // Handle login
        async function handleLogin(event) {
            event.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            try {
                const response = await fetch('/api/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, password })
                });

                const data = await response.json();
                if (response.ok) {
                    currentUser = data.user;
                    closeAuthModal();
                    updateUserInterface();
                    loadChatHistory();
                } else {
                    alert(data.error || 'Ошибка входа');
                }
            } catch (error) {
                console.error('Login error:', error);
                alert('Ошибка подключения');
            }
        }

        // Handle registration
        async function handleRegister(event) {
            event.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            try {
                const response = await fetch('/api/register', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, password })
                });

                const data = await response.json();
                if (response.ok) {
                    currentUser = data.user;
                    closeAuthModal();
                    updateUserInterface();
                    loadChatHistory();
                } else {
                    alert(data.error || 'Ошибка регистрации');
                }
            } catch (error) {
                console.error('Registration error:', error);
                alert('Ошибка подключения');
            }
        }

        // Update user interface with user data
        function updateUserInterface() {
            if (!currentUser) return;

            // Update sidebar
            document.getElementById('sidebar-email').textContent = currentUser.email;
            document.getElementById('sidebar-avatar').textContent = currentUser.email.charAt(0).toUpperCase();
            
            // Update profile modal
            document.getElementById('profile-email').textContent = currentUser.email;
            if (currentUser.avatar) {
                document.getElementById('profile-avatar-img').src = currentUser.avatar;
                document.getElementById('profile-avatar-img').classList.remove('hidden');
                document.getElementById('profile-avatar-text').classList.add('hidden');
                document.getElementById('sidebar-avatar').innerHTML = `<img src="${currentUser.avatar}" class="w-full h-full object-cover rounded-full" />`;
            } else {
                document.getElementById('profile-avatar-img').classList.add('hidden');
                document.getElementById('profile-avatar-text').classList.remove('hidden');
                document.getElementById('profile-avatar-text').textContent = currentUser.email.charAt(0).toUpperCase();
                document.getElementById('sidebar-avatar').textContent = currentUser.email.charAt(0).toUpperCase();
            }
        }

        // Show profile modal
        function handleProfileClick() {
            document.getElementById('profile-modal').style.display = 'flex';
        }

        // Close profile modal
        function closeProfileModal() {
            document.getElementById('profile-modal').style.display = 'none';
        }

        // Hide context menu
        function hideContextMenu() {
            document.getElementById('context-menu').style.display = 'none';
        }

        // Handle new chat click
        function handleNewChatClick() {
            createNewChat();
        }

        // Create new chat
        async function createNewChat() {
            if (!currentUser) return;

            try {
                const response = await fetch('/api/chats', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ title: 'Новый чат' })
                });

                const data = await response.json();
                if (response.ok) {
                    currentChatId = data.chat.id;
                    loadChatHistory();
                    location.hash = `chat-${currentChatId}`;
                }
            } catch (error) {
                console.error('Error creating chat:', error);
            }
        }

        // Toggle settings modal
        function toggleНастройки() {
            const modal = document.getElementById('settings-modal');
            if (modal.style.display === 'flex') {
                modal.style.display = 'none';
            } else {
                modal.style.display = 'flex';
            }
        }

        // Close settings modal
        function closeSettingsModal() {
            document.getElementById('settings-modal').style.display = 'none';
        }

        // Clear chat history
        async function clearHistory() {
            if (!currentChatId || !confirm('Вы уверены, что хотите очистить историю этого чата?')) return;

            try {
                const response = await fetch(`/api/chats/${currentChatId}`, {
                    method: 'DELETE'
                });

                if (response.ok) {
                    // Clear the chat container
                    chatContainer.innerHTML = '<div class="max-w-3xl mx-auto px-4 py-8"><div class="text-center mb-12"><h2 class="text-3xl font-bold mb-4">Добро пожаловать в Proxify AI</h2><p class="text-gray-600 dark:text-gray-400">Задайте вопрос, и я помогу вам найти ответ</p></div></div>';
                    currentChatId = null;
                    loadChatHistory();
                }
            } catch (error) {
                console.error('Error clearing history:', error);
            }
        }

        // Toggle theme
        function toggleTheme() {
            document.documentElement.classList.toggle('dark');
            localStorage.setItem('theme', document.documentElement.classList.contains('dark') ? 'dark' : 'light');
        }

        // Load theme from localStorage
        function loadTheme() {
            const savedTheme = localStorage.getItem('theme');
            if (savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
                document.documentElement.classList.add('dark');
            } else {
                document.documentElement.classList.remove('dark');
            }
        }

        // Toggle coding mode
        function toggleCoding() {
            codingEnabled = !codingEnabled;
            if(codingEnabled) { reasoningEnabled = false; checkToggles(); }
            checkToggles();
        }

        // Toggle reasoning mode
        function toggleReasoning() {
            reasoningEnabled = !reasoningEnabled;
            if(reasoningEnabled) { codingEnabled = false; checkToggles(); }
            checkToggles();
        }

        // Check toggles and update UI
        function checkToggles() {
            const cBtn = document.getElementById("coding-btn");
            const cBadge = document.getElementById("coding-badge");
            const rBtn = document.getElementById("reasoning-btn");
            const rBadge = document.getElementById("reasoning-badge");

            if (codingEnabled) {
                cBtn.classList.add("text-accent", "bg-accent/10");
            } else {
                cBtn.classList.remove("text-accent", "bg-accent/10");
            }

            if (reasoningEnabled) {
                rBtn.classList.add("text-accent", "bg-accent/10");
            } else {
                rBtn.classList.remove("text-accent", "bg-accent/10");
            }
        }

        // Setup event listeners
        function setupEventListeners() {
            // Form submission
            document.getElementById('auth-form').onsubmit = handleLogin;

            // Message input
            messageInput.addEventListener('keydown', function(e) {
                if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    sendMessage();
                }
            });

            // Theme toggle
            const themeToggle = document.getElementById('theme-toggle');
            if (themeToggle) {
                themeToggle.addEventListener('click', function() {
                    document.documentElement.classList.toggle('dark');
                    const isDark = document.documentElement.classList.contains('dark');
                    this.setAttribute('aria-checked', isDark);
                    localStorage.setItem('theme', isDark ? 'dark' : 'light');
                    
                    // Update toggle position
                    const thumb = this.querySelector('div');
                    if (isDark) {
                        thumb.style.transform = 'translateX(1.25rem)';
                    } else {
                        thumb.style.transform = 'translateX(0)';
                    }
                });
            }
        }

        // Handle key down in message input
        function handleKeyDown(event) {
            if (event.key === 'Enter' && !event.shiftKey) {
                event.preventDefault();
                sendMessage();
            }
        }

        // Send message
        async function sendMessage() {
            const message = messageInput.value.trim();
            if (!message || isProcessing) return;

            isProcessing = true;
            sendButton.disabled = true;

            // Add user message to UI
            addMessageToUI('user', message);
            messageInput.value = '';
            
            try {
                // Get or create chat
                if (!currentChatId) {
                    await createNewChat();
                }

                // Send message to server
                const response = await fetch(`/api/chats/${currentChatId}/messages`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ 
                        content: message,
                        coding_enabled: codingEnabled,
                        reasoning_enabled: reasoningEnabled
                    })
                });

                if (response.ok) {
                    const data = await response.json();
                    // The server will return the AI response
                    addMessageToUI('assistant', data.response);
                } else {
                    const error = await response.json();
                    addMessageToUI('assistant', `Ошибка: ${error.error || 'Не удалось получить ответ'}`);
                }
            } catch (error) {
                console.error('Send message error:', error);
                addMessageToUI('assistant', 'Ошибка подключения к серверу');
            } finally {
                isProcessing = false;
                sendButton.disabled = false;
                messageInput.focus();
            }
        }

        // Add message to UI
        function addMessageToUI(role, content) {
            // Remove welcome message if it's the first message
            const welcomeEl = chatContainer.querySelector('.max-w-3xl.text-center');
            if (welcomeEl && chatContainer.children.length <= 2) {
                welcomeEl.parentElement.innerHTML = '';
            }

            const messageDiv = document.createElement('div');
            messageDiv.className = `mb-6 ${role === 'user' ? 'text-right' : 'text-left'}`;
            
            const bubbleDiv = document.createElement('div');
            bubbleDiv.className = role === 'user' 
                ? 'chat-bubble-user inline-block max-w-[85%] break-words' 
                : 'chat-bubble-assistant inline-block max-w-[85%] break-words bg-gray-100 dark:bg-[#18181b] rounded-2xl px-4 py-3';
            
            if (role === 'assistant') {
                // Process markdown content
                bubbleDiv.innerHTML = marked.parse(content);
                // Highlight code blocks
                bubbleDiv.querySelectorAll('pre code').forEach((block) => {
                    hljs.highlightElement(block);
                    
                    // Add copy button to code blocks
                    const copyBtn = document.createElement('button');
                    copyBtn.className = 'code-copy-btn';
                    copyBtn.innerHTML = '<svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1zM6 6a1 1 0 011-1h6a1 1 0 110 2H7a1 1 0 01-1-1z"/></svg> Копировать';
                    copyBtn.onclick = () => copyCode(block);
                    block.parentNode.style.position = 'relative';
                    block.parentNode.appendChild(copyBtn);
                });
            } else {
                bubbleDiv.textContent = content;
            }
            
            messageDiv.appendChild(bubbleDiv);
            chatContainer.appendChild(messageDiv);
            
            // Scroll to bottom
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }

        // Copy code function
        function copyCode(codeElement) {
            navigator.clipboard.writeText(codeElement.textContent).then(() => {
                const btn = codeElement.parentNode.querySelector('.code-copy-btn');
                btn.innerHTML = '<svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg> Скопировано';
                btn.classList.add('copied');
                setTimeout(() => {
                    btn.innerHTML = '<svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1zM6 6a1 1 0 111-1h6a1 1 0 110 2H7a1 1 0 01-1-1z"/></svg> Копировать';
                    btn.classList.remove('copied');
                }, 2000);
            });
        }

        // Quick prompt function
        function quickPrompt(prompt) {
            messageInput.value = prompt;
            messageInput.focus();
        }

        // Load chat history
        async function loadChatHistory() {
            if (!currentUser) return;

            try {
                const response = await fetch('/api/chats');
                if (response.ok) {
                    const chats = await response.json();
                    const chatList = document.getElementById('chat-history-list');
                    chatList.innerHTML = '';

                    chats.forEach(chat => {
                        const chatItem = document.createElement('div');
                        chatItem.className = 'p-2 rounded-xl hover:bg-gray-100 dark:hover:bg-[#18181b]/50 cursor-pointer flex items-center justify-between';
                        chatItem.onclick = () => loadChat(chat.id);
                        
                        const titleSpan = document.createElement('span');
                        titleSpan.className = 'truncate text-sm';
                        titleSpan.textContent = chat.title || 'Новый чат';
                        
                        const deleteBtn = document.createElement('button');
                        deleteBtn.className = 'p-1 rounded-lg hover:bg-gray-200 dark:hover:bg-[#18181b] text-gray-500 hover:text-red-500';
                        deleteBtn.innerHTML = '<svg class="w-4 h-4"><use href="#icon-trash"></use></svg>';
                        deleteBtn.onclick = (e) => {
                            e.stopPropagation();
                            deleteChat(chat.id);
                        };
                        
                        chatItem.appendChild(titleSpan);
                        chatItem.appendChild(deleteBtn);
                        chatList.appendChild(chatItem);
                    });
                }
            } catch (error) {
                console.error('Error loading chat history:', error);
            }
        }

        // Load specific chat
        async function loadChat(chatId) {
            try {
                const response = await fetch(`/api/chats/${chatId}/messages`);
                if (response.ok) {
                    const messages = await response.json();
                    currentChatId = chatId;
                    
                    // Clear chat container and load messages
                    chatContainer.innerHTML = '';
                    messages.forEach(msg => {
                        addMessageToUI(msg.role, msg.content);
                    });
                }
            } catch (error) {
                console.error('Error loading chat:', error);
            }
        }

        // Delete chat
        async function deleteChat(chatId) {
            if (!confirm('Вы уверены, что хотите удалить этот чат?')) return;

            try {
                const response = await fetch(`/api/chats/${chatId}`, {
                    method: 'DELETE'
                });

                if (response.ok) {
                    loadChatHistory();
                    if (currentChatId === chatId) {
                        chatContainer.innerHTML = '<div class="max-w-3xl mx-auto px-4 py-8"><div class="text-center mb-12"><h2 class="text-3xl font-bold mb-4">Добро пожаловать в Proxify AI</h2><p class="text-gray-600 dark:text-gray-400">Задайте вопрос, и я помогу вам найти ответ</p></div></div>';
                        currentChatId = null;
                    }
                }
            } catch (error) {
                console.error('Error deleting chat:', error);
            }
        }

        // Upload avatar
        async function uploadAvatar(input) {
            if (!input.files[0]) return;

            const formData = new FormData();
            formData.append('avatar', input.files[0]);

            try {
                const response = await fetch('/api/avatar', {
                    method: 'POST',
                    body: formData
                });

                if (response.ok) {
                    const data = await response.json();
                    currentUser.avatar = data.avatar_url;
                    updateUserInterface();
                } else {
                    const error = await response.json();
                    alert(error.error || 'Ошибка загрузки аватара');
                }
            } catch (error) {
                console.error('Upload avatar error:', error);
                alert('Ошибка подключения');
            }
        }

        // Change password
        function changePassword() {
            closeProfileModal();
            const newPassword = prompt('Введите новый пароль:');
            if (!newPassword) return;

            updatePassword(newPassword);
        }

        // Update password
        async function updatePassword(newPassword) {
            try {
                const response = await fetch('/api/password', {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ new_password: newPassword })
                });

                const data = await response.json();
                if (response.ok) {
                    alert('Пароль успешно изменен');
                } else {
                    alert(data.error || 'Ошибка изменения пароля');
                }
            } catch (error) {
                console.error('Update password error:', error);
                alert('Ошибка подключения');
            }
        }

        // Export chat history
        async function exportChatHistory() {
            try {
                const response = await fetch('/api/export');
                if (response.ok) {
                    const data = await response.json();
                    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
                    const url = URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = `chat-history-${new Date().toISOString().slice(0, 10)}.json`;
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                    URL.revokeObjectURL(url);
                } else {
                    alert('Ошибка экспорта чатов');
                }
            } catch (error) {
                console.error('Export error:', error);
                alert('Ошибка экспорта чатов');
            }
        }

        // Delete account
        async function deleteAccount() {
            if (!confirm('Вы уверены, что хотите удалить свой аккаунт? Это действие необратимо.')) return;

            try {
                const response = await fetch('/api/account', {
                    method: 'DELETE'
                });

                if (response.ok) {
                    currentUser = null;
                    closeProfileModal();
                    showAuthModal();
                } else {
                    alert('Ошибка удаления аккаунта');
                }
            } catch (error) {
                console.error('Delete account error:', error);
                alert('Ошибка подключения');
            }
        }

        // Context menu functions
        function copyMessage(element) {
            const messageElement = element.closest('.chat-bubble-assistant, .chat-bubble-user');
            if (messageElement) {
                navigator.clipboard.writeText(messageElement.textContent);
            }
            hideContextMenu();
        }

        function regenerateResponse(element) {
            // This would require more complex implementation to regenerate the last response
            alert('Функция в разработке');
            hideContextMenu();
        }

        function deleteMessage(element) {
            const messageElement = element.closest('.mb-6');
            if (messageElement) {
                messageElement.remove();
            }
            hideContextMenu();
        }
    </script>
</body>
</html>
"""