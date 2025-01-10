#jel ticket generator


#Initialize
import turtle
jel = turtle.Turtle()

#Functions

#Draws an admission ticket with a label and customer information inside. This function uses a turtle to draw a ticket with the name of the customer and the price paid for the ticket.
#(string: name) represents the customers name that appears inside the ticket
#(integer: price) represents the price the customer paid that appears inside the ticket
#(string: dayofweek) represents the day of the week that the ticket was purchased
#(integer: y_location) y_location represents the vertical loction of the ticket
def draw_ticket(name, price, dayofweek, y_location):
    jel.goto(-50, y_location)
    jel.write("Ticket", font=("Arial", 15), align="right")
    jel.pendown()
    for i in range(2):
        jel.forward(500)
        jel.left(90)
        jel.forward(250)
        jel.left(90)
    jel.penup()
    jel.goto(50, y_location +215)
    jel.write("Admit One", font=("Arial", 15), align="right")
    jel.goto(440, y_location +215)
    jel.write(dayofweek, font=("Arial", 15), align="right")
    jel.goto(225, y_location +135)
    jel.write(name, font=("Arial", 15), align="right")
    jel.goto(225, y_location +15)
    jel.write(price, font=("Arial", 15), align="right")

def ticketinfo():
    global name
    global age
    global day
    global code
    print("welcome to jel's ticket shop!")
    name = input("What is your name?")
    age = int(input("How old are you?:"))
    day = input("what day of the week is it?:")
    code = input("coupon code: (type 'none' if no code):")

    price = 100
    if age <=3:
        price = 0
    elif 4<=age<=17:
        if day == "Saturday" or day == "Sunday":
            price = 100
        else:
            price = 50
        if code == "FREEFRIDAY" and day == "Friday":
            price = 0
        elif code == "SUNDAY10" and day == "Sunday":
            price = 90
        elif code == "none":
            price = price
    elif age>=18:
            price = 100
    draw_ticket(name,price,day,0)





#Main
ticketinfo()

