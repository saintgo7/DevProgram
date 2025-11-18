class CheckoutController < ApplicationController
  before_action :set_checkout, only: [:show, :edit, :update, :destroy]

  # GET /checkout
  def index
    @checkouts = Checkout.all
    render json: @checkouts
  end

  # GET /checkout/1
  def show
    render json: @checkout
  end

  # POST /checkout
  def create
    @checkout = Checkout.new(checkout_params)

    if @checkout.save
      render json: @checkout, status: :created
    else
      render json: @checkout.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /checkout/1
  def update
    if @checkout.update(checkout_params)
      render json: @checkout
    else
      render json: @checkout.errors, status: :unprocessable_entity
    end
  end

  # DELETE /checkout/1
  def destroy
    @checkout.destroy
    head :no_content
  end

  private

  def set_checkout
    @checkout = Checkout.find(params[:id])
  end

  def checkout_params
    params.require(:checkout).permit(:name)
  end
end
