import yt_dlp as youtube_dl
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QProgressBar,
                             QFileDialog, QComboBox, QTextEdit, QHBoxLayout, QWidget, QCheckBox, QTabWidget,
                             QFormLayout, QSpinBox, QSlider, QMessageBox)
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QIcon
import re
from qt_material import apply_stylesheet  # Importando o qt-material para temas modernos
from datetime import datetime  # Para logs detalhados com data/hora

# Traduções completas para todas as línguas
TRANSLATIONS = {
    "en": {
        "url_label": "Video URL:",
        "preview_button": "Preview Video",
        "folder_label": "Save Folder:",
        "choose_folder": "Choose Folder",
        "format_label": "Output Format:",
        "resolution_label": "Video Resolution (144p to 4K):",
        "start_button": "Start Download",
        "dark_mode": "Dark Mode",
        "language_label": "Language:",
        "status_ready": "Status: Ready",
        "error_fill_fields": "Please fill all fields.",
        "error_url": "Please enter a URL for preview.",
        "error_no_thumbnail": "No thumbnail found for this video.",
        "language_changed": "Language changed to {language} ({code})",
        "main_tab": "Main",
        "advanced_settings": "Advanced Settings",
        "max_threads": "Maximum Threads",
        "bandwidth_limit": "Bandwidth Limit",
        "proxy_optional": "Proxy (Optional)",
        "auto_update": "Auto Update",
        "footer_text": "Programmed by Solarion"
    },
    "pt": {
        "url_label": "URL do Vídeo:",
        "preview_button": "Pré-visualizar Vídeo",
        "folder_label": "Pasta para Salvar:",
        "choose_folder": "Escolher Pasta",
        "format_label": "Formato de Saída:",
        "resolution_label": "Resolução de Vídeo (144p a 4K):",
        "start_button": "Iniciar Download",
        "dark_mode": "Modo Escuro",
        "language_label": "Idioma:",
        "status_ready": "Status: Pronto",
        "error_fill_fields": "Por favor, preencha todos os campos.",
        "error_url": "Por favor, insira uma URL para pré-visualizar.",
        "error_no_thumbnail": "Nenhuma miniatura encontrada para este vídeo.",
        "language_changed": "Idioma alterado para {language} ({code})",
	"main_tab": "Principal",
        "advanced_settings": "Configurações Avançadas",
        "max_threads": "Máximo de Threads",
        "bandwidth_limit": "Limite de Banda",
        "proxy_optional": "Proxy (Opcional)",
        "auto_update": "Atualização Automática",
        "footer_text": "Programado por Solarion"
    },
    "es": {
        "url_label": "URL del Video:",
        "preview_button": "Vista Previa del Video",
        "folder_label": "Carpeta para Guardar:",
        "choose_folder": "Elegir Carpeta",
        "format_label": "Formato de Salida:",
        "resolution_label": "Resolución de Video (144p a 4K):",
        "start_button": "Iniciar Descarga",
        "dark_mode": "Modo Oscuro",
        "language_label": "Idioma:",
        "status_ready": "Estado: Listo",
        "error_fill_fields": "Por favor, complete todos los campos.",
        "error_url": "Por favor, ingrese una URL para la vista previa.",
        "error_no_thumbnail": "No se encontró miniatura para este video.",
        "language_changed": "Idioma cambiado a {language} ({code})",
	"main_tab": "Principal",
        "advanced_settings": "Configuración Avanzada",
        "max_threads": "Máximo de Hilos",
        "bandwidth_limit": "Límite de Ancho de Banda",
        "proxy_optional": "Proxy (Opcional)",
        "auto_update": "Actualización Automática",
        "footer_text": "Programado por Solarion© 2025"
    },
    "ru": {
        "url_label": "Ссылка на видео:",
        "preview_button": "Предпросмотр видео",
        "folder_label": "Папка для сохранения:",
        "choose_folder": "Выбрать папку",
        "format_label": "Формат вывода:",
        "resolution_label": "Разрешение видео (144p до 4K):",
        "start_button": "Начать загрузку",
        "dark_mode": "Тёмный режим",
        "language_label": "Язык:",
        "status_ready": "Статус: Готово",
        "error_fill_fields": "Пожалуйста, заполните все поля.",
        "error_url": "Введите URL для предпросмотра.",
        "error_no_thumbnail": "Миниатюра для этого видео не найдена.",
        "language_changed": "Язык изменен на {language} ({code})",
	"main_tab": "Основное",
        "advanced_settings": "Расширенные настройки",
        "max_threads": "Максимум потоков",
        "bandwidth_limit": "Ограничение пропускной способности",
        "proxy_optional": "Прокси (необязательно)",
        "auto_update": "Автообновление",
        "footer_text": "Разработано Solarion© 2025"
    },
    "zh": {
        "url_label": "视频网址：",
        "preview_button": "视频预览",
        "folder_label": "保存文件夹：",
        "choose_folder": "选择文件夹",
        "format_label": "输出格式：",
        "resolution_label": "视频分辨率 (144p 至 4K)：",
        "start_button": "开始下载",
        "dark_mode": "深色模式",
        "language_label": "语言：",
        "status_ready": "状态：准备就绪",
        "error_fill_fields": "请填写所有字段。",
        "error_url": "请输入一个 URL 以进行预览。",
        "error_no_thumbnail": "未找到此视频的缩略图。",
        "language_changed": "语言已更改为 {language} ({code})",
	"main_tab": "主选项卡",
        "advanced_settings": "高级设置",
        "max_threads": "最大线程数",
        "bandwidth_limit": "带宽限制",
        "proxy_optional": "代理（可选）",
        "auto_update": "自动更新",
        "footer_text": "由 Solarion 编程© 2025"
    },
    "ja": {
        "url_label": "ビデオのURL：",
        "preview_button": "ビデオプレビュー",
        "folder_label": "保存フォルダ：",
        "choose_folder": "フォルダを選択",
        "format_label": "出力形式：",
        "resolution_label": "ビデオ解像度 (144p ～ 4K)：",
        "start_button": "ダウンロードを開始",
        "dark_mode": "ダークモード",
        "language_label": "言語：",
        "status_ready": "ステータス：準備完了",
        "error_fill_fields": "すべてのフィールドに記入してください。",
        "error_url": "プレビュー用のURLを入力してください。",
        "error_no_thumbnail": "このビデオのサムネイルが見つかりませんでした。",
        "language_changed": "言語が {language} ({code}) に変更されました",
	"main_tab": "メイン",
        "advanced_settings": "高度な設定",
        "max_threads": "最大スレッド数",
        "bandwidth_limit": "帯域幅制限",
        "proxy_optional": "プロキシ（任意）",
        "auto_update": "自動更新",
        "footer_text": "ソラリオンによるプログラム© 2025"
    },
    "fr": {
        "url_label": "URL de la Vidéo :",
        "preview_button": "Aperçu de la Vidéo",
        "folder_label": "Dossier de Sauvegarde :",
        "choose_folder": "Choisir le Dossier",
        "format_label": "Format de Sortie :",
        "resolution_label": "Résolution Vidéo (144p à 4K) :",
        "start_button": "Démarrer le Téléchargement",
        "dark_mode": "Mode Sombre",
        "language_label": "Langue :",
        "status_ready": "Statut : Prêt",
        "error_fill_fields": "Veuillez remplir tous les champs.",
        "error_url": "Veuillez entrer une URL pour l'aperçu.",
        "error_no_thumbnail": "Aucune miniature trouvée pour cette vidéo.",
        "language_changed": "Langue changée en {language} ({code})",
	"main_tab": "Principal",
        "advanced_settings": "Paramètres avancés",
        "max_threads": "Nombre maximum de threads",
        "bandwidth_limit": "Limite de bande passante",
        "proxy_optional": "Proxy (Optionnel)",
        "auto_update": "Mise à jour automatique",
        "footer_text": "Programmé par Solarion© 2025"
    },
    "it": {
        "url_label": "URL del Video:",
        "preview_button": "Anteprima Video",
        "folder_label": "Cartella di Salvataggio:",
        "choose_folder": "Scegli Cartella",
        "format_label": "Formato di Uscita:",
        "resolution_label": "Risoluzione Video (144p a 4K):",
        "start_button": "Avvia Download",
        "dark_mode": "Modalità Scura",
        "language_label": "Lingua:",
        "status_ready": "Stato: Pronto",
        "error_fill_fields": "Si prega di compilare tutti i campi.",
        "error_url": "Si prega di inserire un URL per l'anteprima.",
        "error_no_thumbnail": "Nessuna miniatura trovata per questo video.",
        "language_changed": "Lingua cambiata in {language} ({code})",
	"main_tab": "Principale",
        "advanced_settings": "Impostazioni Avanzate",
        "max_threads": "Massimo Thread",
        "bandwidth_limit": "Limite di Banda",
        "proxy_optional": "Proxy (Opzionale)",
        "auto_update": "Aggiornamento Automatico",
        "footer_text": "Programmato da Solarion© 2025"
    },
    "de": {
        "url_label": "Video-URL:",
        "preview_button": "Video Vorschau",
        "folder_label": "Speicherordner:",
        "choose_folder": "Ordner Wählen",
        "format_label": "Ausgabeformat:",
        "resolution_label": "Videoauflösung (144p bis 4K):",
        "start_button": "Download Starten",
        "dark_mode": "Dunkelmodus",
        "language_label": "Sprache:",
        "status_ready": "Status: Bereit",
        "error_fill_fields": "Bitte füllen Sie alle Felder aus.",
        "error_url": "Bitte geben Sie eine URL für die Vorschau ein.",
        "error_no_thumbnail": "Kein Miniaturbild für dieses Video gefunden.",
        "language_changed": "Sprache geändert zu {language} ({code})",
	"main_tab": "Haupt",
        "advanced_settings": "Erweiterte Einstellungen",
        "max_threads": "Maximale Threads",
        "bandwidth_limit": "Bandbreitenbegrenzung",
        "proxy_optional": "Proxy (Optional)",
        "auto_update": "Automatisches Update",
        "footer_text": "Programmiert von Solarion© 2025"
    },
    "ko": {
        "url_label": "비디오 URL:",
        "preview_button": "비디오 미리보기",
        "folder_label": "저장 폴더:",
        "choose_folder": "폴더 선택",
        "format_label": "출력 형식:",
        "resolution_label": "비디오 해상도 (144p ~ 4K):",
        "start_button": "다운로드 시작",
        "dark_mode": "다크 모드",
        "language_label": "언어:",
        "status_ready": "상태: 준비 완료",
        "error_fill_fields": "모든 필드를 작성해 주세요.",
        "error_url": "미리보기를 위한 URL을 입력해 주세요.",
        "error_no_thumbnail": "이 비디오에 대한 썸네일을 찾을 수 없습니다.",
        "language_changed": "언어가 {language} ({code})로 변경되었습니다",
	"main_tab": "메인",
        "advanced_settings": "고급 설정",
        "max_threads": "최대 스레드 수",
        "bandwidth_limit": "대역폭 제한",
        "proxy_optional": "프록시 (선택 사항)",
        "auto_update": "자동 업데이트",
        "footer_text": "솔라리온에서 프로그래밍함© 2025"
    
    }
}

