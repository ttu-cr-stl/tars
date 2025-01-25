from rich.logging import RichHandler
from rich.console import Console
from rich.theme import Theme
import logging
import time

TARS_ASCII = """
╔════════════════════════════════════════╗
║  ████████╗ █████╗ ██████╗ ███████╗    ║
║  ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝    ║
║     ██║   ███████║██████╔╝███████╗    ║
║     ██║   ██╔══██║██╔══██╗╚════██║    ║
║     ██║   ██║  ██║██║  ██║███████║    ║
║     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ║
║                                        ║
║     HONESTY LEVEL: 90%                 ║
║     HUMOR LEVEL: 75%                   ║
╚════════════════════════════════════════╝
"""

class Logger:
    def __init__(self):
        custom_theme = Theme({
            "timestamp": "#7B68EE",  # Medium slate blue for futuristic feel
            "tars": "#00FF00",      # Matrix green
            "alert": "#FF4B4B",     # Bright red
            "warning": "#FFB300",    # Amber
            "success": "#00C853",    # Bright green
            "info": "#7FDBFF",      # Bright cyan
        })
        
        self.console = Console(
            theme=custom_theme,
            color_system="truecolor"
        )
        
        # Display TARS ASCII art on initialization
        self.console.print(TARS_ASCII, style="tars")
        
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(message)s",
            datefmt="[%X]",
            handlers=[RichHandler(console=self.console, rich_tracebacks=True)]
        )
        self.logger = logging.getLogger("rich")

        # Suppress other logs
        logging.getLogger('werkzeug').setLevel(logging.ERROR)
        logging.getLogger('flask').setLevel(logging.ERROR)
        logging.getLogger('requests').setLevel(logging.ERROR)
        logging.getLogger('connectionpool').setLevel(logging.ERROR)
        logging.getLogger('urllib3.connectionpool').setLevel(logging.ERROR)
        logging.getLogger('googleapiclient.discovery').setLevel(logging.ERROR)
        logging.getLogger('google_auth_httplib2').setLevel(logging.ERROR)
        logging.getLogger('feedparser').setLevel(logging.ERROR)
        logging.getLogger('nltk').setLevel(logging.ERROR)
        logging.getLogger('chardet').setLevel(logging.ERROR)
        logging.getLogger('sqlalchemy').setLevel(logging.ERROR)
        logging.getLogger('geventwebsocket').setLevel(logging.ERROR)
        logging.getLogger('httpx').setLevel(logging.ERROR)
        logging.getLogger('httpcore').setLevel(logging.ERROR)

    def info(self, message):
        self.logger.debug(f"[tars]TARS//[/tars] [info]{message}[/info]", extra={'markup': True})

    def success(self, message):
        self.logger.debug(f"[tars]TARS//[/tars] [success]{message}[/success]", extra={'markup': True})

    def announcement(self, message, type='info'):
        if type == 'info':
            self.logger.info(f"[tars]TARS//[/tars] [alert]{message}[/alert]", extra={'markup': True})
        elif type == 'success':
            self.logger.info(f"[tars]TARS//[/tars] [success]{message}[/success]\n", extra={'markup': True})
        else:
            raise ValueError("Invalid type. Choose 'info' or 'success'.")
        
    def warning(self, message):
        self.logger.warning(f"[tars]TARS//[/tars] [warning]{message}[/warning]", extra={'markup': True})

    def error(self, message):
        self.logger.error(f"[tars]TARS//[/tars] [alert]{message}[/alert]", extra={'markup': True})


logger = Logger()
