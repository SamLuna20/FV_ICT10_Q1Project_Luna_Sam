from pyscript import document, display

restaurant_name = "Fit Diners" #String(str)
owner_name = "Sam Luna" #String(str)
year_established = 2025 #Integer(int)
popular_item_price = [150, 170, 180, 80, 60] #List
has_delivery = False #Boolean
product_names = ['Chocolate Protein Shake','Strawberry Protein Shake','Matcha Protein Shake'] #List
business_hours = "10AM - 8PM" #String(str)
menu_prices = {"Chocolate Protein Shake":150,'Strawberry Protein Shake':170,'Matcha Protein Shake':180,'Fit Delight Cupcake':80, 'Protein Bar':60} #Dictionary(dict)
common_allergens = ['Milk','Soy','Eggs'] #List
tax_rate = 0.05 #Float

def placeOrder(e):

    name = document.getElementById("name").value
    address = document.getElementById("address").value
    number = document.getElementById("number1").value
    email = document.getElementById("email1").value

    checked_boxes = document.querySelectorAll("#orderForm input[type=checkbox]:checked")
    total = sum(int(cb.value) for cb in checked_boxes)

    #
    document.getElementById("orderSummary").classList.remove("d-none")
    
    display(" " + name,target="cname")
    display(" " + address,target="cad")
    display(" " + number,target="cnum")
    display(" " + email,target="em")
    display(" ₱" + str(total), target="total")

#displaying values on HTML according to their respective html id
display(restaurant_name, target="storeName")
display(f"Owner: {owner_name}", target="ownerName")
display(f"Est : {year_established}", target="yearFounded")
display(menu_prices ["Chocolate Protein Shake"], target="price1")
display(menu_prices ["Strawberry Protein Shake"], target="price2")
display(menu_prices ["Matcha Protein Shake"], target="price3")
display(menu_prices ["Fit Delight Cupcake"], target="price4")
display(menu_prices ["Protein Bar"], target="price5")
display(f"Open: {business_hours}", target="opening")