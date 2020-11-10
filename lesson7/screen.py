#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)
class Vector:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other):
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, k):
        return Vector((self.x * k), (self.y * k))

    def __truediv__(self, a):
        return Vector((self.x / a), (self.y / a))

    def __abs__(self):
        return (((self.x) ** 2 + (self.y) ** 2 ) ** (1 / 2))

    def int_pair(self):
        return (self.x,self.y)
    def __len__(self):
        return self.__abs__()
class Polyline():
    def __init__(self,points):
        self.p=points

    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        if style == "line":
            for p_n in range(-1, len(self.p) - 1):
                pygame.draw.line(gameDisplay, color,
                                 (int(self.p[p_n][0]), int(self.p[p_n][1])),
                                 (int(self.p[p_n + 1][0]), int(self.p[p_n + 1][1])), width)

        elif style == "points":
            for p in points:
                pygame.draw.circle(gameDisplay, color,
                                   (int(p.x), int(p.y)), width)

    def draw_help(self):
        """функция отрисовки экрана справки программы"""
        gameDisplay.fill((50, 50, 50))
        font1 = pygame.font.SysFont("courier", 24)
        font2 = pygame.font.SysFont("serif", 24)
        data = []
        data.append(["F1", "Show Help"])
        data.append(["R", "Restart"])
        data.append(["P", "Pause/Play"])
        data.append(["Num+", "More points"])
        data.append(["Num-", "Less points"])
        data.append(["", ""])
        data.append([str(steps), "Current points"])

        pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
            (0, 0), (800, 0), (800, 600), (0, 600)], 5)
        for i, text in enumerate(data):
            gameDisplay.blit(font1.render(
                text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
            gameDisplay.blit(font2.render(
                text[1], True, (128, 128, 255)), (200, 100 + 30 * i))

    def set_points(self, speeds):
        """функция перерасчета координат опорных точек"""
        for i in range(len(self.p)):
            self.p[i] = self.p[i] + speeds[i]
            if self.p[i][0] > SCREEN_DIM[0] or self.p[i][0] < 0:
                speeds[i] = (- speeds[i][0], speeds[i][1])
            if self.p[i][1] > SCREEN_DIM[1] or self.p[i][1] < 0:
                speeds[i] = (speeds[i][0], -speeds[i][1])
# =======================================================================================
# Функции для работы с векторами
# =======================================================================================

# def sub(x, y):
#     """"возвращает разность двух векторов"""
#     return x[0] - y[0], x[1] - y[1]
#
#
# def add(x, y):
#     """возвращает сумму двух векторов"""
#     return x[0] + y[0], x[1] + y[1]
#
#
# def length(x):
#     """возвращает длину вектора"""
#     return math.sqrt(x[0] * x[0] + x[1] * x[1])
#
#
# def mul(v, k):
#     """возвращает произведение вектора на число"""
#     return v[0] * k, v[1] * k
#
#
# def vec(x, y):
#     """возвращает пару координат, определяющих вектор (координаты точки конца вектора),
#     координаты начальной точки вектора совпадают с началом системы координат (0, 0)"""
#     return sub(y, x)


# =======================================================================================
# Функции отрисовки
# =======================================================================================
# def draw_points(points, style="points", width=3, color=(255, 255, 255)):
#     """функция отрисовки точек на экране"""
#     if style == "line":
#         for p_n in range(-1, len(points) - 1):
#             pygame.draw.line(gameDisplay, color,
#                              (int(points[p_n][0]), int(points[p_n][1])),
#                              (int(points[p_n + 1][0]), int(points[p_n + 1][1])), width)
#
#     elif style == "points":
#         for p in points:
#             pygame.draw.circle(gameDisplay, color,
#                                (int(p[0]), int(p[1])), width)
#
#
# def draw_help():
#     """функция отрисовки экрана справки программы"""
#     gameDisplay.fill((50, 50, 50))
#     font1 = pygame.font.SysFont("courier", 24)
#     font2 = pygame.font.SysFont("serif", 24)
#     data = []
#     data.append(["F1", "Show Help"])
#     data.append(["R", "Restart"])
#     data.append(["P", "Pause/Play"])
#     data.append(["Num+", "More points"])
#     data.append(["Num-", "Less points"])
#     data.append(["", ""])
#     data.append([str(steps), "Current points"])
#
#     pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
#         (0, 0), (800, 0), (800, 600), (0, 600)], 5)
#     for i, text in enumerate(data):
#         gameDisplay.blit(font1.render(
#             text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
#         gameDisplay.blit(font2.render(
#             text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


# =======================================================================================
# Функции, отвечающие за расчет сглаживания ломаной
# =======================================================================================
class Knot(Polyline):

    def get_point(self, alpha, deg=None):
        if deg is None:
            deg = len(self.p) - 1
        if deg == 0:
            return self.p[0]
        return ((points[deg]* alpha)+ (self.p.get_point( alpha, deg - 1)* 1 - alpha))

    def get_points(self,base_points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(self.get_point(base_points, i * alpha))
        return res


    def get_knot(self, count):
        if len(self.p) < 3:
            return []
        res = []
        for i in range(-2, len(self.p) - 2):
            ptn = []
            ptn.append((self.p[i]+ self.p[i + 1])* 0.5)
            ptn.append(self.p[i + 1])
            ptn.append((self.p[i + 1]+ self.p[i + 2])* 0.5)

            res.extend(self.get_points(ptn, count))
        return res


# def set_points(points, speeds):
#     """функция перерасчета координат опорных точек"""
#     for p in range(len(points)):
#         points[p] = points[p]+ speeds[p]
#         if points[p][0] > SCREEN_DIM[0] or points[p][0] < 0:
#             speeds[p] = (- speeds[p][0], speeds[p][1])
#         if points[p][1] > SCREEN_DIM[1] or points[p][1] < 0:
#             speeds[p] = (speeds[p][0], -speeds[p][1])


# =======================================================================================
# Основная программа
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    points = []
    speeds = []
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    points = []
                    speeds = []
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                points.append(Vector(event.pos[0],event.pos[1]))
                speeds.append((random.random() * 2, random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        p=Knot(points)
        p.draw_points()
        r=Knot(p.get_knot(steps))
        r.draw_points("line", 3, color)
        if not pause:
            p.set_points( speeds)
        if show_help:
            r.draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
