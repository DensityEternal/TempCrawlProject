from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
options = webdriver.ChromeOptions()
headers = {'cookie':'_lxsdk_cuid=18b69f369acc8-01609a07823c92-26031151-18c180-18b69f369ac79; _lxsdk=18b69f369acc8-01609a07823c92-26031151-18c180-18b69f369ac79; isUuidUnion=true; iuuid=18b69f369acc8-01609a07823c92-26031151-18c180-18b69f369ac79; ta.uuid=1717377369176387615; WEBDFPID=y4u89vyzw177566wz1ux0z40x687w46381y30u62wyx97958u1680150-2013649647097-1698289642102CCKSAEWfd79fef3d01d5e9aadc18ccd4d0c95074126; uuid=83b43d6acec542129eac.1698289652.1.0.0; token=AgH-IpYg8e3uEtkP1heXdriklEgVef6E5Rb01AlVB1iPRDTukMedTH5PY1PKwGdttGdU3XNTEOiP5AAAAADKGwAAYsRyoPBkNbze_hlvfHN8qxwDsDfsKY1j2-5xKhJAoxM2MOJLtZt5Duo8aOG_WazG; mt_c_token=AgH-IpYg8e3uEtkP1heXdriklEgVef6E5Rb01AlVB1iPRDTukMedTH5PY1PKwGdttGdU3XNTEOiP5AAAAADKGwAAYsRyoPBkNbze_hlvfHN8qxwDsDfsKY1j2-5xKhJAoxM2MOJLtZt5Duo8aOG_WazG; oops=AgH-IpYg8e3uEtkP1heXdriklEgVef6E5Rb01AlVB1iPRDTukMedTH5PY1PKwGdttGdU3XNTEOiP5AAAAADKGwAAYsRyoPBkNbze_hlvfHN8qxwDsDfsKY1j2-5xKhJAoxM2MOJLtZt5Duo8aOG_WazG; userId=3567872565; u=3567872565; isid=AgH-IpYg8e3uEtkP1heXdriklEgVef6E5Rb01AlVB1iPRDTukMedTH5PY1PKwGdttGdU3XNTEOiP5AAAAADKGwAAYsRyoPBkNbze_hlvfHN8qxwDsDfsKY1j2-5xKhJAoxM2MOJLtZt5Duo8aOG_WazG; wm_order_channel=default; utm_source=; au_trace_key_net=default; openh5_uuid=18b69f369acc8-01609a07823c92-26031151-18c180-18b69f369ac79; isIframe=false; _lx_utm=utm_source%3D70200; _lxsdk_s=18b69f369ae-d1a-839-66e%7C%7C102'}
url='https://market.waimai.meituan.com/gd2/wm/4TeALm?el_biz=waimai&el_page=gundam.loader&gundam_id=4TeALm&tenant=gundam&utm_source=70200&lch=wmsq-notice&click_cps_url=https://click.meituan.com/t?t&c=2&p=dFj_HL5z_4KQ&userId=3567872565&token=AgH-IpYg8e3uEtkP1heXdriklEgVef6E5Rb01AlVB1iPRDTukMedTH5PY1PKwGdttGdU3XNTEOiP5AAAAADKGwAAYsRyoPBkNbze_hlvfHN8qxwDsDfsKY1j2-5xKhJAoxM2MOJLtZt5Duo8aOG_WazG&wm_latitude=32.344287&wm_longitude=119.405587&pickedCityName=%E6%89%AC%E5%B7%9E%E5%B8%82&pickedAddress=%E6%89%AC%E5%B7%9E%E5%A4%A7%E5%AD%A6(%E6%89%AC%E5%AD%90%E6%B4%A5%E6%A0%A1%E5%8C%BA)-%E4%B8%9C%E5%8C%97%E9%97%A8'
options.add_argument(f"--headers={headers}")
chrome = webdriver.Chrome(options=options)
chrome.get(url)
try:
    button=chrome.find_element(By.CLASS_NAME,'redbag-status-will-grab')
    button.click()
except Exception as e:
    print(e)