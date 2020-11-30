radio.onReceivedNumber(function (receivedNumber) {
    their_number = receivedNumber
    if (my_number != 0) {
        show_result(my_number, their_number)
        next_round()
    }
})
function restart () {
    game.setScore(0)
    next_round()
}
input.onButtonPressed(Button.A, function () {
    my_number = randint(1, 9)
    images.iconImage(IconNames.No).showImage(0)
    radio.sendNumber(my_number)
    if (their_number != 0) {
        show_result(my_number, their_number)
        next_round()
    }
})
input.onButtonPressed(Button.AB, function () {
    radio.sendString("restart")
    restart()
})
radio.onReceivedString(function (receivedString) {
    if (receivedString == "restart") {
        restart()
    }
    if (receivedString == "you lose") {
        game.gameOver()
        restart()
    }
})
function next_round () {
    if (game.score() >= 3) {
        radio.sendString("you lose")
        basic.showString("Congratulations")
    }
    my_number = 0
    their_number = 0
    basic.showNumber(game.score())
}
function show_result (num: number, num2: number) {
    if (num > num2) {
        game.addScore(1)
    } else if (num2 > num) {
        images.iconImage(IconNames.Sad).showImage(0)
    } else {
        images.iconImage(IconNames.Heart).showImage(0)
    }
    basic.pause(200)
}
let my_number = 0
let their_number = 0
radio.setGroup(1)
restart()
