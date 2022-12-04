# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    def move(self, field, coord_x, coord_y, direction, is_fly, is_steal, speed = 1):
        if is_fly and is_steal:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
            if direction == 'UP':
                new_y = coord_y + speed
                new_x = coord_x
            elif direction == 'DOWN':
                new_y = coord_y - speed
                new_x = coord_x
            elif direction == 'LEFT':
                new_y = coord_y
                new_x = coord_x - speed
            elif direction == 'RIGHT':
                new_y = coord_y
                new_x = coord_x + speed
        if is_steal:
            speed *= 0.5
            if direction == 'UP':
                new_y = coord_y + speed
                new_x = coord_x
            elif direction == 'DOWN':
                new_y = coord_y - speed
                new_x = coord_x
            elif direction == 'LEFT':
                new_y = coord_y
                new_x = coord_x - speed
            elif direction == 'RIGHT':
                new_y = coord_y
                new_x = coord_x + speed

            field.set_unit(x=new_x, y=new_y, unit=self)
