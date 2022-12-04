# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - y координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, field, x_coord, y_coord):
        self.field = field
        self.x_coord = x_coord
        self.y_coord = y_coord

    def _get_speed(self, state, speed):
        if state == 'fly':
            return speed * 1.2
        elif state == 'crawl':
            return speed * 0.5
        else:
            raise ValueError('Эк тебя раскорячило')

    def move(self, direction, state, base_speed):
        speed = self._get_speed(state, base_speed)

        if direction == 'UP':
            self.field.set_unit(y=self.y_coord + speed, x=self.x_coord, unit=self)
        if direction == 'DOWN':
            self.field.set_unit(y=self.y_coord - speed, x=self.x_coord, unit=self)
        if direction == 'LEFT':
            self.field.set_unit(y=self.y_coord, x=self.x_coord - speed, unit=self)
        if direction == 'RIGTH':
            self.field.set_unit(y=self.y_coord, x=self.x_coord + speed, unit=self)

#     ...
