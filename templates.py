INDEX_HTML = """
<!DOCTYPE html>
<html lang=\"ru\">
<head>
    <meta charset=\"UTF-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
    <title>LocalVisionChat</title>
    <style>
        :root {
            --bg-main: #050816;
            --bg-elevated: #0f172a;
            --bg-elevated-soft: #020617;
            --accent: #38bdf8;
            --accent-soft: rgba(56, 189, 248, 0.1);
            --accent-strong: rgba(56, 189, 248, 0.25);
            --accent-stronger: rgba(56, 189, 248, 0.9);
            --accent-secondary: #a855f7;
            --accent-secondary-soft: rgba(168, 85, 247, 0.25);
            --danger: #f97373;
            --danger-soft: rgba(248, 113, 113, 0.15);
            --text-main: #e2e8f0;
            --text-muted: #94a3b8;
            --text-soft: #64748b;
            --border-soft: rgba(148, 163, 184, 0.35);
            --border-strong: rgba(148, 163, 184, 0.6);
            --tag-bg: rgba(15, 23, 42, 0.95);
            --tag-border: rgba(148, 163, 184, 0.3);
            --radius-lg: 16px;
            --radius-md: 12px;
            --radius-sm: 999px;
            --shadow-soft: 0 18px 60px rgba(15, 23, 42, 0.85);
            --shadow-tag: 0 0 0 1px rgba(148, 163, 184, 0.12);
            --shadow-chip: 0 0 0 1px rgba(148, 163, 184, 0.2);
        }

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            padding: 0;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, \"Segoe UI\", sans-serif;
            background: radial-gradient(circle at top, #020617 0, #020617 40%, #000 100%);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            justify-content: center;
        }

        .page {
            display: flex;
            width: 100%;
            max-width: 1320px;
            padding: 24px 16px 32px;
            gap: 20px;
        }

        .sidebar {
            width: 280px;
            display: flex;
            flex-direction: column;
            gap: 14px;
        }

        .sidebar-card {
            background: radial-gradient(circle at top left, rgba(56, 189, 248, 0.09), rgba(15, 23, 42, 0.98));
            border-radius: var(--radius-lg);
            padding: 14px 14px 12px;
            border: 1px solid rgba(148, 163, 184, 0.4);
            box-shadow: var(--shadow-soft);
        }

        .sidebar-card.secondary {
            background: radial-gradient(circle at top left, rgba(168, 85, 247, 0.1), rgba(15, 23, 42, 0.98));
        }

        .sidebar-title {
            font-size: 13px;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: rgba(148, 163, 184, 0.85);
            margin-bottom: 2px;
        }

        .sidebar-main {
            font-size: 13px;
            color: var(--text-main);
            margin-bottom: 6px;
        }

        .sidebar-note {
            font-size: 12px;
            color: var(--text-muted);
            line-height: 1.45;
            margin-bottom: 8px;
        }

        .sidebar-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 11px;
            color: var(--text-soft);
        }

        .status-pill {
            display: inline-flex;
            align-items: center;
            gap: 5px;
            padding: 3px 8px;
            border-radius: 999px;
            background: rgba(34, 197, 94, 0.18);
            border: 1px solid rgba(34, 197, 94, 0.5);
            color: #bbf7d0;
            font-size: 11px;
        }

        .status-dot {
            width: 6px;
            height: 6px;
            border-radius: 999px;
            background: #22c55e;
            box-shadow: 0 0 0 4px rgba(34, 197, 94, 0.35);
        }

        .status-pill.warn {
            background: rgba(234, 179, 8, 0.16);
            border-color: rgba(234, 179, 8, 0.5);
            color: #facc15;
        }

        .status-dot.warn {
            background: #eab308;
            box-shadow: 0 0 0 4px rgba(234, 179, 8, 0.35);
        }

        .status-pill.bad {
            background: rgba(248, 113, 113, 0.16);
            border-color: rgba(248, 113, 113, 0.5);
            color: #fecaca;
        }

        .status-dot.bad {
            background: #f97373;
            box-shadow: 0 0 0 4px rgba(248, 113, 113, 0.35);
        }

        .status-pill.neutral {
            background: rgba(148, 163, 184, 0.16);
            border-color: rgba(148, 163, 184, 0.5);
            color: #e2e8f0;
        }

        .status-dot.neutral {
            background: #94a3b8;
            box-shadow: 0 0 0 4px rgba(148, 163, 184, 0.35);
        }

        .badge-row {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
        }

        .badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 4px 8px;
            border-radius: 999px;
            background: rgba(15, 23, 42, 0.85);
            border: 1px solid rgba(148, 163, 184, 0.36);
            color: var(--text-muted);
            font-size: 11px;
            box-shadow: var(--shadow-chip);
        }

        .badge-dot.small {
            width: 8px;
            height: 8px;
            border-radius: 999px;
        }

        .badge-dot.blue {
            background: #38bdf8;
        }

        .badge-dot.purple {
            background: #a855f7;
        }

        .badge-dot.orange {
            background: #fb923c;
        }

        .badge-dot.green {
            background: #22c55e;
        }

        .badge-dot.white {
            background: #e5e7eb;
        }

        .badge-label {
            text-transform: uppercase;
            letter-spacing: 0.14em;
            font-size: 10px;
            color: rgba(148, 163, 184, 0.9);
        }

        .badge-value {
            font-size: 11px;
        }

        .badge-metric {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 1px 7px;
            border-radius: 999px;
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid rgba(148, 163, 184, 0.4);
            font-size: 11px;
            color: #e2e8f0;
        }

        .badge-metric strong {
            font-weight: 600;
            color: #38bdf8;
        }

        .badge-metric span {
            color: var(--text-muted);
        }

        .main {
            flex: 1;
            min-width: 0;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 4px;
        }

        .title-block {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .title {
            font-size: 18px;
            font-weight: 600;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }

        .subtitle {
            font-size: 12px;
            color: var(--text-muted);
        }

        .pill-row {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
        }

        .pill {
            display: inline-flex;
            align-items: center;
            gap: 5px;
            padding: 4px 8px;
            border-radius: 999px;
            background: rgba(15, 23, 42, 0.95);
            border: 1px solid rgba(148, 163, 184, 0.45);
            font-size: 11px;
            color: var(--text-muted);
            box-shadow: var(--shadow-chip);
        }

        .pill-emoji {
            font-size: 14px;
        }

        .pill-label {
            text-transform: uppercase;
            letter-spacing: 0.13em;
            font-size: 10px;
            color: rgba(148, 163, 184, 0.9);
        }

        .pill-value {
            color: var(--text-main);
            font-weight: 500;
        }

        .layout {
            display: grid;
            grid-template-columns: minmax(0, 3.2fr) minmax(0, 2.1fr);
            gap: 18px;
        }

        .chat-card {
            background: radial-gradient(circle at top left, rgba(56, 189, 248, 0.12), rgba(15, 23, 42, 0.98));
            border-radius: var(--radius-lg);
            border: 1px solid rgba(148, 163, 184, 0.45);
            box-shadow: var(--shadow-soft);
            display: flex;
            flex-direction: column;
            height: calc(100vh - 128px);
            min-height: 420px;
        }

        .chat-header {
            padding: 10px 12px 8px;
            border-bottom: 1px solid rgba(148, 163, 184, 0.35);
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 8px;
        }

        .chat-title-block {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .chat-title {
            font-size: 13px;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: rgba(148, 163, 184, 0.9);
        }

        .chat-subtitle {
            font-size: 12px;
            color: var(--text-muted);
        }

        .chat-controls-row {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            align-items: center;
            justify-content: flex-end;
        }

        .toggle {
            position: relative;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 3px 9px;
            border-radius: 999px;
            background: rgba(15, 23, 42, 0.95);
            border: 1px solid rgba(148, 163, 184, 0.55);
            color: var(--text-muted);
            font-size: 11px;
            cursor: pointer;
            user-select: none;
            box-shadow: var(--shadow-chip);
        }

        .toggle input {
            display: none;
        }

        .toggle-knob {
            width: 18px;
            height: 18px;
            border-radius: 999px;
            background: radial-gradient(circle at 30% 25%, #38bdf8, #0ea5e9);
            box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.45);
        }

        .toggle-label-main {
            text-transform: uppercase;
            letter-spacing: 0.16em;
            font-size: 10px;
            color: rgba(148, 163, 184, 0.95);
        }

        .toggle-label-sub {
            font-size: 11px;
            color: #e2e8f0;
            font-weight: 500;
        }

        .toggle.disabled {
            opacity: 0.55;
            cursor: default;
        }

        .chip-row {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
        }

        .chip {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 3px 8px;
            border-radius: 999px;
            background: rgba(15, 23, 42, 0.95);
            border: 1px solid rgba(148, 163, 184, 0.4);
            font-size: 11px;
            color: var(--text-muted);
        }

        .chip-label {
            text-transform: uppercase;
            letter-spacing: 0.13em;
            font-size: 10px;
            color: rgba(148, 163, 184, 0.9);
        }

        .chip strong {
            color: #e2e8f0;
            font-weight: 500;
        }

        .chip-tag {
            padding: 1px 7px;
            border-radius: 999px;
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid rgba(148, 163, 184, 0.4);
            color: #e2e8f0;
            font-size: 10px;
        }

        .chip-tag.purple {
            border-color: rgba(168, 85, 247, 0.7);
            color: #e9d5ff;
        }

        .chip-tag.orange {
            border-color: rgba(249, 115, 22, 0.7);
            color: #fed7aa;
        }

        .chip-tag.green {
            border-color: rgba(34, 197, 94, 0.7);
            color: #bbf7d0;
        }

        .chat-body {
            flex: 1;
            display: flex;
            flex-direction: column;
            padding: 10px 10px 8px;
            gap: 8px;
            min-height: 0;
        }

        .conversation {
            flex: 1;
            background: rgba(15, 23, 42, 0.95);
            border-radius: 12px;
            border: 1px solid rgba(148, 163, 184, 0.45);
            padding: 10px 10px 8px;
            overflow-y: auto;
            font-size: 13px;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .message {
            max-width: 92%;
            padding: 8px 10px;
            border-radius: 12px;
            border: 1px solid rgba(148, 163, 184, 0.3);
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), #020617 120%);
            box-shadow: 0 12px 28px rgba(15, 23, 42, 0.75);
            position: relative;
        }

        .message.user {
            align-self: flex-end;
            border-color: rgba(56, 189, 248, 0.8);
            background: radial-gradient(circle at top left, rgba(56, 189, 248, 0.22), rgba(15, 23, 42, 0.98));
        }

        .message.assistant {
            align-self: flex-start;
        }

        .message-role {
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.14em;
            color: rgba(148, 163, 184, 0.9);
            margin-bottom: 3px;
        }

        .message-content {
            font-size: 13px;
            line-height: 1.5;
            color: #e2e8f0;
        }

        .message-meta {
            margin-top: 4px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 10px;
            color: rgba(148, 163, 184, 0.8);
        }

        .message-tags {
            display: flex;
            gap: 5px;
            flex-wrap: wrap;
        }

        .message-tag {
            padding: 1px 6px;
            border-radius: 999px;
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid rgba(148, 163, 184, 0.4);
        }

        .message-time {
            opacity: 0.9;
        }

        .skeleton {
            background: linear-gradient(90deg, rgba(148, 163, 184, 0.15), rgba(15, 23, 42, 0.75), rgba(148, 163, 184, 0.15));
            background-size: 200% 100%;
            animation: skeleton 1.6s infinite ease-in-out;
        }

        @keyframes skeleton {
            0% { background-position: -180% 0; }
            100% { background-position: 180% 0; }
        }

        .quick-row {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-top: 2px;
            margin-bottom: 1px;
        }

        .quick-chip {
            font-size: 11px;
            padding: 3px 7px;
            border-radius: 999px;
            border: 1px solid rgba(148, 163, 184, 0.4);
            background: rgba(15, 23, 42, 0.95);
            color: var(--text-muted);
            cursor: pointer;
        }

        .suggestions {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-top: 4px;
        }

        .suggestion {
            padding: 4px 8px;
            border-radius: 999px;
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid rgba(148, 163, 184, 0.5);
            font-size: 11px;
            color: var(--text-muted);
            cursor: pointer;
        }

        .suggestion-icon {
            font-size: 13px;
            margin-right: 4px;
        }

        .input-area {
            margin-top: 4px;
            padding: 8px 10px 8px;
            border-radius: 12px;
            background: rgba(15, 23, 42, 0.98);
            border: 1px solid rgba(148, 163, 184, 0.65);
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        .model-row {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            align-items: center;
        }

        .model-select {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 4px 8px;
            border-radius: 999px;
            background: rgba(15, 23, 42, 0.95);
            border: 1px solid rgba(148, 163, 184, 0.6);
            color: var(--text-main);
            font-size: 11px;
        }

        .model-select label {
            text-transform: uppercase;
            letter-spacing: 0.14em;
            font-size: 10px;
            color: rgba(148, 163, 184, 0.9);
        }

        .model-select select {
            background: transparent;
            border: none;
            color: var(--text-main);
            font-size: 11px;
            padding-right: 8px;
        }

        .model-select select:focus {
            outline: none;
        }

        .input-row {
            display: flex;
            gap: 8px;
            align-items: flex-end;
        }

        .textarea-wrapper {
            position: relative;
            flex: 1;
        }

        textarea {
            width: 100%;
            resize: none;
            min-height: 48px;
            max-height: 120px;
            padding: 9px 32px 9px 10px;
            border-radius: 10px;
            border: 1px solid rgba(148, 163, 184, 0.65);
            background: radial-gradient(circle at top left, rgba(56, 189, 248, 0.2), rgba(15, 23, 42, 0.98));
            color: var(--text-main);
            font-size: 13px;
            font-family: inherit;
        }

        textarea:focus {
            outline: none;
            border-color: #38bdf8;
            box-shadow: 0 0 0 1px rgba(56, 189, 248, 0.5);
        }

        .textarea-hint {
            position: absolute;
            right: 9px;
            bottom: 5px;
            font-size: 10px;
            color: rgba(148, 163, 184, 0.85);
        }

        .input-actions {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        .row-top {
            display: flex;
            gap: 6px;
        }

        .btn {
            border: 1px solid rgba(148, 163, 184, 0.7);
            background: rgba(15, 23, 42, 0.98);
            color: var(--text-main);
            border-radius: 999px;
            padding: 6px 12px;
            font-size: 11px;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            cursor: pointer;
            white-space: nowrap;
        }

        .btn-primary {
            border-color: rgba(56, 189, 248, 0.9);
            background: radial-gradient(circle at top left, #38bdf8, #0ea5e9);
            color: #0b1120;
            font-weight: 600;
            box-shadow: 0 12px 30px rgba(56, 189, 248, 0.45);
        }

        .btn-icon {
            font-size: 14px;
        }

        .btn-secondary {
            border-color: rgba(148, 163, 184, 0.8);
        }

        .btn-ghost {
            border-color: rgba(148, 163, 184, 0.5);
            background: transparent;
            color: var(--text-muted);
        }

        .input-flags {
            display: flex;
            flex-wrap: wrap;
            gap: 4px;
        }

        .flag {
            font-size: 10px;
            padding: 3px 7px;
            border-radius: 999px;
            border: 1px solid rgba(148, 163, 184, 0.45);
            background: rgba(15, 23, 42, 0.9);
            color: var(--text-muted);
        }

        .flag strong {
            color: #e2e8f0;
        }

        .side-card {
            background: radial-gradient(circle at top left, rgba(148, 163, 184, 0.12), rgba(15, 23, 42, 0.98));
            border-radius: var(--radius-lg);
            border: 1px solid rgba(148, 163, 184, 0.55);
            box-shadow: var(--shadow-soft);
            padding: 10px 10px 12px;
            height: calc(100vh - 128px);
            min-height: 420px;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .side-header {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
        }

        .side-title-block {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .side-title {
            font-size: 13px;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: rgba(148, 163, 184, 0.9);
        }

        .side-subtitle {
            font-size: 12px;
            color: var(--text-muted);
        }

        .side-controls {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            justify-content: flex-end;
        }

        .side-badge {
            padding: 2px 8px;
            border-radius: 999px;
            background: rgba(15, 23, 42, 0.95);
            border: 1px solid rgba(148, 163, 184, 0.6);
            font-size: 11px;
            color: var(--text-muted);
        }

        .side-content {
            flex: 1;
            background: rgba(15, 23, 42, 0.96);
            border-radius: 12px;
            border: 1px solid rgba(148, 163, 184, 0.5);
            padding: 9px 9px 10px;
            overflow-y: auto;
            font-size: 12px;
        }

        .side-section {
            margin-bottom: 10px;
        }

        .side-section-title {
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.14em;
            color: rgba(148, 163, 184, 0.9);
            margin-bottom: 4px;
        }

        .side-section-text {
            font-size: 12px;
            color: var(--text-muted);
            line-height: 1.5;
        }

        .side-section strong {
            color: #e5e7eb;
        }

        .side-list {
            padding-left: 16px;
            margin: 4px 0 2px;
            color: var(--text-muted);
        }

        .side-list li {
            margin-bottom: 2px;
        }

        .side-highlight {
            padding: 7px 8px;
            border-radius: 10px;
            background: rgba(15, 23, 42, 0.96);
            border: 1px dashed rgba(148, 163, 184, 0.7);
            font-size: 12px;
            color: #e5e7eb;
        }

        .side-highlight strong {
            color: #f97316;
        }

        .side-footnote {
            font-size: 11px;
            color: var(--text-soft);
            margin-top: 4px;
        }

        .tag-cloud {
            display: flex;
            flex-wrap: wrap;
            gap: 7px;
        }

        .tag {
            padding: 4px 8px;
            border-radius: 999px;
            border: 1px solid var(--tag-border);
            background: var(--tag-bg);
            color: var(--text-muted);
            font-size: 11px;
            box-shadow: var(--shadow-tag);
        }

        .tag strong {
            color: #e5e7eb;
        }

        .link {
            color: #38bdf8;
            text-decoration: none;
        }

        .link:hover {
            text-decoration: underline;
        }

        .footer-note {
            font-size: 11px;
            color: var(--text-soft);
            margin-top: 3px;
        }

        @media (max-width: 1024px) {
            .page {
                flex-direction: column;
            }

            .sidebar {
                width: 100%;
                flex-direction: row;
                flex-wrap: wrap;
            }

            .sidebar-card {
                flex: 1;
                min-width: 260px;
            }

            .layout {
                grid-template-columns: minmax(0, 1fr);
            }

            .chat-card,
            .side-card {
                height: auto;
                min-height: 380px;
            }
        }

        @media (max-width: 768px) {
            .page {
                padding: 14px 8px 24px;
            }

            .chat-card,
            .side-card {
                min-height: 360px;
            }

            .chat-header,
            .side-header {
                flex-direction: column;
                align-items: flex-start;
                gap: 6px;
            }

            .chat-controls-row,
            .side-controls {
                width: 100%;
                justify-content: flex-start;
            }

            .conversation {
                min-height: 180px;
            }
        }
    </style>
</head>
<body>
    <div class=\"page\">
        <div class=\"sidebar\">
            <div class=\"sidebar-card\">
                <div class=\"sidebar-title\">Статус аккаунта</div>
                <div class=\"sidebar-main\">Аккаунт активен</div>
                <div class=\"sidebar-note\">
                    Лимиты и очередь зависят от конкретной модели и нагрузки на OpenRouter. Если вдруг модель не отвечает, переключитесь на другую из списка.
                </div>
                <div class=\"sidebar-footer\">
                    <div class=\"status-pill\">
                        <span class=\"status-dot\"></span>
                        <span>Все системы в норме</span>
                    </div>
                    <span>Обновлено: 11.12.2025</span>
                </div>
            </div>

            <div class=\"sidebar-card secondary\">
                <div class=\"sidebar-title\">Режимы</div>
                <div class=\"sidebar-main\">Выберите модель или режим Авто.</div>
                <div class=\"sidebar-note\">
                    
                    
                    
                    
                    
                </div>
                <div class=\"badge-row\">
                    <div class=\"badge\">
                        <span class=\"badge-dot small blue\"></span>
                        <span class=\"badge-label\">Авто</span>
                        <span class=\"badge-value\">Самый быстрый из списка</span>
                    </div>
                    <div class=\"badge\">
                        <span class=\"badge-dot small purple\"></span>
                        <span class=\"badge-label\">Код</span>
                        <span class=\"badge-value\">Оптимизированный кодер через OpenRouter</span>
                    </div>
                    <div class=\"badge\">
                        <span class=\"badge-dot small orange\"></span>
                        <span class=\"badge-label\">Reasoning</span>
                        <span class=\"badge-value\">Логика и длинные цепочки</span>
                    </div>
                </div>
            </div>

            <div class=\"sidebar-card\">
                <div class=\"sidebar-title\">Подсказка</div>
                <div class=\"sidebar-main\">Модель для режима кодинга.</div>
                <div class=\"sidebar-note\">
                    В конфиге можно поменять модель для кода (по умолчанию: kwaipilot/kat-coder-pro:free). Для обычных задач используйте режим Авто или конкретную PRO-модель.
                </div>
                <div class=\"badge-row\">
                    <div class=\"badge-metric\">
                        <strong>KAT</strong><span>Coder-Pro</span>
                    </div>
                    <div class=\"badge-metric\">
                        <strong>Context</strong><span>32K+</span>
                    </div>
                </div>
            </div>

            <div class=\"sidebar-card\">
                <div class=\"sidebar-title\">SQL для Supabase</div>
                <div class=\"sidebar-main\">Если вы видите ошибку при выдаче PRO или смене пароля, значит старый SQL код был слишком строгим. Выполните этот НОВЫЙ КОД в Supabase SQL Editor:</div>
                <div class=\"sidebar-note\" style=\"font-size: 11px; line-height: 1.5;\">
                    
                    
                    
                    
                    
                    
                    
                </div>
                <div class=\"footer-note\">
                    После выполнения обновите страницу. Если ошибка не исчезнет — проверьте переменные окружения.
                </div>
            </div>
        </div>

        <div class=\"main\">
            <div class=\"header\">
                <div class=\"title-block\">
                    <div class=\"title\">LocalVisionChat</div>
                    <div class=\"subtitle\">Локальный интерфейс для OpenRouter с мульти-модельной поддержкой и аналитикой рынка LLM.</div>
                </div>
                <div class=\"pill-row\">
                    <div class=\"pill\">
                        <span class=\"pill-emoji\">⚙️</span>
                        <span class=\"pill-label\">Back-end</span>
                        <span class=\"pill-value\">FastAPI + SSE streaming</span>
                    </div>
                    <div class=\"pill\">
                        <span class=\"pill-emoji\">📊</span>
                        <span class=\"pill-label\">Analytics</span>
                        <span class=\"pill-value\">/analytics с Open LLM Leaderboard</span>
                    </div>
                </div>
            </div>

            <div class=\"layout\">
                <div class=\"chat-card\">
                    <div class=\"chat-header\">
                        <div class=\"chat-title-block\">
                            <div class=\"chat-title\">Сессия чата</div>
                            <div class=\"chat-subtitle\">Диалог с выбранной моделью. Поддерживается контекст беседы и stream-вывод.</div>
                        </div>
                        <div class=\"chat-controls-row\">
                            <label class=\"toggle\">
                                <input type=\"checkbox\" id=\"webSearchToggle\" />
                                <div class=\"toggle-knob\"></div>
                                <div>
                                    <div class=\"toggle-label-main\">Web Search</div>
                                    <div class=\"toggle-label-sub\">DuckDuckGo + краткое саммари</div>
                                </div>
                            </label>
                            <div class=\"chip-row\">
                                <div class=\"chip\">
                                    <span class=\"chip-label\">Состояние</span>
                                    <span><strong id=\"streamState\">Готов к запросу</strong></span>
                                </div>
                                <div class=\"chip\">
                                    <span class=\"chip-label\">Источники</span>
                                    <span class=\"chip-tag\">OpenRouter</span>
                                    <span class=\"chip-tag purple\">DuckDuckGo</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class=\"chat-body\">
                        <div id=\"conversation\" class=\"conversation\">
                            <div class=\"message assistant\">
                                <div class=\"message-role\">Assistant</div>
                                <div class=\"message-content\">
                                    Привет! Я — ваш локальный интерфейс к OpenRouter. Задайте вопрос, включите Web Search при необходимости — и получите стриминговый ответ выбранной модели.
                                </div>
                                <div class=\"message-meta\">
                                    <div class=\"message-tags\">
                                        <span class=\"message-tag\">Mode: Auto</span>
                                        <span class=\"message-tag\">Backend: OpenRouter</span>
                                    </div>
                                    <div class=\"message-time\">Сессия инициализирована</div>
                                </div>
                            </div>
                        </div>

                        <div class=\"input-area\">
                            <div class=\"model-row\">
                                <div class=\"model-select\">
                                    <label for=\"modelSelect\">Модель</label>
                                    <select id=\"modelSelect\">
                                        <option value=\"auto\">AUTO — выбрать лучшую бесплатную</option>
                                        <option value=\"mistralai/devstral-2512:free\">Mistral DevStral 2512 (free)</option>
                                        <option value=\"amazon/nova-2-lite-v1:free\">Amazon Nova 2 Lite (free)</option>
                                        <option value=\"google/gemini-2.0-flash-exp:free\">Gemini 2.0 Flash (exp, free)</option>
                                        <option value=\"nvidia/nemotron-nano-12b-v2-vl:free\">NVIDIA Nemotron Nano 12B VL (free)</option>
                                        <option value=\"deepseek/deepseek-chat-v3.1\">DeepSeek Chat V3.1</option>
                                    </select>
                                </div>

                                <div class=\"model-select\">
                                    <label for=\"codingModel\">Coding</label>
                                    <select id=\"codingModel\">
                                        <option value=\"kwaipilot/kat-coder-pro:free\">KAT-Coder-Pro (free)</option>
                                    </select>
                                </div>

                                <label class=\"toggle\" id=\"codingToggleLabel\">
                                    <input type=\"checkbox\" id=\"codingToggle\" />
                                    <div class=\"toggle-knob\"></div>
                                    <div>
                                        <div class=\"toggle-label-main\">Coding Mode</div>
                                        <div class=\"toggle-label-sub\">Оптимизация под код</div>
                                    </div>
                                </label>
                            </div>

                            <div class=\"input-row\">
                                <div class=\"textarea-wrapper\">
                                    <textarea id=\"userInput\" placeholder=\"Задайте вопрос или вставьте текст для анализа...\"></textarea>
                                    <div class=\"textarea-hint\">Shift+Enter — новая строка</div>
                                </div>
                                <div class=\"input-actions\">
                                    <div class=\"row-top\">
                                        <button id=\"sendBtn\" class=\"btn btn-primary\">
                                            <span class=\"btn-icon\">▶</span>
                                            <span>Отправить</span>
                                        </button>
                                        <button id=\"stopBtn\" class=\"btn btn-secondary\" disabled>
                                            <span class=\"btn-icon\">■</span>
                                            <span>Стоп</span>
                                        </button>
                                    </div>
                                    <div class=\"input-flags\">
                                        <div class=\"flag\">Web: <strong id=\"flagWeb\">Off</strong></div>
                                        <div class=\"flag\">Mode: <strong id=\"flagMode\">Chat</strong></div>
                                        <div class=\"flag\">Model: <strong id=\"flagModel\">AUTO</strong></div>
                                    </div>
                                </div>
                            </div>

                            <div class=\"quick-row\">
                                <div class=\"quick-chip\" onclick=\"insertQuick('Сделай краткое резюме статьи по ссылке и выдели ключевые тезисы.')\">Резюме статьи</div>
                                <div class=\"quick-chip\" onclick=\"insertQuick('Напиши функцию на Python, которая парсит JSON и валидирует поля.')\">Функция на Python</div>
                                <div class=\"quick-chip\" onclick=\"insertQuick('Подготовь список идей для небольшого pet-проекта с LLM для резюме.')\">Идеи для pet-проектов</div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class=\"side-card\">
                    <div class=\"side-header\">
                        <div class=\"side-title-block\">
                            <div class=\"side-title\">Подсказки и аналитика</div>
                            <div class=\"side-subtitle\">Лучшие практики работы с LLM в этом интерфейсе.</div>
                        </div>
                        <div class=\"side-controls\">
                            <div class=\"side-badge\">Обновлено: 11.12.2025</div>
                            <a href=\"/analytics\" target=\"_blank\" class=\"side-badge\">Открыть /analytics</a>
                        </div>
                    </div>

                    <div class=\"side-content\">
                        <div class=\"side-section\">
                            <div class=\"side-section-title\">Рекомендации по моделям</div>
                            <div class=\"side-section-text\">
                                <ul class=\"side-list\">
                                    <li><strong>Авто‑режим</strong> использует первую модель из списка <code>FALLBACK_MODELS</code>. По умолчанию это Mistral DevStral 2512.</li>
                                    <li><strong>Код</strong>: для тяжёлых задач по коду включите Coding Mode — запрос пойдёт через KAT-Coder-Pro.</li>
                                    <li><strong>DeepSeek V3.1</strong> хорошо подходит для длинных рассуждений и задач с пошаговой логикой.</li>
                                </ul>
                            </div>
                        </div>

                        <div class=\"side-section\">
                            <div class=\"side-section-title\">Как работает Web Search</div>
                            <div class=\"side-section-text\">
                                При включённом флаге <strong>Web Search</strong> последний запрос пользователя отправляется в DuckDuckGo, берутся топ‑5 результатов, форматируются в виде кратких сниппетов и добавляются в системное сообщение контекста:
                            </div>
                            <div class=\"side-highlight\">
                                <strong>System:</strong> Web search context: ... (далее идут результаты с заголовками, ссылками и краткими фрагментами).
                            </div>
                            <div class=\"side-section-text\">
                                Это позволяет модели использовать свежую информацию, не полагаясь только на свои внутренние данные.
                            </div>
                        </div>

                        <div class=\"side-section\">
                            <div class=\"side-section-title\">Генерация изображений</div>
                            <div class=\"side-section-text\">
                                Для генерации картинок предусмотрен отдельный эндпоинт <code>/generate_image</code> с HTML‑обёрткой. Пример использования:
                            </div>
                            <div class=\"side-highlight\">
                                Откройте в браузере <code>/generate_image?prompt=\"кот в стиле киберпанк\"</code> — будет сгенерировано изображение через Pollinations (модель Flux, 1024x1024).
                            </div>
                            <div class=\"side-section-text\">
                                Триггеры вроде <em>\"нарисуй\"</em>, <em>\"сгенерируй\"</em>, <em>\"/img\"</em> будут автоматически вычищены из prompt, чтобы не портить качество.
                            </div>
                        </div>

                        <div class=\"side-section\">
                            <div class=\"side-section-title\">Аналитика рынка LLM</div>
                            <div class=\"side-section-text\">
                                На странице <a href=\"/analytics\" class=\"link\" target=\"_blank\">/analytics</a> отображается дашборд:
                            </div>
                            <ul class=\"side-list\">
                                <li>Топ‑10 моделей по данным Open LLM Leaderboard.</li>
                                <li>Ежедневное саммари по изменениям позиций.</li>
                                <li>Краткая лента новостей по ключевым моделям.</li>
                            </ul>
                            <div class=\"side-section-text\">
                                Обновление происходит раз в сутки около 3:00 МСК (для теста в коде можно временно поставить 1–2 минуты).
                            </div>
                        </div>

                        <div class=\"side-section\">
                            <div class=\"side-section-title\">Переменные окружения</div>
                            <div class=\"side-section-text\">
                                В проде рекомендуется вынести <code>API_KEY</code> и прочие чувствительные параметры в переменные окружения или .env файл. Сейчас ключ прописан напрямую в <code>config.py</code> для упрощения локального запуска.
                            </div>
                        </div>

                        <div class=\"side-section\">
                            <div class=\"side-section-title\">Теги возможностей</div>
                            <div class=\"tag-cloud\">
                                <div class=\"tag\"><strong>LLM Router</strong> · OpenRouter API</div>
                                <div class=\"tag\"><strong>Streaming</strong> · text/event-stream</div>
                                <div class=\"tag\"><strong>DuckDuckGo</strong> · web search</div>
                                <div class=\"tag\"><strong>Pollinations</strong> · Flux images</div>
                                <div class=\"tag\"><strong>FastAPI</strong> · async backend</div>
                                <div class=\"tag\"><strong>Analytics</strong> · Open LLM Leaderboard</div>
                                <div class=\"tag\"><strong>Coding</strong> · KAT-Coder-Pro</div>
                            </div>
                        </div>

                        <div class=\"side-section\">
                            <div class=\"side-section-title\">Важно</div>
                            <div class=\"side-highlight\">
                                Если что-то не работает (PRO‑выдача, смена пароля, SQL в Supabase) — сначала проверьте актуальность SQL‑скрипта и переменных окружения. Затем перезапустите приложение.
                            </div>
                            <div class=\"side-footnote\">
                                Этот интерфейс сделан как лёгкий локальный клиент, его можно доработать под свои задачи: добавить историю чатов, пользователей, лимиты, billing и т.д.
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        const conversationEl = document.getElementById('conversation');
        const userInputEl = document.getElementById('userInput');
        const sendBtn = document.getElementById('sendBtn');
        const stopBtn = document.getElementById('stopBtn');
        const webSearchToggle = document.getElementById('webSearchToggle');
        const codingToggle = document.getElementById('codingToggle');
        const codingToggleLabel = document.getElementById('codingToggleLabel');
        const modelSelect = document.getElementById('modelSelect');
        const codingModelSelect = document.getElementById('codingModel');
        const streamStateEl = document.getElementById('streamState');
        const flagWebEl = document.getElementById('flagWeb');
        const flagModeEl = document.getElementById('flagMode');
        const flagModelEl = document.getElementById('flagModel');

        let currentController = null;
        let messages = [{ role: 'assistant', content: 'Привет! Я — ваш локальный интерфейс к OpenRouter. Задайте вопрос, включите Web Search при необходимости — и получите стриминговый ответ выбранной модели.' }];

        function appendMessage(role, content, meta = {}) {
            const container = document.createElement('div');
            container.className = 'message ' + role;

            const roleEl = document.createElement('div');
            roleEl.className = 'message-role';
            roleEl.textContent = role === 'user' ? 'User' : 'Assistant';

            const contentEl = document.createElement('div');
            contentEl.className = 'message-content';
            contentEl.textContent = content;

            const metaEl = document.createElement('div');
            metaEl.className = 'message-meta';

            const tagsEl = document.createElement('div');
            tagsEl.className = 'message-tags';

            if (meta.model) {
                const tag = document.createElement('span');
                tag.className = 'message-tag';
                tag.textContent = 'Model: ' + meta.model;
                tagsEl.appendChild(tag);
            }

            if (meta.web_search) {
                const tag = document.createElement('span');
                tag.className = 'message-tag';
                tag.textContent = 'Web Search: ON';
                tagsEl.appendChild(tag);
            }

            const timeEl = document.createElement('div');
            timeEl.className = 'message-time';
            timeEl.textContent = meta.time || 'Только что';

            metaEl.appendChild(tagsEl);
            metaEl.appendChild(timeEl);

            container.appendChild(roleEl);
            container.appendChild(contentEl);
            container.appendChild(metaEl);

            conversationEl.appendChild(container);
            conversationEl.scrollTop = conversationEl.scrollHeight;

            return contentEl;
        }

        function setStreamingState(isStreaming) {
            if (isStreaming) {
                streamStateEl.textContent = 'Идёт генерация ответа...';
                sendBtn.disabled = true;
                stopBtn.disabled = false;
            } else {
                streamStateEl.textContent = 'Готов к запросу';
                sendBtn.disabled = false;
                stopBtn.disabled = true;
            }
        }

        async function sendMessage() {
            const text = userInputEl.value.trim();
            if (!text || currentController) return;

            const useWebSearch = webSearchToggle.checked;
            const useCoding = codingToggle.checked;
            const model = modelSelect.value;
            const codingModel = codingModelSelect.value;

            messages.push({ role: 'user', content: text });
            appendMessage('user', text, { time: 'Сейчас' });

            userInputEl.value = '';

            flagWebEl.textContent = useWebSearch ? 'On' : 'Off';
            flagModeEl.textContent = useCoding ? 'Coding' : 'Chat';
            flagModelEl.textContent = model === 'auto' ? 'AUTO' : model;

            const assistantContentEl = appendMessage('assistant', '', {
                model: useCoding ? codingModel : model,
                web_search: useWebSearch,
                time: 'Streaming...',
            });

            currentController = new AbortController();
            setStreamingState(true);

            try {
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        messages,
                        web_search: useWebSearch,
                        model,
                        coding_mode: useCoding,
                        coding_model: codingModel,
                    }),
                    signal: currentController.signal,
                });

                if (!response.ok) {
                    throw new Error('HTTP error: ' + response.status);
                }

                const reader = response.body.getReader();
                const decoder = new TextDecoder('utf-8');
                let assistantText = '';

                while (true) {
                    const { value, done } = await reader.read();
                    if (done) break;

                    const chunk = decoder.decode(value, { stream: true });
                    const lines = chunk.split('\n');
                    for (const line of lines) {
                        if (line.startsWith('data: ')) {
                            const dataStr = line.slice(6).trim();
                            if (!dataStr || dataStr === '[DONE]') continue;
                            try {
                                const data = JSON.parse(dataStr);
                                if (data.content) {
                                    assistantText += data.content;
                                    assistantContentEl.textContent = assistantText;
                                    conversationEl.scrollTop = conversationEl.scrollHeight;
                                }
                            } catch (e) {
                                console.error('Ошибка парсинга чанка', e);
                            }
                        }
                    }
                }

                messages.push({ role: 'assistant', content: assistantText });
            } catch (e) {
                if (e.name === 'AbortError') {
                    assistantContentEl.textContent += '\n\n[Поток остановлен пользователем]';
                } else {
                    console.error(e);
                    assistantContentEl.textContent = '[Ошибка]: ' + e.message;
                }
            } finally {
                currentController = null;
                setStreamingState(false);
            }
        }

        function stopStreaming() {
            if (currentController) {
                currentController.abort();
            }
        }

        sendBtn.addEventListener('click', sendMessage);
        stopBtn.addEventListener('click', stopStreaming);

        userInputEl.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });

        function insertQuick(text) {
            userInputEl.value = text;
            userInputEl.focus();
        }

        window.insertQuick = insertQuick;
    </script>
</body>
</html>
"""