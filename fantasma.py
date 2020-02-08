import pyautogui
pyautogui.moveTo(797, 521, duration=1)
pyautogui.moveRel(-150, 0, duration=0.5)
pyautogui.moveRel(0, -150, duration=0.5)

for k in range(0, 3):
    pyautogui.moveRel(300, 0, duration=0.5)
    pyautogui.moveRel(0, 300, duration=0.5)
    pyautogui.moveRel(-300, 0, duration=0.5)
    pyautogui.moveRel(0, -300, duration=0.5)

pyautogui.alert('Parabéns! Você criou seu primeiro fantasma digital.')
