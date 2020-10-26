function clearface () {
    basic.showIcon(IconNames.SmallHeart)
    basic.showIcon(IconNames.Heart)
}
input.onButtonPressed(Button.A, function () {
    clearface()
    basic.showIcon(IconNames.Happy)
})
input.onButtonPressed(Button.B, function () {
    clearface()
    basic.showIcon(IconNames.Sad)
})
basic.showIcon(IconNames.Asleep)
let happy = 0
let sad = 0
basic.forever(function () {
	
})
