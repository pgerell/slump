def on_received_number(receivedNumber):
    global their_number
    their_number = receivedNumber
    if my_number != 0:
        show_result(my_number, their_number)
radio.on_received_number(on_received_number)

def restart():
    game.set_score(0)
    next_round()

def on_button_pressed_a():
    global my_number
    my_number = randint(1, 9)
    images.icon_image(IconNames.NO).show_image(0)
    radio.send_number(my_number)
    if their_number != 0:
        show_result(my_number, their_number)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    radio.send_string("restart")
    restart()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    if receivedString == "next round":
        next_round()
    if receivedString == "restart":
        restart()
    if receivedString == "you lose":
        game.game_over()
        restart()
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.send_string("next round")
    next_round()
input.on_button_pressed(Button.B, on_button_pressed_b)

def next_round():
    global my_number, their_number
    my_number = 0
    their_number = 0
    basic.show_number(game.score())
def show_result(num: number, num2: number):
    if num > num2:
        images.icon_image(IconNames.HAPPY).show_image(0)
        game.add_score(1)
        if 0 >= 3:
            radio.send_string("you lose")
            for index in range(4):
                game.add_score(1)
                basic.pause(500)
    elif num2 > num:
        images.icon_image(IconNames.SAD).show_image(0)
    else:
        images.icon_image(IconNames.HEART).show_image(0)
my_number = 0
their_number = 0
radio.set_group(1)
game.set_score(0)
next_round()