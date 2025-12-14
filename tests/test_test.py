from pages.textbox import Text
from pages.checkbox import Checkbox
from pages.radio import Radio
from pages.web_tables import Webtable
from pages.buttons import Buttons
from pages.links import Links
from pages.upload import Upload
from pages.dynamic import Dynamic
from pages.alerts import Alert
from pages.frames import Frames
from pages.nested_frames import Nested_Frames
from utilities.driver_setup import get_driver
def test_test(driver):
    driver.get("https://demoqa.com/")
    text=Text(driver)
    text.text_box()
    checkbox=Checkbox(driver)
    checkbox.check_box()
    radio=Radio(driver)
    radio.radio()
    webtable=Webtable(driver)
    webtable.web_tables()
    buttons=Buttons(driver)
    buttons.clicks()
    link=Links(driver)
    link.links()
    upload=Upload(driver)
    upload.upload_download()
    dynamic=Dynamic(driver)
    dynamic.dynamic()
    alert=Alert(driver)
    alert.alert()
    frame=Frames(driver)
    frame.frames()
    nest=Nested_Frames(driver)
    nest.nested()