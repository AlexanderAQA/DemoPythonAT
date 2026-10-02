# Дока: https://playwright.help/python/docs/api/class-keyboard#keyboard-press
# Пример:

slider = page.locator("#slider-range") # сама полоска слайдера
handles = slider.locator(".ui-slider-handle") # регулятор(ы) слайдера

left = handles.nth(0)
right = handles.nth(1)

# Например, левый ползунок
left.focus()
left.press("ArrowLeft")

# Можно создать функцию, которая будет нажимать нужно количество раз в зависимости от чувствительности самого
# ползунка. Также есть варианты выставить крайние значения на Home, End


# Например, правый ползунок
right.focus()
right.press("ArrowRight")
