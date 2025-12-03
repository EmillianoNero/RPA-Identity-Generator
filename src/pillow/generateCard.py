from PIL import Image, ImageDraw, ImageFont
from entities.id_data import Id

# generate id card with pil library
def generateIdCard(id: Id):
    
    card = Image.new("RGB", (650, 350), "white")
    draw = ImageDraw.Draw(card)
    
    # font part
    font_title = ImageFont.truetype("arial.ttf", 28)
    font_text = ImageFont.truetype("verdana.ttf", 16)

    # image
    photo = Image.open("img/new_person.jpg").resize((180, 180))
    card.paste(photo, (425, 50))

    # text
    draw.text((40, 40), "Identity Card", font=font_title, fill="black")

    draw.text((40, 110), f"Name: {id.name}", font=font_text, fill="black")
    draw.text((40, 150), f"Address: {id.address}", font=font_text, fill="black")
    draw.text((40, 190), f"Birthdate: {id.birthday}", font=font_text, fill="black")
    draw.text((40, 230), f"Email: {id.email}", font=font_text, fill="black")
    draw.text((40, 270), f"Phone: {id.phone}", font=font_text, fill="black")

    # Save
    card.save("img/identity_card.png")
    
    
    