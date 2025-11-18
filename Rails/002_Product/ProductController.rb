class ProductController < ApplicationController
  before_action :set_product, only: [:show, :edit, :update, :destroy]

  # GET /product
  def index
    @products = Product.all
    render json: @products
  end

  # GET /product/1
  def show
    render json: @product
  end

  # POST /product
  def create
    @product = Product.new(product_params)

    if @product.save
      render json: @product, status: :created
    else
      render json: @product.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /product/1
  def update
    if @product.update(product_params)
      render json: @product
    else
      render json: @product.errors, status: :unprocessable_entity
    end
  end

  # DELETE /product/1
  def destroy
    @product.destroy
    head :no_content
  end

  private

  def set_product
    @product = Product.find(params[:id])
  end

  def product_params
    params.require(:product).permit(:name)
  end
end
