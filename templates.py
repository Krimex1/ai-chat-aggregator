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
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        primary: '#6366f1',
                        secondary: '#8b5cf6',
                        background: '#0f172a',
                        surface: '#1e293b',
                        'surface-light': '#334155'
                    }
                }
            }
        }
    </script>
</head>
<body class="bg-background text-gray-100 min-h-screen p-4 md:p-8">
    <div class="max-w-7xl mx-auto">
        <div class="text-center mb-8">
            <h1 class="text-4xl font-bold bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent mb-2">
                Proxify AI
            </h1>
            <p class="text-gray-400">Multi-Model AI Chat with Web Search & Analytics</p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
            <div class="lg:col-span-2 bg-surface rounded-xl p-6 shadow-2xl border border-gray-700">
                <div class="flex items-center justify-between mb-4">
                    <h2 class="text-xl font-semibold">Chat</h2>
                    <div class="flex gap-2">
                        <button id="clear-btn" class="px-4 py-2 bg-red-600 hover:bg-red-700 rounded-lg text-sm transition">
                            Clear
                        </button>
                    </div>
                </div>
                
                <div id="chat-container" class="h-96 overflow-y-auto mb-4 space-y-4 scrollbar-thin scrollbar-thumb-primary scrollbar-track-surface-light">
                </div>

                <div class="space-y-4">
                    <div class="flex gap-2">
                        <select id="model-select" class="flex-1 bg-surface-light border border-gray-600 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-primary">
                            <option value="auto">Auto (Best Free Model)</option>
                            <option value="mistralai/devstral-2512:free">Mistral DevStral 2512</option>
                            <option value="amazon/nova-2-lite-v1:free">Amazon Nova 2 Lite</option>
                            <option value="google/gemini-2.0-flash-exp:free">Gemini 2.0 Flash</option>
                            <option value="nvidia/nemotron-nano-12b-v2-vl:free">NVIDIA Nemotron Nano</option>
                            <option value="deepseek/deepseek-chat-v3.1">DeepSeek Chat V3.1</option>
                        </select>
                    </div>

                    <div class="flex gap-2">
                        <label class="flex items-center gap-2 bg-surface-light px-4 py-2 rounded-lg cursor-pointer hover:bg-gray-600 transition">
                            <input type="checkbox" id="web-search-toggle" class="form-checkbox h-5 w-5 text-primary">
                            <span class="text-sm">Web Search</span>
                        </label>
                        <label class="flex items-center gap-2 bg-surface-light px-4 py-2 rounded-lg cursor-pointer hover:bg-gray-600 transition">
                            <input type="checkbox" id="coding-toggle" class="form-checkbox h-5 w-5 text-secondary">
                            <span class="text-sm">Coding Mode</span>
                        </label>
                    </div>

                    <div class="flex gap-2">
                        <textarea id="user-input" 
                            placeholder="Type your message..." 
                            class="flex-1 bg-surface-light border border-gray-600 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-primary resize-none"
                            rows="3"></textarea>
                        <button id="send-btn" class="px-6 bg-gradient-to-r from-primary to-secondary hover:from-primary/90 hover:to-secondary/90 rounded-lg font-semibold transition shadow-lg">
                            Send
                        </button>
                    </div>
                </div>
            </div>

            <div class="bg-surface rounded-xl p-6 shadow-2xl border border-gray-700">
                <h2 class="text-xl font-semibold mb-4">Settings & Info</h2>
                
                <div class="space-y-4 text-sm">
                    <div class="bg-surface-light p-4 rounded-lg">
                        <h3 class="font-semibold text-primary mb-2">Current Model</h3>
                        <p id="current-model" class="text-gray-300">Auto</p>
                    </div>

                    <div class="bg-surface-light p-4 rounded-lg">
                        <h3 class="font-semibold text-secondary mb-2">Features</h3>
                        <ul class="space-y-2 text-gray-300">
                            <li>✓ Multi-model support</li>
                            <li>✓ Web search integration</li>
                            <li>✓ Coding mode</li>
                            <li>✓ Stream responses</li>
                        </ul>
                    </div>

                    <div class="bg-surface-light p-4 rounded-lg">
                        <h3 class="font-semibold text-primary mb-2">Analytics</h3>
                        <a href="/analytics" target="_blank" class="text-blue-400 hover:text-blue-300 transition">
                            View LLM Leaderboard →
                        </a>
                    </div>

                    <div class="bg-surface-light p-4 rounded-lg">
                        <h3 class="font-semibold text-secondary mb-2">Status</h3>
                        <div class="flex items-center gap-2">
                            <div class="w-3 h-3 bg-green-500 rounded-full animate-pulse"></div>
                            <span class="text-gray-300">Online</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        let messages = [];
        let currentController = null;
        let codingEnabled = false;
        let reasoningEnabled = false;

        const chatContainer = document.getElementById('chat-container');
        const userInput = document.getElementById('user-input');
        const sendBtn = document.getElementById('send-btn');
        const clearBtn = document.getElementById('clear-btn');
        const modelSelect = document.getElementById('model-select');
        const webSearchToggle = document.getElementById('web-search-toggle');
        const codingToggle = document.getElementById('coding-toggle');
        const currentModelDisplay = document.getElementById('current-model');

        function addMessage(role, content) {
            const messageDiv = document.createElement('div');
            messageDiv.className = `p-4 rounded-lg ${role === 'user' ? 'bg-primary/20 ml-8' : 'bg-surface-light mr-8'}`;
            
            const roleSpan = document.createElement('div');
            roleSpan.className = 'font-semibold mb-1 text-sm';
            roleSpan.textContent = role === 'user' ? 'You' : 'AI';
            
            const contentDiv = document.createElement('div');
            contentDiv.className = 'whitespace-pre-wrap';
            contentDiv.textContent = content;
            
            messageDiv.appendChild(roleSpan);
            messageDiv.appendChild(contentDiv);
            chatContainer.appendChild(messageDiv);
            chatContainer.scrollTop = chatContainer.scrollHeight;
            
            return contentDiv;
        }

        async function sendMessage() {
            const text = userInput.value.trim();
            if (!text || currentController) return;

            messages.push({ role: 'user', content: text });
            addMessage('user', text);
            userInput.value = '';

            const assistantDiv = addMessage('assistant', '');
            currentController = new AbortController();

            try {
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        messages,
                        web_search: webSearchToggle.checked,
                        model: modelSelect.value,
                        coding_mode: codingToggle.checked,
                        coding_model: 'kwaipilot/kat-coder-pro:free'
                    }),
                    signal: currentController.signal
                });

                const reader = response.body.getReader();
                const decoder = new TextDecoder();
                let assistantText = '';

                while (true) {
                    const { value, done } = await reader.read();
                    if (done) break;

                    const chunk = decoder.decode(value);
                    const lines = chunk.split('\\n');
                    
                    for (const line of lines) {
                        if (line.startsWith('data: ')) {
                            const data = line.slice(6);
                            if (data === '[DONE]') continue;
                            
                            try {
                                const json = JSON.parse(data);
                                if (json.content) {
                                    assistantText += json.content;
                                    assistantDiv.textContent = assistantText;
                                    chatContainer.scrollTop = chatContainer.scrollHeight;
                                }
                            } catch (e) {}
                        }
                    }
                }

                messages.push({ role: 'assistant', content: assistantText });
            } catch (error) {
                console.error('Error:', error);
                assistantDiv.textContent = 'Error: ' + error.message;
            } finally {
                currentController = null;
            }
        }

        sendBtn.addEventListener('click', sendMessage);
        clearBtn.addEventListener('click', () => {
            messages = [];
            chatContainer.innerHTML = '';
        });

        userInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });

        modelSelect.addEventListener('change', () => {
            currentModelDisplay.textContent = modelSelect.options[modelSelect.selectedIndex].text;
        });

        codingToggle.addEventListener('change', () => {
            codingEnabled = codingToggle.checked;
            if (codingEnabled) reasoningEnabled = false;
        });
    </script>
</body>
</html>
"""
