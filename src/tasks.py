from RPA.Browser.Selenium import Selenium
from RPA.HTTP import HTTP
from pillow.generateCard import generateIdCard
from robocorp.tasks import task
from entities.id_data import Id

browserPhoto = Selenium()
http = HTTP()

# take a new photo in thispersondoesnotexist.com
def takePhoto():
    
    # open web page
    browserPhoto.open_available_browser("https://thispersondoesnotexist.com/")
    browserPhoto.wait_until_element_is_visible("xpath://body", timeout=10)
    
    # find image in page
    img_tag = browserPhoto.get_element_attribute("css:img", "src")
    print(f"Image URL trouvée : {img_tag}")
    
    # Download image
    http.download(url=img_tag, target_file="img/new_person.jpg", overwrite=True)

# take a new identity information
def takeInfo():
    
    # open web page
    browserPhoto.open_available_browser("https://calculatit.com/Security/fake-identity-generator.html")
    browserPhoto.wait_until_element_is_visible("xpath://body", timeout=10)
    
    # get data part
    data = Id()
    data.name = browserPhoto.execute_javascript("return document.querySelector('.identity-value').innerText")
    data.address = browserPhoto.execute_javascript("return document.getElementById('address').innerText")
    data.birthday = browserPhoto.execute_javascript("return document.getElementById('dob').innerText")
    data.phone = browserPhoto.execute_javascript("return document.getElementById('phone').innerText")
    data.email = browserPhoto.execute_javascript("return document.getElementById('email').innerText")
    
    return data

# Run all task 
@task 
def createIDCard():
    takePhoto()
    id_info = takeInfo()
    generateIdCard(id_info)
    close()

# close all browser
def close():
    browserPhoto.close_all_browsers()
