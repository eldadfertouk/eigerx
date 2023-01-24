def priceCheck(products, productPrices, productSold, soldPrice):
    errors = 0
    product_prices = dict(zip(products, productPrices))
    for i in range(len(productSold)):
        if product_prices[productSold[i]] != soldPrice[i]:
            errors += 1
    return errors

def test_priceCheck():
    products = ['eggs', 'milk', 'cheese']
    productPrices = [2.89, 3.29, 5.79]
    productSold = ['eggs', 'eggs', 'cheese', 'milk']
    soldPrice = [2.89, 2.99, 5.97, 3.29]
    assert priceCheck(products, productPrices, productSold, soldPrice) == 2

test_priceCheck()
