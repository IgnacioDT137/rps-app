from flask import Blueprint, flash, redirect, url_for
import random

auth = Blueprint('auth', __name__)

@auth.route('/tijeras')
def tijeras():
    n = random.randint(1,3)
    if n == 1:
        flash('La web ha elegido piedra, perdiste!')
    elif n == 2:
        flash('La web ha elegido papel, ganaste!')
    elif n == 3:
        flash('La web ha elegido tijeras, han empatado!')
    return redirect(url_for('views.home'))

@auth.route('/papel')
def papel():
    n = random.randint(1,3)
    if n == 1:
        flash('La web ha elegido piedra, ganaste!')
    elif n == 2:
        flash('La web ha elegido papel, han empatado!')
    elif n == 3:
        flash('La web ha elegido tijeras, perdiste!')
    return redirect(url_for('views.home'))

@auth.route('/piedra')
def piedra():
    n = random.randint(1,3)
    if n == 1:
        flash('La web ha elegido piedra, han empatado!')
    elif n == 2:
        flash('La web ha elegido papel, perdiste!')
    elif n == 3:
        flash('La web ha elegido tijeras, ganaste!')
    return redirect(url_for('views.home'))