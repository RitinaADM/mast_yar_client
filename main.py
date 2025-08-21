import sys
from PySide6.QtWidgets import QApplication
from src.infrastructure.di.container import create_client

if __name__ == "__main__":
    app = QApplication(sys.argv)
    client = create_client()
    client.run()
    sys.exit(app.exec())