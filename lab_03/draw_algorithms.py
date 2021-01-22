def sign(coord):
    # определение направления изменения координаты
    # при отрисовке
    if coord > 0:
        return 1
    elif coord < 0:
        return -1
    else:
        return 0


def isDot(start, end):
    # проверка на вырожденность
    if start == end:
        return 1
    else:
        return 0


def ddaAlg(painter, start, end, *args):
    # алгоритм цифрового дифференциального анализатора

    # start - координаты точки начала отрезка
    # end - координаты точки конца отрезка

    x0, x1 = start[0], end[0]
    y0, y1 = start[1], end[1]
    L = 0

    # проверка ны вырожденность
    if isDot(start, end):
        painter.drawPoint(x0, y0)
        result = 1
        return result

    x, y = x0, y0

    dx = x1 - x0
    dy = y1 - y0

    Dx, Dy = abs(dx), abs(dy)
    if Dx > Dy:
        L = Dx
    else:
        L = Dy

    dx = dx / L
    dy = dy / L

    for i in range(1, L+1):
        painter.drawPoint(round(x), round(y))
        x += dx  # округлить
        y += dy  # округлить



def decimalAlg(painter, start, end, *args):
    # алгоритм Брезенхема для вещественных

    # start - координаты точки начала отрезка
    # end - координаты точки конца отрезка
    result = 0  # была ли дорисована линия

    x0, x1 = start[0], end[0]
    y0, y1 = start[1], end[1]
    xchng = 0   # флаг, отвечающий за смену dx с dy

    # если линия вырождена
    if isDot(start, end):
        painter.drawPoint(x0, y0)
        result = 1
        return result

    x, y = x0, y0

    dx = x1 - x0
    dy = y1 - y0

    # определяет направление движения отрисовки
    sx, sy = sign(dx), sign(dy)
    dx, dy = abs(dx), abs(dy)

    # проверка на перестановку dx и dy
    if dx <= dy:
        dx, dy = dy, dx
        xchng = 1

    # определение тангенса угла и ошибки
    m = dy / dx  # угловой коэффициент
    e = -0.5  # так как проверяется только знак, устанавливается -0.5
    e = e + m

    for i in range(1, dx+1):
        painter.drawPoint(x, y)

        if e >= 0:
            if not xchng:
                y += sy
            else:
                x += sx
            e -= 1.0  # корректировка ошибки

        if not xchng:
            x += sx
        else:
            y += sy
        e += m

    if x >= x1 and y >= y1:
        result = 1
    return result


def intAlg(painter, start, end, *args):
    # алгоритм Брезенхема только для целочисленных значений
    # должно работать быстрее
    result = 0  # была ли дорисована линия

    x0, x1 = start[0], end[0]
    y0, y1 = start[1], end[1]
    xchng = 0  # флаг для смены dx dy

    # если линия вырождена
    if isDot(start, end):
        painter.drawPoint(x0, y0)
        result = 1
        return result

    x, y = x0, y0

    dx = x1 - x0
    dy = y1 - y0

    sx, sy = sign(dx), sign(dy)  # направление отрисовки
    dx, dy = abs(dx), abs(dy)

    # проверка на перестановку dx dy
    if dx <= dy:
        dx, dy = dy, dx
        xchng = 1

    e = 2 * dy - dx

    for i in range(1, dx+1):
        painter.drawPoint(x, y)

        if e >= 0:
            if not xchng:
                y += sy
            else:
                x += sx
            e -= 2 * dx

        if not xchng:
            x += sx
        else:
            y += sy

        e += 2 * dy

    if x >= x1 and y >= y1:
        result = 1
    return result


def deleteStepAlg(painter, start, end, color):
    # алгоритм Брезенхема с удалением ступенчатости
    result = 0  # была ли дорисована линия

    x0, x1 = start[0], end[0]
    y0, y1 = start[1], end[1]
    xchng = 0

    # если линия вырождена
    if isDot(start, end):
        painter.drawPoint(x0, y0)
        result = 1
        return result

    x, y = x0, y0

    dx = x1 - x0
    dy = y1 - y0

    sx, sy = sign(dx), sign(dy)
    dx, dy = abs(dx), abs(dy)

    if dx <= dy:
        dx, dy = dy, dx
        xchng = 1

    I = 255  # максимальный уровень интенсивности

    m = I * dy / dx  # скорректированный тангенс угла наклона
    # m = dy/dx

    w = I - m  # весовой коэфф
    # w = 1 - m

    e = 0.5  # площадь внутри многоугольника
    # alpha = int(255 * e)
    alpha = int(m/2)

    for i in range(1, dx+1):

        color.setAlpha(alpha)
        painter.setPen(color)
        painter.drawPoint(x, y)

        if e < w:
            if not xchng:
                x += sx
            else:
                y += sy
            e += m
        else:
            y += sy
            x += sx
            e -= w

        e = round(e, 2)

        alpha = int(I - e)
        # alpha = int(255 - 255 * e)

    if x >= x1 and y >= y1:
        result = 1
    return result


def libAlg(painter, start, end, *args):
    painter.drawLine(start[0], start[1],
                     end[0], end[1])
    return 1
