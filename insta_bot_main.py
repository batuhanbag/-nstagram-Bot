from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from time import sleep
import icons_rc
from insta_bot_python import Ui_MainWindow
from selenium import webdriver



class Bott(QMainWindow):

    def __init__(self):

        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit_sifre.setEchoMode(QLineEdit.Passwords


        self.ui.pushButton_start.clicked.connect(self.process)




    def process(self):

        if self.ui.checkBox_begen.setChecked(True):
            driver = webdriver.Chrome()
            driver.get('https://www.instagram.com')
            sleep(2)

            self.kullaniciAD = self.ui.lineEdit_kullaniciAD.text()
            self.sifre = self.ui.lineEdit_sifre.text()
            self.arama_listesi = self.ui.lineEdit_hastag.text()
            self.yorum = self.ui.lineEdit_yorum.text()
            username = driver.find_element_by_name('username').send_keys(self.kullaniciAD)
            password = driver.find_element_by_name('password').send_keys(self.sifre)
            girisbutton = driver.find_element_by_xpath('//button[@type="submit"]').click()
            sleep(2)
            simdidegil = driver.find_element_by_xpath(
                '//button[contains(text(), "Şimdi Değil")]').click()
            sleep(1.5)
            simdidegil = driver.find_element_by_xpath(
                '//button[contains(text(), "Şimdi Değil")]').click()
            sleep(0.5)

            aramakutusu = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(self.arama_listesi)
            sleep(2)
            profile = driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]').click()
            sleep(3)

            def scrollAllWayDown(process):
                # Tll agahis function scroll down to see the footer element and wait for a couple second. If page scroll length has changed then scroin because that mean there is other pictures.
                global driver
                footer = driver.find_element_by_tag_name('footer')  # The footer element
                last_height = driver.execute_script('return document.body.scroll')  # Before scroll down note scroll length
                while True:
                    footer.location_once_scrolled_into_view  # Scroll down to see footer
                    sleep(2)  # Wait for internet
                    new_height = driver.execute_script(
                        'return document.body.scroll')  # Run javascript code again to check scroll length.
                    if new_height == last_height:  # If scroll height hasnt changed then there is no more pictures.

                        break
                    else:  # If it changed set the last height equal new height and repeat function.
                        last_height = new_height
            scrollAllWayDown()
            tumKutular = driver.find_elements_by_class_name(
                    'Nnq7C')  # Every photo attribute has a parent div so first find divs
            tumLinkler = []
            for i in tumKutular:
                tumLinkler.append(i.find_element_by_tag_name('a'))  # And find attribute in divs

            for i in tumLinkler:
                i.click()  # Click link and open photo
                sleep(2)
                begenbuton = driver.find_element_by_xpath(
                        '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
                begenbuton.click()
                sleep(2)
                yorum = driver.find_element_by_class_name('Ypffh')
                yorum.click()
                sleep(1)
                yorum = driver.find_element_by_class_name('Ypffh')
                sleep(1)
                yorum.send_keys(self.yorum)
                sleep(2)
                paylasbutton = driver.find_element_by_xpath(
                        '/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button')
                paylasbutton.click()

                sleep(0.2)
                cikis = driver.find_element_by_xpath('/html/body/div[5]/div[3]/button').click()
            else:
                pass

app = QApplication([])
window = Bott()
window.show()
app.exec_()