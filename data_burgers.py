from burgers_locators import BurgerLocators
# URLs
URL_BASE = 'https://stellarburgers.nomoreparties.site/'
URL_PROFILE_PAGE = f'{URL_BASE}account/profile'
URL_ORDER_HISTORY = f'{URL_BASE}account/order-history'
URL_FORGOT_PASSWORD_PAGE = f'{URL_BASE}forgot-password'
URL_RESET_PASSWORD_PAGE = f'{URL_BASE}reset-password'
URL_LOGIN_PAGE = f'{URL_BASE}login'
URL_ORDER_LIST = f'{URL_BASE}feed'
REGISTER_USER = 'api/auth/register'
DATA_USER = 'api/auth/user'
# test data
LIST_INGREDIENT = [[BurgerLocators.IMG_INGREDIENT_BUN, BurgerLocators.COUNT_INGREDIENT_BUN, '2'],
                   [BurgerLocators.IMG_INGREDIENT_SAUCE, BurgerLocators.COUNT_INGREDIENT_SAUCE, '1'],
                   [BurgerLocators.IMG_INGREDIENT_FILLING, BurgerLocators.COUNT_INGREDIENT_FILLING, '1']]
COUNT_LOCATOR = [BurgerLocators.COUNT_TOTAL_ORDER, BurgerLocators.COUNT_TOTAL_TODAY_ORDER]
