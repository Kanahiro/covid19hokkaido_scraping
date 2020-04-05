import os
import time

from selenium import webdriver

if not os.path.exists("ogp"):
  os.mkdir("ogp")

PATHS = {
  "/cards/current-patients": (959, 910),
  "/cards/contacts": (959, 870),
  "/cards/discharges-summary": (959, 910),
  "/cards/inspections": (959, 870),
  "/cards/patients": (959, 500),
  "/cards/patients-summary": (959, 870),
  "/cards/querents": (959, 890)
}

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--hide-scrollbars")

driver = webdriver.Chrome(options=options)

for lang in ("ja", "en", "zh-cn", "zh-tw", "ko", "ja-basic"):
  if not os.path.exists("ogp/{}".format(lang)):
    os.mkdir("ogp/{}".format(lang))
  for path, size in PATHS.items():
    driver.set_window_size(*size)
    driver.get(
      "https://stopcovid19-dev.hokkaido.dev{}?ogp=true".format(
        path if lang == "ja" else "/{}{}".format(lang, path)
      )
    )
    path = path.replace("/cards/", "").replace("/", "_")
    time.sleep(3)
    driver.save_screenshot(
      "ogp/{}.png".format(
        path if lang == "ja" else "{}/{}".format(lang, path)
      )
    )
