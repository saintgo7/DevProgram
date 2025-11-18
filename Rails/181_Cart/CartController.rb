class CartController < ApplicationController
  before_action :set_cart, only: [:show, :edit, :update, :destroy]

  # GET /cart
  def index
    @carts = Cart.all
    render json: @carts
  end

  # GET /cart/1
  def show
    render json: @cart
  end

  # POST /cart
  def create
    @cart = Cart.new(cart_params)

    if @cart.save
      render json: @cart, status: :created
    else
      render json: @cart.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /cart/1
  def update
    if @cart.update(cart_params)
      render json: @cart
    else
      render json: @cart.errors, status: :unprocessable_entity
    end
  end

  # DELETE /cart/1
  def destroy
    @cart.destroy
    head :no_content
  end

  private

  def set_cart
    @cart = Cart.find(params[:id])
  end

  def cart_params
    params.require(:cart).permit(:name)
  end
end
