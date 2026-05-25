from fastapi import APIRouter, status
from typing import Optional, List

from schemas import (
    Product,
    ProductResponse
)

from crud import (
    create_product,
    get_all_products,
    get_product_by_id,
    update_product,
    delete_product
)

router = APIRouter()


# CREATE PRODUCT
@router.post(
    "/products",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
def add_product(product: Product):

    return create_product(product)


# GET ALL PRODUCTS and FILTER PRODUCTS
@router.get(
    "/products",
    response_model=List[Product],
    status_code=status.HTTP_200_OK
)
def fetch_products(
    category: Optional[str] = None,
    price: Optional[float] = None
):

    return get_all_products(category, price)


# GET PRODUCT BY ID
@router.get(
    "/products/{product_id}",
    response_model=Product,
    status_code=status.HTTP_200_OK
)
def fetch_product(product_id: int):

    return get_product_by_id(product_id)


# UPDATE PRODUCT
@router.put(
    "/products/{product_id}",
    response_model=ProductResponse,
    status_code=status.HTTP_200_OK
)
def edit_product(
    product_id: int,
    updated_product: Product
):

    return update_product(
        product_id,
        updated_product
    )


# DELETE PRODUCT
@router.delete(
    "/products/{product_id}",
    status_code=status.HTTP_200_OK
)
def remove_product(product_id: int):

    return delete_product(product_id)