# Função para validar URLs das plataformas suportadas
def is_supported_url(url):
    supported_domains = [
        "youtube.com", "youtu.be",  # YouTube
        "instagram.com",  # Instagram
        "tiktok.com",  # TikTok
        "facebook.com",  # Facebook
        "twitch.tv",  # Twitch
        "twitter.com",  # Twitter
        "pinterest.com",  # Pinterest
    ]
    return any(domain in url for domain in supported_domains)

class DownloadThread(QThread):
    progress = pyqtSignal(int)
    status = pyqtSignal(str)

    def __init__(self, url, path, formato, quality_option):
        super().__init__()
        self.url = url
        self.path = path
        self.formato = formato
        self.quality_option = quality_option

    def run(self):  # Certifique-se de que 'self' está presente aqui
        ydl_opts = {
            'outtmpl': f'{self.path}/%(title)s.%(ext)s',
            'progress_hooks': [self.hook],
            'prefer_ffmpeg': True,  # Força o uso do FFmpeg
            'verbose': True,  # Habilita logs detalhados
        }

        # Configurações específicas para formatos de áudio
        if self.formato in ['mp3', 'wav']:
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': self.formato,
                    'preferredquality': self.quality_option,
                }],
            })

        # Configurações específicas para AVI, MOV, FLV
        elif self.formato in ['avi', 'mov', 'flv']:
            ydl_opts.update({
                'format': f'bestvideo[height={self.quality_option}]+bestaudio/best[height={self.quality_option}]',
                'merge_output_format': self.formato,
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': self.formato,
                }],
                'postprocessor_args': {
                    'ffmpeg': [
                        '-c:v', 'libx264',  # Força o codec de vídeo H.264
                        '-c:a', 'aac',      # Força o codec de áudio AAC
                    ],
                },
            })

        # Configurações padrão para outros formatos de vídeo
        else:
            ydl_opts.update({
                'format': f'bestvideo[height={self.quality_option}]+bestaudio/best[height={self.quality_option}]',
                'merge_output_format': self.formato,
            })

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])
            self.status.emit("Download completed!")
        except Exception as e:
            self.status.emit(f"Error: {e}")

    def hook(self, d):
        if d['status'] == 'downloading':
            try:
                percent = float(d.get('downloaded_bytes', 0)) / float(d.get('total_bytes', 1)) * 100
                self.progress.emit(int(percent))
            except Exception:
                self.progress.emit(0)
        elif d['status'] == 'finished':
            self.status.emit(f"Completed: {d['filename']}")

class DownloaderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.languages = {
            "Português (Brasil)": "pt",
            "English": "en",
            "Español": "es",
            "Русский": "ru",
            "中文": "zh",
            "日本語": "ja",
            "Français": "fr",
            "Italiano": "it",
            "Deutsch": "de",
            "한국어": "ko"
        }
        self.current_language = "pt"
        self.init_ui()

    def init_ui(self):
	self.setWindowTitle("Downloader e Converter by Solarion")
	self.setWindowIcon(QIcon("icone.ico"))
        self.setGeometry(100, 100, 900, 700)
        self.tabs = QTabWidget()
        self.main_tab = QWidget()
        self.advanced_tab = QWidget()
        self.tabs.addTab(self.main_tab, "Principal")
        self.tabs.addTab(self.advanced_tab, "Configurações Avançadas")

        # Layout da aba principal
        main_layout = QVBoxLayout()
        self.url_label = QLabel()
        main_layout.addWidget(self.url_label)
        self.url_input = QLineEdit()
        main_layout.addWidget(self.url_input)
        self.folder_label = QLabel()
        main_layout.addWidget(self.folder_label)
        self.path_input = QLineEdit()
        self.choose_folder_button = QPushButton()
        self.choose_folder_button.clicked.connect(self.choose_folder)
        path_layout = QHBoxLayout()
        path_layout.addWidget(self.path_input)
        path_layout.addWidget(self.choose_folder_button)
        main_layout.addLayout(path_layout)
        self.format_label = QLabel()
        main_layout.addWidget(self.format_label)
        self.format_combo = QComboBox()
        self.format_combo.addItems(["mp4", "mp3", "mkv", "avi", "mov", "flv", "wav"])
        self.format_combo.currentTextChanged.connect(self.update_quality_options)
        main_layout.addWidget(self.format_combo)

        # Container para opções de qualidade (resolução/bitrate)
        self.quality_container = QWidget()
        self.quality_layout = QVBoxLayout()
        self.quality_container.setLayout(self.quality_layout)

        # Opções de vídeo
        self.video_quality_label = QLabel("Video Resolution:")
        self.video_quality_combo = QComboBox()
        self.video_quality_combo.addItems(["144", "240", "360", "480", "720", "1080", "1440", "2160"])

        # Opções de áudio
        self.audio_quality_label = QLabel("Audio Bitrate (kbps):")
        self.audio_quality_combo = QComboBox()
        self.audio_quality_combo.addItems(["64", "96", "128", "192", "256", "320"])

        self.quality_layout.addWidget(self.video_quality_label)
        self.quality_layout.addWidget(self.video_quality_combo)
        self.quality_layout.addWidget(self.audio_quality_label)
        self.quality_layout.addWidget(self.audio_quality_combo)

        main_layout.addWidget(self.quality_container)
        self.update_quality_options(self.format_combo.currentText())
        self.progress_bar = QProgressBar()
        main_layout.addWidget(self.progress_bar)
        self.status_label = QLabel()
        main_layout.addWidget(self.status_label)
        self.history = QTextEdit()
        self.history.setReadOnly(True)
        main_layout.addWidget(self.history)
        self.download_button = QPushButton()
        self.download_button.clicked.connect(self.start_download)
        main_layout.addWidget(self.download_button)
        self.dark_mode_checkbox = QCheckBox()
        self.dark_mode_checkbox.stateChanged.connect(self.toggle_dark_mode)
        main_layout.addWidget(self.dark_mode_checkbox)
        self.language_label = QLabel()
        main_layout.addWidget(self.language_label)
        self.language_combo = QComboBox()
        self.language_combo.addItems(self.languages.keys())
        self.language_combo.setCurrentText("Português (Brasil)")
        self.language_combo.currentTextChanged.connect(self.change_language)
        main_layout.addWidget(self.language_combo)
        self.main_tab.setLayout(main_layout)

        # Configurações Avançadas
        advanced_layout = QFormLayout()
        self.max_threads = QSpinBox()
        self.max_threads.setRange(1, 16)
        self.max_threads.setValue(4)

        # Bandwidth limit slider com label para mostrar valor
        self.bandwidth_container = QWidget()
        self.bandwidth_layout = QHBoxLayout()
        self.bandwidth_limit = QSlider(Qt.Horizontal)
        self.bandwidth_limit.setRange(0, 100)
        self.bandwidth_limit.setValue(50)
        self.bandwidth_value_label = QLabel("50%")
        self.bandwidth_limit.valueChanged.connect(self.update_bandwidth_label)
        self.bandwidth_layout.addWidget(self.bandwidth_limit)
        self.bandwidth_layout.addWidget(self.bandwidth_value_label)
        self.bandwidth_container.setLayout(self.bandwidth_layout)

        self.proxy_input = QLineEdit()
        self.auto_update_checkbox = QCheckBox("Auto Update")
        advanced_layout.addRow("Máximo de Threads:", self.max_threads)
        advanced_layout.addRow("Limite de Banda:", self.bandwidth_container)
        advanced_layout.addRow("Proxy (Opcional):", self.proxy_input)
        advanced_layout.addRow("", self.auto_update_checkbox)
        self.advanced_tab.setLayout(advanced_layout)

        container = QVBoxLayout()
        container.addWidget(self.tabs)
        self.footer = QLabel("Programmed by Solarion© 2025")
        self.footer.setAlignment(Qt.AlignRight)
        container.addWidget(self.footer)
        widget = QWidget()
        widget.setLayout(container)
        self.setCentralWidget(widget)
        self.update_ui_language()

    def update_bandwidth_label(self, value):
        self.bandwidth_value_label.setText(f"{value}%")

    def update_quality_options(self, format_type):
        is_audio = format_type in ['mp3', 'wav']
        self.video_quality_label.setVisible(not is_audio)
        self.video_quality_combo.setVisible(not is_audio)
        self.audio_quality_label.setVisible(is_audio)
        self.audio_quality_combo.setVisible(is_audio)

    def update_ui_language(self):
        t = TRANSLATIONS[self.current_language]
        self.url_label.setText(t["url_label"])
        self.folder_label.setText(t["folder_label"])
        self.choose_folder_button.setText(t["choose_folder"])
        self.format_label.setText(t["format_label"])
        self.download_button.setText(t["start_button"])
        self.dark_mode_checkbox.setText(t["dark_mode"])
        self.language_label.setText(t["language_label"])
        self.status_label.setText(t["status_ready"])
        self.tabs.setTabText(0, t["main_tab"])
        self.tabs.setTabText(1, t["advanced_settings"])
        advanced_layout = self.advanced_tab.layout()
        advanced_layout.labelForField(self.max_threads).setText(t["max_threads"])
        advanced_layout.labelForField(self.bandwidth_container).setText(t["bandwidth_limit"])
        advanced_layout.labelForField(self.proxy_input).setText(t["proxy_optional"])
        self.auto_update_checkbox.setText(t["auto_update"])
        self.footer.setText(t["footer_text"])

    def change_language(self, language):
        self.current_language = self.languages.get(language, "en")
        self.update_ui_language()

    def choose_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Escolher Pasta")
        if folder:
            self.path_input.setText(folder)

    def start_download(self):
        url = self.url_input.text()
        path = self.path_input.text()
        formato = self.format_combo.currentText()

        # Seleciona a opção de qualidade apropriada baseada no formato
        if formato in ['mp3', 'wav']:
            quality_option = self.audio_quality_combo.currentText()
        else:
            quality_option = self.video_quality_combo.currentText()

        if not url or not path:
            self.status_label.setText(TRANSLATIONS[self.current_language]["error_fill_fields"])
            return

        # Verifica se a URL é suportada
        if not is_supported_url(url):
            self.status_label.setText(TRANSLATIONS[self.current_language]["error_url"])
            return

        self.download_thread = DownloadThread(url, path, formato, quality_option)
        self.download_thread.progress.connect(self.update_progress)
        self.download_thread.status.connect(self.update_status_with_logs)  # Nova função para logs detalhados
        self.download_thread.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def update_status_with_logs(self, status):
        """Atualiza o status e adiciona logs detalhados com data/hora."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"[{timestamp}] {status}"
        self.status_label.setText(status)
        self.history.append(log_message)

    def toggle_dark_mode(self, state):
        if state == Qt.Checked:
            self.setStyleSheet("background-color: #2E2E2E; color: white;")
        else:
            self.setStyleSheet("")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')  # Aplicando tema moderno
    window = DownloaderApp()
    window.show()
    sys.exit(app.exec_())
