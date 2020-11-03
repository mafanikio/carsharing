import os
import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from PyQt5.QtCore import QUrl, QEventLoop
from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebPage(QWebEngineView):
    def __init__(self):
        QWebEngineView.__init__(self)
        self.load(QUrl("http://mafanikio.pythonanywhere.com/cars"))
        self.loadFinished.connect(self._on_load_finished)

    def _on_load_finished(self):
        print("Finished Loading")
        self.page().toHtml(self.Callable)

    def Callable(self, html_str):
        self.html = html_str
        self.page().runJavaScript("document.getElementsByName('loginid')[0].value = 'email@email.com'")
        self.page().runJavaScript("document.getElementsByName('password')[0].value = 'test'")
        self.page().runJavaScript ("document.getElementById('signin').click()")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    web = WebPage()
    web.show()
    sys.exit(app.exec_())  # only need one app, one running event loop