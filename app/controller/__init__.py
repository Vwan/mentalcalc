
"""
Maintain blueprints
"""
from controller.login_view import bp_login
from controller.calc_view import bp_calc

blueprint_views = [
                bp_login,
                bp_calc
                ]

print("---++++---",blueprint_views)

"""
Calc Rules - Add
"""

""" Rule 1: 自左向右法
 Example: 67 + 45 = 67 + 40 + 5 = 107 + 5 = 112
 """
