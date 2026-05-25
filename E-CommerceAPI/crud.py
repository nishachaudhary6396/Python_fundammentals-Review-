from fastapi import HTTPException

from db import load_data, save_data


# CREATE PRODUCT
def create_product(product):

    products = load_data()

    products[str(product.id)] = product.dict()

    save_data(products)

    return {
        "message": "Product created successfully",
        "product": product
    }


# GET ALL PRODUCTS
def get_all_products(category=None, price=None):

    products = load_data()

    product_list = list(products.values())

    # FILTER BY CATEGORY
    if category:

        product_list = [

            product for product in product_list

            if product["category"].lower() == category.lower()
        ]

    # FILTER BY PRICE
    if price:

        product_list = [

            product for product in product_list

            if product["price"] <= price
        ]

    return product_list


# GET PRODUCT BY ID
def get_product_by_id(product_id):

    products = load_data()

    if str(product_id) not in products:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return products[str(product_id)]


# UPDATE PRODUCT
def update_product(product_id, updated_product):

    products = load_data()

    if str(product_id) not in products:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    products[str(product_id)] = updated_product.dict()

    save_data(products)

    return {
        "message": "Product updated successfully",
        "product": updated_product
    }


# DELETE PRODUCT
def delete_product(product_id):

    products = load_data()

    if str(product_id) not in products:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    deleted_product = products.pop(str(product_id))

    save_data(products)

    return {
        "message": "Product deleted successfully",
        "product": deleted_product
    }